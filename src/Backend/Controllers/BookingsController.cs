using Microsoft.AspNetCore.Mvc;
using FootballBookingApi.Services;
using FootballBookingApi.Models;

namespace FootballBookingApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class BookingsController : ControllerBase
    {
        private readonly IBookingService _bookingService;
        private readonly IAIServiceClient _aiClient;

        public BookingsController(IBookingService bookingService, IAIServiceClient aiClient)
        {
            _bookingService = bookingService;
            _aiClient = aiClient;
        }

        [HttpGet("fields")]
        public IActionResult GetFields()
        {
            return Ok(_bookingService.GetFields());
        }

        [HttpGet("fields/{id}/ai-price")]
        public async Task<IActionResult> GetAiPrice(Guid id, [FromQuery] DateTime? bookingTime)
        {
            var field = _bookingService.GetFieldById(id);
            if (field == null) return NotFound(new { message = "Sân bóng không tồn tại" });

            var time = bookingTime ?? DateTime.Now.AddHours(2);
            var aiResult = await _aiClient.GetAiOptimalPriceAsync(id, time, field.BasePrice);
            return Ok(aiResult);
        }

        [HttpPost]
        public IActionResult CreateBooking([FromBody] BookingCreateRequest req)
        {
            var field = _bookingService.GetFieldById(req.FieldId);
            if (field == null) return BadRequest(new { message = "Sân bóng không hợp lệ" });

            // SỬA LỖI LOGIC VALIDATE THỜI GIAN ĐẶT SÂN THEO GIỜ LOCAL BẰNG DATETIME.NOW:
            DateTime bookingTime;
            if (req.BookingTime != default)
            {
                bookingTime = req.BookingTime.Kind == DateTimeKind.Utc 
                    ? req.BookingTime.ToLocalTime() 
                    : req.BookingTime;
            }
            else
            {
                bookingTime = DateTime.Now.AddHours(2);
            }

            var minTime = DateTime.Now.AddHours(2).AddMinutes(-5); // Trừ bớt margin 5 phút tránh chênh lệch giây
            var maxTime = DateTime.Now.AddDays(3).AddMinutes(5);

            if (bookingTime < minTime || bookingTime > maxTime)
            {
                return BadRequest(new
                {
                    message = "Vui lòng chọn thời gian đặt từ 2 tiếng sau đến 3 ngày tới!"
                });
            }

            // Gọi BookingService thực hiện trừ tiền ví ảo & Concurrency Lock
            var (booking, errorMessage) = _bookingService.CreateBooking(req.UserId, req.FieldId, bookingTime, bookingTime.AddHours(1), req.TotalPrice);
            if (booking == null)
            {
                return BadRequest(new { message = errorMessage });
            }

            booking.BookingTime = bookingTime;

            return Ok(new
            {
                status = "success",
                message = "Đặt sân thành công!",
                booking = booking,
                qr_payment_url = $"https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=PAY_BOOKING_{booking.BookingId}"
            });
        }

        [HttpGet]
        public IActionResult GetAllBookings()
        {
            return Ok(_bookingService.GetAllBookings());
        }

        [HttpPost("{id}/cancel")]
        public IActionResult CancelBooking(Guid id)
        {
            var result = _bookingService.CancelBooking(id);
            if (!result) return NotFound(new { message = "Không tìm thấy mã đặt sân" });
            return Ok(new { message = "Đã hủy đặt sân thành công" });
        }
    }

    [ApiController]
    [Route("api/[controller]")]
    public class FieldsController : ControllerBase
    {
        private readonly IBookingService _bookingService;

        public FieldsController(IBookingService bookingService)
        {
            _bookingService = bookingService;
        }

        [HttpGet]
        public IActionResult GetAll() => Ok(_bookingService.GetFields());
    }

    [ApiController]
    [Route("api/[controller]")]
    public class AIController : ControllerBase
    {
        private readonly IAIServiceClient _aiClient;

        public AIController(IAIServiceClient aiClient)
        {
            _aiClient = aiClient;
        }

        [HttpPost("predict")]
        public IActionResult Predict([FromBody] AIPredictRequest req)
        {
            var result = _aiClient.GetAiOptimalPrice(req.FieldId, req.BookingTime, req.BasePrice);
            return Ok(result);
        }
    }

    [ApiController]
    [Route("api/[controller]")]
    public class PaymentsController : ControllerBase
    {
        [HttpPost("process")]
        public IActionResult ProcessPayment([FromBody] dynamic req)
        {
            return Ok(new { status = "Success", transaction_id = Guid.NewGuid().ToString(), message = "Thanh toán thành công qua MoMo/VNPay/Wallet" });
        }
    }

    public class BookingCreateRequest
    {
        public Guid UserId { get; set; } = Guid.NewGuid();
        public Guid FieldId { get; set; }
        public DateTime BookingTime { get; set; }
        public DateTime StartTime { get; set; }
        public DateTime EndTime { get; set; }
        public decimal TotalPrice { get; set; }
    }

    public class AIPredictRequest
    {
        public Guid FieldId { get; set; }
        public DateTime BookingTime { get; set; }
        public decimal BasePrice { get; set; }
    }
}
