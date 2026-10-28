using Microsoft.AspNetCore.Mvc;
using FootballBookingApi.Services;
using FootballBookingApi.Models;

namespace FootballBookingApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class PaymentController : ControllerBase
    {
        private readonly IUserService _userService;

        public PaymentController(IUserService userService)
        {
            _userService = userService;
        }

        [HttpPost("generate-vietqr")]
        public IActionResult GenerateVietQR([FromBody] VietQRRequest req)
        {
            if (req.Amount <= 0)
            {
                return BadRequest(new { message = "Số tiền nạp phải lớn hơn 0 VNĐ!" });
            }

            var user = _userService.GetUserById(req.UserId);
            if (user == null)
            {
                return NotFound(new { message = "Không tìm thấy thông tin tài khoản!" });
            }

            // Gọi API VietQR (api.vietqr.io) tạo mã QR nạp tiền ví ảo cá nhân hóa
            string bankId = "MBBank"; // Ngân hàng MBBank
            string accountNo = "0909123456"; // Số tài khoản ngân hàng chủ sân
            string accountName = "CONG TY SAN BONG PITCHAI";
            string memo = $"NAPTIEN_USER_{user.Id.ToString().Substring(0, 8).ToUpper()}";

            string qrUrl = $"https://img.vietqr.io/image/{bankId}-{accountNo}-compact2.png?amount={req.Amount}&addInfo={Uri.EscapeDataString(memo)}&accountName={Uri.EscapeDataString(accountName)}&t={DateTime.UtcNow.Ticks}";

            return Ok(new
            {
                status = "success",
                qr_url = qrUrl,
                amount = req.Amount,
                memo = memo,
                bank = bankId,
                account_no = accountNo,
                account_name = accountName
            });
        }

        [HttpPost("create-deposit-request")]
        public IActionResult CreateDepositRequest([FromBody] CreateDepositApiRequest req)
        {
            if (req.Amount <= 0)
            {
                return BadRequest(new { message = "Số tiền nạp phải lớn hơn 0 VNĐ!" });
            }

            var user = _userService.GetUserById(req.UserId);
            if (user == null)
            {
                return NotFound(new { message = "Không tìm thấy thông tin tài khoản!" });
            }

            string txnCode = $"DEP{DateTime.UtcNow.Ticks.ToString().Substring(10)}";
            string memo = $"NAPTIEN_USER_{user.Id.ToString().Substring(0, 8).ToUpper()}";

            var deposit = _userService.CreateDepositRequest(req.UserId, req.Amount, txnCode, memo, req.ImageUrl ?? "");

            return Ok(new
            {
                status = "success",
                message = "🎉 Yêu cầu nạp tiền đã được gửi! Vui lòng chờ Admin kiểm tra và phê duyệt.",
                depositId = deposit.Id,
                amount = deposit.Amount,
                statusText = "Pending"
            });
        }

        [HttpGet("deposit-requests")]
        public IActionResult GetAllDepositRequests()
        {
            var list = _userService.GetAllDepositRequests();
            return Ok(list);
        }

        [HttpPost("deposit-requests/{id}/approve")]
        public IActionResult ApproveDeposit(Guid id)
        {
            var (success, message) = _userService.ApproveDepositRequest(id);
            if (!success)
            {
                return BadRequest(new { message });
            }

            return Ok(new { status = "success", message });
        }

        [HttpPost("deposit-requests/{id}/reject")]
        public IActionResult RejectDeposit(Guid id)
        {
            var (success, message) = _userService.RejectDepositRequest(id);
            if (!success)
            {
                return BadRequest(new { message });
            }

            return Ok(new { status = "success", message });
        }

        [HttpPost("confirm-topup")]
        public IActionResult ConfirmTopup([FromBody] VietQRRequest req)
        {
            var user = _userService.GetUserById(req.UserId);
            if (user == null)
            {
                return NotFound(new { message = "Không tìm thấy tài khoản!" });
            }

            // Tạo yêu cầu nạp tiền tự động
            string txnCode = $"AUTO{DateTime.UtcNow.Ticks.ToString().Substring(10)}";
            string memo = $"NAPTIEN_USER_{user.Id.ToString().Substring(0, 8).ToUpper()}";
            var deposit = _userService.CreateDepositRequest(req.UserId, req.Amount, txnCode, memo, "");

            return Ok(new
            {
                status = "success",
                message = $"🎉 Đã gửi yêu cầu nạp {req.Amount.ToString("N0")} VNĐ!\nYêu cầu đang ở trạng thái Chờ Duyệt (Pending) từ Admin.",
                depositId = deposit.Id
            });
        }
    }

    public class VietQRRequest
    {
        public Guid UserId { get; set; }
        public decimal Amount { get; set; }
    }

    public class CreateDepositApiRequest
    {
        public Guid UserId { get; set; }
        public decimal Amount { get; set; }
        public string? ImageUrl { get; set; }
    }
}
