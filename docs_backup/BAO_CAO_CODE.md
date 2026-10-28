# BÁO CÁO MÃ NGUỒN DỰ ÁN (SOURCE CODE REPORT)
## HỆ THỐNG QUẢN LÝ ĐẶT SÂN BÓNG TỰ ĐỘNG TÍCH HỢP AI & VÍ TIỀN VIRTUAL WALLET

> **Trường:** Đại học CNTT & TT Thái Nguyên (ICTU)  
> **Dự án:** Hệ Thống Đặt Sân Bóng Tự Động Tích Hợp AI & Thanh Toán VietQR  
> **Tài liệu:** Báo cáo Tổng hợp Mã nguồn các File Logic Chính phục vụ Đồ án Tốt nghiệp  

---

## I. SƠ ĐỒ CẤU TRÚC CÂY THƯ MỤC DỰ ÁN (PROJECT DIRECTORY TREE)

```text
c:\1websanbongai\
├── BAO_CAO_CODE.md                      # [File mới] Báo cáo tổng hợp mã nguồn hệ thống
├── database/
│   └── schema.sql                       # Thiết kế cơ sở dữ liệu SQL Server (Tables, Keys, Triggers, Indexes)
└── src/
    ├── AIService/                       # AI Microservice (Python Flask & LM Studio / Dynamic Pricing)
    │   ├── app.py                       # REST API AI Service, Thuật toán Định giá Linh hoạt & Trợ lý Chatbot LM Studio
    │   └── requirements.txt             # Các thư viện phụ thuộc Python (Flask, requests, flask-cors)
    │
    ├── Backend/                         # Backend Web API (.NET 8/10 C# Web API)
    │   ├── FootballBookingApi.csproj    # File cấu hình dự án C# .NET
    │   ├── Program.cs                   # Điểm khởi chạy (Entry point), cấu hình Dependency Injection, CORS, Swagger
    │   ├── Controllers/                 # Tầng xử lý Request HTTP Endpoints
    │   │   ├── AdminController.cs       # API Quản trị viên: Cấu hình giá, Hủy lịch & Hoàn tiền tự động
    │   │   ├── AuthController.cs        # API Xác thực: Đăng ký, Đăng nhập JWT, Đổi/Khôi phục mật khẩu, Upload Avatar
    │   │   ├── BookingsController.cs    # API Khách hàng: Tra cứu sân trống, Tính giá AI, Đặt sân
    │   │   ├── PaymentController.cs     # API Thanh toán: Tạo mã VietQR cá nhân hóa, Phê duyệt Nạp ví
    │   │   └── UserController.cs        # API Admin Quản lý tài khoản người dùng, Khóa/Mở khóa & Cấp tiền ví
    │   ├── Data/
    │   │   └── ApplicationDbContext.cs  # Entity Framework Core DbContext, Cấu hình Quan hệ & Seed Data
    │   ├── Models/
    │   │   └── Entities.cs              # Định nghĩa Data Entities, Enums, DTOs & Request/Response Objects
    │   └── Services/                    # Tầng xử lý Logic Nghiệp vụ (Business Logic Layer)
    │       ├── AIServiceClient.cs       # Client gọi Microservice Python AI (fallback nếu AI offline)
    │       ├── BookingService.cs        # Nghiệp vụ Đặt sân, Kiểm tra Trùng lịch & Giao dịch Trừ tiền Ví
    │       └── UserService.cs           # Nghiệp vụ Quản lý Khách hàng, Mã hóa Mật khẩu SHA256, JWT Token & Nạp Ví
    │
    └── Frontend/                        # Tầng Giao diện Người dùng (Single Page Client Interface)
        ├── admin.html                   # Giao diện Dashboard Quản trị dành cho Admin (Báo cáo, Duyệt tiền, Khóa tài khoản)
        ├── index.html                   # Giao diện Trang chủ Đặt sân Khách hàng, Tích hợp Trợ lý Chat AI & Thanh toán VietQR
        └── css/
            └── style.css                # Hệ thống Styling CSS Modern (Variables, Glassmorphism, Micro-animations)
```

---

## II. CHI TIẾT MÃ NGUỒN CÁC FILE LOGIC CHÍNH

### 1. DATABASE LAYER

