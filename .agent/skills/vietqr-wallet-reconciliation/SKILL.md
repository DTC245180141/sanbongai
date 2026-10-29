---
name: vietqr-wallet-reconciliation
description: >-
  Chuyên gia quản trị ví ảo (Virtual Wallet), thanh toán mã động VietQR NAPAS 247 MBBank, đối soát nạp tiền và chính sách
  tự động hoàn cọc 100% khi hủy sân. Sử dụng kỹ năng này khi can thiệp vào logic tài chính, số dư ví, nạp rút hoặc đối soát đơn đặt sân.
---

# Kỹ Năng Quản Lý Ví Ảo & Đối Soát Thanh Toán VietQR (VietQR Wallet Reconciliation)

Kỹ năng này chuẩn hóa toàn bộ vòng đời dòng tiền trong hệ thống PitchAI, từ khâu nạp tiền tự động qua QR ngân hàng đến khâu trừ tiền đặt sân và hoàn cọc khi hủy lịch.

---

## 1. Chuẩn Hóa Mã VietQR Động (Dynamic VietQR Standard)

1. **Cấu trúc sinh mã VietQR:**
   - Định dạng ảnh QR: Chuẩn Quick Response Code tích hợp NAPAS 247 qua ngân hàng MBBank.
   - Cú pháp nội dung chuyển khoản bắt buộc (Transaction Memo):
     `NAPTIEN {UserId}` (Ví dụ: `NAPTIEN 102`).
   - Cú pháp mã định danh này là duy nhất (Unique) để hệ thống tự động bóc tách và cộng tiền vào đúng tài khoản người dùng.

2. **Quy trình Đối soát Nạp tiền (Deposit Reconciliation):**
   - Khi người dùng gửi yêu cầu nạp tiền, hệ sinh thái tạo một bản ghi `DepositRequest` với trạng thái `PENDING`.
   - Quản trị viên (Admin) hoặc Webhook Ngân hàng xác nhận tiền về tài khoản thực $\rightarrow$ Chuyển trạng thái sang `APPROVED`.
   - Số dư ví (`User.WalletBalance`) tăng tương ứng và một bản ghi `Transaction` loại `DEPOSIT` được ghi vào sổ cái.

---

## 2. Quy Định Toàn Vẹn Số Dư & Hoàn Tiền (Financial Integrity & Refund Policy)

1. **Ràng buộc số dư không âm:**
   - CSDL SQL Server và mã nguồn C# bắt buộc kiểm tra điều kiện:
     `WalletBalance >= 0`.
   - Mọi hành vi trừ tiền khiến số dư âm đều bị chặn ngay ở mức Entity Validation.

2. **Quy tắc Hoàn cọc tự động 100% (Automated Refund Rule):**
   - **Điều kiện hoàn tiền:** Khách hàng hủy đặt sân trước giờ bắt đầu thi đấu tối thiểu **02 giờ**.
   - **Xử lý hoàn tiền:**
     - Trạng thái Booking chuyển thành `CANCELLED`.
     - Số dư ví `WalletBalance` được cộng lại đúng 100% số tiền đã thanh toán (`TotalPrice`).
     - Ghi nhận `Transaction` mới với mô tả: `Hoàn tiền hủy sân [Mã Đơn: #{BookingId}]`.
   - **Từ chối hoàn tiền:** Nếu khách hàng yêu cầu hủy khi thời gian còn lại $< 02$ giờ $\rightarrow$ Từ chối thao tác, giữ nguyên trạng thái đơn.
