using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Authorization;
using FootballBookingApi.Services;
using FootballBookingApi.Models;

namespace FootballBookingApi.Controllers
{
    [ApiController]
    [Route("api/admin/users")]
    public class UserController : ControllerBase
    {
        private readonly IUserService _userService;

        public UserController(IUserService userService)
        {
            _userService = userService;
        }

        [HttpGet]
        public IActionResult GetAllUsers()
        {
            var users = _userService.GetAllUsers();
            return Ok(users.Select(u => new
            {
                u.Id,
                u.FullName,
                u.Phone,
                u.Email,
                Role = u.Role.ToString(),
                u.WalletBalance,
                IsLocked = u.IsDeleted
            }));
        }

        [HttpPut("{id}/status")]
        public IActionResult ToggleUserStatus(Guid id, [FromBody] UserStatusRequest req)
        {
            var user = _userService.GetUserById(id);
            if (user == null)
            {
                return NotFound(new { message = "Không tìm thấy người dùng!" });
            }

            user.IsDeleted = req.IsLocked;

            return Ok(new
            {
                status = "success",
                message = req.IsLocked ? $"Đã KHÓA tài khoản của {user.FullName}!" : $"Đã MỞ KHÓA tài khoản của {user.FullName}!",
                user = new { user.Id, user.FullName, user.IsDeleted }
            });
        }

        [HttpPut("{id}/balance")]
        public IActionResult AdjustUserBalance(Guid id, [FromBody] BalanceAdjustRequest req)
        {
            var user = _userService.GetUserById(id);
            if (user == null)
            {
                return NotFound(new { message = "Không tìm thấy tài khoản người dùng!" });
            }

            user.WalletBalance += req.Amount;
            _userService.AddTransaction(id, req.Amount, req.Amount >= 0 ? "AdminAdjustPlus" : "AdminAdjustMinus", null);

            return Ok(new
            {
                status = "success",
                message = $"Đã điều chỉnh số dư ví của {user.FullName}: {(req.Amount >= 0 ? "+" : "")}{req.Amount.ToString("N0")} VNĐ!",
                newBalance = user.WalletBalance
            });
        }
    }

    public class UserStatusRequest
    {
        public bool IsLocked { get; set; }
    }

    public class BalanceAdjustRequest
    {
        public decimal Amount { get; set; }
    }
}