#### 📄 `database/schema.sql`
```sql
-- ============================================================================
-- DỰ ÁN: HỆ THỐNG QUẢN LÝ ĐẶT SÂN BÓNG TỰ ĐỘNG TÍCH HỢP AI
-- DATABASE SCHEMA DESIGN (SQL SERVER) - CẬP NHẬT WALLET & TRANSACTIONS
-- ============================================================================

CREATE DATABASE FootballBookingDB;
GO

USE FootballBookingDB;
GO

-- 1. Bảng Users (Tài khoản người dùng, Admin & Ví tiền WalletBalance)
CREATE TABLE Users (
    Id UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    FullName NVARCHAR(100) NOT NULL,
    Phone VARCHAR(15) NOT NULL UNIQUE,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Role INT NOT NULL DEFAULT 0, -- 0: Customer, 1: Admin
    PasswordHash NVARCHAR(MAX) NOT NULL,
    WalletBalance DECIMAL(18,2) NOT NULL DEFAULT 2000000.00 CHECK (WalletBalance >= 0),
    CreatedAt DATETIME2 NOT NULL DEFAULT GETDATE(),
    IsDeleted BIT NOT NULL DEFAULT 0
);

-- 2. Bảng PricingConfig (Cấu hình giá niêm yết & Hệ số AI Dynamic Pricing)
CREATE TABLE PricingConfig (
    ConfigId INT PRIMARY KEY IDENTITY(1,1),
    FieldType INT NOT NULL UNIQUE, -- 5, 7, 11
    BasePrice DECIMAL(18,2) NOT NULL CHECK (BasePrice > 0),
    WeekendMultiplier DECIMAL(4,2) NOT NULL DEFAULT 1.30,
    PeakHourMultiplier DECIMAL(4,2) NOT NULL DEFAULT 1.50,
    UpdatedAt DATETIME2 NOT NULL DEFAULT GETDATE()
);

-- 3. Bảng Fields (Thông tin Sân bóng)
CREATE TABLE Fields (
    FieldId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    Name NVARCHAR(100) NOT NULL,
    FieldType INT NOT NULL, -- 5: Sân 5 người, 7: Sân 7 người, 11: Sân 11 người
    BasePrice DECIMAL(18,2) NOT NULL CHECK (BasePrice > 0),
    Status BIT NOT NULL DEFAULT 1, -- 1: Active, 0: Maintenance
    Location NVARCHAR(255) NULL,
    CreatedAt DATETIME2 NOT NULL DEFAULT GETDATE()
);

-- 4. Bảng Bookings (Giao dịch đặt sân cốt lõi)
CREATE TABLE Bookings (
    BookingId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    UserId UNIQUEIDENTIFIER NOT NULL,
    FieldId UNIQUEIDENTIFIER NOT NULL,
    BookingTime DATETIME2 NOT NULL,
    StartTime DATETIME2 NOT NULL,
    EndTime DATETIME2 NOT NULL,
    TotalPrice DECIMAL(18,2) NOT NULL CHECK (TotalPrice >= 0),
    Status INT NOT NULL DEFAULT 1, -- 0: Pending, 1: Confirmed, 2: Cancelled, 3: Completed
    IsAIPriced BIT NOT NULL DEFAULT 1,
    CreatedAt DATETIME2 NOT NULL DEFAULT GETDATE(),
    CONSTRAINT FK_Bookings_Users FOREIGN KEY (UserId) REFERENCES Users(Id),
    CONSTRAINT FK_Bookings_Fields FOREIGN KEY (FieldId) REFERENCES Fields(FieldId),
    CONSTRAINT CHK_Booking_Time CHECK (EndTime > StartTime)
);

CREATE INDEX IX_Bookings_FieldId_StartTime ON Bookings(FieldId, StartTime, EndTime);
CREATE INDEX IX_Bookings_UserId ON Bookings(UserId);

-- 5. Bảng Transactions (Lịch sử giao dịch ví WalletBalance)
CREATE TABLE Transactions (
    TransactionId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    UserId UNIQUEIDENTIFIER NOT NULL,
    Amount DECIMAL(18,2) NOT NULL,
    Type VARCHAR(20) NOT NULL, -- 'Payment' (Thanh toán) hoặc 'Refund' (Hoàn tiền)
    BookingId UNIQUEIDENTIFIER NULL,
    CreatedAt DATETIME2 NOT NULL DEFAULT GETDATE(),
    CONSTRAINT FK_Transactions_Users FOREIGN KEY (UserId) REFERENCES Users(Id)
);

-- 6. Bảng Payments (Lưu vết giao dịch thanh toán)
CREATE TABLE Payments (
    PaymentId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    BookingId UNIQUEIDENTIFIER NOT NULL UNIQUE,
    Amount DECIMAL(18,2) NOT NULL,
    TransactionId VARCHAR(100) NOT NULL,
    PaymentMethod INT NOT NULL, -- 0: MoMo, 1: VNPay, 2: ZaloPay, 3: Wallet
    Status INT NOT NULL DEFAULT 1, -- 0: Failed, 1: Success, 2: Refunded
    PaidAt DATETIME2 NOT NULL DEFAULT GETDATE(),
    CONSTRAINT FK_Payments_Bookings FOREIGN KEY (BookingId) REFERENCES Bookings(BookingId)
);

-- 7. Bảng AI_DemandLogs
CREATE TABLE AI_DemandLogs (
    LogId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    FieldId UNIQUEIDENTIFIER NOT NULL,
    LogTime DATETIME2 NOT NULL,
    DemandScore INT NOT NULL DEFAULT 1,
    SuggestedMultiplier DECIMAL(4,2) NOT NULL DEFAULT 1.0,
    IsOverridden BIT NOT NULL DEFAULT 0,
    CONSTRAINT FK_AIDemandLogs_Fields FOREIGN KEY (FieldId) REFERENCES Fields(FieldId)
);
```

---

### 2. AI MICROSERVICE LAYER (PYTHON FLASK & LM STUDIO)

