import io, sys

with open('BAO_CAO_CHI_TIET_DO_AN_TOT_NGHIEP.md', 'r', encoding='utf-8') as f:
    content = f.read()

old_str = """### Hạn chế còn tồn tại:
* Việc phê duyệt nạp tiền ví hiện tại vẫn cần một bước bấm "Xác nhận" thủ công từ Quản trị viên trên trang Admin (chưa tích hợp Webhook tự động lắng nghe biến động số dư ngân hàng qua Open Banking).
* Mô hình Chatbot LLM chạy Local trên máy tính cá nhân nên phụ thuộc vào cấu hình phần cứng (RAM, GPU) của máy chủ triển khai."""

new_str = """### Hạn chế còn tồn tại:
* Việc phê duyệt nạp tiền ví hiện tại vẫn cần một bước bấm "Xác nhận" thủ công từ Quản trị viên trên trang Admin (chưa tích hợp Webhook tự động lắng nghe biến động số dư ngân hàng qua Open Banking).
* Mô hình Chatbot LLM chạy Local trên máy tính cá nhân nên phụ thuộc vào cấu hình phần cứng (RAM, GPU) của máy chủ triển khai.
* Cơ chế lưu trữ mật khẩu hiện tại áp dụng thuật toán băm SHA-256 thuần (chưa tích hợp chuỗi Salt ngẫu nhiên riêng cho từng tài khoản), dù đảm bảo không lưu trữ plaintext nhưng chưa đạt chuẩn kháng Rainbow Table so với các thuật toán chuyên dụng như BCrypt hay PBKDF2."""

old_dev = """## 3. Hướng phát triển và mở rộng trong tương lai
Để phát triển hệ thống thành một nền tảng thương mại toàn diện cung cấp cho các chuỗi thể thao chuyên nghiệp, nhóm đề xuất các hướng nâng cấp tiếp theo:
1. **Tự động hóa hoàn toàn cổng nạp tiền qua Webhook ngân hàng:**"""

new_dev = """## 3. Hướng phát triển và mở rộng trong tương lai
Để phát triển hệ thống thành một nền tảng thương mại toàn diện cung cấp cho các chuỗi thể thao chuyên nghiệp, nhóm đề xuất các hướng nâng cấp tiếp theo:
1. **Nâng cấp cơ chế băm mật khẩu từ SHA-256 thuần lên BCrypt / PBKDF2:**
   * Thay thế hàm băm SHA-256 bằng thuật toán **BCrypt** hoặc **PBKDF2** kèm chuỗi Salt ngẫu nhiên (tối thiểu 128-bit) sinh riêng cho từng người dùng và hệ số độ khó (Cost Factor >= 12) có thể điều chỉnh linh hoạt, bảo vệ tuyệt đối thông tin xác thực của khách hàng trước các nguy cơ tấn công từ điển và Rainbow Table.
2. **Tự động hóa hoàn toàn cổng nạp tiền qua Webhook ngân hàng:**"""

if old_str in content:
    content = content.replace(old_str, new_str)
    print("Updated old_str")
else:
    print("WARNING: old_str not found")

if old_dev in content:
    content = content.replace(old_dev, new_dev)
    content = content.replace('2. **Tích hợp phần cứng IoT', '3. **Tích hợp phần cứng IoT')
    content = content.replace('3. **Nhận diện khuôn mặt', '4. **Nhận diện khuôn mặt')
    content = content.replace('4. **Tính năng Ghép đội', '5. **Tính năng Ghép đội')
    print("Updated old_dev and renumbered")
else:
    print("WARNING: old_dev not found")

with open('BAO_CAO_CHI_TIET_DO_AN_TOT_NGHIEP.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved BAO_CAO_CHI_TIET_DO_AN_TOT_NGHIEP.md successfully!")

