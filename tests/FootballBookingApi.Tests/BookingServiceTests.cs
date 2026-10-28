using System;
using System.Linq;
using System.Threading.Tasks;
using System.Collections.Generic;
using FootballBookingApi.Models;
using FootballBookingApi.Services;
using Moq;
using Xunit;

namespace FootballBookingApi.Tests
{
    public class BookingServiceTests
    {
        private readonly Mock<IUserService> _userServiceMock;
        private readonly BookingService _bookingService;
        private readonly Guid _testFieldId = Guid.Parse("11111111-1111-1111-1111-111111111111");

        public BookingServiceTests()
        {
            _userServiceMock = new Mock<IUserService>();
            _bookingService = new BookingService(_userServiceMock.Object);
        }

        [Fact]
        public void CreateBooking_Success_DeductsWalletBalanceAndReturnsBooking()
        {
            // Arrange
            var userId = Guid.NewGuid();
            var initialBalance = 1000000m;
            var price = 150000m;
            var testUser = new User
            {
                Id = userId,
                Username = "test_player",
                WalletBalance = initialBalance,
                IsDeleted = false
            };

            _userServiceMock.Setup(s => s.GetUserById(userId)).Returns(testUser);

            var startTime = DateTime.UtcNow.AddDays(10).Date.AddHours(8); // Future slot to avoid overlap with others
            var endTime = startTime.AddHours(1.5);

            // Act
            var (booking, errorMessage) = _bookingService.CreateBooking(userId, _testFieldId, startTime, endTime, price);

            // Assert
            Assert.NotNull(booking);
            Assert.True(string.IsNullOrEmpty(errorMessage));
            Assert.Equal(BookingStatus.Confirmed, booking.Status);
            Assert.Equal(price, booking.TotalPrice);
            Assert.Equal(initialBalance - price, testUser.WalletBalance);
            _userServiceMock.Verify(s => s.AddTransaction(userId, price, "Payment", booking.BookingId), Times.Once);
        }

        [Fact]
        public void CreateBooking_InsufficientBalance_ReturnsError()
        {
            // Arrange
            var userId = Guid.NewGuid();
            var testUser = new User
            {
                Id = userId,
                Username = "poor_player",
                WalletBalance = 50000m,
                IsDeleted = false
            };

            _userServiceMock.Setup(s => s.GetUserById(userId)).Returns(testUser);

            var startTime = DateTime.UtcNow.AddDays(11).Date.AddHours(10);
            var endTime = startTime.AddHours(1.5);
            var price = 150000m;

            // Act
            var (booking, errorMessage) = _bookingService.CreateBooking(userId, _testFieldId, startTime, endTime, price);

            // Assert
            Assert.Null(booking);
            Assert.Contains("Số dư ví không đủ", errorMessage);
            Assert.Equal(50000m, testUser.WalletBalance); // Balance unmodified
        }

        [Fact]
        public void CreateBooking_UserLocked_ReturnsError()
        {
            // Arrange
            var userId = Guid.NewGuid();
            var testUser = new User
            {
                Id = userId,
                Username = "banned_player",
                WalletBalance = 2000000m,
                IsDeleted = true // Account locked
            };

            _userServiceMock.Setup(s => s.GetUserById(userId)).Returns(testUser);

            var startTime = DateTime.UtcNow.AddDays(12).Date.AddHours(14);
            var endTime = startTime.AddHours(1.5);
            var price = 150000m;

            // Act
            var (booking, errorMessage) = _bookingService.CreateBooking(userId, _testFieldId, startTime, endTime, price);

            // Assert
            Assert.Null(booking);
            Assert.Contains("Tài khoản của bạn đã bị khóa", errorMessage);
        }