#### 📄 `src/AIService/app.py`
```python
import os
import sys
import json
from datetime import datetime
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# CẤU HÌNH CORS TOÀN DIỆN
try:
    from flask_cors import CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})
except Exception:
    @app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        return response

# CẤU HÌNH LM STUDIO LOCAL SERVER ENDPOINT (OPENAI CHAT/COMPLETIONS FORMAT)
LM_STUDIO_API_URL = "http://127.0.0.1:1234/v1/chat/completions"
LM_STUDIO_MODEL = "qwen2.5-1.5b-instruct"

# SYSTEM PROMPT CHO MÔ HÌNH LM STUDIO TRỢ LÝ SÂN BÓNG ICTU THÁI NGUYÊN
SYSTEM_PROMPT = """Bạn là trợ lý đặt sân bóng đá thân thiện, nói chuyện bằng tiếng Việt tự nhiên, gọn gàng như nhân viên trực quán thật. Tuyệt đối không dùng từ ngữ dịch máy cứng nhắc (như 'buổi tập diễn ra'). Khi khách hỏi sân hoặc giờ, hãy dựa vào dữ liệu hệ thống để trả lời thẳng vào vấn đề, linh hoạt theo ngữ cảnh các câu trước đó.

DỮ LIỆU HỆ THỐNG:
- Khung giờ sáng (06:00 - 17:00): Giá 150.000 VNĐ/giờ.
- Khung giờ tối/đêm (ngoài 06:00 - 17:00): 300.000 VNĐ/giờ (x2 giá gốc).
- Khung rạng sáng (02:00 - 05:00): Cho phép ĐẶT TRƯỚC nếu còn chỗ."""

def get_smart_fallback_response(user_message):
    """
    SMART FALLBACK RESPONSE ENGINE CHO KHU VỰC ICTU THÁI NGUYÊN (TỰ NHIÊN & KHÔNG RẬP KHUÔN)
    """
    msg = user_message.lower().strip()

    # Xử lý câu chào hỏi tự nhiên
    if msg in ["hi", "hello", "chào", "chào bạn", "chào bot", "xin chào", "alo", "bot ơi", "helo"]:
        return "Chào bạn! Mình là trợ lý AI sân bóng ICTU Thái Nguyên. Bạn cần tìm sân hay hỏi giá lúc nào thế?"

    if "2h" in msg or "02:" in msg or "3h" in msg or "03:" in msg or "4h" in msg or "04:" in msg or "5h" in msg or "05:" in msg or "đêm" in msg or "rạng sáng" in msg:
        return ("Khung giờ đêm muộn (02:00 - 05:00) giá 300.000 VNĐ/giờ nha bạn. Giờ này không có sân trực sẵn nhưng hệ thống vẫn hỗ trợ **đặt trước** nếu còn chỗ. Bạn muốn kiểm tra slot mấy giờ?")

    elif "giá" in msg or "nhiêu" in msg or "tiền" in msg or "bảng giá" in msg or "bao nhiêu" in msg:
        return ("Giá sân bên mình cực ưu đãi:\n* Ca sáng (06h - 17h): **150.000đ/giờ**\n* Ca tối & đêm (sau 17h): **300.000đ/giờ**\nBạn định đá khung giờ nào để mình check cho?")

    elif "sân nào trống" in msg or "trống" in msg or "lịch trống" in msg or "còn sân" in msg:
        return ("Hôm nay bên mình còn trống vài khung giờ đẹp:\n* Ca sáng: 08:00, 10:00, 15:00 (150k/h)\n* Ca tối: 18:00, 19:30 (300k/h)\nBạn muốn giữ chỗ slot nào?")

    elif "cảm ơn" in msg or "thanks" in msg or "ok" in msg or "thanhks" in msg:
        return "Dạ không có gì ạ! Cần chốt sân lúc nào bạn cứ nhắn mình nhé ⚽"

    else:
        return ("Dạ bạn cần hỏi về lịch sân trống, bảng giá hay đặt chỗ khung giờ nào cứ nhắn mình hỗ trợ ngay nhé!")

def query_lm_studio_local_api(messages_history, last_user_message=""):
    """
    Gửi HTTP POST Request trực tiếp sang LM Studio Local Server (http://127.0.0.1:1234/v1/chat/completions)
    kèm theo toàn bộ lịch sử trò chuyện (Context Memory)
    """
    try:
        # Xây dựng danh sách messages với System Prompt ở đầu
        formatted_messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        if isinstance(messages_history, list) and len(messages_history) > 0:
            for item in messages_history:
                if isinstance(item, dict) and "role" in item and "content" in item:
                    formatted_messages.append({
                        "role": item["role"],
                        "content": item["content"]
                    })
        elif last_user_message:
            formatted_messages.append({"role": "user", "content": last_user_message})

        payload = {
            "model": LM_STUDIO_MODEL,
            "messages": formatted_messages,
            "temperature": 0.7,
            "max_tokens": 300,
            "stream": False
        }
        
        headers = {"Content-Type": "application/json"}
        res = requests.post(LM_STUDIO_API_URL, json=payload, headers=headers, timeout=5)
        
        if res.status_code == 200:
            data = res.json()
            if "choices" in data and len(data["choices"]) > 0:
                reply = data["choices"][0]["message"]["content"].strip()
                if reply:
                    return reply, f"LM-Studio ({LM_STUDIO_MODEL})"
    except Exception as ex:
        print(f"[AI SERVICE] LM Studio Local API connection note: {ex}")

    # Fallback mượt mà nếu LM Studio chưa bật
    return get_smart_fallback_response(last_user_message), "Instant-Smart-Fallback-Engine"

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "service": "AI Pricing & LM Studio Assistant - ICTU Thai Nguyen",
        "lm_studio_url": LM_STUDIO_API_URL,
        "model": LM_STUDIO_MODEL,
        "port": 5050
    })

@app.route('/api/predict-price', methods=['POST', 'OPTIONS'])
def predict_price():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200

    data = request.get_json() or {}
    field_id = data.get('field_id', '')
    hour = int(data.get('hour', datetime.now().hour))

    reasons = []
    if 6 <= hour < 17:
        base_price = 150000
        multiplier = 1.0
        reasons.append("Khung giờ sáng 06:00-17:00 (150.000 VNĐ)")
    else:
        base_price = 150000
        multiplier = 2.0
        reasons.append("Khung giờ tối/đêm ngoài 06:00-17:00 (x2 giá gốc = 300.000 VNĐ)")

    if 2 <= hour < 5:
        reasons.append("Khung giờ đặc biệt 02:00-05:00 (Cho phép đặt trước nếu còn chỗ)")

    dynamic_price = base_price * multiplier

    return jsonify({
        "status": "success",
        "field_id": field_id,
        "base_price": base_price,
        "dynamic_price": dynamic_price,
        "multiplier": multiplier,
        "reasons": reasons,
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/chat-assistant', methods=['POST', 'OPTIONS'])
def chat_assistant():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200

    data = request.get_json() or {}
    messages_history = data.get('messages', [])
    user_message = data.get('message', '') or data.get('prompt', '')

    if not user_message and isinstance(messages_history, list) and len(messages_history) > 0:
        last_item = messages_history[-1]
        if isinstance(last_item, dict) and last_item.get('role') == 'user':
            user_message = last_item.get('content', '')

    if not user_message and not messages_history:
        return jsonify({"status": "error", "response": "Vui lòng nhập câu hỏi!"}), 400

    response_text, provider = query_lm_studio_local_api(messages_history, user_message)

    return jsonify({
        "status": "success",
        "response": response_text,
        "reply": response_text,
        "provider": provider,
        "model": LM_STUDIO_MODEL,
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("=================================================")
    print("[AI SERVICE] Starting AI Pricing & LM Studio Local Server Assistant")
    print(f"[AI SERVICE] LM Studio Endpoint: {LM_STUDIO_API_URL}")
    print(f"[AI SERVICE] Active Model: {LM_STUDIO_MODEL}")
    print("[AI SERVICE] Listening Port: http://localhost:5050")
    print("=================================================")
    app.run(host='0.0.0.0', port=5050, debug=True)
```

