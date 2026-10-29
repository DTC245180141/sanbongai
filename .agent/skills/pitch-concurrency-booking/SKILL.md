---
name: pitch-concurrency-booking
description: >-
  Chuyên gia xử lý kiểm soát đồng thời (Concurrency Control), chống xung đột lịch đặt sân (Anti-Race Condition),
  và đảm bảo tính toàn vẹn giao dịch đặt sân bóng với ví điện tử Virtual Wallet. Sử dụng kỹ năng này khi xây dựng,
  sửa đổi hoặc xác thực quy trình đặt chỗ sân bóng, kiểm tra tính khả dụng của sân và trừ tiền ví.
---

# Kỹ Năng Kiểm Soát Đồng Thời & Đặt Sân Bóng Toàn Vẹn (Pitch Concurrency Booking)

Kỹ năng này định nghĩa các quy tắc bắt buộc và quy trình chuẩn nhằm loại trừ 100% nguy cơ tranh chấp tài nguyên (Double-Booking) khi nhiều khách hàng cùng thao tác đặt 1 sân bóng tại một thời điểm.

---

## 1. Ràng Buộc Nghiệp Vụ Cốt Lõi (Mandatory Constraints)

1. **Khóa luồng đồng bộ (Thread-Safe Concurrency Lock):**
   - Mọi thao tác kiểm tra tính khả dụng và tạo lịch đặt sân phải nằm trong khối `lock (_lockObj)` tại tầng Application Service (`BookingService.cs`).
   - Tuyệt đối không cho phép 2 tiến trình đồng thời đọc trạng thái "Sân còn trống" của cùng một sân trong cùng một khung giờ.

2. **Ràng buộc múi giờ chuẩn (Local Timezone Enforcement):**
   - Mọi giá trị ngày giờ (`StartTime`, `EndTime`) phải được chuẩn hóa về múi giờ địa phương `SE Asia Standard Time` (+07:00).
   - Công thức kiểm tra trùng lịch hợp lệ:
     `!(NewEnd <= ExistingStart || NewStart >= ExistingEnd)` (Nếu giao nhau thời gian thì lập tức từ chối).

3. **Nguyên tắc giao dịch Ví tiền (Atomic Wallet Transaction):**
   - Chỉ được phép trừ tiền tài khoản ví (`WalletBalance`) **SAU KHI** đã xác nhận sân trống thành công trong vùng khóa luồng.
   - Nếu `WalletBalance < TotalPrice`, ném ngoại lệ `InsufficientBalanceException` và hủy giao dịch ngay lập tức.
   - Giao dịch phải ghi nhận đồng thời vào bảng `Bookings` và `Transactions` (Audit Log) trong cùng một `DbContext.SaveChangesAsync()`.

---

## 2. Quy Trình Thực Hiện Đặt Sân Chuẩn (Step-by-Step Workflow)

```
[Khách hàng gửi Yêu cầu Đặt sân]
                │
                ▼
  [Bước 1: Xác thực dữ liệu đầu vào] ──(Lỗi)──> [Trả về BadRequest]
                │ (Hợp lệ)
                ▼
  [Bước 2: Đi vào Critical Section `lock (_lockObj)`]
                │
                ▼
  [Bước 3: Kiểm tra xung đột thời gian trong CSDL]
        ├──(Đã có lịch trùng)──> [Nhả lock -> Ném ConflictException (409)]
        │
        ▼ (Sân hoàn toàn trống)
  [Bước 4: Kiểm tra số dư ví & Trừ tiền nguyên tử]
        ├──(Số dư không đủ)──> [Nhả lock -> Ném InsufficientBalance (400)]
        │
        ▼ (Đủ tiền)
  [Bước 5: Lưu Booking + Ghi sổ Transaction + Commit EF Core]
                │
                ▼
  [Bước 6: Thoát lock & Trả kết quả thành công cho Client (200 OK)]
```

---

## 3. Tiêu Chí Nghiệm Thu & Kiểm Thử (Validation Criteria)

- Chạy kiểm thử tự động với ít nhất 10 luồng đặt sân đồng thời (Parallel Tasks).
- Kết quả bắt buộc: Duy nhất **1 yêu cầu thành công**, các yêu cầu còn lại nhận thông báo lỗi lịch đã được đặt.
- Số dư ví tiền của người dùng chỉ bị trừ đúng một lần tương ứng với lịch thành công.

