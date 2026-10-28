using System;
using System.Collections.Generic;
using System.Linq;
using FootballBookingApi.Models;

namespace FootballBookingApi.Services
{
    public interface IBookingService
    {
        IEnumerable<FootballField> GetFields();
        FootballField? GetFieldById(Guid id);
        bool ToggleFieldMaintenance(Guid fieldId, bool? status = null);
        bool IsSystemMaintenance { get; set; }
        (Booking? booking, string errorMessage) CreateBooking(Guid userId, Guid fieldId, DateTime startTime, DateTime endTime, decimal price);
        bool CancelBooking(Guid bookingId);
        IEnumerable<Booking> GetUserBookings(Guid userId);
        IEnumerable<Booking> GetAllBookings();
    }

    public class BookingService : IBookingService
    {
        private static readonly object _lockObj = new object();
        public bool IsSystemMaintenance { get; set; } = false;

        private static readonly List<FootballField> _fields = new()
        {
            new FootballField { FieldId = Guid.Parse("11111111-1111-1111-1111-111111111111"), Name = "Sân bóng ICTU - Sân 1 (Sân 5 người)", FieldType = 5, BasePrice = 150000, Location = "Phường Quyết Thắng, TP. Thái Nguyên", Status = true },
            new FootballField { FieldId = Guid.Parse("22222222-2222-2222-2222-222222222222"), Name = "Sân bóng ICTU - Sân 2 (Sân 5 người)", FieldType = 5, BasePrice = 150000, Location = "Phường Quyết Thắng, TP. Thái Nguyên", Status = true },
            new FootballField { FieldId = Guid.Parse("33333333-3333-3333-3333-333333333333"), Name = "Sân bóng ICTU - Sân 3 (Sân 7 người VIP)", FieldType = 7, BasePrice = 150000, Location = "Phường Quyết Thắng, TP. Thái Nguyên", Status = true },
            new FootballField { FieldId = Guid.Parse("44444444-4444-4444-4444-444444444444"), Name = "Sân bóng ICTU - Sân 4 (Sân 7 người VIP)", FieldType = 7, BasePrice = 150000, Location = "Phường Quyết Thắng, TP. Thái Nguyên", Status = true },
            new FootballField { FieldId = Guid.Parse("55555555-5555-5555-5555-555555555555"), Name = "Sân bóng ICTU - Sân 5 (Sân 11 người Quốc tế)", FieldType = 11, BasePrice = 150000, Location = "Phường Quyết Thắng, TP. Thái Nguyên", Status = true }
        };

        private static readonly List<Booking> _bookings = new();
        private readonly IUserService _userService;

        public BookingService(IUserService userService)
        {
            _userService = userService;
        }

        public IEnumerable<FootballField> GetFields() => _fields;

        public FootballField? GetFieldById(Guid id) => _fields.FirstOrDefault(f => f.FieldId == id);

        public bool ToggleFieldMaintenance(Guid fieldId, bool? status = null)
        {
            lock (_lockObj)
            {
                var field = _fields.FirstOrDefault(f => f.FieldId == fieldId);
                if (field == null) return false;

                field.Status = status.HasValue ? status.Value : !field.Status;
                return true;
            }
        }

        public (Booking? booking, string errorMessage) CreateBooking(Guid userId, Guid fieldId, DateTime startTime, DateTime endTime, decimal price)
        {
            lock (_lockObj)
            {
                var field = GetFieldById(fieldId);
                if (field == null)
                {
                    return (null, "Không tìm thấy thông tin sân bóng!");
                }

                if (!field.Status)
                {
                    return (null, "Sân đang được bảo trì");
                }

                var user = _userService.GetUserById(userId);
                if (user == null)
                {
                    return (null, "Không tìm thấy thông tin tài khoản!");
                }

                if (user.IsDeleted)
                {
                    return (null, "Tài khoản của bạn đã bị khóa bởi Admin!");
                }

                if (user.WalletBalance < price)
                {
                    return (null, $"Số dư ví không đủ, vui lòng nạp thêm tiền! (Số dư hiện tại: {user.WalletBalance.ToString("N0")} VNĐ)");
                }

                bool isOverlap = _bookings.Any(b => b.FieldId == fieldId && 
                                                   b.Status == BookingStatus.Confirmed && 
                                                   ((startTime >= b.StartTime && startTime < b.EndTime) ||
                                                    (endTime > b.StartTime && endTime <= b.EndTime)));
                if (isOverlap)
                {
                    return (null, "Khung giờ này đã có người đặt, vui lòng chọn khung giờ khác!");
                }

                // LUỒNG TOÀN VẸN GIAO DỊCH (TRANSACTION):
                // 1. Trừ tiền ví
                user.WalletBalance -= price;

                // 2. Tạo Booking
                var booking = new Booking
                {
                    BookingId = Guid.NewGuid(),
                    UserId = userId,
                    FieldId = fieldId,
                    BookingTime = startTime,
                    StartTime = startTime,
                    EndTime = endTime,
                    TotalPrice = price,
                    Status = BookingStatus.Confirmed,
                    CreatedAt = DateTime.UtcNow
                };

                try
                {
                    _bookings.Add(booking);
                    _userService.AddTransaction(userId, price, "Payment", booking.BookingId);
                    return (booking, string.Empty);
                }
                catch (Exception ex)
                {
                    // Catch & Rollback lại số dư nếu gặp exception bất ngờ
                    user.WalletBalance += price;
                    throw new Exception("Lỗi giao dịch đặt sân, đã hoàn trả lại tiền ví!", ex);
                }
            }
        }

        public bool CancelBooking(Guid bookingId)
        {
            lock (_lockObj)
            {
                var booking = _bookings.FirstOrDefault(b => b.BookingId == bookingId);
                if (booking == null) return false;

                booking.Status = BookingStatus.Cancelled;
                return true;
            }
        }

        public IEnumerable<Booking> GetUserBookings(Guid userId) => _bookings.Where(b => b.UserId == userId);
        public IEnumerable<Booking> GetAllBookings() => _bookings;
    }
}