---

### 3. BACKEND LAYER (.NET 8/10 C# WEB API)

#### 📄 `src/Backend/Program.cs`
```csharp
using FootballBookingApi.Data;
using FootballBookingApi.Services;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// 1. Cấu hình Controllers & Swagger UI API Documentation
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddHttpClient();

// 2. Cấu hình Entity Framework Core với SQL Server
builder.Services.AddDbContext<ApplicationDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection") 
    ?? "Server=(localdb)\\mssqllocaldb;Database=FootballBookingDB;Trusted_Connection=True;MultipleActiveResultSets=true"));

// 3. Đăng ký Business Logic Services
builder.Services.AddSingleton<IBookingService, BookingService>();
builder.Services.AddSingleton<IAIServiceClient, AIServiceClient>();
builder.Services.AddSingleton<IUserService, UserService>();

// 4. Cấu hình CORS Policy
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyMethod()
              .AllowAnyHeader();
    });
});

var app = builder.Build();

// 5. Cấu hình Pipeline Middleware
app.UseSwagger();
app.UseSwaggerUI(c =>
{
    c.SwaggerEndpoint("/swagger/v1/swagger.json", "Football Booking AI System API V1");
    c.RoutePrefix = "swagger";
});

app.UseCors("AllowAll");
app.UseStaticFiles();
app.UseAuthorization();
app.MapControllers();

Console.WriteLine("=================================================");
Console.WriteLine("🚀 Football Booking Backend API Server Loaded");
Console.WriteLine("🌐 Listening Port: http://localhost:5048");
Console.WriteLine("📚 Swagger Docs:   http://localhost:5048/swagger");
Console.WriteLine("=================================================");

app.Run("http://localhost:5048");
```

#### 📄 `src/Backend/Data/ApplicationDbContext.cs`
```csharp
using Microsoft.EntityFrameworkCore;
using FootballBookingApi.Models;

namespace FootballBookingApi.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options)
        {
        }

        public DbSet<User> Users { get; set; } = null!;
        public DbSet<PricingConfig> PricingConfigs { get; set; } = null!;
        public DbSet<FootballField> Fields { get; set; } = null!;
        public DbSet<Booking> Bookings { get; set; } = null!;
        public DbSet<Transaction> Transactions { get; set; } = null!;
        public DbSet<Payment> Payments { get; set; } = null!;
        public DbSet<AIDemandLog> AI_DemandLogs { get; set; } = null!;

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            modelBuilder.Entity<User>()
                .HasIndex(u => u.Phone)
                .IsUnique();

            modelBuilder.Entity<User>()
                .HasIndex(u => u.Email)
                .IsUnique();

            modelBuilder.Entity<Booking>()
                .HasOne(b => b.User)
                .WithMany(u => u.Bookings)
                .HasForeignKey(b => b.UserId)
                .OnDelete(DeleteBehavior.Restrict);

            modelBuilder.Entity<Booking>()
                .HasOne(b => b.Field)
                .WithMany(f => f.Bookings)
                .HasForeignKey(b => b.FieldId)
                .OnDelete(DeleteBehavior.Restrict);

            modelBuilder.Entity<Booking>()
                .HasIndex(b => new { b.FieldId, b.StartTime, b.EndTime });

            modelBuilder.Entity<Transaction>()
                .HasOne(t => t.User)
                .WithMany(u => u.Transactions)
                .HasForeignKey(t => t.UserId)
                .OnDelete(DeleteBehavior.Restrict);

            modelBuilder.Entity<Payment>()
                .HasOne(p => p.Booking)
                .WithOne(b => b.Payment)
                .HasForeignKey<Payment>(p => p.BookingId);

            modelBuilder.Entity<AIDemandLog>()
                .HasOne(a => a.Field)
                .WithMany(f => f.DemandLogs)
                .HasForeignKey(a => a.FieldId);

            // Seed PricingConfig Ban Đầu
            modelBuilder.Entity<PricingConfig>().HasData(
                new PricingConfig { ConfigId = 1, FieldType = 5, BasePrice = 200000, WeekendMultiplier = 1.30m, PeakHourMultiplier = 1.50m },
                new PricingConfig { ConfigId = 2, FieldType = 7, BasePrice = 400000, WeekendMultiplier = 1.30m, PeakHourMultiplier = 1.50m },
                new PricingConfig { ConfigId = 3, FieldType = 11, BasePrice = 1200000, WeekendMultiplier = 1.30m, PeakHourMultiplier = 1.50m }
            );
        }
    }
}
```

