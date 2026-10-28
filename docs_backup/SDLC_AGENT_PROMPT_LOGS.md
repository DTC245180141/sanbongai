# NHẬT KÝ PROMPT VÀ PHẢN HỒI THẬT CỦA CÁC AGENT TRONG QUY TRÌNH SDLC (SDLC AGENT PROMPT LOGS)

> **Dự án:** Hệ Thống Đặt Sân Bóng Tự Động Tích Hợp AI & Ví Tiền Virtual Wallet  
> **Ghi nhận thực tế:** Các phiên làm việc giữa nhóm sinh viên và các tác tử AI (Claude 3.5 Sonnet / Antigravity Agent, GitHub Copilot) trong 9 tuần thực hiện đồ án tốt nghiệp.

---

## 1. PHA 1: THU THẬP & PHÂN TÍCH YÊU CẦU (REQUIREMENTS ELICITATION AGENT)

### Prompt gửi Agent:
```text
[SYSTEM CONTEXT]: Bạn là Chuyên viên Phân tích Nghiệp vụ Phần mềm (Business Analyst).
[DOMAIN CONTEXT]: Chúng tôi đang phát triển hệ thống phần mềm quản lý đặt sân bóng đá mini cho Cụm sân ICTU Thái Nguyên.
Hiện trạng: Chủ sân đang ghi sổ tay, hay bị trùng lịch vào 18h-20h, ngoài giờ hành chính (22h-02h) khách hay nhắn tin hỏi giá và đặt sân nhưng không có người trực.
[TASK]:
1. Thiết kế bảng câu hỏi khảo sát thực tế gồm 30 câu hỏi chuẩn hóa bao quát 5 khía cạnh.
2. Trích xuất danh sách các yêu cầu chức năng (FR) và phi chức năng (NFR).
3. Đề xuất mô hình phân cấp chức năng (FHD) và sơ đồ Use Case tổng quát.
```

### Kết quả Agent sinh ra & Đánh giá của nhóm:
- Agent sinh đầy đủ 30 câu hỏi khảo sát phân tầng theo tỷ lệ Likert.
- Sinh bảng 25 yêu cầu chức năng và 8 yêu cầu phi chức năng.
- **Can thiệp của sinh viên (Bùi Thanh Bình):** Phát hiện Agent đề xuất thêm chức năng "Thanh toán bằng thẻ tín dụng quốc tế Visa/MasterCard" - không phù hợp với đối tượng sinh viên ICTU. Sinh viên đã yêu cầu loại bỏ và thay thế bằng tích hợp **Ví điện tử Virtual Wallet** kết hợp **Mã VietQR NAPAS 247 ngân hàng MBBank**.

---

## 2. PHA 2: THIẾT KẾ CƠ SỞ DỮ LIỆU & KIẾN TRÚC (DATABASE & ARCHITECTURE AGENT)

### Prompt gửi Agent:
```text
[SYSTEM CONTEXT]: Bạn là Kiến trúc sư CSDL SQL Server và Kỹ sư phần mềm hướng đối tượng.
[DATABASE CONTEXT]: Hệ thống gồm: Khách hàng (User), Sân bóng (Fields: 5, 7, 11 người), Đơn đặt sân (Bookings), Ví tiền (WalletBalance), Lịch sử giao dịch (Transactions), Phê duyệt nạp tiền (DepositRequests), Bảng giá (PricingConfig).
[TASK]:
1. Thiết kế lược đồ CSDL đạt dạng chuẩn 3NF.
2. Viết file kịch bản DDL `schema.sql` hoàn chỉnh với ràng buộc toàn vẹn khóa chính, khóa ngoại, CHECK constraints.
3. Tạo chỉ mục để tối ưu hóa truy vấn kiểm tra trùng lịch đặt sân.
```

### Kết quả Agent sinh ra & Đánh giá của nhóm:
- Agent đề xuất 7 bảng quan hệ chuẩn hóa 3NF.
- **Lỗi phát hiện và can thiệp của sinh viên (Lã Quý Doanh):**
  * Lỗi 1: Agent cấu hình mặc định `ON DELETE CASCADE` cho quan hệ `Fields -> Bookings`. Sinh viên phát hiện nếu xóa một sân thì toàn bộ lịch sử kế toán của sân đó sẽ mất. Sinh viên đã sửa thành `ON DELETE RESTRICT` để bảo vệ dữ liệu tài chính.
  * Lỗi 2: Bổ sung chỉ mục phức hợp `CREATE INDEX IX_Bookings_FieldId_StartTime ON Bookings(FieldId, StartTime, EndTime)` để việc kiểm tra xung đột thời gian đạt độ phức tạp $O(\log N)$.

---

## 3. PHA 3: LẬP TRÌNH VÀ TỐI ƯU HÓA HIỆU NĂNG (BACKEND & AI AGENT)

### Prompt gửi Agent:
```text
[SYSTEM CONTEXT]: Bạn là Kỹ sư Backend C# .NET 10 và Kỹ sư AI Python Flask.
[TASK]:
1. Viết `BookingService.cs` trong C# xử lý hàm `CreateBooking`: kiểm tra số dư ví, kiểm tra đụng độ thời gian, trừ tiền ví và ghi nhận transaction.
2. YÊU CẦU ĐẶC BIỆT: Phải bảo đảm an toàn đa luồng (Thread-safe) tuyệt đối khi nhiều người cùng đặt 1 sân trong 1 mili-giây.
3. Viết `app.py` trong Python Flask tính toán Dynamic Pricing và kết nối LM Studio Qwen 7B, kèm cơ chế Smart Fallback nếu LM Studio tắt.
```

### Kết quả Agent sinh ra & Đánh giá của nhóm:
- Agent sinh ra mã nguồn sạch, phân tầng Service/Repository rõ ràng.
- **Lỗi phát hiện và can thiệp của sinh viên (Lã Quý Doanh & Bùi Thanh Bình):**
  * Sinh viên Doanh phát hiện: Ban đầu Agent dùng kiểm tra thời gian bằng `DateTime.UtcNow` dẫn đến sai lệch 7 tiếng so với giờ Việt Nam (UTC+7). Đã sửa thành `DateTime.Now` và trừ biên độ 5 phút.
  * Sinh viên Bình bổ sung: Thêm bộ nhớ đệm RAM `lru_cache(maxsize=256)` vào `app.py` để phản hồi các câu hỏi thông dụng trong 0ms.

---

## 4. PHA 4: KIỂM THỬ TỰ ĐỘNG HÓA & AN TOÀN (QA/QC TESTING AGENT)

### Prompt gửi Agent:
```text
[SYSTEM CONTEXT]: Bạn là Kỹ sư Đảm bảo Chất lượng Phần mềm (QA Automation Engineer) sử dụng xUnit và Moq trong .NET 10.
[TASK]:
1. Thiết kế bộ kiểm thử đơn vị tự động (Unit Tests) cho `BookingService` và `AIServiceClient`.
2. Phải có ít nhất 1 test case giả lập đụng độ 10 luồng song song (Concurrency Stress Test).
3. Thiết kế bộ kiểm thử tích hợp (Integration Tests) kiểm tra luồng End-to-End từ Controller đến Service và hoàn tiền.
```

### Kết quả Agent sinh ra & Đánh giá của nhóm:
- Agent sinh ra 11 Unit Tests và 3 Integration Tests.
- Toàn bộ 14 test cases được thực thi tự động qua lệnh `dotnet test` và đạt kết quả **Passed: 14/14 (100%)**.
