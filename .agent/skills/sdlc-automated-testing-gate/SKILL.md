---
name: sdlc-automated-testing-gate
description: >-
  Cổng kiểm soát chất lượng mã nguồn tự động (CI/QA Testing Gate), xác thực các ca kiểm thử đơn vị xUnit,
  kiểm tra bảo mật và đảm bảo tỷ lệ Pass 100% trước khi nghiệm thu, bàn giao hoặc commit mã nguồn cho đồ án tốt nghiệp ICTU.
---

# Kỹ Năng Cổng Kiểm Thử Tự Động & Đảm Bảo Chất Lượng (SDLC Automated Testing Gate)

Kỹ năng này hoạt động như một "người gác cổng" (Quality Gate) tự động, bảo đảm mọi thay đổi mã nguồn trước khi tích hợp vào nhánh chính đều phải trải qua kiểm tra nghiêm ngặt về cả tính năng, hiệu năng và tính an toàn bảo mật.

---

## 1. Danh Mục Kiểm Thử Tự Động xUnit (xUnit Test Suite)

Dự án có bộ kiểm thử tự động tại `tests/FootballBookingApi.Tests/`. Mọi lần chạy nghiệm thu bắt buộc phải đạt kết quả:
**Passed: 100% (Không chấp nhận bất kỳ Test Case nào bị Failed hoặc Skipped).**

Các nhóm ca kiểm thử trọng yếu:
1. **Kiểm thử Kiểm soát đồng thời (Concurrency Test):**
   - Đảm bảo 2 tiến trình đặt cùng 1 sân tại cùng 1 khung giờ thì chỉ có 1 tiến trình thành công.
2. **Kiểm thử Tính toàn vẹn số dư ví (Wallet Balance Integrity):**
   - Đặt sân khi số dư không đủ $\rightarrow$ Báo lỗi `400 Bad Request`.
   - Đặt sân thành công $\rightarrow$ Số dư ví bị trừ chính xác bằng `TotalPrice`.
3. **Kiểm thử Chính sách Hoàn tiền (Refund Policy Tests):**
   - Hủy trước 2 giờ $\rightarrow$ Hoàn 100% tiền vào ví.
   - Hủy sát giờ ($< 2$ giờ) $\rightarrow$ Từ chối thao tác, không hoàn tiền.
4. **Kiểm thử Mã hóa mật khẩu (Password Security Tests):**
   - Mật khẩu lưu trữ không được ở dạng văn bản thô (Plaintext). Bắt buộc được băm an toàn (SHA-256 / BCrypt).

---

## 2. Quy Trình Chạy Kiểm Thử Tiêu Chuẩn (Execution Runbook)

Trước khi nghiệm thu hoặc nộp bài, Agent hoặc Kỹ sư phải thực hiện lệnh:

```powershell
# Chạy toàn bộ bộ kiểm thử tự động
dotnet test tests/FootballBookingApi.Tests/FootballBookingApi.Tests.csproj --verbosity normal
```

**Tiêu chuẩn chấp nhận (Pass Criteria):**
```text
Passed! - Failed: 0, Passed: 11 (hoặc cao hơn), Skipped: 0, Total: 11
```

Nếu phát hiện bất kỳ lỗi nào, Agent phải dừng quy trình phát hành, phân tích stack trace và khắc phục triệt để trước khi báo cáo hoàn thành.