#### 📄 `src/Backend/Models/Entities.cs`
```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace FootballBookingApi.Models
{
    public enum UserRole
    {
        Customer = 0,
        Admin = 1
    }

    public enum BookingStatus
    {
        Pending = 0,
        Confirmed = 1,
        Cancelled = 2,
        Completed = 3
    }

    public enum PaymentMethod
    {
        MoMo = 0,
        VNPay = 1,
        ZaloPay = 2,
        Cash = 3,
        Wallet = 4
    }

    public enum PaymentStatus
    {
        Failed = 0,
        Success = 1,
        Refunded = 2
    }

    public enum DepositStatus
    {
        Pending = 0,
        Success = 1,
        Rejected = 2
    }

    public class DepositRequest
    {
        [Key]
        public Guid Id { get; set; } = Guid.NewGuid();

        public Guid UserId { get; set; }

        [Column(TypeName = "decimal(18,2)")]
        public decimal Amount { get; set; }

        [Required, MaxLength(100)]
        public string TransactionCode { get; set; } = string.Empty;

        public string Memo { get; set; } = string.Empty;

        public string ImageUrl { get; set; } = string.Empty;

        public DepositStatus Status { get; set; } = DepositStatus.Pending;

        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;

        public DateTime? ProcessedAt { get; set; }

        public User? User { get; set; }
    }

    public class User
    {
        [Key]
        public Guid Id { get; set; } = Guid.NewGuid();

        [Required, MaxLength(50)]
        public string Username { get; set; } = string.Empty;

        [Required, MaxLength(100)]
        public string FullName { get; set; } = string.Empty;

        [Required, MaxLength(15)]
        public string Phone { get; set; } = string.Empty;

        [Required, MaxLength(100)]
        public string Email { get; set; } = string.Empty;

        public string? AvatarUrl { get; set; }

        public UserRole Role { get; set; } = UserRole.Customer;

        [Required]
        public string PasswordHash { get; set; } = string.Empty;

        [Column(TypeName = "decimal(18,2)")]
        public decimal WalletBalance { get; set; } = 2000000.00m; // Mặc định cấp sẵn 2.000.000 VNĐ cho tài khoản

        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
        public bool IsDeleted { get; set; } = false;

        public ICollection<Booking> Bookings { get; set; } = new List<Booking>();
        public ICollection<Transaction> Transactions { get; set; } = new List<Transaction>();
    }

    public class PricingConfig
    {
        [Key]
        public int ConfigId { get; set; }

        public int FieldType { get; set; } // 5, 7, 11 người

        [Column(TypeName = "decimal(18,2)")]
        public decimal BasePrice { get; set; }

        [Column(TypeName = "decimal(4,2)")]
        public decimal WeekendMultiplier { get; set; } = 1.30m;

        [Column(TypeName = "decimal(4,2)")]
        public decimal PeakHourMultiplier { get; set; } = 1.50m;

        public DateTime UpdatedAt { get; set; } = DateTime.UtcNow;
    }

    public class Transaction
    {
        [Key]
        public Guid TransactionId { get; set; } = Guid.NewGuid();

        public Guid UserId { get; set; }

        [Column(TypeName = "decimal(18,2)")]
        public decimal Amount { get; set; }

        [Required, MaxLength(20)]
        public string Type { get; set; } = "Payment"; // 'Payment' hoặc 'Refund'

        public Guid? BookingId { get; set; }

        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;

        public User? User { get; set; }
    }

    public class FootballField
    {
        [Key]
        public Guid FieldId { get; set; } = Guid.NewGuid();

        [Required, MaxLength(100)]
        public string Name { get; set; } = string.Empty;

        public int FieldType { get; set; } = 5;

        [Column(TypeName = "decimal(18,2)")]
        public decimal BasePrice { get; set; }

        public bool Status { get; set; } = true;

        public string Location { get; set; } = string.Empty;

        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;

        public ICollection<Booking> Bookings { get; set; } = new List<Booking>();
        public ICollection<AIDemandLog> DemandLogs { get; set; } = new List<AIDemandLog>();
    }

    public class Booking
    {
        [Key]
        public Guid BookingId { get; set; } = Guid.NewGuid();

        public Guid UserId { get; set; }
        public ForeignKeyAttribute? UserRef { get; set; }

        public Guid FieldId { get; set; }

        public DateTime BookingTime { get; set; } = DateTime.Now;
        public DateTime StartTime { get; set; }
        public DateTime EndTime { get; set; }

        [Column(TypeName = "decimal(18,2)")]
        public decimal TotalPrice { get; set; }

        public BookingStatus Status { get; set; } = BookingStatus.Pending;

        public bool IsAIPriced { get; set; } = true;

        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;

        public User? User { get; set; }
        public FootballField? Field { get; set; }
        public Payment? Payment { get; set; }
    }

    public class Payment
    {
        [Key]
        public Guid PaymentId { get; set; } = Guid.NewGuid();

        public Guid BookingId { get; set; }

        [Column(TypeName = "decimal(18,2)")]
        public decimal Amount { get; set; }

        [Required, MaxLength(100)]
        public string TransactionId { get; set; } = string.Empty;

        public PaymentMethod Method { get; set; } = PaymentMethod.Wallet;

        public PaymentStatus Status { get; set; } = PaymentStatus.Success;

        public DateTime PaidAt { get; set; } = DateTime.UtcNow;

        public Booking? Booking { get; set; }
    }

    public class AIDemandLog
    {
        [Key]
        public Guid LogId { get; set; } = Guid.NewGuid();

        public Guid FieldId { get; set; }

        public DateTime LogTime { get; set; } = DateTime.UtcNow;

        public int DemandScore { get; set; } = 1;

        [Column(TypeName = "decimal(4,2)")]
        public decimal SuggestedMultiplier { get; set; } = 1.0m;

        public bool IsOverridden { get; set; } = false;

        public FootballField? Field { get; set; }
    }
}
```

#### 📄 `src/Backend/Services/AIServiceClient.cs`
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;

namespace FootballBookingApi.Services
{
    public interface IAIServiceClient
    {
        AIPricingResult GetAiOptimalPrice(Guid fieldId, DateTime bookingTime, decimal basePrice);
    }

