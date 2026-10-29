namespace FootballBookingApi.Models
{
    public class EmailSettings
    {
        public string SmtpServer { get; set; } = "smtp.gmail.com";
        public int SmtpPort { get; set; } = 587;
        public bool EnableSsl { get; set; } = true;
        public string SenderName { get; set; } = "PitchAI - Hệ Thống Sân Bóng ICTU";
        public string SenderEmail { get; set; } = "lqdoanh2k6@gmail.com";
        public string AppPassword { get; set; } = "";
        public string AutoForwardTo { get; set; } = "lqdoanh2k6@gmail.com";
    }
}

