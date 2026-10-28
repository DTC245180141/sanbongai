using Microsoft.AspNetCore.Mvc;
using FootballBookingApi.Services;
using FootballBookingApi.Models;

namespace FootballBookingApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class AuthController : ControllerBase
    {
        private readonly IUserService _userService;

        public AuthController(IUserService userService)
        {
            _userService = userService;
        }

        [HttpPost("register")]
        public IActionResult Register([FromBody] RegisterRequest? req)
        {
            try
            {
                if (req == null || string.IsNullOrWhiteSpace(req.Username) || string.IsNullOrWhiteSpace(req.Password))
                {
                    return BadRequest(new { message = "Vui lòng nhập Tên đăng nhập và Mật khẩu!" });
                }

                string username = req.Username.Trim();
                string fullName = string.IsNullOrWhiteSpace(req.FullName) ? username : req.FullName.Trim();
                string phone = string.IsNullOrWhiteSpace(req.Phone) ? "0900000000" : req.Phone.Trim();
                string email = string.IsNullOrWhiteSpace(req.Email) ? $"{username}@gmail.com" : req.Email.Trim();

                var user = _userService.Register(username, fullName, phone, email, req.Password, req.Role);
                if (user == null)
                {
                    return BadRequest(new { message = "Tên đăng nhập, Số điện thoại hoặc Email này đã tồn tại!" });
                }

                return Ok(new
                {
                    status = "success",
                    message = "Đăng ký tài khoản thành công! Vui lòng đăng nhập bằng Tên đăng nhập vừa tạo.",
                    user = new { user.Id, user.Username, user.FullName, user.Email, user.Phone, user.WalletBalance, user.AvatarUrl, role = user.Role.ToString() }
                });
            }
            catch (Exception ex)
            {
                return BadRequest(new { message = $"Lỗi xử lý hệ thống: {ex.Message}" });
            }
        }

        [HttpPost("login")]
        public IActionResult Login([FromBody] LoginRequest? req)
        {
            try
            {
                string input = req?.Username ?? req?.PhoneOrEmail ?? string.Empty;
                if (string.IsNullOrWhiteSpace(input) || string.IsNullOrWhiteSpace(req?.Password))
                {
                    return BadRequest(new { message = "Vui lòng nhập Tên đăng nhập và Mật khẩu!" });
                }

                var (user, token) = _userService.Login(input.Trim(), req.Password);
                if (user == null)
                {
                    return BadRequest(new { message = "Tên đăng nhập hoặc mật khẩu không chính xác." });
                }

                if (user.IsDeleted)
                {
                    return BadRequest(new { message = "Tài khoản của bạn đã bị khóa bởi Quản trị viên!" });
                }

                return Ok(new
                {
                    status = "success",
                    message = "Đăng nhập thành công!",
                    token = token,
                    user = new { user.Id, user.Username, user.FullName, user.Email, user.Phone, user.WalletBalance, user.AvatarUrl, role = user.Role.ToString() }
                });
            }
            catch (Exception ex)
            {
                return BadRequest(new { message = $"Lỗi xử lý hệ thống: {ex.Message}" });
            }
        }

        [HttpPost("forgot-username")]
        public IActionResult ForgotUsername([FromBody] ForgotUsernameRequest? req)
        {
            try
            {
                if (req == null || string.IsNullOrWhiteSpace(req.PhoneOrEmail))
                {
                    return BadRequest(new { message = "Vui lòng nhập Số điện thoại hoặc Email để tìm kiếm tài khoản!" });
                }

                var (success, username, message) = _userService.ForgotUsername(req.PhoneOrEmail.Trim());
                if (!success)
                {
                    return BadRequest(new { message });
                }

                return Ok(new { status = "success", username, message });
            }
            catch (Exception ex)
            {
                return BadRequest(new { message = $"Lỗi hệ thống: {ex.Message}" });
            }
        }

        [HttpPost("forgot-password")]
        [HttpPost("forgot-password/reset")]
        public IActionResult ForgotPasswordDirect([FromBody] DirectResetPasswordRequest? req)
        {
            try
            {
                string searchKey = req?.UsernameOrEmail ?? req?.PhoneOrEmail ?? string.Empty;
                string newPass = req?.NewPassword ?? string.Empty;

                if (string.IsNullOrWhiteSpace(searchKey) || string.IsNullOrWhiteSpace(newPass))
                {
                    return BadRequest(new { message = "Vui lòng nhập Tên đăng nhập/Email và Mật khẩu mới!" });
                }

                var (success, message) = _userService.ResetPasswordDirect(searchKey.Trim(), newPass);
                if (!success)
                {
                    return BadRequest(new { message });
                }

                return Ok(new { status = "success", message });
            }
            catch (Exception ex)
            {
                return BadRequest(new { message = $"Lỗi hệ thống khi khôi phục mật khẩu: {ex.Message}" });
            }
        }

        [HttpPost("forgot-password/request")]
        public IActionResult RequestPasswordReset([FromBody] ForgotPasswordRequest? req)
        {
            try
            {
                if (req == null || string.IsNullOrWhiteSpace(req.UsernameOrEmail))
                {
                    return BadRequest(new { message = "Vui lòng nhập Tên đăng nhập hoặc Email!" });
                }

                var (success, otp, message) = _userService.RequestPasswordReset(req.UsernameOrEmail.Trim());
                if (!success)
                {
                    return BadRequest(new { message });
                }

                return Ok(new { status = "success", otp, message });
            }
            catch (Exception ex)
            {
                return BadRequest(new { message = $"Lỗi hệ thống: {ex.Message}" });
            }
        }

        [HttpPut("profile/{userId}")]
        public IActionResult UpdateProfile(Guid userId, [FromBody] UpdateProfileRequest? req)
        {
            try
            {
                if (req == null || string.IsNullOrWhiteSpace(req.FullName))
                {
                    return BadRequest(new { message = "Vui lòng nhập Họ tên hiển thị!" });
                }

                var updatedUser = _userService.UpdateProfile(userId, req.FullName.Trim(), req.Phone?.Trim() ?? "", req.Email?.Trim() ?? "");
                if (updatedUser == null)
                {
                    return BadRequest(new { message = "Cập nhật thất bại. Số điện thoại hoặc Email có thể đã trùng với tài khoản khác." });
                }

                return Ok(new
                {
                    status = "success",
                    message = "Cập nhật thông tin cá nhân thành công!",
                    user = new { updatedUser.Id, updatedUser.FullName, updatedUser.Email, updatedUser.Phone, updatedUser.WalletBalance, updatedUser.AvatarUrl, role = updatedUser.Role.ToString() }
                });
            }
            catch (Exception ex)
            {
                return BadRequest(new { message = $"Lỗi cập nhật profile: {ex.Message}" });
            }
        }

        [HttpPost("upload-avatar/{userId}")]
        public async Task<IActionResult> UploadAvatar(Guid userId, IFormFile? avatar)
        {
            try
            {
                if (avatar == null || avatar.Length == 0)
                {
                    return BadRequest(new { message = "Vui lòng chọn một file ảnh đại diện hợp lệ." });
                }

                var uploadsFolder = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "uploads");
                if (!Directory.Exists(uploadsFolder))
                {
                    Directory.CreateDirectory(uploadsFolder);
                }

                var fileExt = Path.GetExtension(avatar.FileName);
                var fileName = $"avatar_{userId}_{DateTime.UtcNow.Ticks}{fileExt}";
                var filePath = Path.Combine(uploadsFolder, fileName);

                using (var stream = new FileStream(filePath, FileMode.Create))
                {
                    await avatar.CopyToAsync(stream);
                }

                var avatarUrl = $"/uploads/{fileName}";
                var updatedUser = _userService.UpdateAvatar(userId, avatarUrl);

                return Ok(new
                {
                    status = "success",
                    message = "Tải lên ảnh đại diện thành công!",
                    avatarUrl = avatarUrl
                });
            }
            catch (Exception ex)
            {
                return BadRequest(new { message = $"Lỗi khi tải ảnh lên: {ex.Message}" });
            }
        }

        [HttpPost("change-password")]
        public IActionResult ChangePassword([FromBody] ChangePasswordRequest? req)
        {
            try
            {
                if (req == null || req.UserId == Guid.Empty || string.IsNullOrWhiteSpace(req.OldPassword) || string.IsNullOrWhiteSpace(req.NewPassword))
                {
                    return BadRequest(new { message = "Vui lòng nhập đầy đủ thông tin Mật khẩu cũ và Mật khẩu mới!" });
                }

                if (req.NewPassword.Length < 6)
                {
                    return BadRequest(new { message = "Mật khẩu mới phải có ít nhất 6 ký tự!" });
                }

                var (success, message) = _userService.ChangePassword(req.UserId, req.OldPassword, req.NewPassword);
                if (!success)
                {
                    return BadRequest(new { message });
                }

                return Ok(new { status = "success", message });
            }
            catch (Exception ex)
            {
                return BadRequest(new { message = $"Lỗi xử lý đổi mật khẩu: {ex.Message}" });
            }
        }
    }

    public class ChangePasswordRequest
    {
        public Guid UserId { get; set; }
        public string OldPassword { get; set; } = string.Empty;
        public string NewPassword { get; set; } = string.Empty;
    }

    public class RegisterRequest
    {
        public string Username { get; set; } = string.Empty;
        public string FullName { get; set; } = string.Empty;
        public string Phone { get; set; } = string.Empty;
        public string Email { get; set; } = string.Empty;
        public string Password { get; set; } = string.Empty;
        public UserRole Role { get; set; } = UserRole.Customer;
    }

    public class LoginRequest
    {
        public string Username { get; set; } = string.Empty;
        public string PhoneOrEmail { get; set; } = string.Empty;
        public string Password { get; set; } = string.Empty;
    }

    public class UpdateProfileRequest
    {
        public string FullName { get; set; } = string.Empty;
        public string Phone { get; set; } = string.Empty;
        public string Email { get; set; } = string.Empty;
    }

    public class ForgotUsernameRequest
    {
        public string PhoneOrEmail { get; set; } = string.Empty;
    }

    public class ForgotPasswordRequest
    {
        public string UsernameOrEmail { get; set; } = string.Empty;
    }

    public class DirectResetPasswordRequest
    {
        public string? UsernameOrEmail { get; set; }
        public string? PhoneOrEmail { get; set; }
        public string NewPassword { get; set; } = string.Empty;
    }

    public class ResetPasswordRequest
    {
        public string UsernameOrEmail { get; set; } = string.Empty;
        public string Otp { get; set; } = string.Empty;
        public string NewPassword { get; set; } = string.Empty;
    }
}