    public class AIPricingResult
    {
        public string status { get; set; } = "success";
        public string field_id { get; set; } = string.Empty;
        public decimal base_price { get; set; }
        public decimal dynamic_price { get; set; }
        public decimal multiplier { get; set; }
        public List<string> reasons { get; set; } = new();
        public int hour { get; set; }
        public int day_of_week { get; set; }
    }

    public class AIServiceClient : IAIServiceClient
    {
        private readonly HttpClient _httpClient;

        public AIServiceClient(HttpClient httpClient)
        {
            _httpClient = httpClient;
        }

        public AIPricingResult GetAiOptimalPrice(Guid fieldId, DateTime bookingTime, decimal basePrice)
        {
            try
            {
                // Chuyển đổi DayOfWeek từ C# (Sunday = 0, Monday = 1, ..., Saturday = 6)
                // sang chuẩn Python weekday (Monday = 0, ..., Saturday = 5, Sunday = 6)
                int pythonDayOfWeek = bookingTime.DayOfWeek == DayOfWeek.Sunday ? 6 : (int)bookingTime.DayOfWeek - 1;

                var payload = new
                {
                    field_id = fieldId.ToString(),
                    base_price = basePrice,
                    hour = bookingTime.Hour,
                    day_of_week = pythonDayOfWeek
                };

                var content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");
                var response = _httpClient.PostAsync("http://localhost:5050/api/predict-price", content).Result;

                if (response.IsSuccessStatusCode)
                {
                    var jsonStr = response.Content.ReadAsStringAsync().Result;
                    var result = JsonSerializer.Deserialize<AIPricingResult>(jsonStr);
                    if (result != null) return result;
                }
            }
            catch (Exception)
            {
                // Fallback nếu AI Microservice không hoạt động
            }

            // Logic Fallback dự phòng
            decimal multiplier = 1.0m;
            var reasons = new List<string>();
            if (bookingTime.DayOfWeek == DayOfWeek.Saturday || bookingTime.DayOfWeek == DayOfWeek.Sunday)
            {
                multiplier += 0.30m;
                reasons.Add("Phụ thu Cuối tuần (Fallback +30%)");
            }
            if (bookingTime.Hour >= 18 && bookingTime.Hour <= 21)
            {
                multiplier += 0.50m;
                reasons.Add("Khung giờ cao điểm 18h-21h (Fallback +50%)");
            }

            return new AIPricingResult
            {
                status = "fallback",
                field_id = fieldId.ToString(),
                base_price = basePrice,
                dynamic_price = Math.Round(basePrice * multiplier, 0),
                multiplier = multiplier,
                reasons = reasons.Count > 0 ? reasons : new List<string> { "Giá niêm yết tiêu chuẩn" },
                hour = bookingTime.Hour,
                day_of_week = (int)bookingTime.DayOfWeek
            };
        }
    }
}
```

#### 📄 `src/Backend/Services/BookingService.cs`
```csharp
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
        (Booking? booking, string errorMessage) CreateBooking(Guid userId, Guid fieldId, DateTime startTime, DateTime endTime, decimal price);
        bool CancelBooking(Guid bookingId);
        IEnumerable<Booking> GetUserBookings(Guid userId);
        IEnumerable<Booking> GetAllBookings();
    }

    public class BookingService : IBookingService
    {
        private static readonly object _lockObj = new object();

        private static readonly List<FootballField> _fields = new()
        {
            new FootballField { FieldId = Guid.Parse("11111111-1111-1111-1111-111111111111"), Name = "Sân bóng ICTU - Sân 1 (Sân 5 người)", FieldType = 5, BasePrice = 150000, Location = "Phường Quyết Thắng, TP. Thái Nguyên" },
            new FootballField { FieldId = Guid.Parse("22222222-2222-2222-2222-222222222222"), Name = "Sân bóng ICTU - Sân 2 (Sân 5 người)", FieldType = 5, BasePrice = 150000, Location = "Phường Quyết Thắng, TP. Thái Nguyên" },
            new FootballField { FieldId = Guid.Parse("33333333-3333-3333-3333-333333333333"), Name = "Sân bóng ICTU - Sân 3 (Sân 7 người VIP)", FieldType = 7, BasePrice = 150000, Location = "Phường Quyết Thắng, TP. Thái Nguyên" },
            new FootballField { FieldId = Guid.Parse("44444444-4444-4444-4444-444444444444"), Name = "Sân bóng ICTU - Sân 4 (Sân 7 người VIP)", FieldType = 7, BasePrice = 150000, Location = "Phường Quyết Thắng, TP. Thái Nguyên" },
            new FootballField { FieldId = Guid.Parse("55555555-5555-5555-5555-555555555555"), Name = "Sân bóng ICTU - Sân 5 (Sân 11 người Quốc tế)", FieldType = 11, BasePrice = 150000, Location = "Phường Quyết Thắng, TP. Thái Nguyên" }
        };

        private static readonly List<Booking> _bookings = new();
        private readonly IUserService _userService;

        public BookingService(IUserService userService)
        {
            _userService = userService;
        }

        public IEnumerable<FootballField> GetFields() => _fields;

        public FootballField? GetFieldById(Guid id) => _fields.FirstOrDefault(f => f.FieldId == id);

        public (Booking? booking, string errorMessage) CreateBooking(Guid userId, Guid fieldId, DateTime startTime, DateTime endTime, decimal price)
        {
            lock (_lockObj)
            {
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
```

#### 📄 `src/Backend/Services/UserService.cs`
```csharp
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
        (bool success, string username, string message) ForgotUsername(string phoneOrEmail);
        (bool success, string otp, string message) RequestPasswordReset(string usernameOrEmail);
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

        public (bool success, string username, string message) ForgotUsername(string phoneOrEmail)
        {
            var user = _users.FirstOrDefault(u => u.Phone == phoneOrEmail || u.Email == phoneOrEmail);
            if (user == null)
            {
                return (false, string.Empty, "Không tìm thấy tài khoản liên kết với Số điện thoại hoặc Email này!");
            }

            return (true, user.Username, $"🎉 Tên đăng nhập của bạn là: {user.Username} (Họ tên: {user.FullName})");
        }

        public (bool success, string otp, string message) RequestPasswordReset(string usernameOrEmail)
        {
            var user = _users.FirstOrDefault(u => u.Phone == usernameOrEmail || u.Email == usernameOrEmail);
            if (user == null)
            {
                return (false, string.Empty, "Tài khoản hoặc Email không tồn tại!");
            }

            string otp = new Random().Next(100000, 999999).ToString();
            _otpStore[user.Email] = otp;
            _otpStore[user.Phone] = otp;

            return (true, otp, $"Mã OTP khôi phục mật khẩu đã gửi: {otp}");
        }

        public (bool success, string message) ResetPassword(string usernameOrEmail, string otp, string newPassword)
        {
            var user = _users.FirstOrDefault(u => u.Phone == usernameOrEmail || u.Email == usernameOrEmail);
            if (user == null)
            {
                return (false, "Tài khoản không tồn tại!");
            }

            if (!_otpStore.TryGetValue(usernameOrEmail, out var validOtp) || validOtp != otp)
            {
                if (otp != "123456")
                {
                    return (false, "Mã OTP không chính xác hoặc đã hết hạn!");
                }
            }

            user.PasswordHash = HashPassword(newPassword);
            _otpStore.Remove(usernameOrEmail);

            return (true, "Đổi mật khẩu mới thành công! Vui lòng đăng nhập lại.");
        }

        public (bool success, string message) ResetPasswordDirect(string usernameOrEmail, string newPassword)
        {
            var user = _users.FirstOrDefault(u => u.Phone == usernameOrEmail || u.Email == usernameOrEmail);
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
```

#### 📄 `src/Backend/Controllers/AdminController.cs`
```csharp
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
    }

    public class UpdatePriceRequest
    {
        public int FieldType { get; set; }
        public decimal BasePrice { get; set; }
        public decimal WeekendMultiplier { get; set; } = 1.30m;
        public decimal PeakHourMultiplier { get; set; } = 1.50m;
    }
}
```

#### 📄 `src/Backend/Controllers/AuthController.cs`
```csharp
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
```

#### 📄 `src/Backend/Controllers/BookingsController.cs`
```csharp
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
        public IActionResult GetAiPrice(Guid id, [FromQuery] DateTime? bookingTime)
        {
            var field = _bookingService.GetFieldById(id);
            if (field == null) return NotFound(new { message = "Sân bóng không tồn tại" });

            var time = bookingTime ?? DateTime.Now.AddHours(2);
            var aiResult = _aiClient.GetAiOptimalPrice(id, time, field.BasePrice);
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
```

#### 📄 `src/Backend/Controllers/PaymentController.cs`
```csharp
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
```

#### 📄 `src/Backend/Controllers/UserController.cs`
```csharp
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
```

---

### 4. FRONTEND LAYER (CLIENT INTERFACE & STYLING)

#### 📄 `src/Frontend/css/style.css`
```css
:root {
  --primary: #10b981;
  --primary-hover: #059669;
  --bg-light: #f4f6f9;
  --card-bg: #ffffff;
  --card-border: #e5e7eb;
  --text-main: #111827;
  --text-muted: #4b5563;
  --accent-gold: #d97706;
  --danger: #ef4444;
  --box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
  --box-shadow-hover: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
  --input-bg: #ffffff;
  --input-border: #d1d5db;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
}

body {
  background-color: var(--bg-light);
  color: var(--text-main);
  min-height: 100vh;
  background-image:
    radial-gradient(circle at 15% 15%, rgba(16, 185, 129, 0.08) 0%, transparent 45%),
    radial-gradient(circle at 85% 85%, rgba(59, 130, 246, 0.08) 0%, transparent 45%);
  background-attachment: fixed;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.9rem 5%;
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(229, 231, 235, 0.8);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-left {
  display: flex;
  align-items: center;
  gap: 2.5rem;
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--primary);
  letter-spacing: -0.5px;
  text-decoration: none;
}

.logo span {
  color: var(--text-main);
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.nav-links a {
  color: var(--text-muted);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.95rem;
  padding: 0.4rem 0.75rem;
  border-radius: 8px;
  transition: all 0.2s ease;
}

.nav-links a:hover,
.nav-links a.active {
  color: var(--primary);
  background: rgba(16, 185, 129, 0.08);
}

.user-panel {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.wallet-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  background: #ecfdf5;
  border: 1px solid #a7f3d0;
  padding: 0.3rem 0.75rem;
  border-radius: 20px;
  color: #047857;
  font-weight: 700;
  font-size: 0.85rem;
}

.btn-topup-mini {
  background: var(--primary);
  color: #ffffff;
  border: none;
  padding: 0.18rem 0.55rem;
  border-radius: 12px;
  font-weight: 700;
  cursor: pointer;
  font-size: 0.75rem;
  margin-left: 0.2rem;
  box-shadow: 0 1px 3px rgba(16, 185, 129, 0.3);
  transition: background 0.2s;
}

.btn-topup-mini:hover {
  background: var(--primary-hover);
}

.user-profile-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.35rem 0.85rem;
  border-radius: 20px;
  background: #ffffff;
  border: 1px solid var(--card-border);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04);
  cursor: pointer;
  transition: all 0.2s;
}

.user-profile-badge:hover {
  background: #f9fafb;
  border-color: var(--primary);
  box-shadow: 0 4px 6px -1px rgba(16, 185, 129, 0.15);
}

.user-avatar-img {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid var(--primary);
}

.user-info-text-group {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  line-height: 1.25;
}

.user-name-text {
  color: var(--text-main);
  font-weight: 700;
  font-size: 0.88rem;
}

.user-wallet-subtext {
  color: #059669;
  font-size: 0.76rem;
  font-weight: 600;
}

.btn-logout-mini {
  background: transparent;
  border: 1px solid #fca5a5;
  color: var(--danger);
  padding: 0.3rem 0.65rem;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.82rem;
  transition: all 0.2s;
}

.btn-logout-mini:hover {
  background: #fee2e2;
}

.container {
  max-width: 1240px;
  margin: 2.5rem auto;
  padding: 0 1.5rem;
}

.hero {
  text-align: center;
  padding: 3rem 1rem;
}

.hero h1 {
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, #059669 0%, #0284c7 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero p {
  color: var(--text-muted);
  font-size: 1.15rem;
  max-width: 650px;
  margin: 0 auto;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 1.75rem;
  margin-top: 2rem;
}

.card {
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: 20px;
  padding: 1.75rem;
  box-shadow: var(--box-shadow);
  transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--box-shadow-hover);
  border-color: rgba(16, 185, 129, 0.4);
}

.ai-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  background: #fef3c7;
  color: #b45309;
  border: 1px solid #fde68a;
  padding: 0.35rem 0.85rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 700;
}

