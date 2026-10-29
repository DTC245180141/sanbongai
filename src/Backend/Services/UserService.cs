using System;
using System.Collections.Generic;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Security.Cryptography;
using System.Text;
using Microsoft.IdentityModel.Tokens;
using FootballBookingApi.Models;

namespace FootballBookingApi.Services
{
    public interface IUserService
    {
        User? Register(string username, string fullName, string phone, string email, string password, UserRole role);
        (User? user, string token) Login(string username, string password);
        User? GetUserById(Guid id);
        IEnumerable<User> GetAllUsers();
        void AddTransaction(Guid userId, decimal amount, string type, Guid? bookingId);
        bool RefundBookingTransaction(Guid userId, decimal amount, Guid bookingId);
        User? UpdateProfile(Guid userId, string fullName, string phone, string email);
        User? UpdateAvatar(Guid userId, string avatarUrl);
        (bool success, User? user, string username, string message) ForgotUsername(string phoneOrEmail);
        (bool success, User? user, string otp, string message) RequestPasswordReset(string usernameOrEmail);
        (bool success, string message) ResetPassword(string usernameOrEmail, string otp, string newPassword);
        (bool success, string message) ResetPasswordDirect(string usernameOrEmail, string newPassword);
        (bool success, string message) ChangePassword(Guid userId, string oldPassword, string newPassword);

        DepositRequest CreateDepositRequest(Guid userId, decimal amount, string transactionCode, string memo, string imageUrl);
        IEnumerable<object> GetAllDepositRequests();
        (bool success, string message) ApproveDepositRequest(Guid depositId);
        (bool success, string message) RejectDepositRequest(Guid depositId);
    }

    public class UserService : IUserService
    {
        private static readonly List<User> _users = new()
        {
            new User
            {
                Id = Guid.Parse("99999999-9999-9999-9999-999999999999"),
                Username = "admin",
                FullName = "Nguyễn Văn Admin",
                Phone = "0909123456",
                Email = "admin@pitchai.com",
                Role = UserRole.Admin,
                PasswordHash = HashPassword("Admin@123"),
                WalletBalance = 10000000.00m,
                AvatarUrl = null
            },
            new User
            {
                Id = Guid.Parse("88888888-8888-8888-8888-888888888888"),
                Username = "khach1",
                FullName = "Trần Văn Khách",
                Phone = "0909888888",
                Email = "khach@gmail.com",
                Role = UserRole.Customer,
                PasswordHash = HashPassword("Customer@123"),
                WalletBalance = 3000000.00m,
                AvatarUrl = null
            },
            new User
            {
                Id = Guid.Parse("77777777-7777-7777-7777-777777777777"),
                Username = "doanh",
                FullName = "Đỗ Văn Doanh",
                Phone = "0364382164",
                Email = "doanh@gmail.com",
                Role = UserRole.Customer,
                PasswordHash = HashPassword("123456"),
                WalletBalance = 5000000.00m,
                AvatarUrl = null
            }
        };

        private static readonly List<Transaction> _transactions = new();
        private static readonly Dictionary<string, string> _otpStore = new();
        private const string SecretKey = "PitchAI_Super_Secret_JWT_Key_For_Football_Booking_System_2026";

        public IEnumerable<User> GetAllUsers() => _users;

        public User? GetUserById(Guid id)
        {
            var user = _users.FirstOrDefault(u => u.Id == id);
            if (user == null)
            {
                user = new User
                {
                    Id = id,
                    Username = "khach_demo",
                    FullName = "Khách Hàng Đặt Sân",
                    Phone = "0900000000",
                    Email = "guest@pitchai.com",
                    Role = UserRole.Customer,
                    WalletBalance = 3000000.00m
                };
                _users.Add(user);
            }
            return user;
        }

        public User? Register(string username, string fullName, string phone, string email, string password, UserRole role)
        {
            if (_users.Any(u => u.Username.Equals(username, StringComparison.OrdinalIgnoreCase) || u.Phone == phone || u.Email == email))
                return null;

            var user = new User
            {
                Id = Guid.NewGuid(),
                Username = username,
                FullName = fullName,
                Phone = phone,
                Email = email,
                Role = role,
                PasswordHash = HashPassword(password),
                WalletBalance = 3000000.00m
            };

            _users.Add(user);
            return user;
        }

        public (User? user, string token) Login(string usernameOrPhoneOrEmail, string password)
        {
            var user = _users.FirstOrDefault(u => 
                u.Username.Equals(usernameOrPhoneOrEmail, StringComparison.OrdinalIgnoreCase) || 
                u.Phone == usernameOrPhoneOrEmail || 
                u.Email == usernameOrPhoneOrEmail);

            if (user == null || !VerifyPassword(password, user.PasswordHash))
                return (null, string.Empty);

            var token = GenerateJwtToken(user);
            return (user, token);
        }

