using System;
using System.Linq;
using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;
using FootballBookingApi.Controllers;
using FootballBookingApi.Models;
using FootballBookingApi.Services;
using Microsoft.Extensions.Caching.Memory;
using Xunit;

namespace FootballBookingApi.Tests
{
    /// <summary>
    /// KIỂM THỬ TÍCH HỢP TỰ ĐỘNG (AUTOMATED INTEGRATION TESTS)
    /// Kiểm tra tính tương thích và luồng tích hợp xuyên suốt giữa:
    /// Controllers -> Business Services -> In-Memory Cache -> Financial State
    /// </summary>
    public class IntegrationTests
    {
        private readonly IUserService _userService;
        private readonly IBookingService _bookingService;
        private readonly IAIServiceClient _aiClient;
        private readonly BookingsController _bookingsController;
        private readonly AdminController _adminController;

        public IntegrationTests()
        {
            _userService = new UserService();
            _bookingService = new BookingService(_userService);
            
            var memoryCache = new MemoryCache(new MemoryCacheOptions());
            var httpClient = new System.Net.Http.HttpClient { Timeout = TimeSpan.FromMilliseconds(500) };
            _aiClient = new AIServiceClient(httpClient, memoryCache);

            _bookingsController = new BookingsController(_bookingService, _aiClient);
            _adminController = new AdminController(_bookingService, _userService);
        }

        [Fact]
        public void Integration_GetFields_ReturnsStandard5FieldsWithPricing()
        {
            // Act: Gọi API lấy danh sách sân bóng
            var result = _bookingsController.GetFields() as OkObjectResult;

            // Assert: Trả về HTTP 200 và đủ 5 sân cỏ nhân tạo ICTU
            Assert.NotNull(result);
            Assert.Equal(200, result.StatusCode);
            
            var fields = result.Value as IEnumerable<FootballField>;
            Assert.NotNull(fields);
            Assert.Equal(5, fields.Count());
            Assert.Contains(fields, f => f.FieldType == 5 && f.BasePrice == 150000);
            Assert.Contains(fields, f => f.FieldType == 7 && f.BasePrice == 150000);
            Assert.Contains(fields, f => f.FieldType == 11 && f.BasePrice == 150000);
        }

        [Fact]
        public void Integration_EndToEnd_CreateBooking_And_CancelWithRefund()
        {
            // Arrange: Chuẩn bị tài khoản khách hàng hợp lệ
            var user = _userService.GetAllUsers().First(u => u.Role == UserRole.Customer && !u.IsDeleted);
            decimal initialBalance = user.WalletBalance;
            var field = _bookingService.GetFields().First();

            var bookingTime = DateTime.Now.AddHours(3); // Hợp lệ trong khoảng 2h - 3 ngày
            decimal bookingPrice = 150000m;

            var createReq = new BookingCreateRequest
            {
                UserId = user.Id,
                FieldId = field.FieldId,
                BookingTime = bookingTime,
                StartTime = bookingTime,
                EndTime = bookingTime.AddHours(1),
                TotalPrice = bookingPrice
            };

            // Act 1: Khách hàng gọi API Đặt sân
            var createResult = _bookingsController.CreateBooking(createReq) as OkObjectResult;

            // Assert 1: Đặt sân thành công, tiền ví bị trừ
            Assert.NotNull(createResult);
            Assert.Equal(200, createResult.StatusCode);
            Assert.Equal(initialBalance - bookingPrice, user.WalletBalance);

            // Trích xuất mã BookingId vừa tạo
            var allBookings = _bookingService.GetAllBookings();
            var createdBooking = allBookings.OrderByDescending(b => b.CreatedAt).First(b => b.UserId == user.Id);
            Assert.Equal(BookingStatus.Confirmed, createdBooking.Status);

            // Act 2: Quản trị viên gọi API Hủy đơn và hoàn tiền 100% tự động
            var refundResult = _adminController.CancelAndRefundBooking(createdBooking.BookingId) as OkObjectResult;

            // Assert 2: Hoàn tiền thành công, số dư ví trở về ban đầu, đơn chuyển sang Cancelled
            Assert.NotNull(refundResult);
            Assert.Equal(200, refundResult.StatusCode);
            Assert.Equal(BookingStatus.Cancelled, createdBooking.Status);
            Assert.Equal(initialBalance, user.WalletBalance);
        }

        [Fact]
        public void Integration_Admin_MaintenanceMode_TogglesStateCorrectly()
        {
            // Arrange: Trạng thái ban đầu không bảo trì
            Assert.False(_bookingService.IsSystemMaintenance);

            // Act 1: Bật bảo trì hệ thống
            var toggle1 = _adminController.ToggleSystemMaintenance(new ToggleSystemMaintenanceRequest { IsMaintenance = true }) as OkObjectResult;
            Assert.NotNull(toggle1);
            Assert.True(_bookingService.IsSystemMaintenance);

            // Act 2: Tắt bảo trì hệ thống
            var toggle2 = _adminController.ToggleSystemMaintenance(new ToggleSystemMaintenanceRequest { IsMaintenance = false }) as OkObjectResult;
            Assert.NotNull(toggle2);
            Assert.False(_bookingService.IsSystemMaintenance);
        }
    }
}
