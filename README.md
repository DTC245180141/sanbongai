# ⚽ HỆ THỐNG ĐẶT SÂN BÓNG TỰ ĐỘNG TÍCH HỢP AI & VÍ ĐIỆN TỬ VIRTUAL WALLET
> **Đồ án tốt nghiệp Chuyên ngành Kỹ thuật Phần mềm / Hệ thống Thông tin**  
> **Trường Đại học Công Nghệ Thông Tin & Truyền Thông Thái Nguyên (ICTU)**

[![.NET Version](https://img.shields.io/badge/.NET-10.0-512BD4?logo=dotnet)](https://dotnet.microsoft.com/)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python)](https://python.org/)
[![Database](https://img.shields.io/badge/Database-SQL%20Server-CC292B?logo=microsoftsqlserver)](https://www.microsoft.com/sql-server)
[![AI LLM](https://img.shields.io/badge/AI%20Model-Qwen%202.5%207B%20Instruct-blueviolet)](https://huggingface.co/Qwen)
[![Tests](https://img.shields.io/badge/Unit%20Tests-11%20Passed%20(100%25)-success)](https://github.com/)

---

## 👥 THÀNH VIÊN THỰC HIỆN (NHÓM 02)

| STT | Họ và Tên | Vai trò | Trách nhiệm chuyên môn chính |
|:---:|:---|:---|:---|
| 1 | **Lã Quý Doanh** | Trưởng nhóm | Kiến trúc Hệ thống, Backend .NET 10 Web API, Thiết kế CSDL SQL Server 3NF, Concurrency Lock chống trùng lịch, Quản trị Ví điện tử & Tích hợp VietQR |
| 2 | **Bùi Thanh Bình** | Thành viên | AI Microservice Python Flask, Huấn luyện & Tích hợp LLM Qwen 2.5 7B qua LM Studio, Smart Fallback NLP Engine, Giao diện Frontend UI/UX Responsive & Kiểm thử |

---

## 🌟 ĐẶC ĐIỂM NỔI BẬT CỦA HỆ THỐNG

1. **Chống trùng lịch tuyệt đối (100% Concurrency Safe):** Áp dụng kỹ thuật khóa luồng đồng bộ đa luồng (`lock (_lockObj)`) ở tầng Application Service kết hợp ràng buộc toàn vẹn CSDL, ngăn chặn hoàn toàn lỗi tranh chấp tài nguyên (Race Condition) khi hàng chục người cùng chọn 1 sân trong 1 tích tắc.
2. **Định giá linh hoạt theo thời gian thực (AI Dynamic Pricing):** Thuật toán Machine Learning kết hợp ma trận phụ thu (giờ thấp điểm/cao điểm, cuối tuần, thời tiết) giúp tối ưu hóa doanh thu cho chủ sân và công khai minh bạch bảng chi phí cho cầu thủ.
3. **Trợ lý ảo Chatbot thông minh 24/7:** Vận hành mô hình ngôn ngữ lớn **Qwen 2.5 7B Instruct** chạy hoàn toàn **Local (Zero Cloud Data Leakage)** qua LM Studio; hiểu tiếng Việt tự nhiên, giải đáp bảng giá, tình trạng sân và điều lệ hoàn cọc.
4. **Kiến trúc chịu lỗi 3 tầng (Three-tier Defense Architecture):** Bộ đệm RAM `lru_cache` (đáp ứng 0ms) $\rightarrow$ Smart Fallback NLP Engine (Regex tiếng Việt < 5ms) $\rightarrow$ C# Graceful Degradation (Backend tự tính phụ thu khi AI offline), đảm bảo website **không bao giờ bị gián đoạn hay crash**.
5. **Ví điện tử nội bộ Virtual Wallet & Thanh toán VietQR:** Trừ tiền đặt chỗ tức thì trong **0.1s**, sinh mã động chuẩn NAPAS 247 MBBank cá nhân hóa từng user, hỗ trợ hủy sân tự động hoàn trả 100% tiền ví.
6. **Bảng điều khiển Quản trị (Admin KPI Dashboard):** Giám sát doanh thu lũy kế, đối soát và phê duyệt tiền nạp ví ngân hàng, cấu hình bảng giá và khóa/mở khóa tài khoản chỉ với 1 click.

---

## 🏗️ KIẾN TRÚC HỆ THỐNG (SYSTEM ARCHITECTURE)

```
                       [ 🌐 Client Web Browsers ]
                 (HTML5 / Modern Glassmorphism CSS / Vanilla JS)
                                     │
                        HTTP REST API / Bearer JWT
                                     ▼
                  ┌─────────────────────────────────────┐
                  │   BACKEND ASP.NET CORE (.NET 10)    │
                  │   Port: 5048 (Swagger: /swagger)    │
                  ├─────────────────────────────────────┤
                  │ • Controllers: Auth, Bookings,      │
                  │   Payment, Admin, Pitch             │
                  │ • Business Services:                │
                  │   - BookingService (ConcurrencyLock)│
                  │   - UserService (SHA-256 + JWT)     │
                  │   - AIServiceClient (CircuitBreaker)│
                  │ • Data: Entity Framework Core 8.0   │
                  └──────────┬───────────────────┬──────┘
                             │                   │
                 gọi API REST│ (Port 5050)       │ (T-SQL / TCP 1433)
                             ▼                   ▼
      ┌───────────────────────────────┐   ┌─────────────────────────────┐
      │     AI MICROSERVICE (FLASK)   │   │   DATABASE MICROSOFT SQL    │
      ├───────────────────────────────┤   ├─────────────────────────────┤
      │ • Dynamic Pricing Algorithm   │   │ • Users (Wallet Balance)    │
      │ • Smart Fallback Engine (NLP) │   │ • Fields & Locations        │
      │ • Local LLM Client (Port 1234)│   │ • Bookings & Schedules      │
      └──────────────┬────────────────┘   │ • Transactions (Audit Log)  │
                     │                    │ • DepositRequests (VietQR)  │
                     ▼                    └─────────────────────────────┘
      ┌───────────────────────────────┐
      │   LM STUDIO / LOCAL RUNTIME   │
      │   Model: Qwen2.5-7B-Instruct  │
      └───────────────────────────────┘
```

---

## 📁 CẤU TRÚC MÃ NGUỒN (PROJECT STRUCTURE)

```
1websanbongai/
├── src/
│   ├── Backend/                           # Mã nguồn ASP.NET Core Web API
│   │   ├── Controllers/                   # RESTful API Endpoints
│   │   ├── Data/                          # DbContext & Database Seeding
│   │   ├── Models/                        # Entities & Data Transfer Objects (DTO)
│   │   ├── Services/                      # Nghiệp vụ lõi (BookingService, AIServiceClient...)
│   │   ├── wwwroot/                       # Static files & Uploads
│   │   ├── Program.cs                     # Cấu hình DI, Middleware, Swagger, CORS
│   │   └── FootballBookingApi.csproj
│   │
│   ├── AIService/                         # Microservice Trí tuệ nhân tạo (Python Flask)
│   │   ├── app.py                         # REST API /api/predict-price & /api/chat-assistant
│   │   ├── train_model_7b.py              # Script huấn luyện & Fine-tuning LLM
│   │   ├── training_dataset_7b.jsonl      # Bộ dữ liệu mẫu huấn luyện Prompt Context
│   │   └── requirements.txt               # Thư viện Python (Flask, Flask-CORS, Requests...)
│   │
│   └── Frontend/                          # Giao diện người dùng Web Application
│       ├── index.html                     # Trang chủ, Đặt sân & Widget Chatbot AI
│       ├── admin.html                     # Bảng điều khiển Quản trị viên (Admin Dashboard)
│       ├── css/style.css                  # Giao diện Modern UI Glassmorphism & Responsive
│       └── js/                            # Xử lý tương tác AJAX, JWT & Render Ma trận sân
│
├── tests/
│   └── FootballBookingApi.Tests/          # Bộ kiểm thử đơn vị tự động (Unit Test Suite)
│       ├── BookingServiceTests.cs         # Test Concurrency Lock, Ví tiền, Xung đột lịch
│       ├── AIServiceClientTests.cs        # Test Fallback Engine & Hệ số giờ cao điểm/cuối tuần
│       └── FootballBookingApi.Tests.csproj
│
├── database/
│   └── schema.sql                         # Kịch bản khởi tạo CSDL SQL Server chuẩn 3NF
│
├── BAO_CAO_CHI_TIET_DO_AN_TOT_NGHIEP.md   # Báo cáo chuyên sâu 4.300+ dòng chuẩn Bộ môn ICTU
└── README.md                              # Tài liệu hướng dẫn cài đặt & vận hành hệ thống
```

---

## 🚀 HƯỚNG DẪN CÀI ĐẶT & CHẠY ỨNG DỤNG

### 1. Yêu cầu môi trường chuẩn bị
* **Hệ điều hành:** Windows 10/11, macOS hoặc Linux
* **.NET SDK:** Phiên bản .NET 8.0 hoặc .NET 10.0+ ([Tải về](https://dotnet.microsoft.com/download))
* **Python:** Phiên bản 3.10 trở lên ([Tải về](https://www.python.org/downloads/))
* **Cơ sở dữ liệu:** Microsoft SQL Server 2019/2022 hoặc LocalDB
* **Local LLM (Tùy chọn):** LM Studio ([lmstudio.ai](https://lmstudio.ai/)) tải mô hình `Qwen2.5-7B-Instruct`

---

### 2. Khởi tạo Cơ sở dữ liệu (Database Setup)
1. Mở **SQL Server Management Studio (SSMS)** hoặc **Azure Data Studio**.
2. Kết nối tới máy chủ SQL Server của bạn.
3. Mở file [database/schema.sql](file:///c:/Users/klqdo/Downloads/1websanbongai/database/schema.sql) và nhấn **Execute (F5)** để tự động tạo CSDL `FootballBookingDb` cùng 7 bảng nghiệp vụ và dữ liệu mẫu (Data Seeding).

---

### 3. Khởi chạy AI Microservice (Python Flask)
```bash
# 1. Di chuyển vào thư mục AI
cd src/AIService

# 2. Khởi tạo môi trường ảo (Khuyên dùng)
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 3. Cài đặt các thư viện phụ thuộc
pip install -r requirements.txt

# 4. Khởi chạy dịch vụ AI tại cổng 5050
python app.py
```
> *Dịch vụ AI sẽ khởi chạy tại: `http://localhost:5050`*

*(Tùy chọn)* Nếu muốn kích hoạt Chatbot LLM thời gian thực:
* Bật **LM Studio** $\rightarrow$ Nạp mô hình `qwen2.5-7b-instruct` $\rightarrow$ Bật **Local Server** tại Port `1234`.
* Nếu LM Studio không bật, hệ thống sẽ **tự động chuyển sang Smart Fallback NLP Engine** phản hồi < 5ms.

---

### 4. Khởi chạy Backend ASP.NET Core Web API
```bash
# Di chuyển vào thư mục Backend
cd src/Backend

# Phục hồi packages và biên dịch
dotnet restore
dotnet build

# Chạy Web API
dotnet run
```
> *API lắng nghe tại: `http://localhost:5048`*  
> *Truy cập Swagger UI kiểm thử trực quan: `http://localhost:5048/swagger`*

---

### 5. Khởi chạy Giao diện Frontend
* Chỉ cần mở trực tiếp file `src/Frontend/index.html` bằng trình duyệt (Google Chrome, Microsoft Edge, Firefox), hoặc sử dụng extension **Live Server** trong VS Code:
  * **Trang khách hàng:** `src/Frontend/index.html` (Đặt sân, nạp ví VietQR, Chatbot AI)
  * **Trang quản trị:** `src/Frontend/admin.html` (Duyệt nạp ví, Quản lý sân, Thống kê KPI)

---

## 🧪 CHẠY BỘ KIỂM THỬ ĐƠN VỊ TỰ ĐỘNG (UNIT TESTS)

Dự án trang bị bộ kiểm thử tự động với framework **xUnit** và thư viện **Moq**, bao phủ các ca kiểm thử then chốt:

```bash
# Thực thi toàn bộ Unit Tests
dotnet test tests/FootballBookingApi.Tests/FootballBookingApi.Tests.csproj
```

**Kết quả kiểm thử thực tế:**
```text
Passed!  - Failed: 0, Passed: 11, Skipped: 0, Total: 11, Duration: 2 s
- BookingServiceTests:
  ✔ CreateBooking_Success_DeductsWalletBalanceAndReturnsBooking
  ✔ CreateBooking_InsufficientBalance_ReturnsError
  ✔ CreateBooking_UserLocked_ReturnsError
  ✔ CreateBooking_FieldMaintenance_ReturnsError
  ✔ CreateBooking_OverlappingBooking_ReturnsError
  ✔ CancelBooking_ExistingBooking_SetsStatusToCancelled
  ✔ CreateBooking_ConcurrencySafe_UnderMultiThreading (10 luồng song song)
- AIServiceClientTests:
  ✔ GetAiOptimalPrice_WeekdayNormalHours_AppliesBaseMultiplier (1.0x)
  ✔ GetAiOptimalPrice_WeekendNormalHours_AddsWeekendSurcharge (1.3x)
  ✔ GetAiOptimalPrice_WeekdayPeakHours_AddsPeakSurcharge (1.5x)
  ✔ GetAiOptimalPrice_WeekendPeakHours_CombinesBothSurcharges (1.8x)
```

---

## 🔑 TÀI KHOẢN MẪU TRẢI NGHIỆM

| Vai trò | Tên đăng nhập | Mật khẩu mặc định | Số điện thoại | Số dư ví ban đầu |
|:---|:---|:---|:---|:---|
| **Quản trị viên (Admin)** | `admin` | `123456` | `0987654321` | Không giới hạn |
| **Cầu thủ mẫu 1 (Customer)** | `doanh` | `123456` | `0364382164` | 2.000.000 VNĐ |
| **Cầu thủ mẫu 2 (Customer)** | `binh` | `123456` | `0912345678` | 2.000.000 VNĐ |

---

## 📋 BẢNG ĐỐI CHIẾU YÊU CẦU KỸ THUẬT VÀ HIỆN TRẠNG BÀN GIAO THỰC TẾ

| Chuẩn đầu ra | Nội dung yêu cầu kỹ thuật | Module / Thành phần trong mã nguồn | File minh chứng thực tế | Hiện trạng bàn giao |
|:---:|:---|:---|:---|:---:|
| **CLO1** (Phân tích & Thiết kế) | Khảo sát thực tế, phân tích nghiệp vụ, SRS v1.0, thiết kế kiến trúc phân tầng, CSDL 3NF, lý giải vị trí AI | Khảo sát 30 câu hỏi (150 mẫu), SRS 13 Use Cases, CSDL 7 bảng chuẩn 3NF, sơ đồ ERD & Class Diagram | `database/schema.sql`<br>`BAO_CAO_CHI_TIET.md` (Phần 2, 3, 4, 6) | Đã hoàn thành bàn giao đầy đủ |
| **CLO2** (Hệ thống cốt lõi) | Nghiệp vụ đặt sân, trừ ví tiền tức thì 0.1s, mã VietQR NAPAS 247 MBBank, phân quyền JWT & băm mật khẩu SHA-256 | `BookingService`, `UserService`, `AuthController`, `PaymentController`, `AdminController` | `src/Backend/Services/`<br>`src/Backend/Controllers/`<br>`src/Frontend/index.html, admin.html` | Đã hoàn thành bàn giao, kiểm thử hoạt động thông suốt |
| **CLO3** (Chức năng AI) | AI Dynamic Pricing định giá linh hoạt theo giờ cao điểm/cuối tuần; Chatbot AI tiếng Việt 24/7; Fallback Engine chịu lỗi | Microservice Python Flask, Prompt V3 Context Engineering, Smart Fallback Regex, `AIServiceClient.cs` | `src/AIService/app.py`<br>`training_dataset_7b.jsonl`<br>`src/Backend/Services/AIServiceClient.cs` | Đã hoàn thành bàn giao, 100 truy vấn thực nghiệm đạt 98% accuracy |
| **CLO4** (Kiểm thử & Đánh giá) | Kiểm thử đúng/sai/biên/đồng thời; kiểm thử đơn vị tự động xUnit; so sánh prompt V1-V3; an toàn bảo mật | 31 System Test Cases, bộ 11 Automated Unit Tests xUnit (có Concurrency 10 luồng), rào chắn an toàn 5 lớp | `tests/FootballBookingApi.Tests/`<br>`BAO_CAO_CHI_TIET.md` (Phần 5, 8.4) | Đã hoàn thành bàn giao, 100% Test Cases đều PASS |
| **CLO5 / PLO7** (Vận hành & SDLC) | Giao diện Modern Glassmorphism; triển khai Docker container; minh chứng sửa lỗi AI; vấn đáp độc lập từng thành viên | UI/UX Responsive, Dockerfile Backend & AI, `docker-compose.yml`, 4 Case Studies sửa lỗi AI, kịch bản Demo 8 bước | `docker-compose.yml`<br>`src/Backend/Dockerfile`<br>`src/AIService/Dockerfile`<br>`README.md` | Đã hoàn thành bàn giao, sẵn sàng bảo vệ trước Hội đồng |

---

## 📄 BẢN QUYỀN & THÔNG TIN LIÊN HỆ

* **Đồ án tốt nghiệp Khoa Công nghệ Thông tin - Trường Đại học CNTT & Truyền Thông Thái Nguyên (ICTU)**
* Nhóm tác giả: **Lã Quý Doanh** & **Bùi Thanh Bình** (Nhóm 02)
* Mọi ý kiến đóng góp hoặc thắc mắc vui lòng tạo Issue trên kho lưu trữ hoặc liên hệ qua email sinh viên ICTU.