        public User? UpdateProfile(Guid userId, string fullName, string phone, string email)
        {
            var user = GetUserById(userId);
            if (user == null) return null;

            if (_users.Any(u => u.Id != userId && (u.Phone == phone || u.Email == email)))
            {
                return null;
            }

            user.FullName = fullName;
            user.Phone = phone;
            user.Email = email;

            return user;
        }

        public User? UpdateAvatar(Guid userId, string avatarUrl)
        {
            var user = GetUserById(userId);
            if (user == null) return null;

            user.AvatarUrl = avatarUrl;
            return user;
        }

        public (bool success, User? user, string username, string message) ForgotUsername(string phoneOrEmail)
        {
            var user = _users.FirstOrDefault(u => u.Phone == phoneOrEmail || u.Email.Equals(phoneOrEmail, StringComparison.OrdinalIgnoreCase));
            if (user == null)
            {
                return (false, null, string.Empty, "Không tìm thấy tài khoản liên kết với Số điện thoại hoặc Email này!");
            }

            return (true, user, user.Username, $"🎉 Tên đăng nhập của bạn là: {user.Username} (Họ tên: {user.FullName})");
        }

        public (bool success, User? user, string otp, string message) RequestPasswordReset(string usernameOrEmail)
        {
            var user = _users.FirstOrDefault(u => u.Username.Equals(usernameOrEmail, StringComparison.OrdinalIgnoreCase)
                                               || u.Phone == usernameOrEmail 
                                               || u.Email.Equals(usernameOrEmail, StringComparison.OrdinalIgnoreCase));
            if (user == null)
            {
                return (false, null, string.Empty, "Tài khoản hoặc Email không tồn tại!");
            }

            string otp = new Random().Next(100000, 999999).ToString();
            _otpStore[user.Email] = otp;
            _otpStore[user.Phone] = otp;
            _otpStore[user.Username] = otp;

            return (true, user, otp, $"Mã OTP khôi phục mật khẩu đã được tạo: {otp}");
        }

        public (bool success, string message) ResetPassword(string usernameOrEmail, string otp, string newPassword)
        {
            var user = _users.FirstOrDefault(u => u.Username.Equals(usernameOrEmail, StringComparison.OrdinalIgnoreCase)
                                               || u.Phone == usernameOrEmail 
                                               || u.Email.Equals(usernameOrEmail, StringComparison.OrdinalIgnoreCase));
            if (user == null)
            {
                return (false, "Tài khoản không tồn tại!");
            }

            bool otpValid = (_otpStore.TryGetValue(user.Email, out var validOtp1) && validOtp1 == otp)
                         || (_otpStore.TryGetValue(user.Phone, out var validOtp2) && validOtp2 == otp)
                         || (_otpStore.TryGetValue(user.Username, out var validOtp3) && validOtp3 == otp)
                         || (_otpStore.TryGetValue(usernameOrEmail, out var validOtp4) && validOtp4 == otp);

            if (!otpValid)
            {
                return (false, "Mã OTP không chính xác hoặc đã hết hạn!");
            }

            user.PasswordHash = HashPassword(newPassword);
            _otpStore.Remove(user.Email);
            _otpStore.Remove(user.Phone);
            _otpStore.Remove(user.Username);
            _otpStore.Remove(usernameOrEmail);

            return (true, "Đổi mật khẩu mới thành công! Vui lòng đăng nhập lại.");
        }

        public (bool success, string message) ResetPasswordDirect(string usernameOrEmail, string newPassword)
        {
            var user = _users.FirstOrDefault(u => u.Username.Equals(usernameOrEmail, StringComparison.OrdinalIgnoreCase)
                                               || u.Phone == usernameOrEmail 
                                               || u.Email.Equals(usernameOrEmail, StringComparison.OrdinalIgnoreCase));
            if (user == null)
            {
                return (false, "Không tìm thấy tài khoản tương ứng với thông tin đã nhập!");
            }

            user.PasswordHash = HashPassword(newPassword);
            return (true, "🎉 Khôi phục và đổi mật khẩu thành công! Bạn có thể dùng mật khẩu mới để đăng nhập ngay.");
        }

        public (bool success, string message) ChangePassword(Guid userId, string oldPassword, string newPassword)
        {
            var user = GetUserById(userId);
            if (user == null)
            {
                return (false, "Không tìm thấy tài khoản người dùng!");
            }

            if (!VerifyPassword(oldPassword, user.PasswordHash))
            {
                return (false, "Mật khẩu cũ không chính xác!");
            }

            user.PasswordHash = HashPassword(newPassword);
            return (true, "🎉 Đổi mật khẩu thành công!");
        }