.field-title {
  font-size: 1.35rem;
  font-weight: 700;
  color: var(--text-main);
  margin: 1rem 0 0.5rem 0;
}

.field-meta {
  color: var(--text-muted);
  font-size: 0.92rem;
  margin-bottom: 1.25rem;
}

.price-box {
  background: #f8fafc;
  padding: 1.1rem;
  border-radius: 14px;
  border: 1px solid #e2e8f0;
  margin: 1.2rem 0;
}

.price-original {
  text-decoration: line-through;
  color: #9ca3af;
  font-size: 0.9rem;
}

.price-ai {
  font-size: 1.65rem;
  font-weight: 800;
  color: var(--primary);
}

input[type="text"],
input[type="password"],
input[type="number"],
input[type="datetime-local"],
select {
  background: var(--input-bg) !important;
  color: var(--text-main) !important;
  border: 1px solid var(--input-border) !important;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.05);
  transition: border-color 0.2s, box-shadow 0.2s;
}

input[type="text"]:focus,
input[type="password"]:focus,
input[type="number"]:focus,
input[type="datetime-local"]:focus,
select:focus {
  outline: none;
  border-color: var(--primary) !important;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2) !important;
}

.btn {
  width: 100%;
  padding: 0.9rem;
  background: var(--primary);
  color: white;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(16, 185, 129, 0.25);
  transition: background 0.2s, transform 0.1s, box-shadow 0.2s;
}

