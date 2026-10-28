using Microsoft.AspNetCore.Mvc;
using FootballBookingApi.Services;
using FootballBookingApi.Models;

namespace FootballBookingApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class AdminController : ControllerBase
    {
        private readonly IBookingService _bookingService;
        private readonly IUserService _userService;

        private static readonly List<PricingConfig> _configs = new()
        {
            new PricingConfig { ConfigId = 1, FieldType = 5, BasePrice = 200000, WeekendMultiplier = 1.30m, PeakHourMultiplier = 1.50m },
            new PricingConfig { ConfigId = 2, FieldType = 7, BasePrice = 400000, WeekendMultiplier = 1.30m, PeakHourMultiplier = 1.50m },
            new PricingConfig { ConfigId = 3, FieldType = 11, BasePrice = 1200000, WeekendMultiplier = 1.30m, PeakHourMultiplier = 1.50m }
        };

        public AdminController(IBookingService bookingService, IUserService userService)
        {
            _bookingService = bookingService;
            _userService = userService;
        }

        [HttpGet("pricing-configs")]
        public IActionResult GetPricingConfigs()
        {
            return Ok(_configs);
        }

        [HttpPost("update-price")]
        public IActionResult UpdatePrice([FromBody] UpdatePriceRequest req)
        {
            var config = _configs.FirstOrDefault(c => c.FieldType == req.FieldType);
            if (config == null)
            {
                config = new PricingConfig
                {
                    ConfigId = _configs.Count + 1,
                    FieldType = req.FieldType,
                    BasePrice = req.BasePrice,
                    WeekendMultiplier = req.WeekendMultiplier > 0 ? req.WeekendMultiplier : 1.30m,
                    PeakHourMultiplier = req.PeakHourMultiplier > 0 ? req.PeakHourMultiplier : 1.50m,
                    UpdatedAt = DateTime.UtcNow
                };
                _configs.Add(config);
            }
            else
            {
                config.BasePrice = req.BasePrice;
                if (req.WeekendMultiplier > 0) config.WeekendMultiplier = req.WeekendMultiplier;
                if (req.PeakHourMultiplier > 0) config.PeakHourMultiplier = req.PeakHourMultiplier;
                config.UpdatedAt = DateTime.UtcNow;
            }

            return Ok(new
            {
                status = "success",
                message = $"Đã cập nhật giá niêm yết cho Sân loại {req.FieldType} người thành {req.BasePrice.ToString("N0")} VNĐ!",
                config = config
            });
        }

        [HttpDelete("bookings/{id}")]
        public IActionResult CancelAndRefundBooking(Guid id)
        {
            var allBookings = _bookingService.GetAllBookings();
            var booking = allBookings.FirstOrDefault(b => b.BookingId == id);
            if (booking == null)
            {
                return NotFound(new { message = "Không tìm thấy mã đơn đặt sân!" });
            }

            if (booking.Status == BookingStatus.Cancelled)
            {
                return BadRequest(new { message = "Đơn đặt sân này đã được hủy trước đó!" });
            }

            // SỬ DỤNG DATABASE TRANSACTION LOGIC:
            // 1. Chuyển trạng thái booking sang Cancelled
            var isCancelled = _bookingService.CancelBooking(id);
            if (!isCancelled)
            {
                return StatusCode(500, new { message = "Lỗi hệ thống không thể hủy booking!" });
            }

            // 2. Hoàn tiền lại 100% vào WalletBalance của user và tạo record trong Transactions với Type = "Refund"
            var isRefunded = _userService.RefundBookingTransaction(booking.UserId, booking.TotalPrice, booking.BookingId);
            if (!isRefunded)
            {
                return StatusCode(500, new { message = "Lỗi hệ thống không thể hoàn tiền vào ví!" });
            }

            var user = _userService.GetUserById(booking.UserId);

            return Ok(new
            {
                status = "success",
                message = $"Đã hủy đơn đặt sân {id.ToString().Substring(0, 8)}... và hoàn lại {booking.TotalPrice.ToString("N0")} VNĐ vào ví!",
                refundedAmount = booking.TotalPrice,
                newWalletBalance = user?.WalletBalance ?? 0
            });
        }

        [HttpGet("system-maintenance")]
        public IActionResult GetSystemMaintenance()
        {
            return Ok(new { isMaintenance = _bookingService.IsSystemMaintenance });
        }

        [HttpPost("system-maintenance")]
        public IActionResult ToggleSystemMaintenance([FromBody] ToggleSystemMaintenanceRequest req)
        {
            _bookingService.IsSystemMaintenance = req.IsMaintenance;
            string statusStr = _bookingService.IsSystemMaintenance ? "BẬT" : "TẮT";
            return Ok(new
            {
                status = "success",
                isMaintenance = _bookingService.IsSystemMaintenance,
                message = $"Đã {statusStr} Chế độ bảo trì hệ thống thành công!"
            });
        }

        [HttpPut("fields/{id}/maintenance")]
        public IActionResult ToggleFieldMaintenance(Guid id, [FromBody] ToggleFieldMaintenanceRequest req)
        {
            var field = _bookingService.GetFieldById(id);
            if (field == null) return NotFound(new { message = "Không tìm thấy thông tin sân bóng!" });

            bool newStatus = req.Status.HasValue ? req.Status.Value : !field.Status;
            var success = _bookingService.ToggleFieldMaintenance(id, newStatus);
            if (!success) return BadRequest(new { message = "Cập nhật trạng thái bảo trì sân thất bại!" });

            string statusStr = newStatus ? "Hoạt động" : "Bảo trì";
            return Ok(new
            {
                status = "success",
                fieldId = id,
                fieldStatus = newStatus,
                message = $"Đã chuyển trạng thái sân '{field.Name}' sang: {statusStr}"
            });
        }
    }

    public class ToggleSystemMaintenanceRequest
    {
        public bool IsMaintenance { get; set; }
    }

    public class ToggleFieldMaintenanceRequest
    {
        public bool? Status { get; set; }
    }

    public class UpdatePriceRequest
    {
        public int FieldType { get; set; }
        public decimal BasePrice { get; set; }
        public decimal WeekendMultiplier { get; set; } = 1.30m;
        public decimal PeakHourMultiplier { get; set; } = 1.50m;
    }
}
