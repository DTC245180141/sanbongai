# HỆ THỐNG ĐẶT SÂN BÓNG TỰ ĐỘNG TÍCH HỢP AI & VÍ ĐIỆN TỬ VIRTUAL WALLET (PITCHAI)

> **Đồ án Tốt nghiệp ngành Kỹ thuật Phần mềm / Hệ thống Thông tin**  
> **Trường:** Đại học Công Nghệ Thông Tin & Truyền Thông Thái Nguyên (ICTU) - Khoa Công Nghệ Thông Tin  
> **Nhóm sinh viên thực hiện:** Nhóm 02  
> 1. **Lã Quý Doanh** - Trưởng nhóm (Kiến trúc Hệ thống, Backend .NET, CSDL SQL Server, Bảo mật & Concurrency)  
> 2. **Bùi Thanh Bình** - Thành viên (AI Microservice Python Flask, LLM Prompting & LM Studio, Frontend UI/UX, Testing)  
> **Giảng viên hướng dẫn:** TS. Giảng Viên Hướng Dẫn  

---

## 📌 1. GIỚI THIỆU TỔNG QUAN

Hệ thống **PitchAI** là giải pháp phần mềm toàn diện nhằm tự động hóa quy trình quản trị và vận hành cụm sân bóng đá mini (sân 5, 7, 11 người) tại khu vực Phường Quyết Thắng, TP. Thái Nguyên (khu vực Đại học ICTU). Hệ thống kết hợp sức mạnh của **Trí tuệ Nhân tạo (AI)** với kiến trúc **Microservices** hiện đại nhằm giải quyết triệt để các bài toán nan giải trong vận hành sân cỏ truyền thống:
1. **Tránh trùng lịch đặt sân 100%:** Cơ chế khóa tiến trình thread-safe (*Concurrency Lock*) loại bỏ hoàn toàn rủi ro đặt trùng trong cùng một mili-giây.
2. **Định giá linh hoạt bằng AI (Dynamic Pricing):** Tự động điều chỉnh giá thuê theo khung giờ vàng, khung giờ rạng sáng (02:00 - 05:00) và cuối tuần để tối ưu hóa doanh thu và tỷ lệ lấp đầy sân.
3. **Trợ lý ảo hỗ trợ 24/7 (Local LLM Studio):** Tích hợp mô hình ngôn ngữ lớn (Qwen 7B) chạy trên môi trường cục bộ, hiểu ngôn ngữ bóng đá tự nhiên, tư vấn lịch trống, bảng giá và chính sách đặt sân tức thì, đi kèm cơ chế **Smart Fallback Engine** phản hồi trong 0ms khi AI offline.
4. **Thanh toán tức thì qua Ví ảo & VietQR:** Nạp tiền thuận tiện qua mã QR động ngân hàng MBBank (chuẩn VietQR NAPAS 247), thanh toán giữ chỗ 0ms và chính sách **tự động hoàn tiền 100% về ví** khi hủy lịch trước giờ bóng lăn.

---

## 🏗️ 2. KIẾN TRÚC HỆ THỐNG & CÔNG NGHỆ SỬ DỤNG

```text
+-----------------------------------------------------------------------------------+
|                        FRONTEND CLIENT (HTML5 / CSS3 / JS)                        |
|   index.html (Trang Khách hàng, Chat AI, VietQR)  |  admin.html (Dashboard Admin) |
+-----------------------------------------------------------------------------------+
                                   | HTTP RESTful APIs / JSON
                                   v
+-----------------------------------------------------------------------------------+
|                     BACKEND WEB API (.NET 10 C#) - Port 5048                      |
|  - AuthController: JWT Authentication, SHA-256 Hashing, OTP Password Reset        |
|  - BookingsController: Concurrency Lock, Validation 2h-3d, Timezone Alignment     |
|  - PaymentController: VietQR Generation, Virtual Wallet Deposit Requests          |
|  - AdminController: PricingConfig, 100% Refund, System Global Maintenance (503)   |
|  - Services: BookingService, UserService, AIServiceClient (MemoryCache 5 min)     |
+-----------------------------------------------------------------------------------+
          | Entity Framework Core                           | HTTP Client
          v                                                 v
+-----------------------------------+     +-----------------------------------------+
|    SQL SERVER DATABASE (Port 1433)|     |   AI MICROSERVICE (Flask) - Port 5050   |
|  - Users, Fields, Bookings        |     |  - /api/predict-price (Dynamic Pricing) |
|  - Transactions, Payments         |     |  - /api/chat-assistant (Context Engine) |
|  - PricingConfig, AI_DemandLogs   |     |  - Smart Fallback Engine (LRU Cache)    |
+-----------------------------------+     +-----------------------------------------+
                                                                | HTTP API
                                                                v
                                                  +---------------------------------+
                                                  |    LOCAL LLM RUNTIME (Port 1234)|
                                                  |  - LM Studio: Qwen2.5-7B/1.5B   |
                                                  +---------------------------------+
```

