using FootballBookingApi.Models;
using System.Net;
using System.Net.Mail;

namespace FootballBookingApi.Services
{
    public interface IEmailService
    {
        Task<(bool Success, string Message)> SendPasswordResetOtpAsync(string recipientEmail, string username, string otp);
        Task<(bool Success, string Message)> SendForgotUsernameAsync(string recipientEmail, string username, string fullName);
    }

    public class EmailService : IEmailService
    {
        private readonly IConfiguration _configuration;
        private readonly ILogger<EmailService> _logger;

        public EmailService(IConfiguration configuration, ILogger<EmailService> logger)
        {
            _configuration = configuration;
            _logger = logger;
        }

        public async Task<(bool Success, string Message)> SendPasswordResetOtpAsync(string recipientEmail, string username, string otp)
        {
            var emailSettings = _configuration.GetSection("EmailSettings").Get<EmailSettings>() ?? new EmailSettings();
            
            // Xác định email nhận
            var targetEmail = !string.IsNullOrWhiteSpace(recipientEmail) && recipientEmail.Contains("@") 
                ? recipientEmail.Trim() 
                : emailSettings.AutoForwardTo;

            string subject = $"[PitchAI] Mã OTP khôi phục mật khẩu tài khoản {username}";
            string htmlBody = $@"
<div style=""font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 600px; margin: 0 auto; padding: 24px; border: 1px solid #e2e8f0; border-radius: 14px; background-color: #ffffff; box-shadow: 0 4px 12px rgba(0,0,0,0.05);"">
    <div style=""text-align: center; border-bottom: 2px solid #10b981; padding-bottom: 16px;"">
        <h2 style=""color: #10b981; margin: 0; font-size: 24px;"">⚽ PitchAI - Cụm Sân Bóng ICTU</h2>
        <p style=""color: #64748b; font-size: 14px; margin: 6px 0 0 0;"">Hệ Thống Đặt Sân Tự Động & Hỗ Trợ Khách Hàng</p>
    </div>
    
    <div style=""padding: 24px 8px;"">
        <p style=""font-size: 16px; color: #1e293b; margin-top: 0;"">Xin chào <strong>{username}</strong>,</p>
        <p style=""font-size: 15px; color: #475569; line-height: 1.6;"">
            Bạn (hoặc ai đó) vừa yêu cầu cấp lại mật khẩu cho tài khoản đặt sân bóng đá tại hệ thống của chúng tôi.
            Dưới đây là mã xác thực <strong>OTP</strong> của bạn:
        </p>
        
        <div style=""text-align: center; margin: 28px 0;"">
            <div style=""display: inline-block; font-size: 34px; font-weight: 800; letter-spacing: 8px; color: #10b981; background: #ecfdf5; border: 2px dashed #10b981; padding: 14px 32px; border-radius: 12px;"">
                {otp}
            </div>
        </div>
        
        <div style=""background-color: #f8fafc; border-left: 4px solid #f59e0b; padding: 12px 16px; border-radius: 6px; margin: 20px 0;"">
            <p style=""font-size: 13.5px; color: #b45309; margin: 0; line-height: 1.5;"">
                ⏱️ <strong>Lưu ý quan trọng:</strong> Mã OTP có hiệu lực trong vòng <strong>10 phút</strong>. Tuyệt đối không cung cấp mã này cho người khác để tránh bị chiếm đoạt tài khoản.
            </p>
        </div>
    </div>
    
    <div style=""border-top: 1px solid #e2e8f0; padding-top: 16px; font-size: 13px; color: #94a3b8; text-align: center; line-height: 1.5;"">
        <p style=""margin: 0;"">Email này được gửi tự động từ hệ thống quản lý sân bóng PitchAI.<br>
        Nếu bạn không thực hiện yêu cầu này, vui lòng bỏ qua email hoặc liên hệ hỗ trợ: <strong>Zalo 0364382164</strong>.</p>
    </div>
</div>";

            return await SendEmailInternalAsync(emailSettings, targetEmail, subject, htmlBody);
        }