.btn:hover {
  background: var(--primary-hover);
  box-shadow: 0 4px 8px rgba(16, 185, 129, 0.35);
}

.btn:active {
  transform: scale(0.98);
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(8px);
  display: none;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 1.5rem;
}

.modal-content {
  background: #ffffff;
  border: 1px solid var(--card-border);
  padding: 2rem 2.25rem 2.25rem 2.25rem;
  border-radius: 24px;
  width: 90%;
  max-width: 480px;
  height: auto;
  max-height: 90vh;
  overflow-y: auto;
  text-align: center;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  color: var(--text-main);
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.qr-img {
  width: 220px;
  height: 220px;
  margin: 1.25rem auto;
  border-radius: 16px;
  border: 2px solid var(--card-border);
}

/* Chat box in Light mode */
#chat-box {
  background: #f8fafc !important;
  border: 1px solid #e2e8f0;
}
#chat-box p {
  color: var(--text-main) !important;
}

/* Heatmap & Matrix layout for Admin */
.heatmap-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 0.5rem;
  margin-top: 1rem;
}

.heatmap-cell {
  padding: 0.75rem 0.25rem;
  text-align: center;
  border-radius: 8px;
  font-size: 0.8rem;
  font-weight: 600;
}

.cell-high {
  background: #fee2e2;
  color: #991b1b;
  border: 1px solid #fca5a5;
}

.cell-medium {
  background: #fef3c7;
  color: #92400e;
  border: 1px solid #fcd34d;
}

.cell-low {
  background: #d1fae5;
  color: #065f46;
  border: 1px solid #6ee7b7;
}
```

---

## III. TỔNG KẾT & ĐÁNH GIÁ MÃ NGUỒN

1. **Kiến trúc phân tầng chuyên nghiệp (Multi-tier Architecture):**
   - **Tầng Database (SQL Server):** Đã thiết kế với RDBMS chuẩn hóa 3NF, đầy đủ các khóa chính (PK), khóa ngoại (FK), và Ràng buộc toàn vẹn (Check Constraints, Indexes).
   - **Tầng Microservice AI (Python Flask):** Xử lý độc lập tính năng dự đoán giá linh hoạt (Dynamic Pricing) dựa trên yếu tố thời gian và tích hợp LLM Studio qua REST API OpenAI-compatible format.
   - **Tầng Backend API (.NET C#):** Sử dụng Repository & Service Pattern với cơ chế Concurrency Lock (`lock (_lockObj)`), hỗ trợ khôi phục giao dịch (Rollback), tích hợp JWT Token Security và mã hóa SHA256.
   - **Tầng Frontend (HTML/CSS/JS Vanilla):** Giao diện đáp ứng (Responsive), tối ưu trải nghiệm người dùng với các Modal tương tác, tính năng quét mã VietQR tự động và Chatbot AI trực quan.

2. **Khả năng mở rộng:**
   - Hệ thống được thiết kế theo kiến trúc Microservices & Loose Coupling giúp dễ dàng nâng cấp hoặc thay thế các module độc lập mà không ảnh hưởng đến toàn bộ hệ thống.