        [Fact]
        public void CreateBooking_FieldMaintenance_ReturnsError()
        {
            // Arrange
            var userId = Guid.NewGuid();
            var testUser = new User
            {
                Id = userId,
                Username = "active_player",
                WalletBalance = 2000000m,
                IsDeleted = false
            };

            _userServiceMock.Setup(s => s.GetUserById(userId)).Returns(testUser);

            // Turn off field status to simulate maintenance
            _bookingService.ToggleFieldMaintenance(_testFieldId, false);

            var startTime = DateTime.UtcNow.AddDays(13).Date.AddHours(15);
            var endTime = startTime.AddHours(1.5);
            var price = 150000m;

            // Act
            var (booking, errorMessage) = _bookingService.CreateBooking(userId, _testFieldId, startTime, endTime, price);

            // Restore field status
            _bookingService.ToggleFieldMaintenance(_testFieldId, true);

            // Assert
            Assert.Null(booking);
            Assert.Contains("Sân đang được bảo trì", errorMessage);
        }

        [Fact]
        public void CreateBooking_OverlappingBooking_ReturnsError()
        {
            // Arrange
            var user1 = new User { Id = Guid.NewGuid(), Username = "user1", WalletBalance = 2000000m };
            var user2 = new User { Id = Guid.NewGuid(), Username = "user2", WalletBalance = 2000000m };

            _userServiceMock.Setup(s => s.GetUserById(user1.Id)).Returns(user1);
            _userServiceMock.Setup(s => s.GetUserById(user2.Id)).Returns(user2);

            var startTime = DateTime.UtcNow.AddDays(14).Date.AddHours(18);
            var endTime = startTime.AddHours(1.5);
            var price = 300000m;

            // Act 1: User 1 books first
            var (booking1, error1) = _bookingService.CreateBooking(user1.Id, _testFieldId, startTime, endTime, price);

            // Act 2: User 2 tries to book the exact same time
            var (booking2, error2) = _bookingService.CreateBooking(user2.Id, _testFieldId, startTime, endTime, price);

            // Assert
            Assert.NotNull(booking1);
            Assert.True(string.IsNullOrEmpty(error1));

            Assert.Null(booking2);
            Assert.Contains("Khung giờ này đã có người đặt", error2);
        }

        [Fact]
        public void CancelBooking_ExistingBooking_SetsStatusToCancelled()
        {
            // Arrange
            var userId = Guid.NewGuid();
            var user = new User { Id = userId, Username = "cancel_tester", WalletBalance = 2000000m };
            _userServiceMock.Setup(s => s.GetUserById(userId)).Returns(user);

            var startTime = DateTime.UtcNow.AddDays(15).Date.AddHours(9);
            var endTime = startTime.AddHours(1.5);
            var (booking, _) = _bookingService.CreateBooking(userId, _testFieldId, startTime, endTime, 150000m);
            Assert.NotNull(booking);

            // Act
            var result = _bookingService.CancelBooking(booking.BookingId);

            // Assert
            Assert.True(result);
            Assert.Equal(BookingStatus.Cancelled, booking.Status);
        }

        [Fact]
        public void CreateBooking_ConcurrencySafe_UnderMultiThreading()
        {
            // Arrange
            int threadCount = 10;
            var users = Enumerable.Range(1, threadCount).Select(i => new User
            {
                Id = Guid.NewGuid(),
                Username = $"thread_user_{i}",
                WalletBalance = 2000000m,
                IsDeleted = false
            }).ToList();

            foreach (var u in users)
            {
                _userServiceMock.Setup(s => s.GetUserById(u.Id)).Returns(u);
            }

            var startTime = DateTime.UtcNow.AddDays(16).Date.AddHours(20);
            var endTime = startTime.AddHours(1.5);
            var price = 300000m;

            int successCount = 0;
            int conflictCount = 0;
            object countLock = new object();

            // Act: Fire parallel requests simultaneously
            Parallel.ForEach(users, user =>
            {
                var (booking, err) = _bookingService.CreateBooking(user.Id, _testFieldId, startTime, endTime, price);
                lock (countLock)
                {
                    if (booking != null) successCount++;
                    else if (err.Contains("Khung giờ này đã có người đặt")) conflictCount++;
                }
            });

            // Assert: Exactly 1 thread succeeded, all other 9 threads got rejected cleanly without race condition
            Assert.Equal(1, successCount);
            Assert.Equal(threadCount - 1, conflictCount);
        }
    }
}

