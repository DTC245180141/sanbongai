# QUY CHUẨN ĐIỀU KHIỂN AGENT AI TRONG QUY TRÌNH PHÁT TRIỂN PHẦN MỀM (SDLC AGENT RULES)

> **Dự án:** Hệ Thống Quản Lý Đặt Sân Bóng Tự Động Tích Hợp AI & Ví Tiền Virtual Wallet (PitchAI)  
> **Trường:** Đại học CNTT & TT Thái Nguyên (ICTU) - Khoa Công Nghệ Thông Tin  
> **Nhóm thực hiện:** Lã Quý Doanh (Backend & CSDL) - Bùi Thanh Bình (AI Microservice & Frontend)  
> **Công cụ AI áp dụng:** Claude 3.5 Sonnet (Antigravity Agent), GitHub Copilot, Gemini 1.5 Pro  

---

## 1. ĐỊNH DANH VAI TRÒ CÁC AGENT TRONG "NHÀ MÁY PHẦN MỀM" (AGENT ROLES)

| Tên Agent | Công cụ sử dụng | Vai trò và Trách nhiệm trong SDLC | Rào chắn & Giới hạn thẩm quyền |
| :--- | :--- | :--- | :--- |
| **Requirements Analyst Agent** | Gemini 1.5 Pro / Claude 3.5 | Thu thập yêu cầu, sinh bảng khảo sát 30 câu hỏi thực tế, cấu trúc tài liệu SRS v1.0 và danh mục FR/NFR. | Không tự ý bổ sung các nghiệp vụ ngoài phạm vi sân bóng mini (như bán đồ thể thao, đặt vé máy bay). |
| **Database Architect Agent** | Claude 3.5 Sonnet | Thiết kế lược đồ CSDL SQL Server đạt chuẩn 3NF, sinh file `schema.sql`, cấu hình chỉ mục (Indexes) và ràng buộc khóa ngoại. | Bắt buộc sử dụng `DeleteBehavior.Restrict` (cấm Cascade Delete làm mất dữ liệu lịch sử); `WalletBalance >= 0`. |
| **Backend Engineer Agent** | GitHub Copilot / Antigravity | Sinh mã nguồn C# .NET 10 Web API, Entity Framework Core, Controller RESTful, Service layer. | Bắt buộc kiểm soát Concurrency thread-safe (`lock`); Bắt buộc kiểm tra múi giờ Local time (`ToLocalTime`). |
| **AI Microservice Agent** | Claude 3.5 Sonnet | Xây dựng dịch vụ Python Flask, thuật toán Dynamic Pricing, Smart Fallback Engine, tích hợp LM Studio Local API. | Chỉ chạy mô hình Local (`127.0.0.1:1234`), tuyệt đối không gửi API Key hoặc dữ liệu người dùng lên Cloud công cộng. |
| **QA / Testing Agent** | Antigravity / Copilot | Tự động sinh ma trận 31 kịch bản kiểm thử hệ thống và 14 ca kiểm thử tự động xUnit (Unit Tests & Integration Tests). | Mọi test case phải kiểm tra độc lập bằng Mock (`Moq`), kiểm tra cả trường hợp biên và đụng độ đa luồng. |

---

## 2. NGUYÊN TẮC KỸ NGHỆ NGỮ CẢNH (CONTEXT ENGINEERING FOR AGENTS)

Khi đưa prompt cho các AI Agent sinh mã hoặc phân tích tài liệu, lập trình viên bắt buộc phải nhúng **4 khối ngữ cảnh chuẩn** (Context Injections):
1. **Tech Stack Context:** Target framework .NET 10 C# (nullable enable, implicit usings), Entity Framework Core 8.0, Python 3.10+ Flask, SQL Server 2022.
2. **Architecture Context:** Clean Multi-tier Architecture (Presentation -> Business Services -> Data Access / EF Core -> SQL Server Database) song song Microservice AI Python (Port 5050).
3. **Domain Business Context:** Cụm sân ICTU Thái Nguyên có 5 sân (Sân 1,2: Sân 5; Sân 3,4: Sân 7; Sân 5: Sân 11); Giá sáng 150k/h (06h-17h), Giá tối & rạng sáng 300k/h; Đặt trước từ 2h đến 3 ngày; Hoàn tiền 100% tự động khi hủy đơn.
4. **Security & Financial Context:** Không lưu mật khẩu thô (mã hóa SHA-256); Không trừ tiền trước khi kiểm tra đụng độ thời gian; Mã VietQR chuẩn NAPAS 247 MBBank có Memo duy nhất.

---

## 3. RÀO CHẮN AN TOÀN CHO AGENT (AGENT SAFETY GUARDRAILS)

Nhằm ngăn ngừa AI sinh mã lỗi, rò rỉ bảo mật hoặc phá vỡ tính toàn vẹn hệ thống:
1. **Pre-commit & Secret Scanning Gate:** Tác tử không được phép ghi đè file cấu hình có chứa chuỗi nhạy cảm (Connection String, JWT Secret Key).
2. **Compiler & Linter Gate:** Mã C# do Agent sinh ra phải biên dịch thành công `dotnet build` với 0 Error và tuân thủ Roslyn Analyzer (nullable checking).
3. **Automated Testing Gate (CI Gate):** Sau khi Agent sinh hoặc sửa bất kỳ Service nào, lệnh `dotnet test` bắt buộc phải chạy và đạt **100% Pass** (14/14 tests) mới được chấp nhận.
4. **Human-in-the-Loop Review Gate:** Hai sinh viên (Doanh & Bình) trực tiếp kiểm duyệt từng dòng code trước khi tạo Git commit; Agent đóng vai trò đề xuất, con người giữ quyền quyết định cuối cùng.