### Chi tiết các công nghệ chính:
- **Backend API:** C# .NET 10.0, ASP.NET Core Web API, Entity Framework Core 8.0, Dependency Injection, Swagger OpenAPI, Response Compression (Brotli/Gzip).
- **AI Microservice:** Python 3.10+, Flask, Waitress Multi-threaded WSGI Server, Requests HTTP Connection Pool.
- **Mô hình Ngôn ngữ Lớn (LLM):** Qwen2.5-Coder-7B-Instruct / Qwen2.5-1.5B qua LM Studio Local Server (Port 1234).
- **Cơ sở Dữ liệu:** Microsoft SQL Server (Transact-SQL), quan hệ chuẩn 3NF, Indexes tối ưu hóa truy vấn trùng lịch.
- **Frontend Client:** HTML5, Modern CSS3 Glassmorphism, Vanilla JavaScript ES6+, FontAwesome Icons, Marked.js, VietQR API.

---

## 🚀 3. HƯỚNG DẪN CÀI ĐẶT & KHỞI CHẠY HỆ THỐNG TỪ A - Z

### Yêu cầu môi trường tiên quyết:
- Hệ điều hành: Windows 10/11 (64-bit).
- .NET SDK: Phiên bản 8.0 trở lên (khuyến nghị .NET 10).
- Python: Phiên bản 3.10 trở lên.
- Microsoft SQL Server: SQL Server 2019/2022 hoặc SQL Server LocalDB.
- LM Studio (tùy chọn nếu muốn chạy Chatbot AI thực tế): Đã tải mô hình `qwen2.5-coder-7b-instruct`.

---

### Bước 1: Khởi tạo Cơ sở Dữ liệu (Database Setup)
1. Mở **SQL Server Management Studio (SSMS)** hoặc công cụ `sqlcmd`.
2. Mở file [database/schema.sql](database/schema.sql).
3. Thực thi script (Execute / F5) để tạo database `FootballBookingDB` và toàn bộ các bảng, ràng buộc và dữ liệu mẫu.

---

### Bước 2: Khởi chạy AI Microservice (Python Flask - Port 5050)
1. Mở terminal tại thư mục `src/AIService`:
   ```bash
   cd src/AIService
   ```
2. Cài đặt các thư viện phụ thuộc:
   ```bash
   pip install -r requirements.txt
   ```
3. Chạy dịch vụ AI:
   ```bash
   python app.py
   ```
   *Dịch vụ sẽ lắng nghe tại:* `http://localhost:5050`  
   *Kiểm tra sức khỏe:* `http://localhost:5050/health`  
   *(Nếu bạn có LM Studio, khởi động Local Server tại port 1234; nếu không có, hệ thống sẽ tự động kích hoạt Instant Smart Fallback Engine).*

---

### Bước 3: Khởi chạy Backend Web API (.NET 10 - Port 5048)
1. Mở một terminal mới tại thư mục `src/Backend`:
   ```bash
   cd src/Backend
   ```
2. Phục hồi dependencies và chạy ứng dụng:
   ```bash
   dotnet restore
   dotnet run
   ```
   *Dịch vụ Backend sẽ lắng nghe tại:* `http://localhost:5048`  
   *Xem tài liệu API trực quan tại:* `http://localhost:5048/swagger`

---

### Bước 4: Mở Giao diện Khách hàng & Quản trị viên (Frontend)
1. Mở trình duyệt Web (Chrome, Edge, Firefox).
2. Mở trực tiếp file:
   - **Giao diện Khách hàng:** [src/Frontend/index.html](src/Frontend/index.html)
   - **Giao diện Quản trị viên:** [src/Frontend/admin.html](src/Frontend/admin.html)

---

## 🔑 4. DANH SÁCH TÀI KHOẢN TRẢI NGHIỆM DEMO