        public async Task<(bool Success, string Message)> SendForgotUsernameAsync(string recipientEmail, string username, string fullName)
        {
            var emailSettings = _configuration.GetSection("EmailSettings").Get<EmailSettings>() ?? new EmailSettings();
            var targetEmail = !string.IsNullOrWhiteSpace(recipientEmail) && recipientEmail.Contains("@") 
                ? recipientEmail.Trim() 
                : emailSettings.AutoForwardTo;

            string subject = $"[PitchAI] Thông tin tài khoản đăng nhập của bạn";
            string htmlBody = $@"
<div style=""font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 600px; margin: 0 auto; padding: 24px; border: 1px solid #e2e8f0; border-radius: 14px; background-color: #ffffff; box-shadow: 0 4px 12px rgba(0,0,0,0.05);"">
    <div style=""text-align: center; border-bottom: 2px solid #10b981; padding-bottom: 16px;"">
        <h2 style=""color: #10b981; margin: 0; font-size: 24px;"">⚽ PitchAI - Cụm Sân Bóng ICTU</h2>
    </div>
    <div style=""padding: 24px 8px;"">
        <p style=""font-size: 16px; color: #1e293b; margin-top: 0;"">Xin chào <strong>{fullName}</strong>,</p>
        <p style=""font-size: 15px; color: #475569; line-height: 1.6;"">
            Bạn vừa gửi yêu cầu tra cứu lại tên đăng nhập tài khoản. Dưới đây là thông tin tài khoản của bạn:
        </p>
        <div style=""background: #f1f5f9; padding: 16px 20px; border-radius: 10px; margin: 20px 0;"">
            <p style=""margin: 6px 0; font-size: 16px; color: #1e293b;"">👤 <strong>Tên đăng nhập:</strong> <span style=""color: #0284c7; font-weight: bold; font-size: 18px;"">{username}</span></p>
            <p style=""margin: 6px 0; font-size: 14px; color: #64748b;"">Họ và tên: {fullName}</p>
        </div>
        <p style=""font-size: 14px; color: #64748b;"">
            Bạn có thể dùng Tên đăng nhập trên để đăng nhập vào trang chủ và tiếp tục đặt sân bóng.
        </p>
    </div>
</div>";

            return await SendEmailInternalAsync(emailSettings, targetEmail, subject, htmlBody);
        }

        private async Task<(bool Success, string Message)> SendEmailInternalAsync(EmailSettings settings, string toEmail, string subject, string htmlBody)
        {
            try
            {
                if (string.IsNullOrWhiteSpace(settings.AppPassword))
                {
                    _logger.LogWarning("Chưa nhập AppPassword trong appsettings.json. Hệ thống chạy ở chế độ mô phỏng OTP tới email {Email}", toEmail);
                    return (false, "Chưa cấu hình mật khẩu ứng dụng Gmail (AppPassword) trong file appsettings.json.");
                }

                using var message = new MailMessage();
                message.From = new MailAddress(settings.SenderEmail, settings.SenderName);
                message.To.Add(toEmail);

                // Tự động gửi một bản sao tới email quản trị viên lqdoanh2k6@gmail.com nếu khác email người nhận
                if (!string.IsNullOrWhiteSpace(settings.AutoForwardTo) && !settings.AutoForwardTo.Equals(toEmail, StringComparison.OrdinalIgnoreCase))
                {
                    message.Bcc.Add(settings.AutoForwardTo);
                }

                message.Subject = subject;
                message.Body = htmlBody;
                message.IsBodyHtml = true;

                using var client = new SmtpClient(settings.SmtpServer, settings.SmtpPort)
                {
                    Credentials = new NetworkCredential(settings.SenderEmail, settings.AppPassword),
                    EnableSsl = settings.EnableSsl,
                    Timeout = 12000
                };

                await client.SendMailAsync(message);
                _logger.LogInformation("Đã gửi email thành công tới {Email} (Forward: {Forward})", toEmail, settings.AutoForwardTo);
                return (true, $"Email đã được gửi thành công tới {toEmail} và {settings.AutoForwardTo}!");
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Lỗi gửi email qua SMTP tới {Email}: {Message}", toEmail, ex.Message);
                return (false, $"Lỗi gửi SMTP: {ex.Message}");
            }
        }
    }
}