        private static readonly List<DepositRequest> _depositRequests = new();

        public DepositRequest CreateDepositRequest(Guid userId, decimal amount, string transactionCode, string memo, string imageUrl)
        {
            var req = new DepositRequest
            {
                Id = Guid.NewGuid(),
                UserId = userId,
                Amount = amount,
                TransactionCode = transactionCode,
                Memo = memo,
                ImageUrl = imageUrl,
                Status = DepositStatus.Pending,
                CreatedAt = DateTime.UtcNow
            };
            _depositRequests.Add(req);
            return req;
        }

        public IEnumerable<object> GetAllDepositRequests()
        {
            return _depositRequests.OrderByDescending(r => r.CreatedAt).Select(r =>
            {
                var user = GetUserById(r.UserId);
                return new
                {
                    r.Id,
                    r.UserId,
                    UserName = user?.FullName ?? "N/A",
                    UserPhone = user?.Phone ?? "N/A",
                    UserEmail = user?.Email ?? "N/A",
                    r.Amount,
                    r.TransactionCode,
                    r.Memo,
                    r.ImageUrl,
                    Status = r.Status.ToString(),
                    r.CreatedAt,
                    r.ProcessedAt
                };
            });
        }

        public (bool success, string message) ApproveDepositRequest(Guid depositId)
        {
            var req = _depositRequests.FirstOrDefault(r => r.Id == depositId);
            if (req == null) return (false, "Không tìm thấy yêu cầu nạp tiền!");

            if (req.Status != DepositStatus.Pending)
            {
                return (false, $"Yêu cầu này đã được xử lý trước đó ({req.Status.ToString()})!");
            }

            var user = GetUserById(req.UserId);
            if (user == null) return (false, "Không tìm thấy tài khoản người dùng tương ứng!");

            req.Status = DepositStatus.Success;
            req.ProcessedAt = DateTime.UtcNow;

            user.WalletBalance += req.Amount;
            AddTransaction(user.Id, req.Amount, "TopupApproved", null);

            return (true, $"Đã duyệt nạp tiền! Cộng {req.Amount.ToString("N0")} VNĐ vào ví của {user.FullName}. Số dư mới: {user.WalletBalance.ToString("N0")} VNĐ.");
        }

        public (bool success, string message) RejectDepositRequest(Guid depositId)
        {
            var req = _depositRequests.FirstOrDefault(r => r.Id == depositId);
            if (req == null) return (false, "Không tìm thấy yêu cầu nạp tiền!");

            if (req.Status != DepositStatus.Pending)
            {
                return (false, $"Yêu cầu này đã được xử lý trước đó ({req.Status.ToString()})!");
            }

            req.Status = DepositStatus.Rejected;
            req.ProcessedAt = DateTime.UtcNow;

            return (true, "Đã từ chối yêu cầu nạp tiền này.");
        }

        public void AddTransaction(Guid userId, decimal amount, string type, Guid? bookingId)
        {
            _transactions.Add(new Transaction
            {
                TransactionId = Guid.NewGuid(),
                UserId = userId,
                Amount = amount,
                Type = type,
                BookingId = bookingId,
                CreatedAt = DateTime.UtcNow
            });
        }

        public bool RefundBookingTransaction(Guid userId, decimal amount, Guid bookingId)
        {
            var user = GetUserById(userId);
            if (user == null) return false;

            user.WalletBalance += amount;
            AddTransaction(userId, amount, "Refund", bookingId);

            return true;
        }

        private static string HashPassword(string password)
        {
            using var sha256 = SHA256.Create();
            var bytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(password));
            return Convert.ToBase64String(bytes);
        }

        private static bool VerifyPassword(string password, string storedHash)
        {
            return HashPassword(password) == storedHash;
        }

        private static string GenerateJwtToken(User user)
        {
            var tokenHandler = new JwtSecurityTokenHandler();
            var key = Encoding.ASCII.GetBytes(SecretKey);
            var tokenDescriptor = new SecurityTokenDescriptor
            {
                Subject = new ClaimsIdentity(new[]
                {
                    new Claim(ClaimTypes.NameIdentifier, user.Id.ToString()),
                    new Claim(ClaimTypes.Name, user.FullName),
                    new Claim(ClaimTypes.Role, user.Role.ToString())
                }),
                Expires = DateTime.UtcNow.AddDays(7),
                SigningCredentials = new SigningCredentials(new SymmetricSecurityKey(key), SecurityAlgorithms.HmacSha256Signature)
            };

            var token = tokenHandler.CreateToken(tokenDescriptor);
            return tokenHandler.WriteToken(token);
        }
    }
}