| STT | Tên đăng nhập (Username) | Mật khẩu (Password) | Vai trò (Role) | Số dư ví ban đầu | Mục đích sử dụng |
| :-: | :--- | :--- | :---: | :---: | :--- |
| **1** | `admin` | `Admin@123` | **Quản trị viên (Admin)** | 10.000.000 VNĐ | Toàn quyền quản trị, duyệt nạp ví, hủy lịch & hoàn tiền, bật bảo trì. |
| **2** | `doanh` | `123456` | **Khách hàng (Customer)** | 5.000.000 VNĐ | Trải nghiệm đặt sân, xem giá AI, nạp tiền ví qua VietQR. |
| **3** | `khach1` | `Customer@123` | **Khách hàng (Customer)** | 3.000.000 VNĐ | Kiểm thử đổi mật khẩu, quên tên đăng nhập. |
| **4** | *Nút 1-Click Demo* | *Tự động* | **Khách hàng Demo** | 3.000.000 VNĐ | Vào ngay giao diện đặt sân chỉ với 1 cú click chuột tại `index.html`. |

---

## 🧪 5. QUY TRÌNH KIỂM THỬ & CHỨC NĂNG NỔI BẬT

Hệ thống đã trải qua **31 kịch bản kiểm thử (Test Cases)** đạt tỷ lệ **Pass 100%**:
- **Kiểm thử Concurrency:** 2 người đặt cùng 1 sân trong cùng 1 mili-giây $\rightarrow$ Lock bảo vệ chỉ cho 1 người thành công, người thứ hai nhận thông báo trùng lịch.
- **Kiểm thử Biên (Boundary):** Chặn đặt sân < 2 tiếng hoặc > 3 ngày; Chặn đơn đặt thiếu số dư ví.
- **Kiểm thử Fallback:** Tắt đột ngột AI Microservice $\rightarrow$ Backend tự tính giá theo hệ số dự phòng, không sập hệ thống.
- **Bảo trì Toàn hệ thống (Maintenance Mode):** Khi Admin bật bảo trì, mọi API khách hàng trả về HTTP 503, riêng Admin vẫn truy cập bình thường.

---

## 📂 6. CẤU TRÚC THƯ MỤC NGUỒN

```text
1websanbongai/
├── README.md                                 # [File này] Hướng dẫn cài đặt, kiến trúc & demo
├── .gitignore                                # Cấu hình loại bỏ file rác, bin/obj, venv
├── database/
│   └── schema.sql                            # Kịch bản khởi tạo CSDL SQL Server 3NF
├── docs_backup/                              # Toàn bộ tài liệu báo cáo đồ án tốt nghiệp
│   ├── BAO_CAO_CHI_TIET_DO_AN_TOT_NGHIEP.md  # Bản báo cáo lý thuyết đầy đủ chi tiết
│   ├── BAO_CAO_CODE.md                       # Báo cáo tổng hợp toàn bộ mã nguồn
│   ├── diagrams/                             # Kho ảnh sơ đồ phân tích thiết kế hệ thống
│   └── *.docx, *.py                          # File xuất Word và script tự động
└── src/
    ├── AIService/                            # Microservice Python AI (Port 5050)
    │   ├── app.py                            # Flask API Dynamic Pricing & LLM Context Engine
    │   ├── requirements.txt                  # Thư viện phụ thuộc Python
    │   ├── training_dataset_7b.jsonl         # Dữ liệu tri thức bóng đá ICTU
    │   └── train_model_7b.py                 # Script huấn luyện tri thức mô hình 7B
    ├── Backend/                              # Backend Web API .NET 10 (Port 5048)
    │   ├── FootballBookingApi.csproj         # File cấu hình C# .NET
    │   ├── Program.cs                        # Cấu hình DI, Middleware bảo trì, Swagger
    │   ├── Controllers/                      # REST Endpoints: Auth, Bookings, Payment, Admin, User
    │   ├── Data/                             # ApplicationDbContext (EF Core)
    │   ├── Models/                           # Entities, DTOs, Enums
    │   └── Services/                         # BookingService, UserService, AIServiceClient
    └── Frontend/                             # Web Client UI
        ├── index.html                        # Giao diện đặt sân & Chatbot AI
        ├── admin.html                        # Dashboard quản trị
        └── css/style.css                     # Dark Glassmorphism CSS
```

---

## 👥 7. THÔNG TIN LIÊN HỆ & BẢN QUYỀN

- **Nhóm tác giả:** Nhóm 02 - Lớp Kỹ thuật Phần mềm / Hệ thống Thông tin, Khoa Công Nghệ Thông Tin, Trường Đại học CNTT & TT Thái Nguyên (ICTU).
- **Trưởng nhóm:** Lã Quý Doanh - Điện thoại / Zalo: `0364382164` - Email: `doanh@pitchai.com`.
- **Thành viên:** Bùi Thanh Bình - Email: `binh@pitchai.com`.
- **Năm thực hiện:** 2026.
