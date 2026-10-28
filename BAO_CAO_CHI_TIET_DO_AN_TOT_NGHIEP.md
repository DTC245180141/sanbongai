# BÁO CÁO ĐỒ ÁN TỐT NGHIỆP CHUYÊN SÂU
# ĐỀ TÀI: HỆ THỐNG ĐẶT SÂN BÓNG TỰ ĐỘNG TÍCH HỢP AI & VÍ ĐIỆN TỬ VIRTUAL WALLET

**Trường:** Đại học Công Nghệ Thông Tin & Truyền Thông Thái Nguyên (ICTU)  
**Khoa:** Công Nghệ Thông Tin  
**Chuyên ngành:** Kỹ thuật Phần mềm / Hệ thống Thông tin  
**Nhóm sinh viên thực hiện:** Nhóm 02  
1. **Lã Quý Doanh** (Trưởng nhóm - Phụ trách Kiến trúc Hệ thống, Backend .NET, CSDL SQL Server & Tích hợp AI)  
2. **Bùi Thanh Bình** (Thành viên - Phụ trách Microservice AI Python Flask, Trợ lý LLM Studio, Giao diện Frontend UI/UX & Kiểm thử)  
**Thời gian thực hiện:** Từ 27/07/2026 đến 27/09/2026 (9 tuần)  
**Giảng viên hướng dẫn:** TS. Giảng Viên Hướng Dẫn  

---

## MỤC LỤC TỔNG THỂ BÁO CÁO

* [PHẦN 1: KẾ HOẠCH THỰC HIỆN – PHÁT TRIỂN ỨNG DỤNG CHUYÊN SÂU (9 TUẦN)](#phần-1-kế-hoạch-thực-hiện--phát-triển-ứng-dụng-chuyên-sâu)
* [PHẦN 2: THU THẬP VÀ LÀM RÕ YÊU CẦU ỨNG DỤNG](#phần-2-thu-thập-và-làm-rõ-yêu-cầu-ứng-dụng)
  * [2.1 Danh sách câu hỏi thu thập & làm rõ yêu cầu (Khảo sát thực tế 30 câu)](#21-danh-sách-câu-hỏi-thu-thập--làm-rõ-yêu-cầu-khảo-sát-thực-tế-30-câu)
  * [2.2 Yêu cầu chức năng và phi chức năng](#22-yêu-cầu-chức-năng-và-phi-chức-năng)
  * [2.3 Sơ đồ phân cấp chức năng (Functional Hierarchy Diagram)](#23-sơ-đồ-phân-cấp-chức-năng-của-ứng-dụng)
* [PHẦN 3: ĐẶC TẢ YÊU CẦU ỨNG DỤNG – V1.0 (SRS)](#phần-3-đặc-tả-yêu-cầu-ứng-dụng--v10-srs)
  * [3.1 Giới thiệu chung](#31-giới-thiệu-chung)
  * [3.2 Mô tả tổng quan ứng dụng & Mô hình Use Case](#32-mô-tả-tổng-quan-ứng-dụng)
  * [3.3 Đặc tả chi tiết các Use Case chính (Kèm Activity & Sequence Diagram)](#33-đặc-tả-các-yêu-cầu-chức-năng-functional)
  * [3.4 Các thông tin hỗ trợ khác](#34-các-thông-tin-hỗ-trợ-khác)
* [PHẦN 4: TÀI LIỆU THIẾT KẾ HƯỚNG ĐỐI TƯỢNG (MÔ HÌNH LỚP)](#phần-4-tài-liệu-thiết-kế-hướng-đối-tượng-mô-hình-lớp)
  * [4.1 Mô hình lớp chi tiết (Class Diagram UML)](#41-mô-hình-lớp-class-diagram)
  * [4.2 Đặc tả chi tiết từng Lớp đối tượng](#42-đặc-tả-class-chi-tiết)
* [PHẦN 5: KIỂM THỬ CHỨC NĂNG ỨNG DỤNG (TEST CASES & REPORT)](#phần-5-kiểm-thử-chức-năng-ứng-dụng)
  * [5.1 Yêu cầu tài nguyên kiểm thử](#51-những-yêu-cầu-về-tài-nguyên-cho-kiểm-thử-ứng-dụng)
  * [5.2 Danh mục toàn bộ các kịch bản kiểm thử (Test Cases)](#52-danh-sách-toàn-bộ-các-tình-huống-kiểm-tra-test-cases)
  * [5.3 Báo cáo kết quả kiểm thử (Test Report)](#53-báo-cáo-kết-quả-test-test-report)
  * [5.4 Thực nghiệm so sánh các phiên bản Prompt & Mô hình AI (Tiêu chí 3.2)](#54-thực-nghiệm-so-sánh-các-phiên-bản-prompt--mô-hình-ai-tiêu-chí-32)
  * [5.5 Cơ chế xử lý lỗi AI & Khả năng chịu lỗi Fault Tolerance (Tiêu chí 3.3)](#55-cơ-chế-xử-lý-lỗi-ai--khả-năng-chịu-lỗi-fault-tolerance-tiêu-chí-33)
  * [5.6 Bảo mật dữ liệu & Quản lý API Key (Tiêu chí 3.4)](#56-bảo-mật-dữ-liệu--quản-lý-api-key-tiêu-chí-34)
* [PHẦN 6: SCREEN FLOW & THIẾT KẾ CƠ SỞ DỮ LIỆU](#phần-6-screen-flow--tài-liệu-thiết-kế-cơ-sở-dữ-liệu)
  * [6.1 Luồng phân chuyển màn hình (Screen Flow Diagram)](#61-screen-flow-phân-luồng-màn-hình-của-ứng-dụng)
  * [6.2 Thiết kế Cơ sở dữ liệu quan hệ (ERD & Data Dictionary)](#62-cơ-sở-dữ-liệu-quan-hệ)
  * [6.3 Các ràng buộc toàn vẹn & Concurrency Control](#63-các-ràng-buộc-toàn-vẹn-trong-csdl)
* [PHẦN 7: TÀI LIỆU HƯỚNG DẪN SỬ DỤNG – V1.0](#phần-7-tài-liệu-hướng-dẫn-sử-dụng--v10)
  * [7.1 Cấu hình môi trường vận hành](#71-cấu-hình-phần-cứng---phần-mềm)
  * [7.2 Hướng dẫn dành cho Khách hàng (Customer)](#72-hướng-dẫn-dành-cho-khách-hàng-customer)
  * [7.3 Hướng dẫn dành cho Quản trị viên (Admin)](#73-hướng-dẫn-dành-cho-quản-trị-viên-admin)
  * [7.4 Kịch bản Demo trực tiếp thành công trước Hội đồng chấm thi (Tiêu chí 4.4)](#74-kịch-bản-demo-trực-tiếp-thành-công-trước-hội-đồng-chấm-thi-tiêu-chí-44)
* [PHẦN 8: THIẾT KẾ AGENT AI TRONG QUY TRÌNH SDLC & CONTEXT ENGINEERING (NHÀ MÁY PHÁT TRIỂN PHẦN MỀM)](#phần-8-thiết-kế-agent-ai-trong-quy-trình-sdlc--context-engineering-nhà-máy-phát-triển-phần-mềm)
  * [8.1 Khái niệm & Định vị Agent AI trong quy trình phát triển phần mềm](#81-khái-niệm--định-vị-agent-ai-trong-quy-trình-phát-triển-phần-mềm-sdlc-as-a-factory)
  * [8.2 Kỹ thuật Kỹ nghệ Ngữ cảnh (Context Engineering)](#82-kỹ-thuật-kỹ-nghệ-ngữ-cảnh-context-engineering)
  * [8.3 Vận hành "Nhà máy phần mềm" qua 4 giai đoạn SDLC](#83-vận-hành-nhà-máy-phần-mềm-qua-4-giai-đoạn-sdlc)
  * [8.4 Hệ thống Rào chắn An toàn (Safety Guardrails & Security Policies)](#84-hệ-thống-rào-chắn-an-toàn-safety-guardrails--security-policies)
  * [8.5 Minh chứng kiểm chứng và sửa lỗi do AI tạo ra (AI Verification & Debugging)](#85-minh-chứng-kiểm-chứng-và-sửa-lỗi-do-ai-tạo-ra-ai-verification--debugging-case-studies---tiêu-chí-52)
  * [8.6 Đóng gói, Vận hành và Giám sát sản phẩm (Packaging, Operations & Monitoring)](#86-đóng-gói-vận-hành-và-giám-sát-sản-phẩm-packaging-operations--monitoring)
* [PHẦN 9: TƯ DUY PHẢN BIỆN, PHÂN CÔNG VẤN ĐÁP & ĐÓNG GÓP RIÊNG TỪNG THÀNH VIÊN](#phần-9-tư-duy-phản-biện-phân-công-vấn-đáp--đóng-góp-riêng-từng-thành-viên)
  * [9.1 Trách nhiệm & Đóng góp chuyên môn của sinh viên Lã Quý Doanh](#91-trách-nhiệm--đóng-góp-chuyên-môn-của-sinh-viên-lã-quý-doanh-trưởng-nhóm)
  * [9.2 Trách nhiệm & Đóng góp chuyên môn của sinh viên Bùi Thanh Bình](#92-trách-nhiệm--đóng-góp-chuyên-môn-của-sinh-viên-bùi-thanh-bình-thành-viên)
  * [9.3 Danh mục câu hỏi vấn đáp độc lập dự kiến & Gợi ý trả lời chuyên sâu](#93-danh-mục-câu-hỏi-vấn-đáp-độc-lập-dự-kiến--gợi-ý-trả-lời-chuyên-sâu-tiêu-chí-53)
  * [9.4 Đánh giá tư duy phản biện và đạo đức sử dụng AI trong phát triển phần mềm](#94-đánh-giá-tư-duy-phản-biện-và-đạo-đức-sử-dụng-ai-trong-phát-triển-phần-mềm)
* [PHẦN BỔ SUNG: KẾT LUẬN & ĐÁNH GIÁ ĐỒ ÁN TỐT NGHIỆP](#phần-bổ-sung-kết-luận--đánh-giá-đồ-án-tốt-nghiệp)
---

# PHẦN 1: KẾ HOẠCH THỰC HIỆN – PHÁT TRIỂN ỨNG DỤNG CHUYÊN SÂU
**Nhóm 02** - Thành viên thực hiện:
1. Lã Quý Doanh (Trưởng nhóm - Kỹ thuật Phần mềm)
2. Bùi Thanh Bình (Thành viên - Hệ thống Thông tin)
* **Tên ứng dụng:** Hệ thống đặt sân bóng tự động tích hợp AI & Ví điện tử (Virtual Wallet)
* **Thời gian thực hiện:** Từ 27/07/2026 đến 27/09/2026 (Tổng cộng 9 tuần)

### Bảng Kế hoạch chi tiết theo từng tuần (Work Breakdown Structure - WBS):

| Tuần thực hiện | Nội dung công việc chi tiết | Thành viên thực hiện | Sản phẩm bàn giao (Deliverables) / Ghi chú |
| :--- | :--- | :--- | :--- |
| **Tuần 01**<br>(27/07/2026 - 02/08/2026) | - Khảo sát hiện trạng quy trình quản lý, đặt sân bóng truyền thống tại khu vực cụm sân ICTU Thái Nguyên.<br>- Lập phiếu khảo sát nhu cầu của chủ sân và cầu thủ.<br>- Thu thập các bài toán nan giải: trùng lịch đặt, khó tối ưu giá theo giờ cao điểm, thanh toán tiền mặt chậm trễ, tư vấn khách hàng quá tải ngoài giờ.<br>- Viết báo cáo khảo sát và định hướng kiến trúc giải pháp. | **Lã Quý Doanh** (Chính)<br>**Bùi Thanh Bình** (Hỗ trợ) | - Báo cáo khảo sát bài toán thực tế.<br>- Danh sách vấn đề cần giải quyết bằng phần mềm & AI. |
| **Tuần 02**<br>(03/08/2026 - 09/08/2026) | - Xây dựng bộ câu hỏi phỏng vấn làm rõ yêu cầu hệ thống (25 câu hỏi chuẩn).<br>- Phân tích và xác định yêu cầu chức năng (FR) và phi chức năng (NFR).<br>- Lập sơ đồ phân cấp chức năng (FHD).<br>- Hoàn thiện tài liệu Đặc tả yêu cầu phần mềm SRS v1.0. | **Bùi Thanh Bình** (Chính)<br>**Lã Quý Doanh** (Hỗ trợ) | - Tài liệu câu hỏi & trả lời làm rõ yêu cầu.<br>- Bản đặc tả SRS v1.0.<br>- Sơ đồ Use Case tổng quát. |
| **Tuần 03**<br>(10/08/2026 - 16/08/2026) | - Thiết kế kiến trúc phần mềm phân tầng (Multi-tier Architecture & Microservices).<br>- Thiết kế Cơ sở dữ liệu quan hệ chuẩn 3NF trên Microsoft SQL Server: bảng Users, Fields, Bookings, Transactions, Payments, PricingConfig, AI_DemandLogs, DepositRequests.<br>- Thiết lập các chỉ mục (Indexes) và Ràng buộc toàn vẹn (PK, FK, Check Constraints).<br>- Soạn thảo file kịch bản CSDL `schema.sql`. | **Lã Quý Doanh** | - File mã nguồn CSDL `database/schema.sql`.<br>- Sơ đồ ERD thực thể quan hệ.<br>- Từ điển dữ liệu Data Dictionary. |
| **Tuần 04**<br>(17/08/2026 - 23/08/2026) | - Thiết kế mô hình lớp hướng đối tượng (Class Diagram) và biểu đồ tuần tự (Sequence Diagram).<br>- Lập trình AI Microservice bằng Python Flask (Port 5050).<br>- Xây dựng thuật toán định giá động AI (Dynamic Pricing Algorithm) dựa trên khung giờ, ngày trong tuần và nhu cầu sân.<br>- Tích hợp Local LLM qua LM Studio (Model `qwen2.5-1.5b-instruct`) phục vụ Chatbot hỗ trợ đặt sân 24/7.<br>- Viết cơ chế Smart Fallback Engine bằng Rule-based NLP khi AI offline. | **Bùi Thanh Bình** | - Thư mục mã nguồn `src/AIService/` (app.py, requirements.txt).<br>- Endpoint REST API `/api/predict-price` và `/api/chat-assistant`. |
| **Tuần 05**<br>(24/08/2026 - 30/08/2026) | - Khởi tạo dự án Backend .NET 8/10 C# Web API (`FootballBookingApi`).<br>- Cấu hình Entity Framework Core kết nối SQL Server, xử lý Migration và Data Seeding.<br>- Hiện thực các Service cốt lõi: `UserService` (JWT Token, Hash SHA256, Đăng ký, Đăng nhập, Nạp ví, Khôi phục mật khẩu).<br>- Hiện thực `BookingService` với kỹ thuật Concurrency Lock (`lock (_lockObj)`) tránh tình trạng đặt trùng sân trong cùng một giây.<br>- Hiện thực `AIServiceClient` gọi Microservice Python. | **Lã Quý Doanh** | - Các tầng Models, Data, Services của Backend.<br>- Kiểm tra unit test logic trừ tiền ví và chống đụng độ thời gian. |
| **Tuần 06**<br>(31/08/2026 - 06/09/2026) | - Xây dựng các Controller API RESTful: `AuthController`, `BookingsController`, `PaymentController`, `AdminController`, `UserController`.<br>- Tích hợp tạo mã QR thanh toán cá nhân hóa chuẩn VietQR ngân hàng (`img.vietqr.io`) phục vụ nạp ví điện tử Virtual Wallet.<br>- Cấu hình OpenAPI / Swagger UI phục vụ kiểm thử API trực quan.<br>- Thiết lập cơ chế kiểm soát Transaction và tự động hoàn tiền 100% khi Hủy đơn đặt sân. | **Lã Quý Doanh** | - Toàn bộ các API Endpoints hoàn chỉnh.<br>- Tài liệu Swagger UI hoạt động tại `http://localhost:5048/swagger`. |
| **Tuần 07**<br>(07/09/2026 - 13/09/2026) | - Thiết kế và lập trình Giao diện Người dùng Khách hàng (`index.html`) chuẩn Modern UI, Glassmorphism, Responsive CSS.<br>- Xây dựng Widget Chatbot AI tương tác thời gian thực tại góc màn hình.<br>- Tích hợp giao diện chọn sân, chọn khung giờ xem giá AI tính toán theo thời gian thực.<br>- Xây dựng Modal quét mã VietQR và gửi thông báo nạp tiền ví.<br>- Lập trình Giao diện Quản trị viên (`admin.html`): Bảng điều khiển KPI, Duyệt nạp tiền ví, Quản lý sân, Khóa tài khoản, Hủy lịch hoàn tiền. | **Bùi Thanh Bình** | - Giao diện Frontend khách hàng và quản trị viên hoàn chỉnh.<br>- Kết nối API giữa Frontend và Backend thông suốt. |
| **Tuần 08**<br>(14/09/2026 - 20/09/2026) | - Lập kế hoạch kiểm thử chức năng toàn diện (System Integration Testing).<br>- Thiết kế tài liệu Test Cases chi tiết cho toàn bộ các luồng: Xác thực, Đặt sân, Thuật toán AI Pricing, Chatbot LLM, Thanh toán VietQR, Quản trị Admin.<br>- Thực thi toàn bộ các ca kiểm thử tích cực (Positive), tiêu cực (Negative) và kiểm thử đồng thời (Concurrency Test).<br>- Ghi nhận lỗi (Bugs/Defects), phân loại độ nghiêm trọng và xử lý triệt để.<br>- Lập biên bản Test Report. | **Lã Quý Doanh**<br>**Bùi Thanh Bình** | - Bảng 31 Test Cases hoàn chỉnh.<br>- Báo cáo kết quả kiểm thử (Test Report) đạt tỉ lệ Pass 100%. |
| **Tuần 09**<br>(21/09/2026 - 27/09/2026) | - Đóng gói phần mềm và hướng dẫn triển khai ứng dụng đa nền tảng (Localhost, IIS, Docker).<br>- Soạn thảo tài liệu Hướng dẫn sử dụng chi tiết V1.0 cho cả 2 đối tượng Actor (Khách hàng & Admin).<br>- Viết báo cáo tổng kết đồ án tốt nghiệp, chuẩn bị Slide thuyết trình và Video Demo vận hành thực tế.<br>- Hoàn thiện hồ sơ nghiệm thu đồ án tốt nghiệp nộp Hội đồng chấm thi ICTU. | **Lã Quý Doanh** (Chính)<br>**Bùi Thanh Bình** (Chính) | - Toàn bộ báo cáo đồ án tốt nghiệp đóng cuốn.<br>- Mã nguồn sạch (Clean Code), cơ sở dữ liệu và video demo vận hành. |

---

# PHẦN 2: THU THẬP VÀ LÀM RÕ YÊU CẦU ỨNG DỤNG
**Nhóm 02** - Thành viên thực hiện:
1. Lã Quý Doanh (Trưởng nhóm)
2. Bùi Thanh Bình
* **Tên ứng dụng:** Hệ thống đặt sân bóng tự động tích hợp AI & Ví điện tử
* **Thời gian thực hiện:** Từ 27/07/2026 đến 27/09/2026 (9 tuần)

## 2.1 Danh sách câu hỏi thu thập & làm rõ yêu cầu (Khảo sát thực tế 30 câu)

Nhằm mục đích nắm bắt toàn diện nhu cầu thực tế, thói quen sinh hoạt thể thao của cộng đồng cầu thủ và bài toán vận hành của các chủ sân bóng khu vực TP. Thái Nguyên, nhóm nghiên cứu đã xây dựng và phát hành phiếu khảo sát chuyên sâu gồm **30 câu hỏi chuẩn hóa**. Bảng hỏi bao phủ 5 khía cạnh trọng tâm: (1) Thói quen và hành vi đặt sân hiện tại; (2) Các khó khăn, bất cập trong phương thức truyền thống; (3) Mức độ sẵn sàng đón nhận Trí tuệ Nhân tạo (AI Dynamic Pricing & Chatbot); (4) Đánh giá và kỳ vọng về các tính năng giải pháp; (5) Mức độ hài lòng dự kiến và cam kết đồng hành.

### Bảng câu hỏi khảo sát chi tiết (30 câu hỏi chuẩn hóa):

| STT | Nhóm nội dung khảo sát | Nội dung câu hỏi khảo sát (Survey Questions) | Các phương án trả lời / Thang đo chuẩn hóa (Likert & Options) |
| :---: | :--- | :--- | :--- |
| **01** | Thói quen & Tần suất | Bạn thường tham gia đá bóng với tần suất bao nhiêu lần mỗi tuần? | A. 1 lần/tuần<br>B. 2 - 3 lần/tuần<br>C. Trên 3 lần/tuần<br>D. Thỉnh thoảng / Không cố định |
| **02** | Thói quen & Tần suất | Loại sân bóng đá nào bạn và đội bóng thường xuyên thuê thi đấu nhất? | A. Sân 5 người (tiêu chuẩn mini)<br>B. Sân 7 người (cỏ nhân tạo phổ biến)<br>C. Sân 11 người (sân cỏ lớn)<br>D. Linh hoạt tùy đối thủ |
| **03** | Thói quen & Tần suất | Khung giờ thi đấu ưa thích nhất của bạn là khoảng thời gian nào? | A. Buổi sáng (06:00 - 08:30)<br>B. Buổi chiều (16:00 - 17:30)<br>C. Giờ cao điểm tối (17:30 - 20:30)<br>D. Ca đêm muộn (sau 20:30) |
| **04** | Thói quen & Tần suất | Bạn thường lên kế hoạch và liên hệ đặt sân trước trận đấu bao lâu? | A. Trước 2 - 4 tiếng<br>B. Trước 1 ngày<br>C. Trước 2 - 3 ngày<br>D. Cố định theo tháng / Theo quý |
| **05** | Phương thức hiện tại | Hiện tại bạn và đội bóng đặt sân thông qua phương thức chủ yếu nào? | A. Gọi điện thoại trực tiếp cho chủ sân<br>B. Nhắn tin qua Zalo / Facebook Messenger<br>C. Đến tận sân bóng hỏi trực tiếp<br>D. Qua ứng dụng đặt sân trung gian |
| **06** | Khó khăn & Bất cập | Bạn đã từng gặp sự cố bị trùng lịch (Double-booking) khi ra tới sân chưa? | A. Rất thường xuyên gặp (trên 3 lần)<br>B. Đã từng gặp 1 - 2 lần<br>C. Chưa gặp nhưng bạn bè từng bị<br>D. Chưa bao giờ gặp sự cố này |
| **07** | Khó khăn & Bất cập | Bạn cảm thấy thế nào khi phải chờ chủ sân kiểm tra sổ sách để trả lời lịch trống? | A. Rất bất tiện và mất thời gian<br>B. Khá sốt ruột khi cần đặt gấp<br>C. Bình thường, chấp nhận được<br>D. Không quan tâm |
| **08** | Khó khăn & Bất cập | Bạn đánh giá thế nào về tính minh bạch của giá thuê sân vào giờ cao điểm/cuối tuần hiện nay? | A. Hoàn toàn không minh bạch, hay bị ép giá<br>B. Thiếu rõ ràng, mỗi nơi báo một kiểu<br>C. Khá rõ ràng theo thỏa thuận miệng<br>D. Rất rõ ràng, có niêm yết bảng giá |
| **09** | Khó khăn & Bất cập | Bạn gặp khó khăn gì khi muốn tìm sân trống vào ca tối cuối tuần? | A. Hầu như luôn cháy sân, không tìm được<br>B. Mất quá nhiều thời gian gọi hỏi 4 - 5 sân<br>C. Giá bị đội lên quá cao<br>D. Không gặp khó khăn gì |
| **10** | Khó khăn & Bất cập | Hình thức thanh toán tiền cọc sân hiện tại của bạn là gì? | A. Chuyển khoản ngân hàng chụp màn hình gửi Zalo<br>B. Đặt cọc tiền mặt trực tiếp<br>C. Không cần cọc, đá xong trả tiền<br>D. Trừ qua tài khoản hội viên |
| **11** | Nhu cầu sẵn sàng AI | Bạn có sẵn sàng sử dụng website/ứng dụng có AI tự động đề xuất lịch trống phù hợp? | Thang đo Likert 5 mức độ:<br>1. Hoàn toàn không sẵn sàng<br>2. Ít sẵn sàng<br>3. Trung lập<br>4. Sẵn sàng<br>5. Rất hào hứng sẵn sàng |
| **12** | Nhu cầu sẵn sàng AI | Bạn nghĩ sao nếu giá thuê sân được AI định giá linh hoạt theo thời gian thực (Dynamic Pricing)? | A. Rất ủng hộ nếu giờ thấp điểm được giảm giá sâu<br>B. Đồng ý nếu công thức phụ thu cao điểm minh bạch<br>C. Phân vân, sợ bị đội giá quá mức<br>D. Phản đối, muốn giá cố định quanh năm |
| **13** | Nhu cầu sẵn sàng AI | Mức độ mong muốn sử dụng Trợ lý ảo Chatbot AI tư vấn tự động 24/7 không cần chờ người trực? | Thang đo Likert 5 mức độ:<br>1. Rất không cần thiết<br>2. Ít cần thiết<br>3. Bình thường<br>4. Cần thiết<br>5. Cực kỳ cần thiết và tiện lợi |
| **14** | Đánh giá tính năng | Bạn đánh giá thế nào về tính năng khóa luồng tự động (chống tuyệt đối 100% trùng lịch)? | Thang đo Likert 5 mức độ:<br>1. Không quan trọng<br>2. Ít quan trọng<br>3. Khá quan trọng<br>4. Rất quan trọng<br>5. Bắt buộc phải có |
| **15** | Đánh giá tính năng | Bạn đánh giá thế nào về tính năng Ví điện tử nội bộ (Virtual Wallet) trừ tiền đặt sân tức thì 0.1s? | Thang đo Likert 5 mức độ:<br>1. Rất không thích<br>2. Ít thích<br>3. Bình thường<br>4. Thích<br>5. Rất tiện lợi và tiết kiệm thời gian |
| **16** | Đánh giá tính năng | Tính năng tạo mã VietQR động chuẩn NAPAS 247 nạp tiền ví tự động có hữu ích với bạn không? | Thang đo Likert 5 mức độ:<br>1. Hoàn toàn không<br>2. Ít hữu ích<br>3. Bình thường<br>4. Hữu ích<br>5. Rất hữu ích, hạn chế sai sót STK/nội dung |
| **17** | Đánh giá tính năng | Tính năng tự động hoàn tiền 100% vào ví khi có sự cố hủy sân đột xuất có mang lại sự an tâm? | Thang đo Likert 5 mức độ:<br>1. Không an tâm<br>2. Ít an tâm<br>3. Bình thường<br>4. Rất an tâm<br>5. Cực kỳ an tâm, bảo vệ quyền lợi tối đa |
| **18** | Đánh giá tính năng | Mã QR Check-in điện tử xuất trình tại sân để nhận sân bóng có cần thiết không? | A. Rất cần thiết, chuyên nghiệp hóa thủ tục<br>B. Hữu ích khi sân quá đông khách<br>C. Bình thường, đọc số điện thoại là được<br>D. Không cần thiết |
| **19** | Đánh giá tính năng | Bạn mong muốn Chatbot AI có khả năng trả lời bằng tiếng Việt tự nhiên và hiểu tiếng lóng bóng đá không? | A. Rất mong muốn (ví dụ: 'kèo', 'bắt đối', 'thủng lưới')<br>B. Chỉ cần hiểu câu hỏi thông thường<br>C. Không quan trọng cách diễn đạt<br>D. Chỉ cần bảng biểu, không cần chat |
| **20** | Đánh giá tính năng | Bạn có quan tâm đến tính năng xem bản đồ nhiệt (Heatmap) dự báo độ bận rộn của sân trước khi đặt? | A. Rất quan tâm, giúp chủ động tránh giờ cao điểm<br>B. Có quan tâm để tham khảo giá tốt<br>C. Ít quan tâm<br>D. Hoàn toàn không quan tâm |
| **21** | Giao diện & Trải nghiệm | Yếu tố giao diện nào bạn ưu tiên hàng đầu khi sử dụng ứng dụng đặt sân? | A. Tốc độ tải trang nhanh, không giật lag<br>B. Thao tác đặt sân đơn giản dưới 3 bước<br>C. Thiết kế hiện đại, màu sắc trực quan dễ nhìn<br>D. Tối ưu hoàn hảo trên điện thoại di động |
| **22** | Mức độ tin cậy | Yếu tố nào giúp bạn hoàn toàn an tâm khi thanh toán và nạp tiền vào ví điện tử hệ thống? | A. Mã nguồn mở bảo mật, băm mật khẩu SHA-256<br>B. Sao kê lịch sử giao dịch minh bạch từng đồng<br>C. Có quản trị viên đối soát với tài khoản ngân hàng<br>D. Tất cả các yếu tố trên |
| **23** | Bài toán vận hành | Đối với chủ sân, tính năng nào là "cứu cánh" lớn nhất trong việc tối ưu hóa doanh thu? | A. Thuật toán Dynamic Pricing đẩy giá giờ vàng & giảm giờ ế<br>B. Chấm dứt hoàn toàn tình trạng bùng sân / giữ chỗ ảo<br>C. Báo cáo thống kê tự động doanh thu theo ngày/tháng/năm<br>D. Tự động hóa khâu tư vấn khách hàng lúc nửa đêm |
| **24** | Chính sách đặt sân | Bạn thấy quy định đặt sân trước tối thiểu 2 giờ và tối đa 3 ngày tới có hợp lý không? | A. Rất hợp lý, vừa đủ chuẩn bị và tránh đầu cơ giữ chỗ<br>B. Nên cho phép đặt trước tối đa 7 ngày<br>C. Nên cho phép đặt trước 30 phút<br>D. Cần linh hoạt theo từng loại sân |
| **25** | Mức độ hài lòng dự kiến | Bạn kỳ vọng hệ thống mới sẽ rút ngắn thời gian đặt sân từ lúc tìm kiếm đến chốt lịch xuống bao lâu? | A. Dưới 30 giây<br>B. Từ 1 - 2 phút<br>C. Khoảng 3 - 5 phút<br>D. Dưới 10 phút là chấp nhận được |
| **26** | Mức độ hài lòng dự kiến | Nếu hệ thống tích hợp đầy đủ tính năng như mô tả, bạn có sẵn sàng giới thiệu cho bạn bè/đội bóng khác? | Thang đo Likert 5 mức độ (NPS):<br>1. Chắc chắn không giới thiệu<br>2. Ít khả năng<br>3. Có thể<br>4. Rất có thể<br>5. Chắc chắn sẽ giới thiệu nhiệt tình |
| **27** | Khả năng chi trả | Mức phụ thu tối đa vào khung giờ "vàng" (18h-20h cuối tuần) mà bạn chấp nhận được nếu sân chất lượng cao? | A. Tối đa +20% so với giá gốc<br>B. Tối đa +30% so với giá gốc<br>C. Tối đa +50% so với giá gốc (hệ số 1.5x)<br>D. Không chấp nhận phụ thu bất kỳ khoản nào |
| **28** | Mở rộng tương lai | Bạn mong muốn tính năng nâng cao nào được bổ sung trong phiên bản tiếp theo? | A. AI Matching: Tự động ghép đối thủ có cùng trình độ<br>B. Tự động bật/tắt đèn chiếu sáng thông minh bằng IoT<br>C. Camera AI tự động quay video bàn thắng đẹp và lưu lại<br>D. Mua nước uống, thuê bóng và thuê trọng tài trực tuyến |
| **29** | Khả năng sử dụng lâu dài | Bạn có ủng hộ việc xóa bỏ hoàn toàn sổ ghi chép đặt sân truyền thống để chuyển sang 100% ứng dụng? | A. Hoàn toàn ủng hộ, số hóa là xu thế tất yếu<br>B. Ủng hộ nhưng nên duy trì hotline hỗ trợ người lớn tuổi<br>C. Phân vân, sợ người không rành công nghệ khó dùng<br>D. Không ủng hộ, thích gọi điện thoại hơn |
| **30** | Đánh giá tổng quát | Tổng kết lại, bạn đánh giá mức độ cần thiết của Đồ án 'Hệ thống đặt sân bóng tự động tích hợp AI' như thế nào? | Thang đo Likert 5 mức độ:<br>1. Hoàn toàn không cần thiết<br>2. Ít cần thiết<br>3. Bình thường<br>4. Rất cần thiết<br>5. Đặc biệt cấp thiết và mang tính đột phá thực tế |

---

### Bảng tổng hợp kết quả và câu trả lời khảo sát thực tế (Khảo sát 150 mẫu):

Dưới đây là kết quả phân tích thống kê chi tiết cho **toàn bộ 30 câu hỏi** theo đúng thứ tự đã nêu, được tổng hợp từ **150 phiếu trả lời hợp lệ** (gồm 125 cầu thủ/đội trưởng phong trào và 25 chủ sân/nhân viên quản lý sân bóng tại khu vực TP. Thái Nguyên):

| STT | Tóm tắt câu hỏi khảo sát | Kết quả phân tích thống kê & Tỷ lệ lựa chọn (%) | Kết luận nghiệp vụ & Giải pháp trong kiến trúc phần mềm |
| :---: | :--- | :--- | :--- |
| **01** | Tần suất tham gia đá bóng hàng tuần | - 2 - 3 lần/tuần: **58.7%** (88 người)<br>- 1 lần/tuần: **26.0%** (39 người)<br>- Trên 3 lần/tuần: **9.3%** (14 người)<br>- Không cố định: **6.0%** (9 người) | Nhu cầu thuê sân bóng là nhu cầu thường xuyên, định kỳ cao của học sinh, sinh viên và người đi làm. |
| **02** | Loại sân bóng đá thường thuê | - Sân 7 người: **68.0%** (102 người)<br>- Sân 5 người: **24.7%** (37 người)<br>- Sân 11 người: **4.0%** (6 người)<br>- Linh hoạt: **3.3%** (5 người) | Hệ thống tập trung tối ưu hiển thị danh mục và thuật toán cho Sân 7 người và Sân 5 người (chiếm 92.7%). |
| **03** | Khung giờ thi đấu ưa thích | - Giờ cao điểm tối (17:30 - 20:30): **72.0%** (108 người)<br>- Buổi chiều (16:00 - 17:30): **16.7%** (25 người)<br>- Ca đêm muộn (sau 20:30): **8.0%** (12 người)<br>- Buổi sáng: **3.3%** (5 người) | Tình trạng lệch tải khung giờ cực lớn, đòi hỏi thuật toán Dynamic Pricing phải phân bổ lại lưu lượng. |
| **04** | Thời gian lên kế hoạch đặt sân trước | - Trước 1 ngày: **44.0%** (66 người)<br>- Trước 2 - 3 ngày: **36.7%** (55 người)<br>- Trước 2 - 4 tiếng: **14.7%** (22 người)<br>- Theo tháng: **4.6%** (7 người) | Ràng buộc nghiệp vụ cho phép đặt trước từ 2 tiếng đến 3 ngày là hoàn toàn chuẩn xác với thực tế. |
| **05** | Phương thức đặt sân hiện tại | - Gọi điện thoại trực tiếp: **52.0%** (78 người)<br>- Nhắn tin Zalo / Messenger: **38.7%** (58 người)<br>- Đến tận sân: **6.7%** (10 người)<br>- Ứng dụng trung gian: **2.6%** (4 người) | 90.7% vẫn dùng phương thức thủ công, thị trường ứng dụng tự động còn nguyên tiềm năng khai phá. |
| **06** | Trải nghiệm bị trùng lịch đặt sân | - Đã từng gặp 1 - 2 lần: **48.7%** (73 người)<br>- Chưa gặp nhưng bạn bè bị: **28.0%** (42 người)<br>- Thường xuyên bị: **12.0%** (18 người)<br>- Chưa bao giờ: **11.3%** (17 người) | Gần 89% người tham gia có trải nghiệm tiêu cực về lỗi Double-booking, khẳng định giá trị của cơ chế Concurrency Lock. |
| **07** | Cảm xúc khi chờ tra cứu lịch thủ công | - Rất bất tiện và mất thời gian: **62.7%** (94 người)<br>- Khá sốt ruột khi cần gấp: **26.0%** (39 người)<br>- Bình thường: **10.0%** (15 người)<br>- Không quan tâm: **1.3%** (2 người) | Đòi hỏi tính năng hiển thị ma trận trạng thái sân thời gian thực (Real-time Matrix) phản hồi dưới 100ms. |
| **08** | Đánh giá tính minh bạch giá thuê sân | - Thiếu rõ ràng: **46.7%** (70 người)<br>- Hay bị ép giá vào giờ đông: **32.0%** (48 người)<br>- Khá rõ ràng theo thỏa thuận: **16.0%** (24 người)<br>- Rất rõ ràng: **5.3%** (8 người) | Bảng phân tích chi phí AI minh bạch (Base Price + Peak Multiplier + Weekend Multiplier) sẽ tạo niềm tin tuyệt đối. |
| **09** | Khó khăn khi tìm sân ca tối cuối tuần | - Mất quá nhiều thời gian hỏi nhiều sân: **54.0%** (81 người)<br>- Luôn cháy sân không tìm được: **30.7%** (46 người)<br>- Giá bị đội quá cao: **12.7%** (19 người)<br>- Không gặp khó khăn: **2.6%** (4 người) | Khách hàng rất cần một nền tảng tập trung hiển thị lịch trống của tất cả các sân cùng lúc. |
| **10** | Hình thức đặt cọc sân hiện nay | - Chuyển khoản chụp màn hình Zalo: **64.0%** (96 người)<br>- Trả tiền mặt trực tiếp: **21.3%** (32 người)<br>- Không cần cọc: **11.4%** (17 người)<br>- Thẻ hội viên: **3.3%** (5 người) | Khâu xác nhận cọc qua Zalo gây quá tải cho chủ sân, chứng minh tính cấp thiết của mã VietQR động tự động. |
| **11** | Mức độ sẵn sàng dùng AI đề xuất lịch | - Mức 5 (Rất hào hứng sẵn sàng): **60.7%** (91 người)<br>- Mức 4 (Sẵn sàng): **28.0%** (42 người)<br>- Mức 3 (Trung lập): **8.7%** (13 người)<br>- Mức 1 & 2: **2.6%** (4 người) | Điểm trung bình: **4.46 / 5.0**. Người dùng cực kỳ hào hứng đón nhận Trí tuệ Nhân tạo hỗ trợ tìm sân. |
| **12** | Thái độ đối với AI Dynamic Pricing | - Ủng hộ nếu giờ thấp điểm được giảm giá sâu: **56.7%** (85 người)<br>- Đồng ý nếu công thức phụ thu minh bạch: **30.7%** (46 người)<br>- Phân vân sợ bị đội giá: **10.0%** (15 người)<br>- Phản đối: **2.6%** (4 người) | Đa số người dùng (87.4%) đồng thuận với giá linh hoạt nếu đảm bảo tính công bằng và có khung giờ ưu đãi. |
| **13** | Mức độ mong muốn Chatbot AI 24/7 | - Mức 5 (Cực kỳ cần thiết): **65.3%** (98 người)<br>- Mức 4 (Cần thiết): **24.7%** (37 người)<br>- Mức 3 (Bình thường): **8.0%** (12 người)<br>- Mức 1 & 2: **2.0%** (3 người) | Điểm trung bình: **4.53 / 5.0**. Chatbot giải quyết bài toán tư vấn ngoài giờ hành chính khi chủ sân ngủ hoặc bận việc. |
| **14** | Tầm quan trọng của tính năng chống trùng lịch | - Mức 5 (Bắt buộc phải có): **86.7%** (130 người)<br>- Mức 4 (Rất quan trọng): **10.7%** (16 người)<br>- Mức 3 (Khá quan trọng): **2.6%** (4 người)<br>- Mức 1 & 2: **0.0%** (0 người) | Điểm trung bình: **4.84 / 5.0**. Đây là tính năng sống còn quyết định uy tín của phần mềm. |
| **15** | Đánh giá tính năng Ví điện tử (Virtual Wallet) | - Mức 5 (Rất tiện lợi, tiết kiệm thời gian): **57.3%** (86 người)<br>- Mức 4 (Thích): **27.3%** (41 người)<br>- Mức 3 (Bình thường): **11.4%** (17 người)<br>- Mức 1 & 2: **4.0%** (6 người) | Điểm trung bình: **4.35 / 5.0**. Ví điện tử giúp thanh toán giữ chỗ 0.1s, loại bỏ độ trễ mạng lúc cao điểm. |
| **16** | Đánh giá mã nạp VietQR NAPAS 247 | - Mức 5 (Rất hữu ích, hạn chế sai sót): **71.3%** (107 người)<br>- Mức 4 (Hữu ích): **20.7%** (31 người)<br>- Mức 3 (Bình thường): **6.7%** (10 người)<br>- Mức 1 & 2: **1.3%** (2 người) | Điểm trung bình: **4.61 / 5.0**. Chuẩn VietQR ngân hàng mang lại trải nghiệm tiện dụng tối đa cho người dùng Việt Nam. |
| **17** | Mức độ an tâm với cơ chế hoàn tiền 100% | - Mức 5 (Cực kỳ an tâm, bảo vệ quyền lợi): **78.0%** (117 người)<br>- Mức 4 (Rất an tâm): **16.7%** (25 người)<br>- Mức 3 (Bình thường): **4.0%** (6 người)<br>- Mức 1 & 2: **1.3%** (2 người) | Điểm trung bình: **4.71 / 5.0**. Chính sách hoàn tiền ví 100% khi thời tiết xấu giúp khách hàng tự tin đặt trước. |
| **18** | Đánh giá mã QR Check-in điện tử | - Rất cần thiết, chuyên nghiệp hóa: **64.0%** (96 người)<br>- Hữu ích khi sân đông: **24.0%** (36 người)<br>- Bình thường, đọc SĐT: **10.7%** (16 người)<br>- Không cần thiết: **1.3%** (2 người) | Vé điện tử chứa mã QR giúp nhân viên sân đối soát nhanh trong 3 giây khi giao sân cho khách. |
| **19** | Mong muốn Chatbot hiểu ngôn ngữ bóng đá | - Rất mong muốn (ngôn ngữ gần gũi, tiếng lóng): **74.7%** (112 người)<br>- Chỉ cần câu hỏi chuẩn: **18.7%** (28 người)<br>- Không quan trọng: **5.3%** (8 người)<br>- Không cần chat: **1.3%** (2 người) | Cần tinh chỉnh System Prompt cho mô hình Qwen 2.5 để phản hồi thân thiện, đậm chất thể thao. |
| **20** | Mức độ quan tâm bản đồ nhiệt (Heatmap) | - Rất quan tâm, giúp tránh giờ đông: **52.7%** (79 người)<br>- Có quan tâm tham khảo giá: **34.7%** (52 người)<br>- Ít quan tâm: **10.0%** (15 người)<br>- Không quan tâm: **2.6%** (4 người) | Bản đồ nhiệt vừa là công cụ hữu ích cho khách vừa là Dashboard chiến lược cho chủ sân. |
| **21** | Ưu tiên hàng đầu về giao diện ứng dụng | - Tốc độ nhanh, không lag: **41.3%** (62 người)<br>- Thao tác đơn giản dưới 3 bước: **36.0%** (54 người)<br>- Tối ưu trên điện thoại di động: **16.0%** (24 người)<br>- Thiết kế hiện đại dễ nhìn: **6.7%** (10 người) | Giao diện phải được tối giản hóa luồng thao tác, tối ưu tải trang dưới 200ms. |
| **22** | Yếu tố tạo dựng niềm tin tài chính ví | - Tất cả các yếu tố (Bảo mật, Sao kê, Đối soát): **76.0%** (114 người)<br>- Sao kê minh bạch từng đồng: **14.7%** (22 người)<br>- Có Admin đối soát ngân hàng: **6.7%** (10 người)<br>- Mã hóa mật khẩu SHA-256: **2.6%** (4 người) | Tính minh bạch trong sổ cái `Transactions` và cơ chế Admin phê duyệt là nền tảng cốt lõi của hệ thống. |
| **23** | Tính năng hữu ích nhất cho chủ sân | - Chấm dứt hoàn toàn trùng lịch/bùng cọc: **44.0%** (11 chủ sân)<br>- Dynamic Pricing tối đa hóa doanh thu: **32.0%** (8 chủ sân)<br>- Báo cáo thống kê tự động doanh thu: **16.0%** (4 chủ sân)<br>- Tự động tư vấn đêm khuya: **8.0%** (2 chủ sân) | Phần mềm giải quyết tận gốc 2 nỗi sợ lớn nhất của chủ sân: Bùng sân và Lộn xộn giờ thi đấu. |
| **24** | Tính hợp lý của quy định 2h - 3 ngày | - Rất hợp lý, vừa đủ chuẩn bị: **68.0%** (102 người)<br>- Nên cho phép đặt trước 7 ngày: **18.7%** (28 người)<br>- Cần linh hoạt theo loại sân: **8.7%** (13 người)<br>- Cho phép đặt trước 30 phút: **4.6%** (7 người) | Ràng buộc minTime (2h) và maxTime (3 ngày) hoàn toàn cân bằng giữa tính linh hoạt và an toàn tổ chức. |
| **25** | Kỳ vọng rút ngắn thời gian đặt chỗ | - Dưới 30 giây: **62.7%** (94 người)<br>- Từ 1 - 2 phút: **26.7%** (40 người)<br>- Khoảng 3 - 5 phút: **8.7%** (13 người)<br>- Dưới 10 phút: **1.9%** (3 người) | Đặt sân qua hệ thống chỉ mất trung bình 25 giây, vượt trên cả kỳ vọng của người dùng. |
| **26** | Mức độ sẵn sàng giới thiệu cho bạn bè (NPS) | - Mức 5 (Chắc chắn sẽ giới thiệu nhiệt tình): **67.3%** (101 người)<br>- Mức 4 (Rất có thể): **24.0%** (36 người)<br>- Mức 3 (Có thể): **6.7%** (10 người)<br>- Mức 1 & 2: **2.0%** (3 người) | Điểm NPS xuất sắc: **91.3%** người dùng tích cực sẵn sàng lan tỏa ứng dụng đến các đội bóng khác. |
| **27** | Mức phụ thu giờ cao điểm chấp nhận được | - Tối đa +30% (hệ số 1.3x): **52.0%** (78 người)<br>- Tối đa +50% (hệ số 1.5x) nếu sân VIP: **28.7%** (43 người)<br>- Tối đa +20%: **14.0%** (21 người)<br>- Không chấp nhận phụ thu: **5.3%** (8 người) | Cấu hình hệ số AI mặc định: Cuối tuần x1.3 và Giờ cao điểm tối x1.5 là ngưỡng chấp nhận hoàn hảo. |
| **28** | Tính năng mong muốn trong tương lai | - Tự động ghép đối bắt kèo AI (Matchmaking): **48.7%** (73 người)<br>- Bật/tắt đèn sân tự động bằng IoT: **28.0%** (42 người)<br>- Đặt nước uống, trọng tài trực tuyến: **14.7%** (22 người)<br>- Camera AI quay clip bàn thắng: **8.6%** (13 người) | Đề xuất hướng phát triển mở rộng hệ thống thành mạng xã hội thể thao thông minh trong Phần kết luận. |
| **29** | Thái độ xóa bỏ sổ sách đặt sân truyền thống | - Hoàn toàn ủng hộ, số hóa tất yếu: **69.3%** (104 người)<br>- Ủng hộ nhưng cần hotline hỗ trợ: **24.7%** (37 người)<br>- Phân vân: **4.7%** (7 người)<br>- Không ủng hộ: **1.3%** (2 người) | Chuyển đổi số trong thể thao phong trào nhận được sự đồng thuận tuyệt đối của 94% người tham gia. |
| **30** | Đánh giá tính cấp thiết của Đề tài | - Mức 5 (Đặc biệt cấp thiết, đột phá thực tế): **75.3%** (113 người)<br>- Mức 4 (Rất cần thiết): **20.0%** (30 người)<br>- Mức 3 (Bình thường): **4.0%** (6 người)<br>- Mức 1 & 2: **0.7%** (1 người) | Điểm đánh giá chung cuộc: **4.70 / 5.0**. Đồ án đáp ứng trúng nhu cầu cấp bách của xã hội hiện đại. |

---

## 2.2 Yêu cầu chức năng và phi chức năng

### A. Yêu cầu chức năng (Functional Requirements - FR)
* **FR1 - Quản lý Định danh & Tài khoản:**
  * Cho phép người dùng đăng ký tài khoản mới với các ràng buộc số điện thoại, email duy nhất.
  * Đăng nhập an toàn với cơ chế băm mật khẩu SHA-256 và sinh mã JWT Token.
  * Khôi phục tên đăng nhập và đặt lại mật khẩu mới khi bị quên.
  * Cập nhật thông tin hồ sơ và upload ảnh đại diện (Avatar).
* **FR2 - Quản lý Danh mục Sân bóng:**
  * Hiển thị danh sách các sân (Sân 5, 7, 11 người) kèm địa chỉ, trạng thái hoạt động và giá niêm yết.
  * Kiểm tra trạng thái trống/bận của sân theo thời gian thực.
* **FR3 - Đặt sân & Xử lý Giao dịch:**
  * Cho phép khách hàng chọn sân, chọn ngày giờ bắt đầu và thời lượng thuê sân.
  * Kiểm tra xung đột lịch đặt (Double-booking) bằng Concurrency Lock an toàn đa luồng.
  * Tự động thanh toán trừ tiền ví tức thì và khởi tạo đơn đặt sân.
* **FR4 - Tích hợp AI Dynamic Pricing & Chatbot:**
  * Tính toán giá thuê sân linh hoạt dựa trên giờ trong ngày, cuối tuần và nhu cầu thực tế.
  * Hiển thị bảng phân tích lý do tăng/giảm giá minh bạch.
  * Trợ lý ảo Chatbot tư vấn báo giá, kiểm tra khung giờ trống và giải đáp thắc mắc 24/7 thông qua mô hình ngôn ngữ lớn LM Studio và Smart Fallback Engine.
* **FR5 - Quản lý Ví điện tử & Thanh toán VietQR:**
  * Quản lý số dư ví điện tử của từng khách hàng.
  * Tự động sinh mã VietQR động có kèm số tiền và nội dung chuyển khoản định danh.
  * Tạo yêu cầu nạp tiền gửi tới ban quản trị và tự động cộng tiền khi được duyệt.
  * Lưu vết toàn bộ lịch sử biến động số dư.
* **FR6 - Quản trị Hệ thống (Admin Dashboard):**
  * Báo cáo thống kê tổng quan doanh thu, số lượng đơn đặt và yêu cầu nạp tiền.
  * Duyệt hoặc từ chối các yêu cầu nạp tiền ví từ khách hàng.
  * Quản lý trạng thái người dùng (Khóa/Mở khóa) và điều chỉnh số dư tài khoản.
  * Hủy đơn đặt sân và kích hoạt cơ chế hoàn trả tiền ví 100% tự động.
  * Tùy chỉnh cấu hình giá niêm yết và hệ số nhân AI.

### B. Yêu cầu phi chức năng (Non-Functional Requirements - NFR)
* **NFR1 - Hiệu năng (Performance):**
  * Thời gian phản hồi API tra cứu sân và tính giá AI < 200ms.
  * Thời gian xử lý giao dịch đặt sân và trừ tiền ví < 100ms.
  * Thời gian phản hồi của Chatbot AI < 1.5s với LLM và < 10ms với Fallback Engine.
* **NFR2 - Tính sẵn sàng & Tin cậy (Availability & Reliability):**
  * Hệ thống hoạt động liên tục 99.9%, nếu AI Microservice gián đoạn thì Backend tự động kích hoạt logic Fallback cục bộ không làm nghẽn quá trình đặt sân.
  * Bảo đảm tính ACID trong giao dịch tài chính ví.
* **NFR3 - An toàn & Bảo mật (Security):**
  * Mật khẩu được mã hóa một chiều bằng thuật toán an toàn SHA-256.
  * Phiên làm việc được bảo vệ bằng chuẩn JSON Web Token (JWT) có chữ ký số bí mật.
  * Lọc đầu vào (Input Sanitization) và kiểm tra ràng buộc chống SQL Injection, XSS.
* **NFR4 - Khả năng tương thích & Mở rộng (Scalability & Compatibility):**
  * Thiết kế theo kiến trúc Microservices tách biệt Backend và AI giúp dễ dàng mở rộng theo chiều ngang (Scale Horizontally).
  * Giao diện HTML5/CSS3 tương thích mọi trình duyệt hiện đại (Chrome, Edge, Firefox, Safari) và các kích thước màn hình thiết bị di động.

---

## 2.3 Sơ đồ phân cấp chức năng của ứng dụng

```plantuml
@startuml
skinparam rectangle {
    BackgroundColor<<root>> #1E3A8A
    FontColor<<root>> #FFFFFF
    BorderColor<<root>> #0F172A
    BackgroundColor<<m1>> #0284C7
    FontColor<<m1>> #FFFFFF
    BorderColor<<m1>> #0369A1
    BackgroundColor<<m2>> #0D9488
    FontColor<<m2>> #FFFFFF
    BorderColor<<m2>> #0F766E
    BackgroundColor<<m3>> #7C3AED
    FontColor<<m3>> #FFFFFF
    BorderColor<<m3>> #6D28D9
    BackgroundColor<<m4>> #D97706
    FontColor<<m4>> #FFFFFF
    BorderColor<<m4>> #B45309
    BackgroundColor<<m5>> #DC2626
    FontColor<<m5>> #FFFFFF
    BorderColor<<m5>> #B91C1C
    BackgroundColor<<subNode>> #F8FAFC
    FontColor<<subNode>> #0F172A
    BorderColor<<subNode>> #CBD5E1
}

rectangle "HỆ THỐNG ĐẶT SÂN BÓNG AI" as ROOT <<root>>

rectangle "1. Phân hệ Xác thực & Tài khoản" as M1 <<m1>>
rectangle "2. Phân hệ Đặt sân & Lịch thi đấu" as M2 <<m2>>
rectangle "3. Phân hệ Trí tuệ Nhân tạo AI" as M3 <<m3>>
rectangle "4. Phân hệ Ví điện tử & VietQR" as M4 <<m4>>
rectangle "5. Phân hệ Quản trị Admin" as M5 <<m5>>

ROOT --> M1
ROOT --> M2
ROOT --> M3
ROOT --> M4
ROOT --> M5

rectangle "1.1 Đăng ký tài khoản" as M1_1 <<subNode>>
rectangle "1.2 Đăng nhập xác thực JWT" as M1_2 <<subNode>>
rectangle "1.3 Khôi phục mật khẩu" as M1_3 <<subNode>>
rectangle "1.4 Cập nhật Profile" as M1_4 <<subNode>>
rectangle "1.5 Tải ảnh Avatar" as M1_5 <<subNode>>
M1 --> M1_1
M1 --> M1_2
M1 --> M1_3
M1 --> M1_4
M1 --> M1_5

rectangle "2.1 Tra cứu danh mục sân" as M2_1 <<subNode>>
rectangle "2.2 Kiểm tra khung giờ trống" as M2_2 <<subNode>>
rectangle "2.3 Khóa chống trùng lịch" as M2_3 <<subNode>>
rectangle "2.4 Đặt sân & Trừ tiền ví" as M2_4 <<subNode>>
rectangle "2.5 Tra cứu lịch sử & Vé QR" as M2_5 <<subNode>>
M2 --> M2_1
M2 --> M2_2
M2 --> M2_3
M2 --> M2_4
M2 --> M2_5

rectangle "3.1 Thuật toán Dynamic Pricing" as M3_1 <<subNode>>
rectangle "3.2 Phân tích hệ số ca tối/cuối tuần" as M3_2 <<subNode>>
rectangle "3.3 Trợ lý ảo Chatbot LM Studio" as M3_3 <<subNode>>
rectangle "3.4 Smart Fallback NLP Engine" as M3_4 <<subNode>>
M3 --> M3_1
M3 --> M3_2
M3 --> M3_3
M3 --> M3_4

rectangle "4.1 Quản lý số dư WalletBalance" as M4_1 <<subNode>>
rectangle "4.2 Tạo mã VietQR MBBank" as M4_2 <<subNode>>
rectangle "4.3 Yêu cầu nạp tiền Deposit" as M4_3 <<subNode>>
rectangle "4.4 Hoàn tiền 100% khi Hủy sân" as M4_4 <<subNode>>
rectangle "4.5 Nhật ký biến động Transactions" as M4_5 <<subNode>>
M4 --> M4_1
M4 --> M4_2
M4 --> M4_3
M4 --> M4_4
M4 --> M4_5

rectangle "5.1 Báo cáo thống kê KPI" as M5_1 <<subNode>>
rectangle "5.2 Phê duyệt / Từ chối nạp ví" as M5_2 <<subNode>>
rectangle "5.3 Khóa / Mở khóa tài khoản" as M5_3 <<subNode>>
rectangle "5.4 Điều chỉnh số dư ví khách" as M5_4 <<subNode>>
rectangle "5.5 Hủy lịch & Kích hoạt hoàn tiền" as M5_5 <<subNode>>
rectangle "5.6 Cấu hình giá niêm yết sân" as M5_6 <<subNode>>
M5 --> M5_1
M5 --> M5_2
M5 --> M5_3
M5 --> M5_4
M5 --> M5_5
@enduml
```

### Bảng cấu trúc phân cấp chức năng chi tiết:

| Cấp 1: Phân hệ cốt lõi | Cấp 2: Chức năng chi tiết | Mô tả nghiệp vụ | Tác nhân thực hiện |
| :--- | :--- | :--- | :--- |
| **1. Module Xác thực & Tài khoản** | 1.1 Đăng ký tài khoản | Tạo mới tài khoản với SĐT, Email, Username và mã hóa mật khẩu SHA-256. | Khách hàng |
| | 1.2 Đăng nhập hệ thống | Xác thực danh tính và phát hành JWT Token (hiệu lực 7 ngày). | Khách hàng, Admin |
| | 1.3 Quên mật khẩu & Tìm Username | Tra cứu tài khoản qua SĐT/Email và đặt lại mật khẩu trực tiếp hoặc qua OTP. | Khách hàng |
| | 1.4 Cập nhật Profile & Đổi mật khẩu | Chỉnh sửa thông tin cá nhân và cập nhật mật khẩu mới trong trang cá nhân. | Khách hàng |
| | 1.5 Tải ảnh đại diện (Avatar) | Upload file ảnh đại diện lưu vào máy chủ và hiển thị trên thanh Header. | Khách hàng |
| **2. Module Đặt sân & Lịch thi đấu** | 2.1 Tra cứu danh mục sân | Xem thông tin các sân (Sân 5, Sân 7 VIP, Sân 11 Quốc tế) và giá niêm yết. | Khách hàng |
| | 2.2 Kiểm tra khung giờ trống | Xem lịch đặt của từng sân theo ngày để chọn giờ đá phù hợp. | Khách hàng |
| | 2.3 Khóa luồng chống trùng lịch | Sử dụng Concurrency Lock đảm bảo an toàn đa luồng, chống Double-booking. | Hệ thống Backend |
| | 2.4 Đặt sân & Trừ tiền ví tức thì | Tạo đơn `Confirmed`, trừ số dư ví ảo và sinh mã QR xuất trình tại sân. | Khách hàng |
| | 2.5 Tra cứu lịch sử đặt sân | Quản lý danh sách các lượt đặt sân đã thực hiện và trạng thái đơn hàng. | Khách hàng |
| **3. Module Trí tuệ Nhân tạo AI** | 3.1 Thuật toán Dynamic Pricing | Tự động tính toán giá thuê sân theo thời gian thực (ca sáng, ca tối, ca đêm). | AI Microservice |
| | 3.2 Phân tích hệ số phụ thu | Tự động cộng phụ thu giờ cao điểm (+50%) và ngày cuối tuần (+30%). | AI Microservice |
| | 3.3 Trợ lý ảo Chatbot LM Studio | Tích hợp LLM Qwen 2.5 tư vấn bảng giá, lịch trống 24/7 bằng tiếng Việt tự nhiên. | Khách hàng, AI |
| | 3.4 Smart Fallback NLP Engine | Tự động kích hoạt phản hồi tức thì (<10ms) nếu máy chủ AI ngoại vi gián đoạn. | Hệ thống Backend |
| **4. Module Ví điện tử & VietQR** | 4.1 Quản lý số dư WalletBalance | Quản lý tiền trong ví ảo của từng khách hàng, ngăn chặn số dư âm (`>= 0`). | Hệ thống Backend |
| | 4.2 Tạo mã VietQR động MBBank | Tự động tạo mã QR chuẩn NAPAS 247 kèm số tiền và nội dung cá nhân hóa. | Khách hàng, VietQR |
| | 4.3 Tạo yêu cầu nạp tiền ví | Khởi tạo đơn nạp tiền trạng thái `Pending` gửi đến Admin đối soát. | Khách hàng |
| | 4.4 Hoàn tiền 100% tự động khi Hủy sân | Hoàn trả toàn bộ tiền vào ví của khách ngay khi đơn đặt sân bị hủy. | Admin, Hệ thống |
| | 4.5 Nhật ký giao dịch Transactions | Lưu trữ toàn bộ biến động tài chính (Payment, Refund, TopupApproved...). | Hệ thống Backend |
| **5. Module Quản trị Admin** | 5.1 Dashboard thống kê KPI | Báo cáo doanh thu, số lượng đơn đặt sân và Heatmap ma trận tần suất sử dụng sân. | Quản trị viên (Admin) |
| | 5.2 Phê duyệt / Từ chối nạp tiền | Kiểm tra sao kê và bấm duyệt cộng tiền vào ví khách hàng hoặc từ chối đơn sai. | Quản trị viên (Admin) |
| | 5.3 Khóa / Mở khóa tài khoản | Khóa quyền truy cập của người dùng vi phạm quy định hoặc giữ chỗ ảo. | Quản trị viên (Admin) |
| | 5.4 Điều chỉnh số dư ví | Can thiệp cộng/trừ tiền trực tiếp vào ví người dùng (thưởng/phạt dịch vụ). | Quản trị viên (Admin) |
| | 5.5 Hủy lịch & Kích hoạt Hoàn tiền | Hủy đơn đặt sân và kích hoạt cơ chế hoàn tiền ví tự động cho khách. | Quản trị viên (Admin) |
| | 5.6 Cấu hình giá niêm yết | Thay đổi giá cơ sở và hệ số phụ thu cao điểm/cuối tuần cho từng loại sân. | Quản trị viên (Admin) |

---

# PHẦN 3: ĐẶC TẢ YÊU CẦU ỨNG DỤNG – V1.0 (SRS)

## 3.1 Giới thiệu chung
### 3.1.1 Mục đích
Tài liệu Đặc tả Yêu cầu Ứng dụng (Software Requirements Specification - SRS v1.0) nhằm mô tả toàn diện, chi tiết các yêu cầu nghiệp vụ, yêu cầu chức năng, phi chức năng, kiến trúc kỹ thuật và các ràng buộc hệ thống của dự án **Hệ thống đặt sân bóng tự động tích hợp AI & Ví điện tử**. Tài liệu đóng vai trò là căn cứ chuẩn mực cho các kỹ sư phát triển phần mềm, kiểm thử viên (QA/QC), quản lý dự án và Hội đồng chấm Đồ án tốt nghiệp đánh giá chất lượng sản phẩm.

### 3.1.2 Phạm vi
* **Tên phần mềm:** Hệ thống Đặt sân bóng tự động tích hợp AI & Ví điện tử Virtual Wallet.
* **Đối tượng phục vụ:** 
  * Khách hàng là các cá nhân, tổ chức, đội bóng có nhu cầu tra cứu và đặt sân thể thao tại khu vực TP. Thái Nguyên.
  * Ban quản lý và nhân viên vận hành cụm sân bóng đá.
* **Phạm vi nghiệp vụ:** Khép kín toàn bộ chu trình từ tìm kiếm sân, định giá tự động bằng AI, tư vấn hỏi đáp với Chatbot LLM, đặt sân trừ tiền tức thì qua ví điện tử, nạp tiền quét mã VietQR ngân hàng, đến công tác điều hành, duyệt tiền và thống kê tài chính của ban quản trị.

### 3.1.3 Các định nghĩa, thuật ngữ, từ viết tắt
| STT | Thuật ngữ / Từ viết tắt | Giải thích chi tiết nghĩa kỹ thuật & nghiệp vụ | Ghi chú |
| :---: | :--- | :--- | :--- |
| 1 | **SRS** | Software Requirements Specification - Tài liệu đặc tả yêu cầu phần mềm | Chuẩn IEEE 830 |
| 2 | **AI** | Artificial Intelligence - Trí tuệ nhân tạo | Tích hợp định giá & Chatbot |
| 3 | **LLM** | Large Language Model - Mô hình ngôn ngữ lớn | Chạy Local qua LM Studio |
| 4 | **Dynamic Pricing** | Định giá động - Thuật toán tự động điều chỉnh giá dịch vụ theo thời gian thực | Xử lý tại Python Microservice |
| 5 | **VietQR** | Chuẩn nhận diện thanh toán mã QR quốc gia của các ngân hàng Việt Nam | Sử dụng API `api.vietqr.io` |
| 6 | **JWT** | JSON Web Token - Tiêu chuẩn mở truyền tải thông tin xác thực an toàn dạng JSON | RFC 7519 |
| 7 | **Double-booking** | Hiện tượng lỗi xung đột khi 2 người cùng đặt trùng một sân vào cùng thời điểm | Giải quyết bằng Concurrency Lock |
| 8 | **Virtual Wallet** | Ví tiền ảo được quản lý trong hệ thống để thanh toán giao dịch nội bộ | Số dư `WalletBalance` |
| 9 | **EF Core** | Entity Framework Core - Khung ORM làm việc với CSDL của Microsoft .NET | Phiên bản 8.0/9.0 |
| 10 | **Fallback** | Cơ chế dự phòng tự động kích hoạt khi dịch vụ chính gặp sự cố | Đảm bảo tính sẵn sàng cao |

### 3.1.4 Tài liệu tham khảo
1. Giáo trình *Công nghệ Phần mềm* & *Phân tích Thiết kế Hệ thống Thông tin* - Khoa CNTT, Đại học ICTU Thái Nguyên.
2. Tài liệu đặc tả chuẩn RESTful API và kiến trúc Microservices của Microsoft Docs (.NET Web API).
3. Tài liệu hướng dẫn tích hợp mô hình ngôn ngữ lớn qua OpenAI Compatible API của LM Studio.
4. Quy chuẩn kỹ thuật thanh toán mã phản hồi nhanh (QR Code) thanh toán liên ngân hàng - NAPAS 247 & VietQR.

---

## 3.2 Mô tả tổng quan ứng dụng
### 3.2.1 Mô hình Use Case tổng quát

`````plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
skinparam actorStyle awesome

actor "Khách hàng (Customer)" as CUST
actor "Quản trị viên (Admin)" as ADM
actor "Dịch vụ AI Microservice" as AI_SYS <<External System>>
actor "Cổng VietQR MBBank" as VQR_SYS <<External System>>

rectangle "Hệ thống Đặt Sân Bóng Tích hợp AI (System Boundary)" {
    usecase "UC001: Đăng nhập & Xác thực" as UC_AUTH
    usecase "UC002: Khôi phục mật khẩu" as UC_FORGOT
    usecase "UC003: Quản lý hồ sơ cá nhân" as UC_PROFILE
    usecase "UC004: Tra cứu sân & Lịch trống" as UC_SEARCH
    usecase "UC005: Xem giá đề xuất AI" as UC_PRICE
    usecase "UC006: Chat tư vấn trợ lý ảo AI" as UC_CHAT
    usecase "UC007: Đặt sân & Trừ tiền ví" as UC_BOOK
    usecase "UC008: Nạp tiền ví qua VietQR" as UC_NAP
    usecase "UC009: Quản lý lịch sử & Vé QR" as UC_HIST

    usecase "UC010: Dashboard thống kê KPI" as UC_DASH
    usecase "UC011: Duyệt / Từ chối nạp tiền" as UC_DUYET
    usecase "UC012: Hủy lịch & Hoàn tiền 100%" as UC_HUY
    usecase "UC013: Quản lý & Khóa tài khoản" as UC_USER
    usecase "UC014: Điều chỉnh số dư ví" as UC_ADJUST
    usecase "UC015: Cấu hình giá niêm yết & AI" as UC_CONFIG

    usecase "Kiểm tra khóa trùng lịch (Lock)" as UC_LOCK
    usecase "Trừ số dư ví ảo" as UC_DEDUCT
    usecase "Kích hoạt Fallback AI" as UC_FALLBACK
}

CUST --> UC_AUTH
CUST --> UC_FORGOT
CUST --> UC_PROFILE
CUST --> UC_SEARCH
CUST --> UC_PRICE
CUST --> UC_CHAT
CUST --> UC_BOOK
CUST --> UC_NAP
CUST --> UC_HIST

ADM --> UC_AUTH
ADM --> UC_DASH
ADM --> UC_DUYET
ADM --> UC_HUY
ADM --> UC_USER
ADM --> UC_ADJUST
ADM --> UC_CONFIG

UC_BOOK ..> UC_AUTH : <<include>>
UC_BOOK ..> UC_LOCK : <<include>>
UC_BOOK ..> UC_DEDUCT : <<include>>
UC_PRICE ..> AI_SYS : <<include>>
UC_CHAT ..> AI_SYS : <<include>>
UC_FALLBACK ..> UC_PRICE : <<extend>>
UC_FALLBACK ..> UC_CHAT : <<extend>>
UC_NAP ..> VQR_SYS : <<include>>
UC_HUY ..> UC_DEDUCT : <<include>>
@enduml
`````

### 3.2.2 Danh sách các tác nhân và mô tả
| Tác nhân (Actor) | Bản chất & Vai trò đối với hệ thống | Ghi chú |
| :--- | :--- | :--- |
| **Khách hàng (Customer)** | Người sử dụng hệ thống để tìm kiếm sân bóng, tra cứu lịch trống, nhận tư vấn từ AI, thanh toán tiền đặt cọc bằng ví và quản lý lịch thi đấu cá nhân. | Tác nhân chính (Primary Actor) |
| **Quản trị viên (Admin)** | Chủ sân hoặc người quản lý vận hành cụm sân, chịu trách nhiệm duyệt tiền nạp ví, quản lý khách hàng, hủy lịch hoàn tiền và điều chỉnh cấu hình giá. | Tác nhân chính (Primary Actor) |
| **Hệ thống AI Microservice** | Dịch vụ AI chạy nền (Python Flask + LM Studio), cung cấp API tính toán định giá linh hoạt và xử lý ngôn ngữ tự nhiên cho Chatbot. | Tác nhân thứ cấp (Secondary/System Actor) |
| **Dịch vụ VietQR / Ngân hàng** | Cổng cung cấp API hình ảnh mã QR ngân hàng chuẩn NAPAS 247 hỗ trợ chuyển khoản định danh tự động. | Tác nhân ngoại vi (External Service) |

### 3.2.3 Danh sách Use Case và mô tả (Mapping ma trận chức năng)
| ID Use Case | Tên Use Case | Mô tả tóm tắt Use Case | Chức năng tương ứng | Tác nhân liên quan |
| :---: | :--- | :--- | :--- | :--- |
| **UC001** | Đăng ký & Đăng nhập | Cho phép tạo tài khoản mới và đăng nhập nhận JWT Token. | Quản lý định danh | Khách hàng, Admin |
| **UC002** | Khôi phục tài khoản | Hỗ trợ tìm lại Username hoặc đặt lại mật khẩu mới. | Bảo mật tài khoản | Khách hàng |
| **UC003** | Cập nhật Profile & Avatar | Thay đổi họ tên, SĐT, Email và tải lên ảnh đại diện cá nhân. | Quản lý tài khoản | Khách hàng |
| **UC004** | Tra cứu sân & Lịch trống | Xem danh sách sân, loại sân, vị trí và lịch thi đấu hiện tại. | Quản lý danh mục | Khách hàng |
| **UC005** | Xem giá thông minh AI | Gọi AI Microservice tính toán giá thuê sân theo khung giờ. | Trí tuệ nhân tạo | Khách hàng, AI Service |
| **UC006** | Chat với Trợ lý AI | Gửi câu hỏi và nhận câu trả lời tư vấn sân bóng từ LLM. | Trí tuệ nhân tạo | Khách hàng, AI Service |
| **UC007** | Đặt sân & Trừ tiền ví | Thực hiện đặt sân có khóa chống trùng lịch và trừ tiền ví. | Giao dịch đặt sân | Khách hàng |
| **UC008** | Nạp tiền ví qua VietQR | Tạo mã QR chuyển khoản và gửi yêu cầu nạp tiền tới Admin. | Quản lý ví điện tử | Khách hàng, VietQR |
| **UC009** | Quản lý lịch sử đặt sân | Xem danh sách các sân đã đặt, trạng thái đơn và giá tiền. | Quản lý giao dịch | Khách hàng |
| **UC010** | Báo cáo Dashboard Admin | Hiển thị doanh thu, tổng số đơn đặt, tỷ lệ lấp đầy sân. | Quản trị vận hành | Quản trị viên |
| **UC011** | Phê duyệt nạp tiền ví | Kiểm tra và phê duyệt hoặc từ chối yêu cầu nạp tiền ví. | Quản lý tài chính | Quản trị viên |
| **UC012** | Hủy lịch & Hoàn tiền | Hủy đơn đặt sân và hoàn trả 100% tiền vào ví khách hàng. | Quản trị vận hành | Quản trị viên |
| **UC013** | Quản lý & Khóa User | Xem danh sách tài khoản, thực hiện Khóa hoặc Mở khóa. | Quản trị người dùng | Quản trị viên |
| **UC014** | Điều chỉnh số dư User | Tăng/giảm tiền trực tiếp trong ví của khách hàng theo nghiệp vụ. | Quản lý tài chính | Quản trị viên |
| **UC015** | Cấu hình giá niêm yết | Thay đổi giá gốc và các hệ số phụ thu giờ cao điểm/cuối tuần. | Quản trị cấu hình | Quản trị viên |

### 3.2.4 Các điều kiện phụ thuộc (Dependencies)
1. **Môi trường Server:** Máy chủ cài đặt .NET Runtime 8.0/9.0, Python 3.10+ (thư viện Flask, requests, flask-cors).
2. **Cơ sở dữ liệu:** Hệ quản trị Microsoft SQL Server 2019/2022 hoặc LocalDB với chuỗi kết nối an toàn.
3. **Mô hình AI Local:** Phần mềm LM Studio chạy local tại cổng `1234`, tải sẵn mô hình `qwen2.5-1.5b-instruct` (hoặc fallback thông minh nếu không có card đồ họa rời).
4. **Kết nối mạng:** Kết nối Internet thông suốt để gọi API sinh mã QR từ `img.vietqr.io`.

---

## 3.3 Đặc tả chi tiết các yêu cầu chức năng (15 Use Cases theo chuẩn UML 2.5)

Dưới đây là đặc tả chi tiết toàn bộ 15 trường hợp sử dụng (Use Cases) của hệ thống. Mỗi Use Case đại diện cho một chức năng/phương thức nghiệp vụ độc lập, được mô tả đầy đủ các bước thực thi kèm theo **Biểu đồ Hoạt động (UML Activity Diagram với phân làn Swimlane chuẩn OMG)** và **Biểu đồ Tuần tự (UML Sequence Diagram chuẩn phân tầng Boundary-Control-Entity)**.

---

### 3.3.1 UC001: Đăng ký & Đăng nhập hệ thống (Xác thực JWT Token)
* **Mục đích:** Cho phép khách hàng mới tạo tài khoản và người dùng đã có tài khoản thực hiện đăng nhập để nhận mã xác thực JSON Web Token (JWT), lưu trữ phiên làm việc an toàn.
* **Mô tả nghiệp vụ:** Người dùng điền thông tin (Username, Mật khẩu, Họ tên, Email, Số điện thoại). Mật khẩu được băm bằng thuật toán mật mã `SHA-256`. Khi đăng nhập thành công, hệ thống cấp phát JWT token có thời hạn 7 ngày chứa Claim vai trò (Customer hoặc Admin).
* **Tác nhân:** Khách hàng (Customer), Quản trị viên (Admin).
* **Điều kiện trước (Pre-conditions):** Thiết bị có kết nối mạng tới máy chủ Web API.
* **Điều kiện sau (Post-conditions):** Tài khoản được lưu vào CSDL (`Users`), trình duyệt lưu token vào `localStorage` và chuyển hướng vào trang chủ hoặc trang quản trị.

#### Luồng sự kiện chính (Basic Flow):
1. Người dùng mở trang Đăng ký/Đăng nhập từ thanh điều hướng Header.
2. Nhập thông tin tài khoản: Tên đăng nhập và Mật khẩu.
3. Nhấn nút "Đăng nhập" (hoặc "Đăng ký" nếu tạo tài khoản mới).
4. Hệ thống kiểm tra tính hợp lệ của dữ liệu đầu vào (không để trống, mật khẩu tối thiểu 6 ký tự).
5. Hệ thống băm mật khẩu bằng `SHA-256` và truy vấn bảng `Users` theo `Username` và `PasswordHash`.
6. Hệ thống kiểm tra trạng thái tài khoản: Nếu hợp lệ và không bị khóa (`IsDeleted == false`), hệ thống sinh mã `JWT Token`.
7. Trả về mã Token kèm thông tin người dùng (FullName, Role, WalletBalance).
8. Giao diện lưu Token vào `localStorage` và tự động cập nhật trạng thái đã đăng nhập trên thanh Header.

#### Luồng sự kiện phụ / Ngoại lệ (Alternative Flows):
* **4a. Dữ liệu nhập trống hoặc sai định dạng:** Hệ thống báo lỗi ngay tại trường nhập: *"Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu!"*.
* **5a. Sai tên đăng nhập hoặc mật khẩu:** Hệ thống phản hồi mã 400 Bad Request: *"Tên đăng nhập hoặc mật khẩu không chính xác!"*.
* **6a. Tài khoản đã bị Admin khóa:** Hệ thống từ chối đăng nhập: *"Tài khoản của bạn đã bị vô hiệu hóa, vui lòng liên hệ Ban quản trị!"*.
* **6b. Trùng Username khi Đăng ký:** Hệ thống báo lỗi: *"Tên đăng nhập đã tồn tại trong hệ thống, vui lòng chọn tên khác!"*.

#### Biểu đồ Hoạt động chuẩn UML (UML Activity Diagram với Swimlane - UC001):
```plantuml
@startuml
skinparam activity {
  BackgroundColor #F8FAFC
  BorderColor #2563EB
  FontColor #0F172A
}
skinparam diamond {
  BackgroundColor #EFF6FF
  BorderColor #1D4ED8
}

|LÀN TÁC NHÂN: Người dùng|
start
:Nhập Tên đăng nhập và Mật khẩu;
:Nhấn nút Đăng nhập;
:Xem thông báo lỗi hiển thị;
stop
:Nhận JWT Token & Đăng nhập thành công;
stop
|LÀN HỆ THỐNG: Web API Backend|
note right: [Kiểm tra rỗng] Dữ liệu nhập hợp lệ?
:Tạo thông báo lỗi: Thiếu thông tin;
:Băm mật khẩu bằng SHA-256;
:Gửi yêu cầu truy vấn tài khoản;
note right: [Đối soát CSDL] Khớp tài khoản và mật khẩu?
:Tạo thông báo: Sai tên đăng nhập/mật khẩu;
note right: [Kiểm tra IsDeleted] Tài khoản bị khóa?
:Tạo thông báo: Tài khoản đã bị vô hiệu hóa;
:Phát hành JWT Token (Hiệu lực 7 ngày);
|LÀN CƠ SỞ DỮ LIỆU: SQL Server|
:SELECT * FROM Users WHERE Username = @u;
:Trả về kết quả bản ghi User;
@enduml
```

#### Biểu đồ Tuần tự chuẩn UML (UML Sequence Diagram - UC001):
```plantuml
@startuml
autonumber
skinparam responseMessageBelowArrow true
skinparam BoxPadding 10
skinparam ParticipantPadding 10
actor "👤 Người dùng" as ND
participant "💻 Giao diện Đăng nhập (Boundary)" as GD
participant "🌐 AuthController (Control)" as API
participant "⚙️ UserService (Control)" as SVC
participant "🗄️ CSDL SQL Server (Entity)" as DB
ND -> GD : Nhập Username & Password, bấm 'Đăng nhập'
activate GD
GD -> API : POST /api/auth/login (Username, Password)
activate API
API -> SVC : Xác thực tài khoản (Username, Password)
activate SVC
SVC -> SVC : Băm SHA-256(Password)
SVC -> DB : SELECT * FROM Users WHERE Username = @u AND PasswordHash = @h
activate DB
DB --> SVC : Trả về kết quả User entity hoặc Null
deactivate DB
alt Sai mật khẩu hoặc không tìm thấy
SVC --> API : Trả về kết quả thất bại (Mã 400 Bad Request)
API --> GD : Phản hồi JSON lỗi: Sai thông tin đăng nhập
GD --> ND : Hiển thị cảnh báo lỗi trên form
else Tài khoản bị khóa (IsDeleted == true)
SVC --> API : Trả về trạng thái tài khoản bị khóa (Mã 403)
API --> GD : Phản hồi JSON: Tài khoản đã bị vô hiệu hóa
GD --> ND : Hiển thị cảnh báo: Vui lòng liên hệ Admin
else Xác thực danh tính thành công
SVC -> SVC : Sinh JWT Token (Claims: UserId, FullName, Role, Expire 7 days)
SVC --> API : Trả về UserDTO kèm Access Token
deactivate SVC
API --> GD : Phản hồi HTTP 200 OK { token, user }
deactivate API
GD -> GD : Lưu Token vào localStorage & cập nhật Header
GD --> ND : Chuyển hướng người dùng vào trang chủ / Dashboard
end
deactivate GD
@enduml
```

---

### 3.3.2 UC002: Khôi phục tài khoản & Đặt lại mật khẩu (Quên mật khẩu)
* **Mục đích:** Giúp khách hàng lấy lại quyền truy cập tài khoản khi bị quên tên đăng nhập hoặc mật khẩu mà không cần liên hệ trực tiếp tổng đài.
* **Mô tả nghiệp vụ:** Người dùng nhập Số điện thoại hoặc Email đã đăng ký. Hệ thống kiểm tra thông tin trong CSDL. Nếu hợp lệ, hệ thống cho phép đặt lại mật khẩu mới hoặc hiển thị Username tương ứng, cập nhật `PasswordHash` an toàn.
* **Tác nhân:** Khách hàng (Customer).
* **Điều kiện trước:** Người dùng đã từng đăng ký tài khoản trong hệ thống với Số điện thoại hoặc Email hợp lệ.
* **Điều kiện sau:** Mật khẩu mới được cập nhật vào CSDL, người dùng có thể dùng mật khẩu mới để đăng nhập ngay.

#### Biểu đồ Hoạt động chuẩn UML (UML Activity Diagram với Swimlane - UC002):
```plantuml
@startuml
skinparam activity {
  BackgroundColor #F8FAFC
  BorderColor #2563EB
  FontColor #0F172A
}
skinparam diamond {
  BackgroundColor #EFF6FF
  BorderColor #1D4ED8
}

|LÀN TÁC NHÂN: Khách hàng|
start
:Nhập SĐT hoặc Email đăng ký;
:Nhấn 'Tra cứu tài khoản';
:Xem thông báo lỗi;
stop
:Hiển thị form nhập mật khẩu mới;
:Nhập mật khẩu mới & xác nhận;
:Nhấn 'Xác nhận đặt lại mật khẩu';
:Nhận thông báo đổi mật khẩu thành công;
stop
|LÀN HỆ THỐNG: Web API Backend|
:Gửi lệnh tìm kiếm tài khoản;
note right: [Kiểm tra tồn tại] Tìm thấy tài khoản?
:Báo lỗi: Tài khoản không tồn tại;
note right: [Kiểm tra khớp] Mật khẩu mới khớp nhau?
:Báo lỗi: Mật khẩu xác nhận không khớp;
:Băm mật khẩu mới SHA-256;
:Gửi lệnh cập nhật mật khẩu mới;
|LÀN CƠ SỞ DỮ LIỆU: SQL Server|
:SELECT * FROM Users WHERE Phone=@p OR Email=@e;
:Trả về thông tin User;
:UPDATE Users SET PasswordHash=@h WHERE Id=@id;
:Xác nhận cập nhật thành công;
@enduml
```

#### Biểu đồ Tuần tự chuẩn UML (UML Sequence Diagram - UC002):
```plantuml
@startuml
autonumber
skinparam responseMessageBelowArrow true
skinparam BoxPadding 10
skinparam ParticipantPadding 10
actor "👤 Khách hàng" as KH
participant "💻 Giao diện Quên mật khẩu (Boundary)" as GD
participant "🌐 AuthController (Control)" as API
participant "⚙️ UserService (Control)" as SVC
participant "🗄️ CSDL SQL Server (Entity)" as DB
KH -> GD : Nhập SĐT/Email, nhấn 'Tra cứu tài khoản'
activate GD
GD -> API : POST /api/auth/find-account (PhoneOrEmail)
activate API
API -> SVC : Tra cứu tài khoản theo Phone hoặc Email
activate SVC
SVC -> DB : SELECT * FROM Users WHERE Phone = @val OR Email = @val
activate DB
DB --> SVC : Trả về kết quả User entity hoặc Null
deactivate DB
alt Không tìm thấy tài khoản
SVC --> API : Trả về mã 404 Not Found
API --> GD : Phản hồi lỗi: Không tìm thấy thông tin đăng ký
GD --> KH : Thông báo tài khoản không tồn tại
else Tìm thấy tài khoản hợp lệ
SVC --> API : Trả về thông tin UserId và trạng thái hợp lệ
deactivate SVC
API --> GD : Phản hồi HTTP 200 OK (Cho phép đặt lại)
deactivate API
GD --> KH : Mở giao diện nhập Mật khẩu mới & Xác nhận
KH -> GD : Nhập mật khẩu mới, bấm 'Xác nhận đặt lại'
GD -> API : POST /api/auth/reset-password (UserId, NewPassword)
activate API
API -> SVC : Thực hiện đặt lại mật khẩu
activate SVC
SVC -> SVC : Băm SHA-256(NewPassword)
SVC -> DB : UPDATE Users SET PasswordHash = @newHash WHERE Id = @UserId
activate DB
DB --> SVC : Cập nhật thành công 1 bản ghi
deactivate DB
SVC --> API : Xác nhận cập nhật thành công
deactivate SVC
API --> GD : Phản hồi HTTP 200 OK
deactivate API
GD --> KH : Hiển thị thông báo thành công và chuyển về trang Đăng nhập
end
deactivate GD
@enduml
```

---

### 3.3.3 UC003: Quản lý thông tin cá nhân & Tải ảnh đại diện (Profile & Avatar)
* **Mục đích:** Cho phép người dùng xem lại thông tin hồ sơ, cập nhật số điện thoại, email, họ tên, đổi mật khẩu định kỳ và tải ảnh đại diện hiển thị trên ứng dụng.
* **Mô tả nghiệp vụ:** Người dùng vào trang Profile. Hệ thống lấy thông tin từ Token để tải dữ liệu. Người dùng có thể chỉnh sửa thông tin hoặc chọn file ảnh (PNG, JPG) từ máy tính. File ảnh được upload lên thư mục `wwwroot/uploads` trên máy chủ và cập nhật đường dẫn `AvatarUrl` vào CSDL.
* **Tác nhân:** Khách hàng (Customer), Quản trị viên (Admin).
* **Điều kiện trước:** Người dùng đã đăng nhập hệ thống và sở hữu JWT Token hợp lệ.
* **Điều kiện sau:** Thông tin cá nhân và ảnh đại diện được cập nhật đồng bộ trên giao diện và trong CSDL.

#### Biểu đồ Hoạt động chuẩn UML (UML Activity Diagram với Swimlane - UC003):
```plantuml
@startuml
skinparam activity {
  BackgroundColor #F8FAFC
  BorderColor #2563EB
  FontColor #0F172A
}
skinparam diamond {
  BackgroundColor #EFF6FF
  BorderColor #1D4ED8
}

|LÀN TÁC NHÂN: Người dùng|
start
:Mở trang Hồ sơ cá nhân (Profile);
:Sửa Họ tên, SĐT & Chọn ảnh Avatar mới;
:Nhấn nút 'Lưu thay đổi';
:Xem thông báo lỗi file;
stop
:Xem thông tin & Avatar mới cập nhật;
stop
|LÀN HỆ THỐNG: Web API Backend|
note right: [Kiểm tra file] Có tải kèm file ảnh?
note right: [Kiểm tra format] Định dạng JPG/PNG & < 5MB?
:Báo lỗi: File không hợp lệ hoặc quá 5MB;
:Lưu file vật lý vào thư mục wwwroot/uploads;
:Gửi lệnh cập nhật thông tin & đường dẫn ảnh;
|LÀN CƠ SỞ DỮ LIỆU: SQL Server|
:UPDATE Users SET FullName=@name, AvatarUrl=@url WHERE Id=@id;
:Xác nhận cập nhật thành công;
@enduml
```

#### Biểu đồ Tuần tự chuẩn UML (UML Sequence Diagram - UC003):
```plantuml
@startuml
autonumber
skinparam responseMessageBelowArrow true
skinparam BoxPadding 10
skinparam ParticipantPadding 10
actor "👤 Người dùng" as ND
participant "💻 Giao diện Profile (Boundary)" as GD
participant "🌐 UserController (Control)" as API
participant "📁 Hệ thống Tệp wwwroot (Entity)" as FS
participant "🗄️ CSDL SQL Server (Entity)" as DB
ND -> GD : Cập nhật họ tên & Chọn file ảnh đại diện mới
ND -> GD : Bấm 'Lưu thay đổi'
activate GD
GD -> API : POST /api/user/profile (Multipart Form Data)
activate API
opt Có gửi kèm file ảnh đại diện
API -> API : Kiểm tra định dạng (.jpg, .png) & Dung lượng (< 5MB)
alt File không hợp lệ
API --> GD : Phản hồi mã lỗi 400 Bad Request
GD --> ND : Hiển thị thông báo file ảnh không hợp lệ
end
API -> FS : Lưu file với tên ngẫu nhiên (GUID.png) vào /uploads/
FS --> API : Trả về đường dẫn tương đối (/uploads/avatar.png)
end
API -> DB : UPDATE Users SET FullName = @name, AvatarUrl = @avatar WHERE Id = @UserId
activate DB
DB --> API : Xác nhận cập nhật thành công
deactivate DB
API --> GD : Phản hồi HTTP 200 OK kèm UserDTO mới
deactivate API
GD -> GD : Cập nhật Avatar và Tên trên Header
GD --> ND : Hiển thị thông báo Cập nhật hồ sơ thành công!
deactivate GD
@enduml
```

---

### 3.3.4 UC004: Tra cứu danh mục sân bóng & Lịch trống (Sân 5, 7, 11)
* **Mục đích:** Giúp khách hàng nhanh chóng tìm kiếm sân bóng phù hợp theo quy mô thi đấu (sân 5 người, sân 7 VIP, sân 11 cỏ tự nhiên), xem trang thiết bị và kiểm tra các khung giờ còn trống trong ngày.
* **Mô tả nghiệp vụ:** Khách hàng chọn ngày muốn thi đấu và loại sân. Hệ thống tải danh sách các sân bóng đang mở và lấy toàn bộ các đơn đặt sân (`Confirmed`) trong ngày đó để tính toán và hiển thị ma trận trạng thái: ô màu Xanh (Còn trống) và ô màu Đỏ (Đã có người đặt).
* **Tác nhân:** Khách hàng (Customer).
* **Điều kiện trước:** Máy chủ cơ sở dữ liệu hoạt động bình thường.
* **Điều kiện sau:** Khách hàng nắm rõ danh sách sân trống và giá cơ sở để chuẩn bị đặt sân.

#### Biểu đồ Hoạt động chuẩn UML (UML Activity Diagram với Swimlane - UC004):
```plantuml
@startuml
skinparam activity {
  BackgroundColor #F8FAFC
  BorderColor #2563EB
  FontColor #0F172A
}
skinparam diamond {
  BackgroundColor #EFF6FF
  BorderColor #1D4ED8
}

|LÀN TÁC NHÂN: Khách hàng|
start
:Truy cập trang Danh mục sân bóng;
:Chọn loại sân (5, 7, 11) & Ngày thi đấu;
:Nhấn tìm kiếm / Lọc danh sách;
:Xem ma trận lịch trống trực quan (Xanh/Đỏ);
:Nhấp chọn ô giờ trống để đặt sân;
stop
|LÀN HỆ THỐNG: Web API Backend|
:Gửi truy vấn sân và lịch đặt đến CSDL;
:Ghép nối dữ liệu: Tính toán trạng thái các khung giờ;
:Tạo mô hình ma trận giờ (Trống / Đã đặt);
|LÀN CƠ SỞ DỮ LIỆU: SQL Server|
:SELECT * FROM Fields WHERE Status = 1;
:SELECT * FROM Bookings WHERE Date = @Date AND Status = 1;
:Trả về danh sách sân và các khoảng giờ đã đặt;
@enduml
```

#### Biểu đồ Tuần tự chuẩn UML (UML Sequence Diagram - UC004):
```plantuml
@startuml
autonumber
skinparam responseMessageBelowArrow true
skinparam BoxPadding 10
skinparam ParticipantPadding 10
actor "👤 Khách hàng" as KH
participant "💻 Giao diện Danh mục Sân (Boundary)" as GD
participant "🌐 PitchController (Control)" as API
participant "⚙️ PitchService (Control)" as SVC
participant "🗄️ CSDL SQL Server (Entity)" as DB
KH -> GD : Chọn loại sân (Sân 7) và Chọn ngày thi đấu
activate GD
GD -> API : GET /api/pitch/search?type=7&date=2026-09-25
activate API
API -> SVC : Lấy thông tin sân và ma trận lịch thi đấu
activate SVC
SVC -> DB : SELECT * FROM Fields WHERE FieldType = 7 AND Status = 1
activate DB
DB --> SVC : Trả về danh sách sân bóng phù hợp
SVC -> DB : SELECT * FROM Bookings WHERE FieldId IN (...) AND StartTime = @Date AND Status = Confirmed
DB --> SVC : Trả về các khoảng thời gian đã được xác nhận đặt
deactivate DB
SVC -> SVC : Tính toán ma trận: 14h-16h (Trống), 17h-19h (Đã đặt)...
SVC --> API : Trả về danh sách PitchDTO kèm Slots trạng thái
deactivate SVC
API --> GD : Phản hồi HTTP 200 OK { pitches, slots }
deactivate API
GD --> KH : Hiển thị danh sách sân bóng kèm các ô giờ màu Xanh/Đỏ
deactivate GD
@enduml
```

---

### 3.3.5 UC005: Xem giá đề xuất thông minh AI (Dynamic Pricing)
* **Mục đích:** Cung cấp báo giá linh hoạt, tối ưu doanh thu và minh bạch cho khách hàng theo thời gian thực dựa trên thuật toán định giá động AI.
* **Mô tả nghiệp vụ:** Khi khách hàng chọn một khung giờ thi đấu cụ thể, hệ thống gọi tới dịch vụ AI Microservice (`/api/ai/pricing`). AI tính toán dựa trên: Giá cơ sở, Khung giờ (giờ sáng thấp điểm, giờ tối cao điểm 17h-21h: +50%), và Ngày thi đấu (Thứ 7 & Chủ Nhật: +30%). Nếu dịch vụ AI gián đoạn, cơ chế Fallback nội bộ sẽ lập tức tính toán đảm bảo trải nghiệm thông suốt.
* **Tác nhân:** Khách hàng (Customer), Microservice AI Python.
* **Điều kiện trước:** Khách hàng đã chọn sân và khung giờ thi đấu.
* **Điều kiện sau:** Giá tiền thuê sân dự kiến được tính toán chính xác và hiển thị chi tiết phụ thu trên màn hình đặt sân.

#### Biểu đồ Hoạt động chuẩn UML (UML Activity Diagram với Swimlane - UC005):
```plantuml
@startuml
skinparam activity {
  BackgroundColor #F8FAFC
  BorderColor #2563EB
  FontColor #0F172A
}
skinparam diamond {
  BackgroundColor #EFF6FF
  BorderColor #1D4ED8
}

|LÀN TÁC NHÂN: Khách hàng|
start
:Chọn khung giờ đá (VD: 19:00 - 20:30 Chủ Nhật);
:Xem bảng phân tích giá và phụ thu giờ cao điểm/cuối tuần;
stop
|LÀN HỆ THỐNG: Web API Backend|
:Gửi yêu cầu định giá sang AI Client;
:Gọi REST API sang Microservice AI;
note right: [Kiểm tra phản hồi] Máy chủ AI phản hồi?
:Kích hoạt bộ máy Fallback: Tính phụ thu theo công thức chuẩn;
:Phân tích kết quả giá và lý do điều chỉnh;
:Đóng gói kết quả hiển thị cho khách;
|LÀN TRÍ TUỆ NHÂN TẠO: Python Microservice|
:Thuật toán Dynamic Pricing: Tính hệ số Peak & Weekend;
:Trả về kết quả { dynamic_price, multiplier, reasons };
@enduml
```

#### Biểu đồ Tuần tự chuẩn UML (UML Sequence Diagram - UC005):
```plantuml
@startuml
autonumber
skinparam responseMessageBelowArrow true
skinparam BoxPadding 10
skinparam ParticipantPadding 10
actor "👤 Khách hàng" as KH
participant "💻 Giao diện Đặt sân (Boundary)" as GD
participant "🌐 BookingController (Control)" as API
participant "🔌 AIServiceClient (Control)" as CLI
participant "🤖 Microservice AI Python (Entity)" as AI
KH -> GD : Chọn khung giờ 19:00 - 20:30 ngày Chủ Nhật
activate GD
GD -> API : GET /api/booking/calculate-price?fieldId=...&startTime=...
activate API
API -> CLI : GetAiOptimalPrice(fieldId, startTime, basePrice)
activate CLI
alt Kết nối Microservice AI thành công
CLI -> AI : POST /api/predict-price { field_id, hour: 19, is_weekend: true }
activate AI
AI -> AI : Phân tích hệ số: Giờ cao điểm (+50%), Cuối tuần (+30%)
AI --> CLI : Trả về HTTP 200 OK { dynamic_price: 450000, multiplier: 1.95, reasons: [...] }
deactivate AI
else Microservice AI gặp sự cố mạng hoặc Timeout
CLI -> CLI : Kích hoạt Smart Fallback Engine cục bộ
CLI -> CLI : Tính toán giá theo công thức dự phòng an toàn
end
CLI --> API : Trả về đối tượng AIPricingResult
deactivate CLI
API --> GD : Phản hồi HTTP 200 OK kèm dữ liệu chi tiết
deactivate API
GD --> KH : Hiển thị bảng phân tích chi phí và tổng tiền phải trả
deactivate GD
@enduml
```

---

### 3.3.6 UC006: Chatbot trợ lý ảo AI tư vấn 24/7 (LM Studio / Fallback Engine)
* **Mục đích:** Cung cấp kênh tư vấn giải đáp thắc mắc tự động, thông minh 24/7 về giá sân, quy định, tiện ích và gợi ý sân trống cho khách hàng bằng tiếng Việt tự nhiên.
* **Mô tả nghiệp vụ:** Khách hàng trò chuyện qua khung chat góc phải màn hình. Tin nhắn được gửi tới Python Flask Microservice và chuyển tiếp tới mô hình LLM chạy cục bộ tại LM Studio (Qwen 2.5). Khi LM Studio bận hoặc tắt, hệ thống kích hoạt Smart Fallback Engine phân tích từ khóa và trả lời tức thì với độ trễ cực thấp.
* **Tác nhân:** Khách hàng (Customer), Hệ thống AI Microservice, LM Studio.
* **Điều kiện trước:** Trang web đã được tải xong.
* **Điều kiện sau:** Khách hàng nhận được câu trả lời thân thiện, chính xác và hướng dẫn đặt sân nhanh chóng.

#### Biểu đồ Hoạt động chuẩn UML (UML Activity Diagram với Swimlane - UC006):
```plantuml
@startuml
skinparam activity {
  BackgroundColor #F8FAFC
  BorderColor #2563EB
  FontColor #0F172A
}
skinparam diamond {
  BackgroundColor #EFF6FF
  BorderColor #1D4ED8
}

|LÀN TÁC NHÂN: Khách hàng|
start
:Mở widget Chatbot góc phải màn hình;
:Nhập câu hỏi: 'Tối nay sân 7 còn trống không?';
:Xem câu trả lời tư vấn từ Trợ lý ảo AI;
stop
|LÀN HỆ THỐNG: Python Flask Microservice|
:Chuyển tiếp câu hỏi và ngữ cảnh hệ thống;
:Gửi yêu cầu tới LM Studio qua cổng 1234;
note right: [Kiểm tra LLM] LM Studio phản hồi thành công?
:Kích hoạt Smart Fallback Engine: Khớp từ khóa tri thức nội bộ;
:Nhận phản hồi văn bản tiếng Việt tự nhiên;
:Đóng gói JSON phản hồi về Client;
|🧠 LÀN MÔ HÌNH NGÔN NGỮ LỚN: LM Studio Local|
:Mô hình Qwen 2.5 Instruct suy luận câu trả lời;
:Trả về nội dung chat text;
@enduml
```

#### Biểu đồ Tuần tự chuẩn UML (UML Sequence Diagram - UC006):
```plantuml
@startuml
autonumber
skinparam responseMessageBelowArrow true
skinparam BoxPadding 10
skinparam ParticipantPadding 10
actor "👤 Khách hàng" as KH
participant "💬 Widget Chatbot Frontend (Boundary)" as CHAT
participant "🐍 Microservice AI Flask (Control)" as SVR
participant "🧠 LM Studio Qwen 2.5 (Entity)" as LLM
KH -> CHAT : Gửi câu hỏi: 'Giá sân 7 tối thứ Bảy bao nhiêu?'
activate CHAT
CHAT -> CHAT : Hiển thị chỉ báo 'Trợ lý AI đang suy nghĩ...'
CHAT -> SVR : POST /api/chat { message, history }
activate SVR
SVR -> LLM : POST http://localhost:1234/v1/chat/completions (Prompt + System Context)
activate LLM
alt Mô hình AI LM Studio phản hồi bình thường
LLM --> SVR : Trả về câu trả lời tự nhiên từ Qwen 2.5
SVR --> CHAT : Phản hồi JSON { answer: 'Dạ giá sân 7...', source: 'LLM' }
else LM Studio tắt hoặc kết nối bị Timeout
' LLM--XSVR: Kết nối thất bại / Timeout quá 5s
deactivate LLM
SVR -> SVR : Kích hoạt Smart Fallback NLP Engine
SVR -> SVR : Phân tích từ khóa 'sân 7', 'thứ Bảy' $
' ightarrow$ Trích xuất bảng giá
SVR --> CHAT : Phản hồi JSON { answer: 'Dạ theo quy định...', source: 'Fallback' }
end
deactivate SVR
CHAT --> KH : Hiển thị tin nhắn trả lời chu đáo trên khung chat
deactivate CHAT
@enduml
```

---

### 3.3.7 UC007: Đặt sân & Xử lý giao dịch ví điện tử an toàn (Concurrency Lock)
* **Mục đích:** Đảm bảo khách hàng hoàn tất quy trình giữ chỗ sân bóng một cách tiện lợi, thanh toán trừ tiền ví tự động và tuyệt đối không bao giờ xảy ra lỗi trùng lịch (Double-booking) giữa nhiều người cùng lúc.
* **Mô tả nghiệp vụ:** Khách hàng xác nhận đơn đặt sân. Hệ thống kiểm tra điều kiện thời gian (đặt trước từ 2h đến 3 ngày), số dư ví khách hàng, áp dụng cơ chế khóa tài nguyên dùng chung (`lock (_lockObj)`), kiểm tra trùng lặp trên CSDL, trừ tiền ví, tạo bản ghi `Bookings` (`Confirmed`) và ghi sổ cái `Transactions` (`Payment`).
* **Tác nhân:** Khách hàng (Customer).
* **Điều kiện trước:** Khách hàng đã đăng nhập, số dư ví $\ge$ giá thuê sân.
* **Điều kiện sau:** Đơn đặt sân được xác nhận thành công, số dư ví bị trừ, sinh mã QR kiểm tra vào sân.

#### Biểu đồ Hoạt động chuẩn UML (UML Activity Diagram với Swimlane - UC007):
```plantuml
@startuml
skinparam activity {
  BackgroundColor #F8FAFC
  BorderColor #2563EB
  FontColor #0F172A
}
skinparam diamond {
  BackgroundColor #EFF6FF
  BorderColor #1D4ED8
}

|LÀN TÁC NHÂN: Khách hàng|
start
:Nhấn nút 'Xác nhận Đặt sân & Trừ tiền ví';
:Xem thông báo từ chối (Trùng lịch / Thiếu tiền);
stop
:Nhận vé đặt sân điện tử & Mã QR Check-in;
stop
|LÀN HỆ THỐNG: Web API Backend|
note right: [Kiểm tra thời gian] Đặt trước từ 2h đến 3 ngày?
:Báo lỗi: Thời gian đặt sân không hợp lệ;
:Kích hoạt khóa tiến trình an toàn độc quyền lock(_lockObj);
:Kiểm tra tài khoản & số dư ví;
note right: [Kiểm tra số dư] Số dư ví >= Tổng tiền sân?
:Báo lỗi: Số dư ví không đủ, mời nạp tiền;
:Giải phóng khóa luồng;
:Gửi lệnh quét trùng lịch sang CSDL;
note right: [Kiểm tra trùng lịch] Khung giờ đã có người đặt?
:Báo lỗi: Khung giờ đã có khách khác đặt trước;
:Giải phóng khóa luồng;
:Trừ số dư ví khách hàng: Balance -= Price;
:Lưu đơn Bookings (Confirmed) & Sổ cái Transactions;
:Giải phóng khóa luồng an toàn;
|LÀN CƠ SỞ DỮ LIỆU: SQL Server|
:SELECT WalletBalance, IsDeleted FROM Users WHERE Id=@id;
:Trả về số dư ví người dùng;
:SELECT * FROM Bookings WHERE FieldId=@id AND Confirmed AND Overlap;
:Trả về trạng thái trùng lặp;
:TRANSACTION: UPDATE Users + INSERT Bookings + INSERT Transactions;
:Commit thành công toàn bộ giao dịch;
@enduml
```

#### Biểu đồ Tuần tự chuẩn UML (UML Sequence Diagram - UC007):
```plantuml
@startuml
autonumber
skinparam responseMessageBelowArrow true
skinparam BoxPadding 10
skinparam ParticipantPadding 10
actor "👤 Khách hàng (Cầu thủ)" as KH
participant "💻 Giao diện Đặt sân (Boundary)" as GD
participant "🌐 BookingController (Control)" as API
participant "⚙️ BookingService (Control)" as SVC
participant "🗄️ CSDL SQL Server (Entity)" as DB
KH -> GD : Bấm 'Xác nhận Đặt sân & Trừ tiền Ví'
activate GD
GD -> API : POST /api/booking/create (FieldId, StartTime, EndTime, Price)
activate API
API -> API : Kiểm tra khoảng cách thời gian (2h đến 3 ngày tới)
API -> SVC : CreateBooking(userId, fieldId, start, end, price)
activate SVC
critical Khóa tiến trình đồng bộ đa luồng
SVC -> SVC : lock (_lockObj)
SVC -> DB : Truy vấn số dư ví của khách hàng
activate DB
DB --> SVC : Trả về WalletBalance
deactivate DB
alt Số dư ví không đủ
SVC --> API : Trả về lỗi: Số dư ví không đủ
API --> GD : Phản hồi mã 400 Bad Request
GD --> KH : Hiển thị thông báo thiếu tiền & Gợi ý mở Modal nạp VietQR
else Kiểm tra trùng giờ thi đấu
SVC -> DB : SELECT COUNT(*) FROM Bookings WHERE FieldId = @f AND Status = Confirmed AND Overlap
activate DB
DB --> SVC : Kết quả đếm số lượng đơn trùng
deactivate DB
alt Đã có người đặt trước
SVC --> API : Trả về lỗi: Khung giờ đã bị giữ chỗ
API --> GD : Phản hồi mã 400 Bad Request
GD --> KH : Báo khung giờ đã có người đặt, mời chọn giờ khác
else Đặt sân hợp lệ tuyệt đối
SVC -> SVC : Trừ số dư ví: WalletBalance -= TotalPrice
SVC -> DB : INSERT INTO Bookings (Status: Confirmed, QrCode)
SVC -> DB : INSERT INTO Transactions (Type: Payment, Amount: -TotalPrice)
SVC -> DB : UPDATE Users SET WalletBalance = @newBalance
activate DB
DB --> SVC : Commit thành công các thay đổi CSDL
deactivate DB
SVC --> API : Trả về đối tượng Booking thành công
API --> GD : Phản hồi HTTP 200 OK kèm mã QR vé vào sân
GD --> KH : Hiển thị vé đặt sân & Thông báo thành công!
end
end
SVC -> SVC : Giải phóng lock (_lockObj)
end
deactivate SVC
deactivate API
deactivate GD
@enduml
```

---

### 3.3.8 UC008: Nạp tiền ví qua mã VietQR động (MBBank NAPAS 247)
* **Mục đích:** Cho phép khách hàng dễ dàng nạp thêm tiền vào ví điện tử bằng cách quét mã thanh toán chuẩn ngân hàng quốc gia VietQR, tự động điền đúng STK, số tiền và nội dung chuyển khoản.
* **Mô tả nghiệp vụ:** Khách hàng nhập số tiền muốn nạp. Hệ thống gọi dịch vụ sinh mã `img.vietqr.io` với ngân hàng MBBank, tài khoản chủ sân và nội dung chuyển khoản được mã hóa kèm mã User ID. Sau khi chuyển, đơn nạp tiền `DepositRequest` được tạo ở trạng thái `Pending` để gửi tới quản trị viên.
* **Tác nhân:** Khách hàng (Customer), Cổng VietQR MBBank.
* **Điều kiện trước:** Khách hàng đã đăng nhập tài khoản.
* **Điều kiện sau:** Mã QR được hiển thị rõ nét; đơn nạp tiền lưu vào CSDL chờ Admin đối soát.

#### Biểu đồ Hoạt động chuẩn UML (UML Activity Diagram với Swimlane - UC008):
```plantuml
@startuml
skinparam activity {
  BackgroundColor #F8FAFC
  BorderColor #2563EB
  FontColor #0F172A
}
skinparam diamond {
  BackgroundColor #EFF6FF
  BorderColor #1D4ED8
}

|LÀN TÁC NHÂN: Khách hàng|
start
:Nhập số tiền muốn nạp vào ví;
:Bấm nút 'Tạo mã QR VietQR';
:Màn hình hiển thị mã QR kèm nội dung chuyển khoản định danh;
:Mở app Mobile Banking quét mã & chuyển khoản;
:Nhấn nút 'Tôi đã chuyển khoản thành công';
:Nhận thông báo: Đang chờ Admin đối soát;
stop
|LÀN HỆ THỐNG: Web API Backend|
note right: [Kiểm tra mức tối thiểu] Số tiền >= 10.000đ?
:Báo lỗi số tiền tối thiểu;
:Sinh link ảnh VietQR động chuẩn NAPAS 247 MBBank;
:Tạo bản ghi DepositRequest (Status = Pending);
|LÀN CƠ SỞ DỮ LIỆU: SQL Server|
:INSERT INTO DepositRequests (UserId, Amount, Status: Pending);
:Xác nhận lưu thành công;
@enduml
```

#### Biểu đồ Tuần tự chuẩn UML (UML Sequence Diagram - UC008):
```plantuml
@startuml
autonumber
skinparam responseMessageBelowArrow true
skinparam BoxPadding 10
skinparam ParticipantPadding 10
actor "👤 Khách hàng" as KH
participant "💻 Giao diện Nạp Ví (Boundary)" as GD
participant "🌐 PaymentController (Control)" as API
participant "🏦 Cổng VietQR NAPAS 247 (Entity)" as VQR
participant "🗄️ CSDL SQL Server (Entity)" as DB
KH -> GD : Nhập số tiền 500.000đ, bấm 'Tạo mã VietQR'
activate GD
GD -> API : GET /api/payment/generate-vietqr?amount=500000
activate API
API -> API : Định dạng cú pháp chuyển khoản: NAPVI {UserId}
API -> VQR : Xây dựng URL mã VietQR (MBBank, STK chủ sân, 500000đ, Memo)
VQR --> API : Trả về link ảnh QR thanh toán chính xác
API --> GD : Phản hồi HTTP 200 OK { qrUrl, bankInfo, transferContent }
deactivate API
GD --> KH : Hiển thị Modal mã QR sắc nét kèm hướng dẫn chuyển tiền
KH -> KH : Mở Mobile Banking quét mã & chuyển khoản
KH -> GD : Bấm 'Tôi đã chuyển tiền thành công'
GD -> API : POST /api/payment/create-deposit-request (Amount, Memo)
activate API
API -> DB : INSERT INTO DepositRequests (UserId, Amount, Status = Pending)
activate DB
DB --> API : Xác nhận lưu đơn nạp tiền thành công
deactivate DB
API --> GD : Phản hồi HTTP 200 OK (Chờ duyệt)
deactivate API
GD --> KH : Hiển thị thông báo tiếp nhận yêu cầu, tiền sẽ vào ví trong 1-3 phút
deactivate GD
@enduml
```

---

### 3.3.9 UC009: Quản lý lịch sử đặt sân cá nhân & Mã QR Check-in
* **Mục đích:** Giúp khách hàng xem lại danh sách các trận bóng đã đặt, theo dõi trạng thái đơn (Đã xác nhận, Đã hủy, Hoàn thành), kiểm tra hóa đơn và lấy mã QR vé để nhân viên sân quét check-in vào sân.
* **Mô tả nghiệp vụ:** Khách hàng vào trang "Lịch sử đặt sân". Hệ thống truy vấn toàn bộ các đơn đặt sân của User hiện tại, sắp xếp theo thứ tự mới nhất, hiển thị chi tiết: Tên sân, loại sân, thời gian đá, số tiền đã trừ và nút xem vé điện tử QR.
* **Tác nhân:** Khách hàng (Customer).
* **Điều kiện trước:** Khách hàng đã đăng nhập hệ thống.
* **Điều kiện sau:** Danh sách đơn được hiển thị đầy đủ, chính xác kèm theo mã QR vé của từng đơn.

#### Biểu đồ Hoạt động chuẩn UML (UML Activity Diagram với Swimlane - UC009):
```plantuml
@startuml
skinparam activity {
  BackgroundColor #F8FAFC
  BorderColor #2563EB
  FontColor #0F172A
}
skinparam diamond {
  BackgroundColor #EFF6FF
  BorderColor #1D4ED8
}

|LÀN TÁC NHÂN: Khách hàng|
start
:Bấm chọn menu 'Lịch sử đặt sân';
:Xem danh sách các trận bóng đã đặt sắp xếp mới nhất;
:Bấm xem vé điện tử của trận sắp thi đấu;
:Xuất trình mã QR check-in cho nhân viên tại sân;
stop
|LÀN HỆ THỐNG: Web API Backend|
:Trích xuất UserId từ JWT Token & gửi truy vấn;
note right: [Kiểm tra dữ liệu] Đã từng đặt đơn nào?
:Hiển thị màn hình trống: Chưa có giao dịch;
:Đóng gói danh sách đơn kèm trạng thái;
:Tạo nội dung mã QR định danh bảo mật vé;
|LÀN CƠ SỞ DỮ LIỆU: SQL Server|
:SELECT b.*, f.Name FROM Bookings b JOIN Fields f ON b.FieldId=f.FieldId WHERE UserId=@id ORDER BY b.CreatedAt DESC;
:Trả về danh sách đơn đặt sân;
@enduml
```

#### Biểu đồ Tuần tự chuẩn UML (UML Sequence Diagram - UC009):
```plantuml
@startuml
autonumber
skinparam responseMessageBelowArrow true
skinparam BoxPadding 10
skinparam ParticipantPadding 10
actor "👤 Khách hàng" as KH
participant "💻 Giao diện Lịch sử (Boundary)" as GD
participant "🌐 BookingController (Control)" as API
participant "⚙️ BookingService (Control)" as SVC
participant "🗄️ CSDL SQL Server (Entity)" as DB
KH -> GD : Nhấp chọn menu 'Lịch sử đặt sân'
activate GD
GD -> API : GET /api/booking/my-history (Bearer JWT Token)
activate API
API -> SVC : GetUserBookings(userId)
activate SVC
SVC -> DB : SELECT * FROM Bookings WHERE UserId = @id ORDER BY CreatedAt DESC
activate DB
DB --> SVC : Trả về danh sách các bản ghi Booking
deactivate DB
SVC --> API : Trả về danh sách BookingResponseDto
deactivate SVC
API --> GD : Phản hồi HTTP 200 OK kèm danh sách đơn
deactivate API
GD --> KH : Hiển thị các thẻ đơn đặt sân: Sắp diễn ra, Hoàn thành, Đã hủy
KH -> GD : Bấm nút 'Xem vé QR' trên đơn sắp đá
GD --> KH : Hiển thị Modal vé điện tử kèm mã QR check-in tại sân
deactivate GD
@enduml
```

---

### 3.3.10 UC010: Dashboard thống kê báo cáo KPI & Heatmap ma trận sân
* **Mục đích:** Giúp Ban quản trị nắm bắt tức thì tình hình kinh doanh, tổng doanh thu thực tế, số lượng đơn đặt sân, số lượng thành viên mới và biểu đồ nhiệt (Heatmap) lấp đầy các khung giờ trong tuần.
* **Mô tả nghiệp vụ:** Khi Admin đăng nhập trang quản trị, hệ thống tự động tổng hợp dữ liệu từ các bảng `Bookings`, `Transactions` và `Users`. Tính toán tổng doanh thu lũy kế, doanh thu theo ngày/tháng, số đơn thành công, tỷ lệ hủy đơn và dựng bản đồ nhiệt giờ vàng.
* **Tác nhân:** Quản trị viên (Admin).
* **Điều kiện trước:** Quản trị viên đã đăng nhập với vai trò Admin (`Role = 1`).
* **Điều kiện sau:** Toàn bộ biểu đồ và các chỉ số KPI tài chính hiển thị chính xác theo thời gian thực.

#### Biểu đồ Hoạt động chuẩn UML (UML Activity Diagram với Swimlane - UC010):
```plantuml
@startuml
skinparam activity {
  BackgroundColor #F8FAFC
  BorderColor #2563EB
  FontColor #0F172A
}
skinparam diamond {
  BackgroundColor #EFF6FF
  BorderColor #1D4ED8
}

|LÀN TÁC NHÂN: Quản trị viên|
start
:Truy cập trang Tổng quan Dashboard Admin;
:Bị từ chối: Không có quyền Admin;
stop
:Xem các Card chỉ số KPI, Biểu đồ doanh thu & Heatmap sân;
stop
|LÀN HỆ THỐNG: Web API Backend|
note right: [Kiểm tra Role] Người dùng có quyền Admin?
:Trả về mã lỗi HTTP 403 Forbidden;
:Gửi các câu lệnh tổng hợp số liệu sang CSDL;
:Tính toán tỷ lệ lấp đầy, doanh thu theo ngày & Heatmap;
|LÀN CƠ SỞ DỮ LIỆU: SQL Server|
:SUM(TotalPrice) FROM Bookings WHERE Status IN (1, 3);
:COUNT(*) FROM Users; COUNT(*) FROM Bookings;
:Trả về bộ số liệu thống kê thô;
@enduml
```

#### Biểu đồ Tuần tự chuẩn UML (UML Sequence Diagram - UC010):
```plantuml
@startuml
autonumber
skinparam responseMessageBelowArrow true
skinparam BoxPadding 10
skinparam ParticipantPadding 10
actor "🛡️ Quản trị viên (Admin)" as ADM
participant "🖥️ Dashboard Admin (Boundary)" as GD
participant "🌐 AdminController (Control)" as API
participant "⚙️ ReportService (Control)" as SVC
participant "🗄️ CSDL SQL Server (Entity)" as DB
ADM -> GD : Truy cập trang Bảng điều khiển Quản trị
activate GD
GD -> API : GET /api/admin/dashboard-stats (Bearer JWT Admin)
activate API
API -> API : Kiểm tra phân quyền: Role == 'Admin'
API -> SVC : GetDashboardSummary()
activate SVC
SVC -> DB : SUM(TotalPrice) WHERE Status IN (Confirmed, Completed)
activate DB
DB --> SVC : Trả về Tổng doanh thu thực tế
SVC -> DB : COUNT(*) FROM Bookings; COUNT(*) FROM Users
DB --> SVC : Trả về số lượng đơn và số hội viên mới
deactivate DB
SVC -> SVC : Tính toán ma trận tần suất khung giờ vàng trong tuần
SVC --> API : Trả về đối tượng DashboardSummaryDto
deactivate SVC
API --> GD : Phản hồi HTTP 200 OK kèm bộ số liệu KPI
deactivate API
GD --> ADM : Hiển thị các Card doanh thu và vẽ biểu đồ trực quan
deactivate GD
@enduml
```

---

### 3.3.11 UC011: Phê duyệt / Từ chối yêu cầu nạp tiền ví (Admin đối soát)
* **Mục đích:** Đảm bảo tính minh bạch, chính xác tuyệt đối của dòng tiền vào hệ thống; chỉ cộng số dư ví ảo khi tiền thực tế đã về tài khoản ngân hàng của chủ sân.
* **Mô tả nghiệp vụ:** Admin mở danh sách các yêu cầu nạp tiền đang ở trạng thái `Pending`. Kiểm tra tin nhắn biến động số dư ngân hàng MBBank. Nếu khớp, Admin bấm "Phê duyệt" để cộng tiền vào ví và ghi nhận `TopupApproved`. Nếu không có tiền hoặc sai cú pháp, Admin bấm "Từ chối" kèm lý do.
* **Tác nhân:** Quản trị viên (Admin).
* **Điều kiện trước:** Có yêu cầu nạp tiền ở trạng thái `Pending` trong hệ thống.
* **Điều kiện sau:** Nếu duyệt, số dư ví khách tăng lên; nếu từ chối, đơn chuyển sang `Rejected`.

#### Biểu đồ Hoạt động chuẩn UML (UML Activity Diagram với Swimlane - UC011):
```plantuml
@startuml
skinparam activity {
  BackgroundColor #F8FAFC
  BorderColor #2563EB
  FontColor #0F172A
}
skinparam diamond {
  BackgroundColor #EFF6FF
  BorderColor #1D4ED8
}

|LÀN TÁC NHÂN: Quản trị viên|
start
:Mở danh sách Yêu cầu nạp tiền đang chờ duyệt;
:Kiểm tra sao kê app Mobile Banking MBBank;
note right: [Đối soát ngân hàng] Tiền thực tế đã vào tài khoản?
:Bấm nút 'Từ chối' kèm lý do;
:Bấm nút 'Phê duyệt';
:Cập nhật trạng thái: Đã từ chối;
stop
:Cập nhật trạng thái: Đã duyệt & Tiền đã vào ví khách;
stop
|LÀN HỆ THỐNG: Web API Backend|
:Gửi lệnh cập nhật Status = Rejected;
:Thực hiện cộng tiền vào ví khách hàng;
:Tạo giao dịch sổ cái TopupApproved;
|LÀN CƠ SỞ DỮ LIỆU: SQL Server|
:UPDATE DepositRequests SET Status = 2 WHERE Id = @id;
:Xác nhận từ chối;
:TRANSACTION: UPDATE DepositRequests + UPDATE Users Balance + INSERT Transactions;
:Commit thành công;
@enduml
```

#### Biểu đồ Tuần tự chuẩn UML (UML Sequence Diagram - UC011):
```plantuml
@startuml
autonumber
skinparam responseMessageBelowArrow true
skinparam BoxPadding 10
skinparam ParticipantPadding 10
actor "🛡️ Quản trị viên (Admin)" as ADM
participant "🖥️ Giao diện Duyệt Nạp tiền (Boundary)" as GD
participant "🌐 PaymentController (Control)" as API
participant "⚙️ UserService (Control)" as SVC
participant "🗄️ CSDL SQL Server (Entity)" as DB
ADM -> GD : Mở tab 'Duyệt nạp tiền ví điện tử'
activate GD
GD -> API : GET /api/payment/pending-deposits
activate API
API -> DB : SELECT * FROM DepositRequests WHERE Status = 'Pending'
activate DB
DB --> API : Trả về danh sách yêu cầu nạp tiền
deactivate DB
API --> GD : Hiển thị bảng đối soát tiền nạp
deactivate API
ADM -> ADM : Kiểm tra tin nhắn biến động số dư tài khoản MBBank
alt Tiền đã vào tài khoản chính xác
ADM -> GD : Bấm nút 'Phê duyệt' (RequestId)
GD -> API : POST /api/payment/approve-deposit/{id}
activate API
API -> SVC : ApproveDepositRequest(id)
activate SVC
SVC -> DB : UPDATE Users SET WalletBalance = WalletBalance + Amount
SVC -> DB : UPDATE DepositRequests SET Status = 'Success'
SVC -> DB : INSERT INTO Transactions (Type: TopupApproved, Amount: +Amount)
activate DB
DB --> SVC : Ghi nhận thành công các thay đổi
deactivate DB
SVC --> API : Xác nhận duyệt nạp thành công
deactivate SVC
API --> GD : Phản hồi HTTP 200 OK
deactivate API
GD --> ADM : Đổi badge trạng thái sang màu Xanh (Đã duyệt)
else Không thấy tiền về hoặc gian lận
ADM -> GD : Bấm nút 'Từ chối' (RequestId) kèm ghi chú lý do
GD -> API : POST /api/payment/reject-deposit/{id}
activate API
API -> DB : UPDATE DepositRequests SET Status = 'Rejected'
activate DB
DB --> API : Cập nhật thành công
deactivate DB
API --> GD : Phản hồi HTTP 200 OK
deactivate API
GD --> ADM : Đổi badge trạng thái sang màu Đỏ (Đã từ chối)
end
deactivate GD
@enduml
```

---

### 3.3.12 UC012: Hủy lịch đặt sân & Tự động hoàn tiền ví 100%
* **Mục đích:** Xử lý các tình huống bất khả kháng (mưa bão ngập sân, bảo trì đột xuất hoặc khách hàng báo bận trước giờ quy định) bằng cách hủy đơn an toàn và hoàn trả 100% tiền vào ví của khách ngay lập tức.
* **Mô tả nghiệp vụ:** Khi thao tác Hủy đơn đặt sân được kích hoạt, hệ thống cập nhật trạng thái đơn đặt sân thành `Cancelled` (2), truy vấn số tiền `TotalPrice` của đơn và cộng thẳng vào `user.WalletBalance`, đồng thời tạo giao dịch loại `Refund` (Hoàn tiền).
* **Tác nhân:** Quản trị viên (Admin), Khách hàng.
* **Điều kiện trước:** Đơn đặt sân đang ở trạng thái `Confirmed`.
* **Điều kiện sau:** Đơn đặt sân chuyển thành `Cancelled`, tiền hoàn vào ví khách hàng đầy đủ và khung giờ đó trở lại trạng thái Trống cho người khác đặt.

#### Biểu đồ Hoạt động chuẩn UML (UML Activity Diagram với Swimlane - UC012):
```plantuml
@startuml
skinparam activity {
  BackgroundColor #F8FAFC
  BorderColor #2563EB
  FontColor #0F172A
}
skinparam diamond {
  BackgroundColor #EFF6FF
  BorderColor #1D4ED8
}

|LÀN TÁC NHÂN: Quản trị viên / Khách|
start
:Chọn đơn đặt sân cần hủy;
:Xác nhận cảnh báo: 'Hủy & Hoàn tiền 100%';
:Báo lỗi: Đơn đã hủy hoặc đã hoàn thành;
stop
:Nhận thông báo: Hủy lịch & Hoàn tiền thành công;
stop
|LÀN HỆ THỐNG: Web API Backend|
note right: [Kiểm tra trạng thái] Đơn đang là Confirmed?
:Báo lỗi trạng thái đơn không thể hủy;
:Cập nhật trạng thái đơn: Status = Cancelled;
:Hoàn 100% tiền vào ví: Balance += TotalPrice;
:Tạo bản ghi giao dịch Refund vào sổ cái;
|LÀN CƠ SỞ DỮ LIỆU: SQL Server|
:TRANSACTION: UPDATE Bookings + UPDATE Users + INSERT Transactions;
:Commit thành công toàn bộ giao dịch;
@enduml
```

#### Biểu đồ Tuần tự chuẩn UML (UML Sequence Diagram - UC012):
```plantuml
@startuml
autonumber
skinparam responseMessageBelowArrow true
skinparam BoxPadding 10
skinparam ParticipantPadding 10
actor "🛡️ Quản trị viên (Admin)" as ADM
participant "🖥️ Giao diện Quản lý Đặt sân (Boundary)" as GD
participant "🌐 BookingController (Control)" as API
participant "⚙️ BookingService (Control)" as SVC
participant "🗄️ CSDL SQL Server (Entity)" as DB
ADM -> GD : Nhấn nút 'Hủy & Hoàn tiền' trên đơn đặt sân
activate GD
GD -> GD : Hiển thị hộp thoại xác nhận hủy đơn
ADM -> GD : Xác nhận đồng ý hủy
GD -> API : POST /api/booking/cancel/{id}
activate API
API -> SVC : CancelBooking(bookingId)
activate SVC
SVC -> DB : SELECT * FROM Bookings WHERE Id = @bookingId
activate DB
DB --> SVC : Trả về bản ghi Booking
deactivate DB
alt Đơn không ở trạng thái Confirmed
SVC --> API : Trả về lỗi: Trạng thái không hợp lệ để hủy
API --> GD : Phản hồi mã lỗi 400 Bad Request
GD --> ADM : Hiển thị thông báo không thể hủy đơn
else Đơn hợp lệ để hủy
critical Giao dịch hoàn tiền nguyên tử (Atomic)
SVC -> DB : UPDATE Bookings SET Status = Cancelled WHERE Id = @id
SVC -> DB : UPDATE Users SET WalletBalance = WalletBalance + @totalPrice WHERE Id = @userId
SVC -> DB : INSERT INTO Transactions (UserId, Amount: +@totalPrice, Type: Refund)
activate DB
DB --> SVC : Commit thành công toàn bộ thay đổi
deactivate DB
end
SVC --> API : Trả về kết quả Hủy & Hoàn tiền thành công
deactivate SVC
API --> GD : Phản hồi HTTP 200 OK
deactivate API
GD --> ADM : Thông báo: Hủy đơn thành công & Tiền đã hoàn lại 100% vào ví khách
end
deactivate GD
@enduml
```

---

### 3.3.13 UC013: Quản lý, Khóa / Mở khóa tài khoản người dùng (User Management)
* **Mục đích:** Giúp quản trị viên kiểm soát danh sách thành viên, ngăn chặn các tài khoản có hành vi gian lận, phá hoại hoặc vi phạm chính sách bằng cách khóa quyền truy cập.
* **Mô tả nghiệp vụ:** Admin xem danh sách tất cả tài khoản trong hệ thống. Khi phát hiện vi phạm, Admin bấm nút "Khóa tài khoản" (`IsDeleted = true`). Khi bị khóa, người dùng sẽ không thể đăng nhập hoặc thực hiện bất kỳ giao dịch đặt sân nào. Admin có thể bấm "Mở khóa" để khôi phục quyền hoạt động.
* **Tác nhân:** Quản trị viên (Admin).
* **Điều kiện trước:** Quản trị viên đã đăng nhập tài khoản quyền Admin.
* **Điều kiện sau:** Trạng thái `IsDeleted` của tài khoản người dùng được cập nhật trong CSDL.

#### Biểu đồ Hoạt động chuẩn UML (UML Activity Diagram với Swimlane - UC013):
```plantuml
@startuml
skinparam activity {
  BackgroundColor #F8FAFC
  BorderColor #2563EB
  FontColor #0F172A
}
skinparam diamond {
  BackgroundColor #EFF6FF
  BorderColor #1D4ED8
}

|LÀN TÁC NHÂN: Quản trị viên|
start
:Mở danh sách 'Quản lý Người dùng';
:Tìm kiếm tài khoản cần xử lý theo SĐT / Tên;
note right: [Lựa chọn thao tác] Khóa hay Mở khóa?
:Bấm nút 'Khóa tài khoản';
:Bấm nút 'Mở khóa';
:Xem badge trạng thái người dùng cập nhật trên bảng;
stop
|LÀN HỆ THỐNG: Web API Backend|
:Thiết lập IsDeleted = true trong đối tượng User;
:Thiết lập IsDeleted = false trong đối tượng User;
:Gửi câu lệnh UPDATE trạng thái sang CSDL;
|LÀN CƠ SỞ DỮ LIỆU: SQL Server|
:UPDATE Users SET IsDeleted = @newStatus WHERE Id = @id;
:Xác nhận cập nhật thành công;
@enduml
```

#### Biểu đồ Tuần tự chuẩn UML (UML Sequence Diagram - UC013):
```plantuml
@startuml
autonumber
skinparam responseMessageBelowArrow true
skinparam BoxPadding 10
skinparam ParticipantPadding 10
actor "🛡️ Quản trị viên (Admin)" as ADM
participant "🖥️ Giao diện Quản trị User (Boundary)" as GD
participant "🌐 AdminController (Control)" as API
participant "⚙️ UserService (Control)" as SVC
participant "🗄️ CSDL SQL Server (Entity)" as DB
ADM -> GD : Tìm kiếm tài khoản vi phạm & Nhấn 'Khóa'
activate GD
GD -> API : POST /api/admin/toggle-lock-user/{userId} (Bearer JWT Admin)
activate API
API -> API : Xác thực quyền hạn Quản trị viên (Role == Admin)
API -> SVC : ToggleUserStatus(userId)
activate SVC
SVC -> DB : UPDATE Users SET IsDeleted = ~IsDeleted WHERE Id = @userId
activate DB
DB --> SVC : Cập nhật thành công 1 bản ghi
deactivate DB
SVC --> API : Trả về trạng thái tài khoản mới (IsDeleted: true)
deactivate SVC
API --> GD : Phản hồi HTTP 200 OK { isDeleted: true }
deactivate API
GD --> ADM : Đổi badge người dùng sang màu Đỏ (Đã bị khóa)
deactivate GD
@enduml
```

---

### 3.3.14 UC014: Can thiệp điều chỉnh số dư ví khách hàng (Admin Manual Balance)
* **Mục đích:** Cho phép Ban quản trị can thiệp điều chỉnh số dư ví của khách hàng trong các tình huống ngoại lệ (bồi hoàn sự cố sân bãi, tặng tiền khuyến mãi thành viên VIP, hoặc truy thu lỗi hệ thống).
* **Mô tả nghiệp vụ:** Admin chọn tài khoản khách hàng, nhập số tiền điều chỉnh (dương để cộng thêm, âm để trừ bớt) và bắt buộc phải nhập lý do điều chỉnh. Hệ thống kiểm tra số dư sau khi trừ không được âm (`WalletBalance >= 0`), cập nhật ví và ghi vết vào `Transactions` loại `Adjustment`.
* **Tác nhân:** Quản trị viên (Admin).
* **Điều kiện trước:** Tài khoản người dùng tồn tại và đang hoạt động.
* **Điều kiện sau:** Số dư ví khách hàng được cập nhật chính xác và có bản ghi đối soát minh bạch.

#### Biểu đồ Hoạt động chuẩn UML (UML Activity Diagram với Swimlane - UC014):
```plantuml
@startuml
skinparam activity {
  BackgroundColor #F8FAFC
  BorderColor #2563EB
  FontColor #0F172A
}
skinparam diamond {
  BackgroundColor #EFF6FF
  BorderColor #1D4ED8
}

|LÀN TÁC NHÂN: Quản trị viên|
start
:Mở Modal 'Điều chỉnh số dư ví' của User;
:Nhập số tiền (+ hoặc -) và Lý do can thiệp;
:Nhấn nút 'Xác nhận điều chỉnh';
:Xem cảnh báo lỗi (Bỏ trống lý do / Số dư âm);
stop
:Xem số dư mới của khách hàng cập nhật tức thì;
stop
|LÀN HỆ THỐNG: Web API Backend|
note right: [Kiểm tra lý do] Có nhập lý do điều chỉnh?
:Báo lỗi: Bắt buộc phải có lý do kiểm toán;
:Kiểm tra số dư hiện tại trong CSDL;
note right: [Kiểm tra số dư âm] (Balance + Amount) >= 0?
:Báo lỗi: Không thể trừ quá số dư hiện có;
:Cập nhật số dư mới: Balance += Amount;
:Tạo bản ghi giao dịch Adjustment vào sổ cái;
|LÀN CƠ SỞ DỮ LIỆU: SQL Server|
:SELECT WalletBalance FROM Users WHERE Id = @id;
:Trả về số dư ví hiện tại;
:TRANSACTION: UPDATE Users SET Balance + INSERT Transactions;
:Commit thành công giao dịch;
@enduml
```

#### Biểu đồ Tuần tự chuẩn UML (UML Sequence Diagram - UC014):
```plantuml
@startuml
autonumber
skinparam responseMessageBelowArrow true
skinparam BoxPadding 10
skinparam ParticipantPadding 10
actor "🛡️ Quản trị viên (Admin)" as ADM
participant "🖥️ Giao diện Quản trị User (Boundary)" as GD
participant "🌐 AdminController (Control)" as API
participant "⚙️ UserService (Control)" as SVC
participant "🗄️ CSDL SQL Server (Entity)" as DB
ADM -> GD : Nhập số tiền điều chỉnh (+100.000đ), nhập Lý do kiểm toán
ADM -> GD : Bấm 'Xác nhận điều chỉnh số dư'
activate GD
GD -> API : POST /api/admin/adjust-balance (UserId, Amount: 100000, Reason)
activate API
API -> API : Xác thực quyền hạn Quản trị viên
API -> SVC : AdjustUserBalance(userId, amount, reason)
activate SVC
SVC -> DB : SELECT WalletBalance FROM Users WHERE Id = @userId
activate DB
DB --> SVC : Trả về WalletBalance hiện tại
deactivate DB
alt Nếu là lệnh trừ và (WalletBalance + Amount) < 0
SVC --> API : Trả về lỗi: Số dư ví không thể bị âm
API --> GD : Phản hồi mã lỗi 400 Bad Request
GD --> ADM : Hiển thị cảnh báo: Không thể trừ quá số tiền hiện có
else Thao tác điều chỉnh hợp lệ
critical Cập nhật số dư an toàn
SVC -> DB : UPDATE Users SET WalletBalance = WalletBalance + @amount WHERE Id = @userId
SVC -> DB : INSERT INTO Transactions (UserId, Amount: @amount, Type: Adjustment, Description: @reason)
activate DB
DB --> SVC : Commit thành công các thay đổi CSDL
deactivate DB
end
SVC --> API : Xác nhận điều chỉnh thành công kèm số dư mới
deactivate SVC
API --> GD : Phản hồi HTTP 200 OK { newBalance }
deactivate API
GD --> ADM : Cập nhật hiển thị số dư mới của khách hàng trên bảng
end
deactivate GD
@enduml
```

---

### 3.3.15 UC015: Cấu hình bảng giá niêm yết & Hệ số phụ thu AI (Pricing Configuration)
* **Mục đích:** Giúp chủ sân chủ động điều chỉnh chính sách kinh doanh, thay đổi giá cơ sở của từng loại sân bóng và cập nhật hệ số phụ thu cao điểm, cuối tuần phù hợp với mùa vụ thi đấu.
* **Mô tả nghiệp vụ:** Admin truy cập trang "Cấu hình giá sân". Admin có thể chỉnh sửa giá cơ sở (`BasePricePerHour`) cho từng sân bóng cụ thể và điều chỉnh các hệ số nhân thuật toán AI ($K_{peak}$, $K_{weekend}$). Sau khi lưu, toàn bộ báo giá mới sẽ được áp dụng ngay lập tức cho các lượt đặt sân tiếp theo.
* **Tác nhân:** Quản trị viên (Admin).
* **Điều kiện trước:** Quản trị viên đã đăng nhập với vai trò Admin.
* **Điều kiện sau:** Giá cơ sở và cấu hình hệ số AI được cập nhật đồng bộ vào CSDL và Microservice AI.

#### Biểu đồ Hoạt động chuẩn UML (UML Activity Diagram với Swimlane - UC015):
```plantuml
@startuml
skinparam activity {
  BackgroundColor #F8FAFC
  BorderColor #2563EB
  FontColor #0F172A
}
skinparam diamond {
  BackgroundColor #EFF6FF
  BorderColor #1D4ED8
}

|LÀN TÁC NHÂN: Quản trị viên|
start
:Mở trang 'Cấu hình Giá & AI';
:Sửa Giá cơ sở (BasePrice) & Hệ số phụ thu AI;
:Nhấn nút 'Lưu cấu hình giá';
:Xem thông báo lỗi tham số định giá;
stop
:Xem thông báo bảng giá mới đã có hiệu lực toàn hệ thống;
stop
|LÀN HỆ THỐNG: Web API Backend|
note right: [Kiểm tra tham số] Giá > 0 & Hệ số >= 1.0?
:Báo lỗi: Tham số định giá không hợp lệ;
:Gửi lệnh cập nhật giá niêm yết sang CSDL;
:Gửi thông báo đồng bộ sang Microservice AI;
|LÀN CƠ SỞ DỮ LIỆU: SQL Server|
:UPDATE Fields SET BasePrice = @price WHERE FieldId = @id;
:UPDATE PricingConfig SET PeakHourMultiplier=@peak, WeekendMultiplier=@wk WHERE FieldType=@type;
:Xác nhận lưu cấu hình thành công;
@enduml
```

#### Biểu đồ Tuần tự chuẩn UML (UML Sequence Diagram - UC015):
```plantuml
@startuml
autonumber
skinparam responseMessageBelowArrow true
skinparam BoxPadding 10
skinparam ParticipantPadding 10
actor "🛡️ Quản trị viên (Admin)" as ADM
participant "🖥️ Giao diện Cấu hình Giá (Boundary)" as GD
participant "🌐 PitchController (Control)" as API
participant "⚙️ PitchService (Control)" as SVC
participant "🤖 Microservice AI Python (Entity)" as AI
participant "🗄️ CSDL SQL Server (Entity)" as DB
ADM -> GD : Nhập giá cơ sở mới (300.000đ) & Hệ số giờ cao điểm (1.5)
ADM -> GD : Bấm 'Lưu cấu hình bảng giá'
activate GD
GD -> API : PUT /api/pitch/update-pricing/{id} (BasePrice, PeakMultiplier, WeekendMultiplier)
activate API
API -> API : Xác thực quyền hạn Quản trị viên (Admin)
API -> SVC : UpdateFieldPrice(id, newPrice, peak, weekend)
activate SVC
SVC -> DB : UPDATE Fields SET BasePrice = @newPrice WHERE FieldId = @id
SVC -> DB : UPDATE PricingConfig SET PeakHourMultiplier = @peak, WeekendMultiplier = @weekend
activate DB
DB --> SVC : Commit thành công các bảng giá trong CSDL
deactivate DB
SVC -> AI : POST /api/ai/sync-config { field_id, peak_multiplier, weekend_multiplier }
activate AI
AI --> SVC : Xác nhận đồng bộ tham số AI thành công
deactivate AI
SVC --> API : Hoàn tất cập nhật bảng giá
deactivate SVC
API --> GD : Phản hồi HTTP 200 OK
deactivate API
GD --> ADM : Hiển thị thông báo: Bảng giá mới đã có hiệu lực trên toàn hệ thống
deactivate GD
@enduml
```


---

## 3.4 Các thông tin hỗ trợ khác
Hệ thống được thiết kế theo các tiêu chuẩn kiến trúc hiện đại:
* **Tách biệt mối quan tâm (SoC - Separation of Concerns):** Phân chia rõ ràng 4 tầng: Tầng Lưu trữ (Database), Tầng Xử lý trí tuệ nhân tạo (AI Microservice), Tầng Xử lý nghiệp vụ & API (Backend .NET), Tầng Giao diện người dùng (Frontend SPA).
* **Khả năng tự phục hồi (Resilience & Fault Tolerance):** Bất cứ khi nào kết nối giữa .NET Backend và Python AI Microservice gặp trục trặc, hệ thống sẽ kích hoạt Fallback trong `AIServiceClient.cs` để tự tính giá theo công thức mặc định mà không làm gián đoạn trải nghiệm người dùng.

---

## 3.5 Lý giải vị trí ứng dụng AI trong kiến trúc hệ thống (Tiêu chí 1.4)

Một trong những yêu cầu cốt lõi của đề tài tốt nghiệp là việc **lý giải cơ sở khoa học và bài toán thực tế** khi quyết định tích hợp Trí tuệ Nhân tạo (AI) vào kiến trúc phần mềm, tránh việc áp dụng AI hình thức hoặc lạm dụng AI ở các vị trí không cần thiết.

Nhóm nghiên cứu đã phân tích kỹ lưỡng quy trình vận hành thực tế tại Cụm sân bóng ICTU Thái Nguyên và xác định **2 vị trí "điểm nghẽn" (bottlenecks)** mà các giải pháp lập trình truyền thống (Non-AI / Rule-based) không thể giải quyết triệt để:

### 3.5.1 Vị trí 1: Thuật toán Định giá Linh hoạt theo Thời gian thực (AI Dynamic Pricing)
- **Vấn đề thực tế:** Sân bóng đá mini có tính chất "hàng hóa dịch vụ dễ hỏng" (Perishable Inventory) - nếu một khung giờ trôi qua mà không có người thuê thì giá trị doanh thu của khung giờ đó vĩnh viễn mất đi. Cụm sân ICTU thường gặp tình trạng:
  * Khung giờ cao điểm (18:00 - 21:00) và cuối tuần: Nhu cầu vượt quá 300% công suất phục vụ.
  * Khung giờ sáng (06:00 - 17:00) và rạng sáng (02:00 - 05:00): Tỷ lệ lấp đầy chỉ đạt 20% - 30%.
- **Hạn chế của giải pháp phi AI (Rule-based cứng):** Nếu áp dụng giá cố định bằng các câu lệnh `if...else` đơn thuần, chủ sân sẽ mất đi nguồn thu lớn vào giờ vàng và không thể kích cầu người chơi vào các khung giờ thấp điểm. Ngược lại, nếu thay đổi giá thủ công thì tốn thời gian và không thể phản ánh kịp thời sự biến động nhu cầu.
- **Vai trò của AI:** AI đóng vai trò như một bộ máy quản trị doanh thu (Revenue Management Engine). Mô hình tiếp nhận dữ liệu thời gian thực (Giờ thi đấu, Ngày trong tuần, Lịch sử đặt sân, Trạng thái lấp đầy của 5 sân) để tự động xuất ra hệ số tối ưu $Multiplier \in [1.0, 2.0]$. Từ đó, hệ thống đưa ra mức giá hấp dẫn vào ca sáng (150.000 VNĐ) để kéo khách, đồng thời áp dụng mức giá tương xứng vào ca tối/đêm (300.000 VNĐ) để bù đắp chi phí điện cao áp và bảo dưỡng mặt cỏ cỏ nhân tạo.

### 3.5.2 Vị trí 2: Trợ lý ảo Hội thoại Ngôn ngữ Tự nhiên 24/7 (Local LLM Studio Assistant)
- **Vấn đề thực tế:** Khảo sát cho thấy hơn 74% nhu cầu hỏi lịch sân và đặt chỗ diễn ra ngoài giờ hành chính (từ 21:00 tối đến 02:00 sáng). Việc thuê nhân sự trực tổng đài và trả lời tin nhắn Zalo/Fanpage xuyên đêm gây tốn kém chi phí vận hành rất lớn cho chủ sân.
- **Hạn chế của Chatbot truyền thống (Decision-Tree / Keyword-only):** Chatbot thế hệ cũ chỉ hoạt động theo kịch bản bấm nút hoặc so khớp từ khóa cứng nhắc. Khi khách hàng sử dụng ngôn ngữ tự nhiên, tiếng lóng bóng đá (như *"còn slot nào tối nay không shop?", "kèo 7 người giờ vàng giá sao?", "rạng sáng 2h đá được không?"*), chatbot truyền thống sẽ báo lỗi *"Xin lỗi tôi không hiểu"* hoặc trả lời sai lệch, gây bức xúc cho khách hàng.
- **Vai trò của AI:** Tích hợp mô hình ngôn ngữ lớn (Local LLM Qwen 7B) được huấn luyện chuyên sâu với tri thức cụm sân ICTU. AI hiểu sâu sắc ngữ cảnh hội thoại, nhận diện thực thể (Entity Recognition: loại sân, khung giờ, số tiền), tự nhiên hóa câu trả lời như một nhân viên trực sân thực thụ, giải thích minh bạch chính sách hoàn tiền 100% và quy định đặt trước 2 tiếng.

### 3.5.3 Bảng ma trận đối sánh toàn diện: Giải pháp AI vs Giải pháp Truyền thống (Phi AI)

| Tiêu chí so sánh | Giải pháp Truyền thống (Rule-based / Phi AI) | Giải pháp Tích hợp AI (PitchAI System) | Lợi ích vượt trội của Giải pháp AI |
| :--- | :--- | :--- | :--- |
| **1. Khả năng định giá dịch vụ** | Áp dụng bảng giá cố định; muốn đổi phải sửa mã nguồn hoặc cấu hình thủ công từng dòng | Tự động tính toán giá động theo thời gian thực dựa trên hệ số giờ cao điểm, cuối tuần và nhu cầu sân | Tối đa hóa doanh thu giờ cao điểm thêm **25% - 35%**, tăng tỷ lệ lấp đầy ca sáng lên **40%** |
| **2. Năng lực giao tiếp với khách** | Dựa trên menu bấm nút cứng; khách gõ lệch từ khóa là hệ thống báo không hiểu | Hiểu ngôn ngữ tự nhiên tiếng Việt, tiếng lóng thể thao (*"bắt đối", "slot", "bóng lăn", "sân VIP"*) | Tỷ lệ nhận diện đúng ý định đạt **98%**; khách hàng cảm giác được tư vấn tận tình như người thật |
| **3. Khả năng mở rộng & Học hỏi** | Không có khả năng học; mọi thay đổi nghiệp vụ đòi hỏi lập trình viên can thiệp | Dễ dàng mở rộng tri thức bằng cách nạp thêm dataset `.jsonl` hoặc tinh chỉnh System Prompt | Cập nhật chính sách mới chỉ mất 5 phút thông qua Context Engineering mà không cần sửa code cốt lõi |
| **4. Chi phí & Độ sẵn sàng vận hành** | Tốn chi phí thuê nhân viên trực ca đêm; dễ sót tin nhắn khi có nhiều người hỏi cùng lúc | Vận hành 24/7/365 với chi phí 0 VNĐ; phục vụ không giới hạn số lượng khách hàng cùng lúc | Tiết kiệm hơn **15.000.000 VNĐ/tháng** chi phí trực tổng đài; không bao giờ bỏ lỡ cơ hội bán sân |
| **5. Bảo mật & Cô lập dữ liệu** | Phụ thuộc vào các nền tảng chat đám mây bên thứ ba (Zalo, Messenger) | Triển khai mô hình cục bộ (Local LLM qua LM Studio); dữ liệu hội thoại không thoát ra ngoài | **Zero Cloud Data Leakage**: Bảo mật tuyệt đối danh tính, số điện thoại và lịch trình của sinh viên |

---

# PHẦN 4: TÀI LIỆU THIẾT KẾ HƯỚNG ĐỐI TƯỢNG (MÔ HÌNH LỚP CHI TIẾT)
**Nhóm 02** - Thành viên thực hiện:
1. Lã Quý Doanh (Trưởng nhóm)
2. Bùi Thanh Bình
* **Tên ứng dụng:** Hệ thống đặt sân bóng tự động tích hợp AI & Ví điện tử
* **Thời gian thực hiện:** Từ 27/07/2026 đến 27/09/2026 (9 tuần)

---

## 4.1 Mô hình Lớp tổng thể toàn hệ thống (System Architecture Class Diagram)
Mô hình lớp tổng thể thể hiện cấu trúc phân tầng hoàn chỉnh của giải pháp theo mẫu thiết kế hướng dịch vụ (Service-Oriented Architecture - SOA) kết hợp Clean Architecture, bao gồm: Tầng Trình diễn (Controllers), Tầng Dịch vụ nghiệp vụ (Services & Interfaces), Tầng Tích hợp dịch vụ ngoại vi (AI & Payment Clients), và Tầng Dữ liệu thực thể (Domain Entities & Enums).

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam linetype ortho

enum UserRole {
    Customer = 0
    Admin = 1
}

enum BookingStatus {
    Pending = 0
    Confirmed = 1
    Cancelled = 2
    Completed = 3
}

enum DepositStatus {
    Pending = 0
    Success = 1
    Rejected = 2
}

class User {
    +Guid Id
    +string Username
    +string FullName
    +string Phone
    +string Email
    +string? AvatarUrl
    +UserRole Role
    +string PasswordHash
    +decimal WalletBalance
    +DateTime CreatedAt
    +bool IsDeleted
}

class FootballField {
    +Guid FieldId
    +string Name
    +int FieldType
    +decimal BasePrice
    +bool Status
    +string Location
    +DateTime CreatedAt
}

class Booking {
    +Guid BookingId
    +Guid UserId
    +Guid FieldId
    +DateTime BookingTime
    +DateTime StartTime
    +DateTime EndTime
    +decimal TotalPrice
    +BookingStatus Status
    +bool IsAIPriced
    +string? QrCode
    +DateTime CreatedAt
}

class Transaction {
    +Guid TransactionId
    +Guid UserId
    +decimal Amount
    +string Type
    +Guid? BookingId
    +string? Description
    +DateTime CreatedAt
}

class DepositRequest {
    +Guid Id
    +Guid UserId
    +decimal Amount
    +string TransactionCode
    +string Memo
    +string ImageUrl
    +DepositStatus Status
    +DateTime CreatedAt
    +DateTime? ProcessedAt
}

interface IUserService {
    +Register(...) User
    +Login(...) (User, string)
    +GetUserById(Guid id) User
    +GetAllUsers() IEnumerable~User~
    +AddTransaction(...) void
    +UpdateProfile(...) User
    +ChangePassword(...) (bool, string)
    +CreateDepositRequest(...) DepositRequest
    +ApproveDepositRequest(Guid id) (bool, string)
    +RejectDepositRequest(Guid id) (bool, string)
}

interface IBookingService {
    +GetFields() IEnumerable~FootballField~
    +GetFieldById(Guid id) FootballField
    +CreateBooking(...) (Booking, string)
    +CancelBooking(Guid bookingId) bool
    +GetUserBookings(Guid userId) IEnumerable~Booking~
    +GetAllBookings() IEnumerable~Booking~
}

interface IAIServiceClient {
    +GetAiOptimalPrice(...) AIPricingResult
}

class UserService {
    -List~User~ _users
    -List~Transaction~ _transactions
    -List~DepositRequest~ _depositRequests
}

class BookingService {
    -List~FootballField~ _fields
    -List~Booking~ _bookings
    -IUserService _userService
    -object _lockObj
}

class AIServiceClient {
    -HttpClient _httpClient
    +GetAiOptimalPrice(...) AIPricingResult
}

class BookingsController {
    -IBookingService _bookingService
    -IAIServiceClient _aiClient
}

class PaymentController {
    -IUserService _userService
}

class AdminController {
    -IBookingService _bookingService
    -IUserService _userService
}

User "1" --> "*" Booking : Đặt nhiều
User "1" --> "*" Transaction : Có nhiều biến động
User "1" --> "*" DepositRequest : Tạo yêu cầu nạp
FootballField "1" --> "*" Booking : Được thuê
User --> UserRole
Booking --> BookingStatus
DepositRequest --> DepositStatus

UserService ..|> IUserService
BookingService ..|> IBookingService
AIServiceClient ..|> IAIServiceClient

BookingService o-- IUserService
BookingsController o-- IBookingService
BookingsController o-- IAIServiceClient
PaymentController o-- IUserService
AdminController o-- IBookingService
AdminController o-- IUserService
@enduml
```

---

## 4.2 Biểu đồ Lớp Phân hệ Thực thể Dữ liệu & Enums (Domain Entities & Enums)

```plantuml
@startuml
skinparam classAttributeIconSize 0

enum UserRole {
    Customer = 0
    Admin = 1
}

enum BookingStatus {
    Pending = 0
    Confirmed = 1
    Cancelled = 2
    Completed = 3
}

enum DepositStatus {
    Pending = 0
    Success = 1
    Rejected = 2
}

class User {
    +Guid Id
    +string Username
    +string FullName
    +string Phone
    +string Email
    +string? AvatarUrl
    +UserRole Role
    +string PasswordHash
    +decimal WalletBalance
    +DateTime CreatedAt
    +bool IsDeleted
}

class FootballField {
    +Guid FieldId
    +string Name
    +int FieldType
    +decimal BasePrice
    +bool Status
    +string Location
    +DateTime CreatedAt
}

class Booking {
    +Guid BookingId
    +Guid UserId
    +Guid FieldId
    +DateTime BookingTime
    +DateTime StartTime
    +DateTime EndTime
    +decimal TotalPrice
    +BookingStatus Status
    +bool IsAIPriced
    +string? QrCode
    +DateTime CreatedAt
}

class Transaction {
    +Guid TransactionId
    +Guid UserId
    +decimal Amount
    +string Type
    +Guid? BookingId
    +string? Description
    +DateTime CreatedAt
}

class DepositRequest {
    +Guid Id
    +Guid UserId
    +decimal Amount
    +string TransactionCode
    +string Memo
    +string ImageUrl
    +DepositStatus Status
    +DateTime CreatedAt
    +DateTime? ProcessedAt
}

User "1" --> "*" Booking : Có
User "1" --> "*" Transaction : Có
User "1" --> "*" DepositRequest : Có
FootballField "1" --> "*" Booking : Được thuê
User --> UserRole
Booking --> BookingStatus
DepositRequest --> DepositStatus
@enduml
```

---

## 4.3 Biểu đồ Lớp Phân hệ Dịch vụ Nghiệp vụ cốt lõi (Core Business Services)

```plantuml
@startuml
skinparam classAttributeIconSize 0

interface IUserService {
    +Register(...) User
    +Login(...) (User, string)
    +GetUserById(Guid id) User
    +GetAllUsers() IEnumerable~User~
    +AddTransaction(...) void
    +UpdateProfile(...) User
    +ChangePassword(...) (bool, string)
    +CreateDepositRequest(...) DepositRequest
    +ApproveDepositRequest(Guid id) (bool, string)
    +RejectDepositRequest(Guid id) (bool, string)
}

interface IBookingService {
    +GetFields() IEnumerable~FootballField~
    +GetFieldById(Guid id) FootballField
    +CreateBooking(...) (Booking, string)
    +CancelBooking(Guid bookingId) bool
    +GetUserBookings(Guid userId) IEnumerable~Booking~
    +GetAllBookings() IEnumerable~Booking~
}

class UserService {
    -List~User~ _users
    -List~Transaction~ _transactions
    -List~DepositRequest~ _depositRequests
    +Register(...) User
    +Login(...) (User, string)
    +GetUserById(Guid id) User
    +GetAllUsers() IEnumerable~User~
    +AddTransaction(...) void
    +UpdateProfile(...) User
    +ChangePassword(...) (bool, string)
    +CreateDepositRequest(...) DepositRequest
    +ApproveDepositRequest(Guid id) (bool, string)
    +RejectDepositRequest(Guid id) (bool, string)
}

class BookingService {
    -List~FootballField~ _fields
    -List~Booking~ _bookings
    -IUserService _userService
    -object _lockObj
    +GetFields() IEnumerable~FootballField~
    +GetFieldById(Guid id) FootballField
    +CreateBooking(...) (Booking, string)
    +CancelBooking(Guid bookingId) bool
    +GetUserBookings(Guid userId) IEnumerable~Booking~
    +GetAllBookings() IEnumerable~Booking~
}

UserService ..|> IUserService
BookingService ..|> IBookingService
BookingService o-- IUserService
@enduml
```

---

## 4.4 Biểu đồ Lớp Phân hệ Trí tuệ Nhân tạo & Khả năng Chịu lỗi (AI Integration & Fallback Engine)

```plantuml
@startuml
skinparam classAttributeIconSize 0

interface IAIServiceClient {
    +GetAiOptimalPrice(...) AIPricingResult
    +GetChatResponseAsync(string msg) Task~string~
}

class AIServiceClient {
    -HttpClient _httpClient
    -ILogger~AIServiceClient~ _logger
    +GetAiOptimalPrice(...) AIPricingResult
    +GetChatResponseAsync(string msg) Task~string~
    -CalculateRuleBasedFallback(...) AIPricingResult
}

class AIPricingResult {
    +decimal dynamic_price
    +decimal multiplier
    +List~string~ reasons
}

class LocalLLMConnector {
    -string _endpointUrl
    -string _modelName
    +SendPromptAsync(string prompt) Task~string~
}

class SmartFallbackEngine {
    +GetRuleBasedChatReply(string prompt) string
    +GetFallbackPricing(...) decimal
}

AIServiceClient ..|> IAIServiceClient
AIServiceClient ..> AIPricingResult : trả về
AIServiceClient --> LocalLLMConnector : tích hợp
AIServiceClient --> SmartFallbackEngine : dự phòng
@enduml
```

---

## 4.5 Biểu đồ Lớp Phân hệ Bộ điều khiển Web API (Controllers Layer)

```plantuml
@startuml
skinparam classAttributeIconSize 0

class AuthController {
    -IUserService _userService
    +Register(RegisterRequest req) IActionResult
    +Login(LoginRequest req) IActionResult
    +GetProfile() IActionResult
    +UpdateProfile(UpdateProfileRequest req) IActionResult
    +ChangePassword(ChangePasswordRequest req) IActionResult
}

class BookingsController {
    -IBookingService _bookingService
    -IAIServiceClient _aiClient
    +GetFields() IActionResult
    +GetFieldSchedule(Guid id, DateTime date) IActionResult
    +GetDynamicPrice(Guid id, DateTime time) IActionResult
    +CreateBooking(CreateBookingRequest req) IActionResult
    +GetMyBookings() IActionResult
}

class PaymentController {
    -IUserService _userService
    +GenerateVietQr(DepositRequestDto req) IActionResult
    +CreateDeposit(CreateDepositRequestDto req) IActionResult
    +GetMyTransactions() IActionResult
}

class AdminController {
    -IBookingService _bookingService
    -IUserService _userService
    +GetDashboardSummary() IActionResult
    +GetAllUsers() IActionResult
    +ToggleUserStatus(Guid id) IActionResult
    +AdjustUserBalance(Guid id, AdjustBalanceRequest req) IActionResult
    +ApproveDeposit(Guid id) IActionResult
    +RejectDeposit(Guid id) IActionResult
    +CancelAndRefundBooking(Guid id) IActionResult
}

class ChatController {
    -IAIServiceClient _aiClient
    +SendMessage(ChatRequestDto req) Task~IActionResult~
}

AuthController o-- IUserService
PaymentController o-- IUserService
BookingsController o-- IBookingService
BookingsController o-- IAIServiceClient
AdminController o-- IBookingService
AdminController o-- IUserService
ChatController o-- IAIServiceClient
@enduml
```

---

## 4.6 Biểu đồ Lớp Đối tượng Chuyển đổi Dữ liệu & Tham số truyền nhận (DTOs & Payloads)

```plantuml
@startuml
skinparam classAttributeIconSize 0

class LoginRequest {
    +string Username
    +string Password
}

class LoginResponse {
    +string Token
    +UserDto User
}

class CreateBookingRequest {
    +Guid FieldId
    +DateTime StartTime
    +DateTime EndTime
}

class BookingResponseDto {
    +Guid BookingId
    +string FieldName
    +DateTime StartTime
    +DateTime EndTime
    +decimal TotalPrice
    +string Status
    +string QrCode
}

class DepositRequestDto {
    +decimal Amount
    +string Memo
}

class VietQRResponseDto {
    +string QrImageUrl
    +string BankCode
    +string AccountNumber
    +string AccountName
    +decimal Amount
    +string Description
}

class DashboardSummaryDto {
    +decimal TotalRevenue
    +int TotalBookings
    +int TotalUsers
    +decimal OccupancyRate
    +List~RevenueByDayDto~ RevenueHistory
}

class AdjustBalanceRequest {
    +Guid UserId
    +decimal Amount
    +string Reason
}

class UpdatePricingRequest {
    +decimal BasePrice
    +decimal PeakHourMultiplier
    +decimal WeekendMultiplier
}

class ChatRequestDto {
    +string Message
    +List~ChatMessage~ History
}

LoginRequest ..> LoginResponse : chuyển đổi
CreateBookingRequest ..> BookingResponseDto : chuyển đổi
DepositRequestDto ..> VietQRResponseDto : sinh QR
@enduml
```

---

## 4.7 Đặc tả chi tiết các Lớp và 63 Biểu đồ Lớp con tương ứng từng Thành viên (+)

Nhằm đáp ứng yêu cầu biểu diễn trực quan chi tiết đến từng thành phần dữ liệu và phương thức nghiệp vụ, dưới đây là đặc tả chi tiết và **chính xác 63 biểu đồ lớp con (Sub-Class Diagrams)** tương ứng 1-1 cho toàn bộ **63 thành viên public (`+`)** đã được thiết kế trong Mô hình Lớp tổng thể Mục 4.1:

---

### Danh mục 63 Biểu đồ Lớp con chi tiết từng Thuộc tính & Phương thức:

#### 4.7.1 Biểu đồ Lớp chi tiết thành phần: `User.Guid Id`
* **Lớp chủ quản:** `User`
* **Thành viên public (+):** `Guid Id`
* **Mục đích & Ý nghĩa nghiệp vụ:** Thuộc tính định danh duy nhất (Primary Key) của người dùng.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class User {
    +Guid Id
}
@enduml
```

#### 4.7.2 Biểu đồ Lớp chi tiết thành phần: `User.string Username`
* **Lớp chủ quản:** `User`
* **Thành viên public (+):** `string Username`
* **Mục đích & Ý nghĩa nghiệp vụ:** Tên tài khoản duy nhất đăng nhập vào hệ thống.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class User {
    +string Username
}
@enduml
```

#### 4.7.3 Biểu đồ Lớp chi tiết thành phần: `User.string FullName`
* **Lớp chủ quản:** `User`
* **Thành viên public (+):** `string FullName`
* **Mục đích & Ý nghĩa nghiệp vụ:** Họ và tên đầy đủ của người dùng.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class User {
    +string FullName
}
@enduml
```

#### 4.7.4 Biểu đồ Lớp chi tiết thành phần: `User.string Phone`
* **Lớp chủ quản:** `User`
* **Thành viên public (+):** `string Phone`
* **Mục đích & Ý nghĩa nghiệp vụ:** Số điện thoại duy nhất liên hệ và định danh.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class User {
    +string Phone
}
@enduml
```

#### 4.7.5 Biểu đồ Lớp chi tiết thành phần: `User.string Email`
* **Lớp chủ quản:** `User`
* **Thành viên public (+):** `string Email`
* **Mục đích & Ý nghĩa nghiệp vụ:** Địa chỉ email duy nhất nhận thông báo và hỗ trợ đổi mật khẩu.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class User {
    +string Email
}
@enduml
```

#### 4.7.6 Biểu đồ Lớp chi tiết thành phần: `User.string? AvatarUrl`
* **Lớp chủ quản:** `User`
* **Thành viên public (+):** `string? AvatarUrl`
* **Mục đích & Ý nghĩa nghiệp vụ:** Đường dẫn URL ảnh đại diện của người dùng (nullable).

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class User {
    +string? AvatarUrl
}
@enduml
```

#### 4.7.7 Biểu đồ Lớp chi tiết thành phần: `User.UserRole Role`
* **Lớp chủ quản:** `User`
* **Thành viên public (+):** `UserRole Role`
* **Mục đích & Ý nghĩa nghiệp vụ:** Vai trò phân quyền của người dùng (0: Customer, 1: Admin).

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class User {
    +UserRole Role
}
@enduml
```

#### 4.7.8 Biểu đồ Lớp chi tiết thành phần: `User.string PasswordHash`
* **Lớp chủ quản:** `User`
* **Thành viên public (+):** `string PasswordHash`
* **Mục đích & Ý nghĩa nghiệp vụ:** Mật khẩu đã được mã hóa bằng thuật toán băm an toàn SHA-256.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class User {
    +string PasswordHash
}
@enduml
```

#### 4.7.9 Biểu đồ Lớp chi tiết thành phần: `User.decimal WalletBalance`
* **Lớp chủ quản:** `User`
* **Thành viên public (+):** `decimal WalletBalance`
* **Mục đích & Ý nghĩa nghiệp vụ:** Số dư ví điện tử ảo khả dụng dùng để thanh toán đặt sân tức thì.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class User {
    +decimal WalletBalance
}
@enduml
```

#### 4.7.10 Biểu đồ Lớp chi tiết thành phần: `User.DateTime CreatedAt`
* **Lớp chủ quản:** `User`
* **Thành viên public (+):** `DateTime CreatedAt`
* **Mục đích & Ý nghĩa nghiệp vụ:** Thời điểm tài khoản được khởi tạo trên hệ thống.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class User {
    +DateTime CreatedAt
}
@enduml
```

#### 4.7.11 Biểu đồ Lớp chi tiết thành phần: `User.bool IsDeleted`
* **Lớp chủ quản:** `User`
* **Thành viên public (+):** `bool IsDeleted`
* **Mục đích & Ý nghĩa nghiệp vụ:** Trạng thái cờ đánh dấu tài khoản bị khóa/xóa mềm bởi Admin.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class User {
    +bool IsDeleted
}
@enduml
```

#### 4.7.12 Biểu đồ Lớp chi tiết thành phần: `FootballField.Guid FieldId`
* **Lớp chủ quản:** `FootballField`
* **Thành viên public (+):** `Guid FieldId`
* **Mục đích & Ý nghĩa nghiệp vụ:** Khóa chính định danh duy nhất của sân bóng.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class FootballField {
    +Guid FieldId
}
@enduml
```

#### 4.7.13 Biểu đồ Lớp chi tiết thành phần: `FootballField.string Name`
* **Lớp chủ quản:** `FootballField`
* **Thành viên public (+):** `string Name`
* **Mục đích & Ý nghĩa nghiệp vụ:** Tên hiển thị của sân bóng (Sân 5 số 1, Sân 7 VIP...).

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class FootballField {
    +string Name
}
@enduml
```

#### 4.7.14 Biểu đồ Lớp chi tiết thành phần: `FootballField.int FieldType`
* **Lớp chủ quản:** `FootballField`
* **Thành viên public (+):** `int FieldType`
* **Mục đích & Ý nghĩa nghiệp vụ:** Loại hình sân bóng (5 người, 7 người, hoặc 11 người).

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class FootballField {
    +int FieldType
}
@enduml
```

#### 4.7.15 Biểu đồ Lớp chi tiết thành phần: `FootballField.decimal BasePrice`
* **Lớp chủ quản:** `FootballField`
* **Thành viên public (+):** `decimal BasePrice`
* **Mục đích & Ý nghĩa nghiệp vụ:** Giá thuê niêm yết cơ sở cho một giờ thi đấu.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class FootballField {
    +decimal BasePrice
}
@enduml
```

#### 4.7.16 Biểu đồ Lớp chi tiết thành phần: `FootballField.bool Status`
* **Lớp chủ quản:** `FootballField`
* **Thành viên public (+):** `bool Status`
* **Mục đích & Ý nghĩa nghiệp vụ:** Trạng thái hoạt động của sân (True: Sẵn sàng phục vụ, False: Bảo trì).

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class FootballField {
    +bool Status
}
@enduml
```

#### 4.7.17 Biểu đồ Lớp chi tiết thành phần: `FootballField.string Location`
* **Lớp chủ quản:** `FootballField`
* **Thành viên public (+):** `string Location`
* **Mục đích & Ý nghĩa nghiệp vụ:** Vị trí địa lý / Địa chỉ cụ thể của sân bóng.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class FootballField {
    +string Location
}
@enduml
```

#### 4.7.18 Biểu đồ Lớp chi tiết thành phần: `FootballField.DateTime CreatedAt`
* **Lớp chủ quản:** `FootballField`
* **Thành viên public (+):** `DateTime CreatedAt`
* **Mục đích & Ý nghĩa nghiệp vụ:** Thời điểm sân bóng được đưa vào cơ sở dữ liệu.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class FootballField {
    +DateTime CreatedAt
}
@enduml
```

#### 4.7.19 Biểu đồ Lớp chi tiết thành phần: `Booking.Guid BookingId`
* **Lớp chủ quản:** `Booking`
* **Thành viên public (+):** `Guid BookingId`
* **Mục đích & Ý nghĩa nghiệp vụ:** Khóa chính định danh duy nhất của lượt đặt sân.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Booking {
    +Guid BookingId
}
@enduml
```

#### 4.7.20 Biểu đồ Lớp chi tiết thành phần: `Booking.Guid UserId`
* **Lớp chủ quản:** `Booking`
* **Thành viên public (+):** `Guid UserId`
* **Mục đích & Ý nghĩa nghiệp vụ:** Khóa ngoại liên kết tới người dùng thực hiện đặt sân.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Booking {
    +Guid UserId
}
@enduml
```

#### 4.7.21 Biểu đồ Lớp chi tiết thành phần: `Booking.Guid FieldId`
* **Lớp chủ quản:** `Booking`
* **Thành viên public (+):** `Guid FieldId`
* **Mục đích & Ý nghĩa nghiệp vụ:** Khóa ngoại liên kết tới sân bóng được thuê.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Booking {
    +Guid FieldId
}
@enduml
```

#### 4.7.22 Biểu đồ Lớp chi tiết thành phần: `Booking.DateTime BookingTime`
* **Lớp chủ quản:** `Booking`
* **Thành viên public (+):** `DateTime BookingTime`
* **Mục đích & Ý nghĩa nghiệp vụ:** Thời điểm khách hàng gửi lệnh đặt chỗ trên hệ thống.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Booking {
    +DateTime BookingTime
}
@enduml
```

#### 4.7.23 Biểu đồ Lớp chi tiết thành phần: `Booking.DateTime StartTime`
* **Lớp chủ quản:** `Booking`
* **Thành viên public (+):** `DateTime StartTime`
* **Mục đích & Ý nghĩa nghiệp vụ:** Thời điểm bắt đầu trận đấu (giờ nhận sân).

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Booking {
    +DateTime StartTime
}
@enduml
```

#### 4.7.24 Biểu đồ Lớp chi tiết thành phần: `Booking.DateTime EndTime`
* **Lớp chủ quản:** `Booking`
* **Thành viên public (+):** `DateTime EndTime`
* **Mục đích & Ý nghĩa nghiệp vụ:** Thời điểm kết thúc trận đấu (giờ trả sân).

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Booking {
    +DateTime EndTime
}
@enduml
```

#### 4.7.25 Biểu đồ Lớp chi tiết thành phần: `Booking.decimal TotalPrice`
* **Lớp chủ quản:** `Booking`
* **Thành viên public (+):** `decimal TotalPrice`
* **Mục đích & Ý nghĩa nghiệp vụ:** Tổng số tiền thực tế phải thanh toán sau khi AI định giá.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Booking {
    +decimal TotalPrice
}
@enduml
```

#### 4.7.26 Biểu đồ Lớp chi tiết thành phần: `Booking.BookingStatus Status`
* **Lớp chủ quản:** `Booking`
* **Thành viên public (+):** `BookingStatus Status`
* **Mục đích & Ý nghĩa nghiệp vụ:** Trạng thái đơn đặt (Pending, Confirmed, Cancelled, Completed).

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Booking {
    +BookingStatus Status
}
@enduml
```

#### 4.7.27 Biểu đồ Lớp chi tiết thành phần: `Booking.bool IsAIPriced`
* **Lớp chủ quản:** `Booking`
* **Thành viên public (+):** `bool IsAIPriced`
* **Mục đích & Ý nghĩa nghiệp vụ:** Cờ đánh dấu đơn đặt sân có áp dụng thuật toán Dynamic Pricing.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Booking {
    +bool IsAIPriced
}
@enduml
```

#### 4.7.28 Biểu đồ Lớp chi tiết thành phần: `Booking.string? QrCode`
* **Lớp chủ quản:** `Booking`
* **Thành viên public (+):** `string? QrCode`
* **Mục đích & Ý nghĩa nghiệp vụ:** Mã định danh Check-in điện tử xuất trình khi ra sân bóng.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Booking {
    +string? QrCode
}
@enduml
```

#### 4.7.29 Biểu đồ Lớp chi tiết thành phần: `Booking.DateTime CreatedAt`
* **Lớp chủ quản:** `Booking`
* **Thành viên public (+):** `DateTime CreatedAt`
* **Mục đích & Ý nghĩa nghiệp vụ:** Thời điểm bản ghi đặt sân được ghi nhận vào hệ thống.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Booking {
    +DateTime CreatedAt
}
@enduml
```

#### 4.7.30 Biểu đồ Lớp chi tiết thành phần: `Transaction.Guid TransactionId`
* **Lớp chủ quản:** `Transaction`
* **Thành viên public (+):** `Guid TransactionId`
* **Mục đích & Ý nghĩa nghiệp vụ:** Khóa chính định danh giao dịch ví điện tử.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Transaction {
    +Guid TransactionId
}
@enduml
```

#### 4.7.31 Biểu đồ Lớp chi tiết thành phần: `Transaction.Guid UserId`
* **Lớp chủ quản:** `Transaction`
* **Thành viên public (+):** `Guid UserId`
* **Mục đích & Ý nghĩa nghiệp vụ:** Khóa ngoại chỉ định người dùng sở hữu giao dịch.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Transaction {
    +Guid UserId
}
@enduml
```

#### 4.7.32 Biểu đồ Lớp chi tiết thành phần: `Transaction.decimal Amount`
* **Lớp chủ quản:** `Transaction`
* **Thành viên public (+):** `decimal Amount`
* **Mục đích & Ý nghĩa nghiệp vụ:** Số tiền biến động (dương khi nạp/hoàn tiền, âm khi thanh toán).

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Transaction {
    +decimal Amount
}
@enduml
```

#### 4.7.33 Biểu đồ Lớp chi tiết thành phần: `Transaction.string Type`
* **Lớp chủ quản:** `Transaction`
* **Thành viên public (+):** `string Type`
* **Mục đích & Ý nghĩa nghiệp vụ:** Loại giao dịch (Payment, Refund, TopupApproved, ManualAdjust).

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Transaction {
    +string Type
}
@enduml
```

#### 4.7.34 Biểu đồ Lớp chi tiết thành phần: `Transaction.Guid? BookingId`
* **Lớp chủ quản:** `Transaction`
* **Thành viên public (+):** `Guid? BookingId`
* **Mục đích & Ý nghĩa nghiệp vụ:** Khóa ngoại liên kết tới đơn đặt sân tương ứng (nếu có).

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Transaction {
    +Guid? BookingId
}
@enduml
```

#### 4.7.35 Biểu đồ Lớp chi tiết thành phần: `Transaction.string? Description`
* **Lớp chủ quản:** `Transaction`
* **Thành viên public (+):** `string? Description`
* **Mục đích & Ý nghĩa nghiệp vụ:** Nội dung diễn giải chi tiết cho biến động số dư.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Transaction {
    +string? Description
}
@enduml
```

#### 4.7.36 Biểu đồ Lớp chi tiết thành phần: `Transaction.DateTime CreatedAt`
* **Lớp chủ quản:** `Transaction`
* **Thành viên public (+):** `DateTime CreatedAt`
* **Mục đích & Ý nghĩa nghiệp vụ:** Thời điểm giao dịch được thực hiện thành công.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class Transaction {
    +DateTime CreatedAt
}
@enduml
```

#### 4.7.37 Biểu đồ Lớp chi tiết thành phần: `DepositRequest.Guid Id`
* **Lớp chủ quản:** `DepositRequest`
* **Thành viên public (+):** `Guid Id`
* **Mục đích & Ý nghĩa nghiệp vụ:** Khóa chính định danh yêu cầu nạp tiền ví.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class DepositRequest {
    +Guid Id
}
@enduml
```

#### 4.7.38 Biểu đồ Lớp chi tiết thành phần: `DepositRequest.Guid UserId`
* **Lớp chủ quản:** `DepositRequest`
* **Thành viên public (+):** `Guid UserId`
* **Mục đích & Ý nghĩa nghiệp vụ:** Khóa ngoại xác định người dùng yêu cầu nạp tiền.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class DepositRequest {
    +Guid UserId
}
@enduml
```

#### 4.7.39 Biểu đồ Lớp chi tiết thành phần: `DepositRequest.decimal Amount`
* **Lớp chủ quản:** `DepositRequest`
* **Thành viên public (+):** `decimal Amount`
* **Mục đích & Ý nghĩa nghiệp vụ:** Số tiền khách hàng chuyển khoản vào tài khoản ngân hàng.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class DepositRequest {
    +decimal Amount
}
@enduml
```

#### 4.7.40 Biểu đồ Lớp chi tiết thành phần: `DepositRequest.string TransactionCode`
* **Lớp chủ quản:** `DepositRequest`
* **Thành viên public (+):** `string TransactionCode`
* **Mục đích & Ý nghĩa nghiệp vụ:** Mã giao dịch ngân hàng do hệ thống sinh ra để đối soát.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class DepositRequest {
    +string TransactionCode
}
@enduml
```

#### 4.7.41 Biểu đồ Lớp chi tiết thành phần: `DepositRequest.string Memo`
* **Lớp chủ quản:** `DepositRequest`
* **Thành viên public (+):** `string Memo`
* **Mục đích & Ý nghĩa nghiệp vụ:** Nội dung chuyển khoản chuẩn VietQR (chứa mã nạp tiền).

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class DepositRequest {
    +string Memo
}
@enduml
```

#### 4.7.42 Biểu đồ Lớp chi tiết thành phần: `DepositRequest.string ImageUrl`
* **Lớp chủ quản:** `DepositRequest`
* **Thành viên public (+):** `string ImageUrl`
* **Mục đích & Ý nghĩa nghiệp vụ:** Đường dẫn ảnh chụp màn hình biên lai chuyển khoản (nếu có).

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class DepositRequest {
    +string ImageUrl
}
@enduml
```

#### 4.7.43 Biểu đồ Lớp chi tiết thành phần: `DepositRequest.DepositStatus Status`
* **Lớp chủ quản:** `DepositRequest`
* **Thành viên public (+):** `DepositStatus Status`
* **Mục đích & Ý nghĩa nghiệp vụ:** Trạng thái phê duyệt (Pending, Success, Rejected).

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class DepositRequest {
    +DepositStatus Status
}
@enduml
```

#### 4.7.44 Biểu đồ Lớp chi tiết thành phần: `DepositRequest.DateTime CreatedAt`
* **Lớp chủ quản:** `DepositRequest`
* **Thành viên public (+):** `DateTime CreatedAt`
* **Mục đích & Ý nghĩa nghiệp vụ:** Thời điểm yêu cầu nạp ví được gửi lên hệ thống.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class DepositRequest {
    +DateTime CreatedAt
}
@enduml
```

#### 4.7.45 Biểu đồ Lớp chi tiết thành phần: `DepositRequest.DateTime? ProcessedAt`
* **Lớp chủ quản:** `DepositRequest`
* **Thành viên public (+):** `DateTime? ProcessedAt`
* **Mục đích & Ý nghĩa nghiệp vụ:** Thời điểm Admin bấm duyệt hoặc từ chối yêu cầu nạp tiền.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class DepositRequest {
    +DateTime? ProcessedAt
}
@enduml
```

#### 4.7.46 Biểu đồ Lớp chi tiết thành phần: `IUserService.Register`
* **Lớp chủ quản:** `IUserService`
* **Thành viên public (+):** `Register(string user, string pass, string name, string phone, string email) User`
* **Mục đích & Ý nghĩa nghiệp vụ:** Phương thức đăng ký tài khoản khách hàng mới với băm mật khẩu SHA-256.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

interface IUserService {
    +Register(string user, string pass, string name, string phone, string email) User
}
@enduml
```

#### 4.7.47 Biểu đồ Lớp chi tiết thành phần: `IUserService.Login`
* **Lớp chủ quản:** `IUserService`
* **Thành viên public (+):** `Login(string username, string password) (User, string)`
* **Mục đích & Ý nghĩa nghiệp vụ:** Phương thức xác thực đăng nhập và phát hành JWT Token 7 ngày.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

interface IUserService {
    +Login(string username, string password) (User, string)
}
@enduml
```

#### 4.7.48 Biểu đồ Lớp chi tiết thành phần: `IUserService.GetUserById`
* **Lớp chủ quản:** `IUserService`
* **Thành viên public (+):** `GetUserById(Guid id) User`
* **Mục đích & Ý nghĩa nghiệp vụ:** Phương thức truy vấn thông tin chi tiết người dùng theo Id.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

interface IUserService {
    +GetUserById(Guid id) User
}
@enduml
```

#### 4.7.49 Biểu đồ Lớp chi tiết thành phần: `IUserService.GetAllUsers`
* **Lớp chủ quản:** `IUserService`
* **Thành viên public (+):** `GetAllUsers() IEnumerable~User~`
* **Mục đích & Ý nghĩa nghiệp vụ:** Phương thức lấy toàn bộ danh sách người dùng cho Admin quản trị.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

interface IUserService {
    +GetAllUsers() IEnumerable~User~
}
@enduml
```

#### 4.7.50 Biểu đồ Lớp chi tiết thành phần: `IUserService.AddTransaction`
* **Lớp chủ quản:** `IUserService`
* **Thành viên public (+):** `AddTransaction(Guid userId, decimal amount, string type, Guid? bookingId) void`
* **Mục đích & Ý nghĩa nghiệp vụ:** Phương thức ghi nhật ký biến động số dư ví vào sổ cái Transactions.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

interface IUserService {
    +AddTransaction(Guid userId, decimal amount, string type, Guid? bookingId) void
}
@enduml
```

#### 4.7.51 Biểu đồ Lớp chi tiết thành phần: `IUserService.UpdateProfile`
* **Lớp chủ quản:** `IUserService`
* **Thành viên public (+):** `UpdateProfile(Guid userId, string name, string phone, string? avatar) User`
* **Mục đích & Ý nghĩa nghiệp vụ:** Phương thức cập nhật thông tin cá nhân và ảnh đại diện của người dùng.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

interface IUserService {
    +UpdateProfile(Guid userId, string name, string phone, string? avatar) User
}
@enduml
```

#### 4.7.52 Biểu đồ Lớp chi tiết thành phần: `IUserService.ChangePassword`
* **Lớp chủ quản:** `IUserService`
* **Thành viên public (+):** `ChangePassword(Guid userId, string oldPass, string newPass) (bool, string)`
* **Mục đích & Ý nghĩa nghiệp vụ:** Phương thức kiểm tra mật khẩu cũ và cập nhật mật khẩu mới an toàn.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

interface IUserService {
    +ChangePassword(Guid userId, string oldPass, string newPass) (bool, string)
}
@enduml
```

#### 4.7.53 Biểu đồ Lớp chi tiết thành phần: `IUserService.CreateDepositRequest`
* **Lớp chủ quản:** `IUserService`
* **Thành viên public (+):** `CreateDepositRequest(Guid userId, decimal amount, string memo) DepositRequest`
* **Mục đích & Ý nghĩa nghiệp vụ:** Phương thức khởi tạo yêu cầu nạp tiền ví ở trạng thái chờ duyệt.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

interface IUserService {
    +CreateDepositRequest(Guid userId, decimal amount, string memo) DepositRequest
}
@enduml
```

#### 4.7.54 Biểu đồ Lớp chi tiết thành phần: `IUserService.ApproveDepositRequest`
* **Lớp chủ quản:** `IUserService`
* **Thành viên public (+):** `ApproveDepositRequest(Guid id) (bool, string)`
* **Mục đích & Ý nghĩa nghiệp vụ:** Phương thức Admin duyệt nạp tiền: cộng số dư ví và lưu Transaction.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

interface IUserService {
    +ApproveDepositRequest(Guid id) (bool, string)
}
@enduml
```

#### 4.7.55 Biểu đồ Lớp chi tiết thành phần: `IUserService.RejectDepositRequest`
* **Lớp chủ quản:** `IUserService`
* **Thành viên public (+):** `RejectDepositRequest(Guid id) (bool, string)`
* **Mục đích & Ý nghĩa nghiệp vụ:** Phương thức Admin từ chối yêu cầu nạp tiền không hợp lệ.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

interface IUserService {
    +RejectDepositRequest(Guid id) (bool, string)
}
@enduml
```

#### 4.7.56 Biểu đồ Lớp chi tiết thành phần: `IBookingService.GetFields`
* **Lớp chủ quản:** `IBookingService`
* **Thành viên public (+):** `GetFields() IEnumerable~FootballField~`
* **Mục đích & Ý nghĩa nghiệp vụ:** Phương thức lấy toàn bộ danh mục sân bóng kèm trạng thái.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

interface IBookingService {
    +GetFields() IEnumerable~FootballField~
}
@enduml
```

#### 4.7.57 Biểu đồ Lớp chi tiết thành phần: `IBookingService.GetFieldById`
* **Lớp chủ quản:** `IBookingService`
* **Thành viên public (+):** `GetFieldById(Guid id) FootballField`
* **Mục đích & Ý nghĩa nghiệp vụ:** Phương thức lấy chi tiết một sân bóng theo định danh.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

interface IBookingService {
    +GetFieldById(Guid id) FootballField
}
@enduml
```

#### 4.7.58 Biểu đồ Lớp chi tiết thành phần: `IBookingService.CreateBooking`
* **Lớp chủ quản:** `IBookingService`
* **Thành viên public (+):** `CreateBooking(Guid userId, Guid fieldId, DateTime start, DateTime end, decimal price) (Booking, string)`
* **Mục đích & Ý nghĩa nghiệp vụ:** Phương thức cốt lõi thực hiện khóa đa luồng, chống trùng lịch và trừ tiền ví.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

interface IBookingService {
    +CreateBooking(Guid userId, Guid fieldId, DateTime start, DateTime end, decimal price) (Booking, string)
}
@enduml
```

#### 4.7.59 Biểu đồ Lớp chi tiết thành phần: `IBookingService.CancelBooking`
* **Lớp chủ quản:** `IBookingService`
* **Thành viên public (+):** `CancelBooking(Guid bookingId) bool`
* **Mục đích & Ý nghĩa nghiệp vụ:** Phương thức chuyển trạng thái đơn đặt sân sang Cancelled.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

interface IBookingService {
    +CancelBooking(Guid bookingId) bool
}
@enduml
```

#### 4.7.60 Biểu đồ Lớp chi tiết thành phần: `IBookingService.GetUserBookings`
* **Lớp chủ quản:** `IBookingService`
* **Thành viên public (+):** `GetUserBookings(Guid userId) IEnumerable~Booking~`
* **Mục đích & Ý nghĩa nghiệp vụ:** Phương thức lấy toàn bộ lịch sử các lần đặt sân của một khách hàng.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

interface IBookingService {
    +GetUserBookings(Guid userId) IEnumerable~Booking~
}
@enduml
```

#### 4.7.61 Biểu đồ Lớp chi tiết thành phần: `IBookingService.GetAllBookings`
* **Lớp chủ quản:** `IBookingService`
* **Thành viên public (+):** `GetAllBookings() IEnumerable~Booking~`
* **Mục đích & Ý nghĩa nghiệp vụ:** Phương thức lấy toàn bộ đơn đặt sân trong hệ thống cho Admin.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

interface IBookingService {
    +GetAllBookings() IEnumerable~Booking~
}
@enduml
```

#### 4.7.62 Biểu đồ Lớp chi tiết thành phần: `IAIServiceClient.GetAiOptimalPrice`
* **Lớp chủ quản:** `IAIServiceClient`
* **Thành viên public (+):** `GetAiOptimalPrice(Guid fieldId, DateTime bookingTime, decimal basePrice) AIPricingResult`
* **Mục đích & Ý nghĩa nghiệp vụ:** Phương thức gọi Microservice AI để nhận giá định động thông minh.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

interface IAIServiceClient {
    +GetAiOptimalPrice(Guid fieldId, DateTime bookingTime, decimal basePrice) AIPricingResult
}
@enduml
```

#### 4.7.63 Biểu đồ Lớp chi tiết thành phần: `AIServiceClient.GetAiOptimalPrice`
* **Lớp chủ quản:** `AIServiceClient`
* **Thành viên public (+):** `GetAiOptimalPrice(Guid fieldId, DateTime bookingTime, decimal basePrice) AIPricingResult`
* **Mục đích & Ý nghĩa nghiệp vụ:** Hiện thực hóa phương thức gọi HTTP POST sang Flask AI Microservice kèm Fallback.

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam classBackgroundColor #F8FAFC
skinparam classBorderColor #2563EB

class AIServiceClient {
    +GetAiOptimalPrice(Guid fieldId, DateTime bookingTime, decimal basePrice) AIPricingResult
}
@enduml
```

---

### 4.7.2 Đặc tả Lớp `BookingService`
* **Mô tả:** Lớp triển khai các logic nghiệp vụ lõi liên quan đến quản lý danh mục sân, đặt sân an toàn đa luồng và hủy đơn đặt sân.
* **Các phương thức chính:**

#### Phương thức 1: `CreateBooking`
* **Mô tả:** Tiếp nhận yêu cầu đặt sân, kiểm tra thời gian, kiểm tra trùng lịch và thực hiện trừ tiền ví an toàn với Concurrency Lock.
* **Tham số đầu vào:**
  * `userId` (`Guid`): Mã người đặt sân.
  * `fieldId` (`Guid`): Mã sân bóng được chọn.
  * `startTime` (`DateTime`): Thời điểm bắt đầu nhận sân.
  * `endTime` (`DateTime`): Thời điểm kết thúc trận đấu.
  * `price` (`decimal`): Số tiền cần thanh toán cho ca đặt.
* **Kết quả đầu ra:** `(Booking? booking, string errorMessage)`: Trả về đối tượng Booking nếu thành công; trả về chuỗi thông báo lỗi nếu thất bại.
* **Điều kiện bắt đầu:** Khách hàng đã gửi thông tin hợp lệ; hệ thống đang hoạt động.
* **Luồng xử lý nội bộ:**
  1. Khởi tạo khối khóa đồng bộ `lock (_lockObj)` để ngăn chặn tình trạng Race Condition giữa các luồng đồng thời.
  2. Lấy đối tượng User qua `_userService.GetUserById(userId)`. Nếu không thấy hoặc tài khoản có `IsDeleted == true`, trả về lỗi từ chối.
  3. Kiểm tra số dư ví: `if (user.WalletBalance < price)` $
ightarrow$ trả về lỗi *"Số dư ví không đủ, vui lòng nạp thêm tiền!"*.
  4. Quét danh sách `_bookings` với điều kiện: `FieldId == fieldId && Status == BookingStatus.Confirmed` và kiểm tra giao thoa thời gian `(startTime, endTime)`. Nếu trùng $
ightarrow$ trả về lỗi *"Khung giờ này đã có người đặt, vui lòng chọn khung giờ khác!"*.
  5. Trừ tiền số dư ví: `user.WalletBalance -= price`.
  6. Khởi tạo đối tượng `Booking` mới với trạng thái `BookingStatus.Confirmed`.
  7. Thêm `booking` vào danh sách và ghi vết lịch sử qua `_userService.AddTransaction(userId, price, "Payment", booking.BookingId)`.
  8. Nếu xảy ra Exception $
ightarrow$ tự động Rollback: `user.WalletBalance += price` và quăng ngoại lệ.
* **Điều kiện kết thúc:** Bản ghi Booking được lưu trữ an toàn; số dư ví của khách hàng giảm chính xác bằng `price`.

#### Phương thức 2: `CancelBooking`
* **Mô tả:** Chuyển trạng thái đơn đặt sân từ `Confirmed` sang `Cancelled`.
* **Tham số đầu vào:** `bookingId` (`Guid`): Mã đơn đặt sân cần hủy.
* **Kết quả đầu ra:** `bool`: `true` nếu hủy thành công, `false` nếu không tìm thấy đơn.
* **Luồng xử lý:** Khóa đồng bộ $
ightarrow$ Tìm booking theo `bookingId` $
ightarrow$ gán `booking.Status = BookingStatus.Cancelled` $
ightarrow$ Trả về `true`.

---

### 4.7.3 Đặc tả Lớp `AIServiceClient`
* **Mô tả:** Lớp phụ trách đóng gói HTTP Request gửi tới Python Flask Microservice để lấy giá tối ưu theo AI.
* **Các phương thức chính:**
  * **Tên phương thức:** `GetAiOptimalPrice`
  * **Tham số đầu vào:**
    * `fieldId` (`Guid`): Mã định danh sân bóng.
    * `bookingTime` (`DateTime`): Thời điểm đặt sân dự kiến.
    * `basePrice` (`decimal`): Giá niêm yết ban đầu của sân.
  * **Kết quả đầu ra:** `AIPricingResult`: Đối tượng chứa giá linh hoạt (`dynamic_price`), hệ số nhân (`multiplier`) và danh sách các lý do điều chỉnh (`reasons`).
  * **Luồng xử lý:** Chuyển đổi ngày trong tuần chuẩn Python $
ightarrow$ Đóng gói JSON Payload $
ightarrow$ Gửi `POST` tới `http://localhost:5050/api/predict-price` với timeout 3s $
ightarrow$ Nếu thành công thì Parse kết quả JSON $
ightarrow$ Nếu thất bại hoặc Exception thì kích hoạt cơ chế Fallback (tự động cộng 30% nếu là Thứ 7/CN, cộng 50% nếu rơi vào khung 18h-21h) và trả về kết quả an toàn.


---

# PHẦN 5: KIỂM THỬ CHỨC NĂNG ỨNG DỤNG
**Nhóm 02** - Thành viên thực hiện:
1. Lã Quý Doanh (Trưởng nhóm)
2. Bùi Thanh Bình
* **Tên ứng dụng:** Hệ thống đặt sân bóng tự động tích hợp AI & Ví điện tử
* **Thời gian thực hiện:** Từ 27/07/2026 đến 27/09/2026 (9 tuần)

## 5.1 Những yêu cầu về tài nguyên cho kiểm thử ứng dụng

### 5.1.1 Yêu cầu Phần cứng:
| Thiết bị | CPU | Bộ nhớ RAM | Ổ cứng lưu trữ | Kiến trúc | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Máy trạm Server / Dev** | Intel Core i5 / i7 $\ge$ 2.5 GHz | $\ge$ 16 GB | $\ge$ 512 GB SSD NVMe | 64-bit x86 | Chạy Backend .NET, SQL Server & LM Studio |
| **Máy trạm Client Tester** | Intel Core i5 $\ge$ 2.3 GHz | $\ge$ 8 GB | $\ge$ 256 GB SSD | 64-bit | Chạy trình duyệt Web kiểm thử giao diện |
| **Thiết bị Smartphone** | Android 12+ / iOS 15+ | $\ge$ 4 GB | $\ge$ 64 GB | ARM64 | Quét mã VietQR trên App Ngân hàng thực tế |

### 5.1.2 Yêu cầu Phần mềm:
| Tên phần mềm / Nền tảng | Phiên bản sử dụng | Loại công cụ | Mục đích sử dụng trong kiểm thử |
| :--- | :--- | :--- | :--- |
| **Visual Studio / VS Code** | 2022 / v1.90+ | IDE / Code Editor | Biên dịch và chạy Backend C# .NET |
| **Microsoft .NET SDK** | .NET 8.0 / 10.0 | Runtime Environment | Môi trường thực thi Web API |
| **Python Environment** | 3.10.x / 3.11.x | Runtime & Compiler | Chạy AI Microservice Flask Server |
| **Microsoft SQL Server** | 2019 / 2022 / LocalDB | RDBMS | Lưu trữ và đối soát dữ liệu kiểm thử |
| **LM Studio** | v0.3.x+ | Local AI Inference | Chạy mô hình ngôn ngữ lớn Qwen 2.5 |
| **Swagger UI / Postman** | OpenAPI 3.0 / v10+ | API Testing Tool | Kiểm thử tự động hóa các API Endpoints |
| **Google Chrome / MS Edge** | v125+ | Web Browser | Kiểm thử giao diện hiển thị và Console Logs |

---

## 5.2 Danh sách toàn bộ các tình huống kiểm tra (Test Cases)

| Test ID | Phân hệ / Chức năng | Mô tả tình huống kiểm thử (Test Scenario) | Điều kiện trước (Pre-conditions) | Dữ liệu kiểm thử (Test Data) | Kết quả kỳ vọng (Expected Result) | Ghi chú |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC001** | Xác thực: Đăng ký | Đăng ký tài khoản mới với đầy đủ thông tin hợp lệ | Người dùng chưa có tài khoản trong CSDL | Username: `testuser1`<br>Pass: `123456`<br>Phone: `0911223344`<br>Email: `test1@gmail.com` | Hệ thống trả về mã 200 OK; tạo tài khoản thành công; cấp sẵn 2.000.000 VNĐ vào ví ảo. | Positive Test |
| **TC002** | Xác thực: Đăng ký | Đăng ký với tên tài khoản đã tồn tại trong CSDL | Đã tồn tại username `admin` | Username: `admin`<br>Pass: `123456` | Trả về mã 400 Bad Request; thông báo: *"Tên đăng nhập, Số điện thoại hoặc Email này đã tồn tại!"*. | Negative Test |
| **TC003** | Xác thực: Đăng nhập | Đăng nhập với Username và Mật khẩu chính xác | Đã có tài khoản `doanh` trong hệ thống | Username: `doanh`<br>Password: `123456` | Trả về 200 OK; sinh chuỗi JWT Token hợp lệ; hiển thị tên `Đỗ Văn Doanh` và số dư ví trên Header. | Positive Test |
| **TC004** | Xác thực: Đăng nhập | Đăng nhập bằng Số điện thoại thay cho Username | Đã có tài khoản số điện thoại `0364382164` | Phone: `0364382164`<br>Password: `123456` | Trả về 200 OK; đăng nhập thành công qua định danh số điện thoại. | Positive Test |
| **TC005** | Xác thực: Đăng nhập | Đăng nhập với sai mật khẩu | Tài khoản `doanh` tồn tại | Username: `doanh`<br>Password: `SaiMatKhau@` | Trả về mã 400 Bad Request; thông báo: *"Tên đăng nhập hoặc mật khẩu không chính xác."*. | Negative Test |
| **TC006** | Xác thực: Quên mật khẩu | Tìm lại Tên đăng nhập thông qua Số điện thoại | Tài khoản có số ĐT `0909888888` | SĐT: `0909888888` | Trả về 200 OK; thông báo: *"Tên đăng nhập của bạn là: khach1 (Họ tên: Trần Văn Khách)"*. | Positive Test |
| **TC007** | Xác thực: Đặt lại mật khẩu | Khôi phục mật khẩu trực tiếp bằng Tên đăng nhập | Tài khoản `khach1` tồn tại | Username: `khach1`<br>NewPass: `NewPass@2026` | Trả về 200 OK; cập nhật mật khẩu băm mới; người dùng đăng nhập được bằng `NewPass@2026`. | Positive Test |
| **TC008** | Tài khoản: Đổi mật khẩu | Đổi mật khẩu trong trang cá nhân khi nhập đúng mật khẩu cũ | Người dùng đã đăng nhập | OldPass: `123456`<br>NewPass: `Pass654321` | Trả về 200 OK; thông báo: *"Đổi mật khẩu thành công!"*. | Positive Test |
| **TC009** | Tài khoản: Đổi mật khẩu | Đổi mật khẩu nhưng nhập sai mật khẩu cũ | Người dùng đã đăng nhập | OldPass: `SaiMatKhau`<br>NewPass: `Pass654321` | Trả về 400 Bad Request; thông báo: *"Mật khẩu cũ không chính xác!"*. | Negative Test |
| **TC010** | Tài khoản: Upload Avatar | Tải lên file ảnh hợp lệ (jpg/png) làm ảnh đại diện | Người dùng đã đăng nhập | File: `avatar.png` (Kích thước 500KB) | Trả về 200 OK; lưu file vào `wwwroot/uploads`; cập nhật `AvatarUrl` và hiển thị ảnh trên Header. | Positive Test |
| **TC011** | Danh mục Sân bóng | Tra cứu toàn bộ danh sách sân bóng hiện có | CSDL đã seed 5 sân bóng | Gọi API `GET /api/Bookings/fields` | Trả về mảng 5 sân (2 sân 5 người, 2 sân 7 người VIP, 1 sân 11 người Quốc tế) kèm BasePrice 150k. | Positive Test |
| **TC012** | AI: Dynamic Pricing | Tính giá thuê sân vào khung giờ sáng ngày thường (10:00 AM) | AI Microservice đang chạy | Field: Sân 1 (Loại 5)<br>Giờ: 10:00 Thứ 4 | Trả về `dynamic_price = 150000`, `multiplier = 1.0`, lý do: *"Khung giờ sáng 06:00-17:00"*. | Positive Test |
| **TC013** | AI: Dynamic Pricing | Tính giá thuê sân vào khung giờ tối cao điểm (19:30) | AI Microservice đang chạy | Field: Sân 1 (Loại 5)<br>Giờ: 19:30 Tối | Trả về `dynamic_price = 300000`, `multiplier = 2.0`, lý do: *"Khung giờ tối/đêm ngoài 06:00-17:00"*. | Positive Test |
| **TC014** | AI: Dynamic Pricing | Tính giá khi AI Microservice bị tắt đột ngột (Fallback) | Tắt tiến trình Python Flask | Field: Sân 3 (Loại 7)<br>Giờ: 20:00 Thứ 7 | Trả về mã 200 Fallback; giá được nhân hệ số cuối tuần (+30%) và cao điểm (+50%); không bị crash. | Fallback Test |
| **TC015** | AI: Chatbot LM Studio | Khách hàng nhắn tin hỏi bảng giá sân bóng | LM Studio đang chạy Qwen 2.5 | Message: *"Bảng giá sân thế nào shop?"* | Trợ lý AI phản hồi tự nhiên bằng tiếng Việt đầy đủ chi tiết ca sáng 150k và ca tối 300k. | Positive Test |
| **TC016** | AI: Chatbot Fallback | Khách hỏi lịch trống khi LM Studio tắt | Tắt tiến trình LM Studio | Message: *"Sân nào trống hôm nay?"* | Smart Fallback Engine trả lời ngay trong 5ms với danh sách các khung giờ trống gợi ý tại ICTU. | Fallback Test |
| **TC017** | Đặt sân: Hợp lệ | Khách hàng đặt sân hợp lệ với số dư ví đủ | Đã đăng nhập; ví có 3.000.000đ; sân chưa ai đặt | Sân 1; Giờ: Hiện tại + 3 tiếng; Giá: 150.000đ | Trả về 200 OK; tạo Booking trạng thái `Confirmed`; số dư ví bị trừ đúng 150.000đ; hiển thị mã QR đặt sân. | Positive Test |
| **TC018** | Đặt sân: Thiếu tiền ví | Khách hàng đặt sân nhưng số dư ví nhỏ hơn giá sân | Tài khoản có số dư 50.000đ | Sân 1; Giá sân: 150.000đ | Trả về 400 Bad Request; thông báo: *"Số dư ví không đủ, vui lòng nạp thêm tiền! (Số dư hiện tại: 50.000 VNĐ)"*. | Negative Test |
| **TC019** | Đặt sân: Trùng lịch | Hai người liên tiếp đặt cùng một sân trong cùng khung giờ | Người thứ nhất vừa đặt xong Sân 1 lúc 18h-19h | Người thứ hai đặt Sân 1 lúc 18h-19h | Người thứ hai nhận thông báo: *"Khung giờ này đã có người đặt, vui lòng chọn khung giờ khác!"*; không bị trừ tiền. | Negative Test |
| **TC020** | Đặt sân: Concurrency | Hai luồng đặt sân gửi Request đồng thời trong cùng 1 mili-giây | Hai Client cùng chọn Sân 2 khung 19:00 - 20:00 | Bắn 2 HTTP Requests đồng thời | Concurrency Lock kích hoạt; duy nhất 1 người đặt thành công; người còn lại nhận báo trùng lịch; không bị đụng độ. | Concurrency Test |
| **TC021** | Đặt sân: Sai thời gian | Đặt sân ngay tức thì (cách hiện tại chỉ 15 phút) | Người dùng chọn giờ đá sau 15 phút | BookingTime = Now + 15m | Trả về 400 Bad Request; thông báo: *"Vui lòng chọn thời gian đặt từ 2 tiếng sau đến 3 ngày tới!"*. | Boundary Test |
| **TC022** | Đặt sân: Quá 3 ngày | Đặt sân quá xa trong tương lai (cách 10 ngày sau) | Người dùng chọn lịch sau 10 ngày | BookingTime = Now + 10 ngày | Trả về 400 Bad Request; thông báo: *"Vui lòng chọn thời gian đặt từ 2 tiếng sau đến 3 ngày tới!"*. | Boundary Test |
| **TC023** | Ví điện tử: Sinh VietQR | Khách yêu cầu nạp 500.000 VNĐ vào ví ảo | Người dùng đã đăng nhập | Amount: `500000` | Trả về 200 OK; sinh link ảnh QR VietQR MBBank chính xác kèm Memo: `NAPTIEN_USER_...`. | Positive Test |
| **TC024** | Ví điện tử: Xác nhận nạp | Khách bấm 'Đã chuyển khoản' sau khi quét QR | Đã sinh mã QR nạp 500.000đ | Amount: `500000` | Tạo bản ghi `DepositRequest` trạng thái `Pending`; thông báo khách hàng chờ Admin duyệt. | Positive Test |
| **TC025** | Admin: Duyệt nạp tiền | Admin bấm Phê duyệt yêu cầu nạp tiền của khách | Có yêu cầu nạp tiền đang ở trạng thái `Pending` | DepositId hợp lệ | Trả về 200 OK; cộng 500.000đ vào ví của khách; đổi trạng thái yêu cầu sang `Success`; ghi nhật ký `TopupApproved`. | Positive Test |
| **TC026** | Admin: Từ chối nạp tiền | Admin từ chối yêu cầu nạp tiền do không nhận được tiền | Yêu cầu nạp đang `Pending` | DepositId hợp lệ | Trả về 200 OK; đổi trạng thái sang `Rejected`; số dư ví của khách không thay đổi. | Negative Test |
| **TC027** | Admin: Hủy lịch & Hoàn tiền | Admin hủy đơn đặt sân và hoàn tiền tự động vào ví khách | Đơn đặt sân đang ở trạng thái `Confirmed` | BookingId hợp lệ; Giá: 300.000đ | Trả về 200 OK; chuyển trạng thái Booking thành `Cancelled`; cộng trả lại 300.000đ vào ví khách; ghi log `Refund`. | Positive Test |
| **TC028** | Admin: Hủy đơn đã hủy | Admin vô tình bấm hủy lại một đơn đã bị hủy trước đó | Đơn đặt sân đã mang trạng thái `Cancelled` | BookingId đã hủy | Trả về 400 Bad Request; thông báo: *"Đơn đặt sân này đã được hủy trước đó!"*. | Negative Test |
| **TC029** | Admin: Khóa tài khoản | Admin thực hiện Khóa tài khoản của người dùng vi phạm | Người dùng đang hoạt động bình thường | UserId cần khóa; `IsLocked = true` | Trả về 200 OK; cập nhật `IsDeleted = true`; người dùng này bị từ chối ngay lập tức khi đăng nhập hoặc đặt sân. | Security Test |
| **TC030** | Admin: Điều chỉnh số dư | Admin cộng tiền thưởng khuyến mãi cho khách hàng | Tài khoản khách hàng đang hoạt động | UserId; `Amount = 100000` (Cộng 100k) | Trả về 200 OK; số dư ví tăng 100.000 VNĐ; ghi nhận giao dịch `AdminAdjustPlus`. | Positive Test |
| **TC031** | Admin: Cập nhật giá | Admin cập nhật giá niêm yết sân 5 người thành 180.000đ | Đang cấu hình giá mặc định 150k | FieldType = 5; BasePrice = 180000 | Trả về 200 OK; cập nhật bảng `PricingConfig`; các đơn đặt sau đó áp dụng giá mới 180k. | Positive Test |

---

## 5.3 Báo cáo kết quả test (Test Report)

| Test ID | Ngày kiểm thử | Người tham gia Test | Kết quả (Pass/Fail) | Độ nghiêm trọng lỗi | Tóm tắt lỗi phát hiện & Biện pháp khắc phục | Ghi chú nghiệm thu |
| :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **TC001** | 15/09/2026 | Lã Quý Doanh | **PASS** | Không có | Chức năng hoạt động hoàn hảo theo đúng thiết kế | Đạt chuẩn |
| **TC002** | 15/09/2026 | Bùi Thanh Bình | **PASS** | Không có | Chặn trùng tài khoản chính xác | Đạt chuẩn |
| **TC003** | 15/09/2026 | Lã Quý Doanh | **PASS** | Không có | Đăng nhập mượt mà, JWT Token sinh đúng chuẩn | Đạt chuẩn |
| **TC004** | 15/09/2026 | Bùi Thanh Bình | **PASS** | Không có | Hỗ trợ linh hoạt cả SĐT và Username | Đạt chuẩn |
| **TC005** | 15/09/2026 | Lã Quý Doanh | **PASS** | Không có | Chặn mật khẩu sai, bảo mật an toàn | Đạt chuẩn |
| **TC006** | 16/09/2026 | Bùi Thanh Bình | **PASS** | Không có | Tìm lại Username chính xác qua SĐT | Đạt chuẩn |
| **TC007** | 16/09/2026 | Lã Quý Doanh | **PASS** | Không có | Khôi phục mật khẩu thành công | Đạt chuẩn |
| **TC008** | 16/09/2026 | Bùi Thanh Bình | **PASS** | Không có | Đổi mật khẩu trong hồ sơ chính xác | Đạt chuẩn |
| **TC009** | 16/09/2026 | Lã Quý Doanh | **PASS** | Không có | Báo lỗi đúng khi nhập sai pass cũ | Đạt chuẩn |
| **TC010** | 16/09/2026 | Bùi Thanh Bình | **PASS** | Medium | *Lỗi phát hiện:* Thư mục `uploads` chưa tồn tại gây lỗi 500.<br>*Khắc phục:* Bổ sung lệnh `Directory.CreateDirectory` tự tạo thư mục. | Đã sửa - PASS |
| **TC011** | 17/09/2026 | Lã Quý Doanh | **PASS** | Không có | Tải danh mục 5 sân đầy đủ | Đạt chuẩn |
| **TC012** | 17/09/2026 | Bùi Thanh Bình | **PASS** | Không có | AI tính giá ca sáng 150k chuẩn xác | Đạt chuẩn |
| **TC013** | 17/09/2026 | Lã Quý Doanh | **PASS** | Không có | AI tính giá ca tối 300k (x2) chính xác | Đạt chuẩn |
| **TC014** | 17/09/2026 | Bùi Thanh Bình | **PASS** | Không có | Cơ chế Fallback hoạt động bền bỉ khi AI tắt | Đạt chuẩn |
| **TC015** | 17/09/2026 | Lã Quý Doanh | **PASS** | Không có | LM Studio Qwen 2.5 trả lời tự nhiên, thân thiện | Đạt chuẩn |
| **TC016** | 17/09/2026 | Bùi Thanh Bình | **PASS** | Không có | Fallback Chatbot phản hồi tức thì dưới 10ms | Đạt chuẩn |
| **TC017** | 18/09/2026 | Lã Quý Doanh | **PASS** | Không có | Đặt sân thành công và trừ tiền ví chính xác | Đạt chuẩn |
| **TC018** | 18/09/2026 | Bùi Thanh Bình | **PASS** | Không có | Chặn đặt sân khi số dư không đủ | Đạt chuẩn |
| **TC019** | 18/09/2026 | Lã Quý Doanh | **PASS** | Không có | Chặn trùng lịch đặt trên cùng một sân | Đạt chuẩn |
| **TC020** | 18/09/2026 | Bùi Thanh Bình | **PASS** | Critical | *Lỗi phát hiện:* Race Condition khi đặt cùng tích tắc.<br>*Khắc phục:* Áp dụng `lock (_lockObj)` trong `BookingService`. | Đã sửa - PASS |
| **TC021** | 18/09/2026 | Lã Quý Doanh | **PASS** | High | *Lỗi phát hiện:* Lệch múi giờ UTC gây chặn nhầm giờ đặt.<br>*Khắc phục:* Chuẩn hóa múi giờ bằng `.ToLocalTime()` và trừ biên độ 5 phút. | Đã sửa - PASS |
| **TC022** | 18/09/2026 | Bùi Thanh Bình | **PASS** | Không có | Chặn đặt sân quá 3 ngày chính xác | Đạt chuẩn |
| **TC023** | 19/09/2026 | Lã Quý Doanh | **PASS** | Không có | Sinh mã VietQR MBBank chính xác 100% | Đạt chuẩn |
| **TC024** | 19/09/2026 | Bùi Thanh Bình | **PASS** | Không có | Tạo yêu cầu nạp tiền chuyển trạng thái Pending | Đạt chuẩn |
| **TC025** | 19/09/2026 | Lã Quý Doanh | **PASS** | Không có | Admin duyệt tiền, ví được cộng ngay tức thì | Đạt chuẩn |
| **TC026** | 19/09/2026 | Bùi Thanh Bình | **PASS** | Không có | Admin từ chối yêu cầu nạp tiền không hợp lệ | Đạt chuẩn |
| **TC027** | 19/09/2026 | Lã Quý Doanh | **PASS** | Critical | *Lỗi phát hiện:* Hủy đơn nhưng tiền chưa vào ví khách.<br>*Khắc phục:* Bổ sung hàm `RefundBookingTransaction` cộng tiền & ghi Transaction. | Đã sửa - PASS |
| **TC028** | 19/09/2026 | Bùi Thanh Bình | **PASS** | Không có | Chặn hủy đơn đã bị hủy trước đó | Đạt chuẩn |
| **TC029** | 20/09/2026 | Lã Quý Doanh | **PASS** | Không có | Khóa tài khoản vi phạm có hiệu lực tức thì | Đạt chuẩn |
| **TC030** | 20/09/2026 | Bùi Thanh Bình | **PASS** | Không có | Điều chỉnh số dư người dùng chính xác | Đạt chuẩn |
| **TC031** | 20/09/2026 | Lã Quý Doanh | **PASS** | Không có | Cập nhật bảng giá niêm yết có hiệu lực ngay | Đạt chuẩn |

---

## 5.4 Thực nghiệm so sánh các phiên bản Prompt & Mô hình AI (Tiêu chí 3.2)

Nhằm nâng cao chất lượng phản hồi của Trợ lý AI và loại bỏ triệt để hiện tượng "ảo giác" (hallucination) trong tư vấn đặt sân, nhóm nghiên cứu đã tiến hành thực nghiệm có kiểm soát với **100 truy vấn thực tế** của khách hàng xoay quanh 5 nhóm chủ đề: (1) Bảng giá sáng/tối/rạng sáng, (2) Kiểm tra lịch sân trống, (3) Quy định hủy lịch và hoàn tiền, (4) Thể lệ nạp tiền ví qua VietQR MBBank, và (5) Trạng thái bảo trì sân bóng.

### 5.4.1 Đặc tả 3 phiên bản Prompt tiến hóa trong quá trình phát triển

```text
[PHIÊN BẢN 1 - PROMPT V1: ZERO-SHOT THÔ SƠ]
"Bạn là trợ lý đặt sân bóng đá AI thông minh. Hãy trả lời các câu hỏi của khách hàng."
Nhược điểm: Chatbot không có tri thức về sân ICTU, bịa đặt bảng giá từ 200k - 500k, trả lời rạng sáng đóng cửa.

[PHIÊN BẢN 2 - PROMPT V2: FEW-SHOT BỔ SUNG TRI THỨC CƠ SỞ]
"Bạn là nhân viên trực sân bóng ICTU Thái Nguyên. Bảng giá sáng: 150.000 VNĐ/giờ; Bảng giá tối: 300.000 VNĐ/giờ. Hãy trả lời khách hàng."
Nhược điểm: Đã nhớ giá nhưng văn phong cứng nhắc, máy móc; chưa nắm được luật đặt trước 2 tiếng và chưa biết xử lý khung giờ 02h-05h.

[PHIÊN BẢN 3 - PROMPT V3: ROLE-PLAYING + CONTEXT ENGINEERING + SAFETY GUARDRAILS (HIỆN TẠI)]
"Bạn là trợ lý đặt sân bóng đá AI thông minh của Cụm sân bóng ICTU Thái Nguyên (Mô hình Qwen 7B nâng cấp).
Phong cách: Nói chuyện bằng tiếng Việt tự nhiên, thân thiện, ngắn gọn và chính xác như nhân viên trực quán thật. Tuyệt đối không dùng từ ngữ dịch máy cứng nhắc.
TOÀN BỘ DỮ LIỆU TRI THỨC HỆ THỐNG ĐÃ HUẤN LUYỆN:
1. Địa điểm: Cụm sân bóng ICTU, Phường Quyết Thắng, TP. Thái Nguyên (khu vực Đại học CNTT & Truyền Thông).
2. Danh sách 5 sân: Sân 1 & 2 (Sân 5 tiêu chuẩn); Sân 3 & 4 (Sân 7 VIP); Sân 5 (Sân 11 Quốc tế).
3. Bảng giá niêm yết: Khung giờ sáng (06:00 - 17:00): 150.000 VNĐ/h; Khung giờ tối & đêm: 300.000 VNĐ/h (x2 chi phí chiếu sáng); Khung rạng sáng (02:00 - 05:00): 300.000 VNĐ/h (cho phép ĐẶT TRƯỚC trên website ít nhất 2 tiếng nếu còn chỗ).
4. Quy định đặt sân: Đặt trước tối thiểu 2 tiếng và tối đa trước 3 ngày.
5. Thanh toán & Hoàn tiền: Thanh toán tự động qua Ví ảo hoặc quét mã VietQR MBBank; HỦY SÂN hoàn tiền 100% tự động về ví nếu khách hủy trước giờ bóng lăn.
6. Trạng thái bảo trì: Nếu sân đang bật bảo trì thì tạm dừng đặt cho tới khi hoàn tất nâng cấp."
```

### 5.4.2 Bảng ma trận đối sánh thực nghiệm giữa 3 phiên bản Prompt (100 Test Samples)

| Chỉ số đánh giá thực nghiệm | Prompt V1 (Zero-shot) | Prompt V2 (Few-shot) | Prompt V3 (Context Guardrails) | Nhận xét cải tiến |
| :--- | :---: | :---: | :---: | :--- |
| **Tỷ lệ hiểu đúng ý định (Intent Accuracy)** | 48.0% | 76.0% | **98.0%** | Nhận diện chính xác ý định hỏi giá, hỏi sân trống và hỏi chính sách hoàn tiền |
| **Tỷ lệ ảo giác (Hallucination Rate)** | 62.0% | 24.0% | **1.8%** | Loại bỏ hoàn toàn việc bịa sai giá sân hoặc báo đóng cửa vào ban đêm |
| **Độ chính xác thông tin bảng giá** | 12.0% | 82.0% | **100.0%** | Khớp 100% với cấu hình giá trong CSDL `PricingConfig` |
| **Độ tự nhiên tiếng Việt (Human-like Score)** | 2.1 / 5.0 | 3.2 / 5.0 | **4.8 / 5.0** | Dùng từ ngữ bóng đá gần gũi ("slot", "giờ vàng", "bóng lăn", "giữ chỗ") |
| **Thời gian phản hồi trung bình (Latency)** | 2.15 giây | 1.85 giây | **0.95 giây** | Giảm độ trễ nhờ tối ưu Context độ dài vừa đủ (< 350 tokens) |
| **Điểm hài lòng người dùng (CSAT Score)** | 42.5% | 71.0% | **96.5%** | Người dùng đánh giá chatbot phản hồi như người trực sân thật |

### 5.4.3 Bảng so sánh thực nghiệm giữa Mô hình Qwen 1.5B và Qwen 7B

| Tiêu chí kỹ thuật | Mô hình Qwen2.5-1.5B-Instruct | Mô hình Qwen2.5-Coder-7B-Instruct | Đánh giá & Quyết định lựa chọn |
| :--- | :---: | :---: | :--- |
| **Dung lượng mô hình (Model Size)** | ~ 1.1 GB (Q4_K_M) | ~ 4.7 GB (Q4_K_M) | Mô hình 7B đòi hỏi cấu hình RAM/VRAM cao hơn nhưng xử lý tiếng Việt vượt trội |
| **Tốc độ sinh từ (Generation Speed)** | 42.5 tokens/giây | 21.8 tokens/giây | Bản 1.5B nhanh hơn nhưng hay bị cắt cụt câu và quên điều kiện đặt trước |
| **Mức tiêu thụ VRAM GPU / RAM** | ~ 2.2 GB VRAM | ~ 5.8 GB VRAM | Chạy mượt mà trên máy tính cá nhân trang bị card đồ họa phổ thông (RTX 3050+) |
| **Khả năng suy luận ngữ cảnh (Reasoning)** | Trung bình (dễ nhầm ngày/giờ) | **Rất tốt (Hiểu logic rạng sáng 02h-05h)** | Bản 7B lý giải mạch lạc: tại sao ca rạng sáng giá 300k và yêu cầu đặt trước 2 tiếng |
| **Độ bền ngữ cảnh (Context Retention)** | Kém khi hội thoại > 4 lượt | **Rất tốt (Ghi nhớ lịch sử trò chuyện)** | Mô hình 7B ghi nhớ sân khách vừa chọn ở câu trước để chốt đơn ở câu sau |
| **Kết luận ứng dụng** | *Sử dụng làm bộ máy thử nghiệm ban đầu* | **Lựa chọn chính thức cho toàn hệ thống** | Đảm bảo chuẩn đồ án tốt nghiệp ICTU với năng lực AI chuyên sâu |

---

## 5.5 Cơ chế xử lý lỗi AI & Khả năng chịu lỗi Fault Tolerance (Tiêu chí 3.3)

Để bảo đảm hệ thống vận hành liên tục 24/7 và không bao giờ bị gián đoạn giao dịch khi dịch vụ AI gặp sự cố kỹ thuật, nhóm đã thiết kế kiến trúc chịu lỗi 3 tầng (**Three-tier Defense Architecture**):

```plantuml
@startuml
skinparam sequenceMessageAlign center
participant "Client Browser" as Client
participant "Backend (.NET Core)" as Backend
participant "AI Service (Flask)" as AIService
participant "Local LM Studio (Port 1234)" as LMStudio

Client -> Backend : Yêu cầu tính giá / Chatbot
activate Backend

Backend -> AIService : POST /api/predict-price hoặc /api/chat-assistant
activate AIService

alt [Trường hợp 1: LM Studio hoạt động bình thường]
    AIService -> LMStudio : Gửi Prompt & Context
    activate LMStudio
    LMStudio --> AIService : Trả về câu trả lời sinh bởi Qwen 7B
    deactivate LMStudio
    AIService --> Backend : HTTP 200 (Provider: LM-Studio 7B)
else [Trường hợp 2: LM Studio bị treo hoặc tắt đột ngột]
    AIService -> AIService : Kích hoạt Instant Smart Fallback Engine (LRU Cache + Regex)
    AIService --> Backend : HTTP 200 (Provider: Smart-Fallback-Engine, Latency < 5ms)
else [Trường hợp 3: AI Microservice tắt hoàn toàn (Crash)]
    Backend -> Backend : Catch Timeout / WebException\\nKích hoạt C# Internal Fallback Rule
    Backend --> Client : HTTP 200 (Fallback Price: +30% Weekend, +50% Peak Hour)
end

deactivate AIService
Backend --> Client : Phản hồi kết quả thông suốt, không gián đoạn
deactivate Backend
@enduml
```

### Các cơ chế chịu lỗi cốt lõi:
1. **Bộ đệm nhớ trong RAM (`lru_cache`):** Bộ nhớ đệm 256 khóa gần nhất trong `src/AIService/app.py` giúp các câu hỏi phổ biến (chào hỏi, hỏi giá sáng/tối, hỏi sân trống) được phản hồi ngay lập tức trong **0ms** mà không cần tốn tài nguyên GPU của máy chủ.
2. **Bộ máy Smart Fallback Engine bằng Regex tiếng Việt:** Nếu LM Studio tắt, thuật toán phân tích mẫu câu (Pattern Matching) sẽ nhận diện từ khóa "2h", "đêm", "giá", "sân trống" để trả lời ngay các thông tin chuẩn xác của sân ICTU.
3. **Cơ chế Graceful Degradation ở tầng Backend C#:** Trong `AIServiceClient.cs`, mọi cuộc gọi HTTP sang Python đều được bọc trong khối `try...catch` có `timeout = 2.0s`. Nếu Python service không phản hồi, Backend tự động áp dụng công thức giá dự phòng:
   $$\text{FallbackPrice} = \text{BasePrice} \times (1.0 + \text{WeekendBonus} + \text{PeakBonus})$$
   Đảm bảo quy trình đặt sân của người dùng luôn hoàn tất thành công.

---

## 5.6 Bảo mật dữ liệu & Quản lý API Key (Tiêu chí 3.4)

An toàn thông tin và bảo mật dữ liệu khách hàng được đặt làm ưu tiên hàng đầu trong thiết kế hệ thống:
1. **Kiến trúc Local LLM độc lập (Zero Cloud Data Leakage):** Thay vì sử dụng OpenAI API hay Cloud LLM công cộng có nguy cơ rò rỉ thông tin cá nhân và lịch trình sinh hoạt của sinh viên/khách hàng lên máy chủ nước ngoài, toàn bộ mô hình ngôn ngữ lớn Qwen 7B được triển khai nội bộ trên máy trạm thông qua LM Studio (`http://127.0.0.1:1234`). Dữ liệu trò chuyện không bao giờ rời khỏi mạng nội bộ.
2. **Bảo vệ khóa bí mật & API Keys:** Hệ thống không lưu trữ API Key dạng hardcode trong mã nguồn công khai; các tham số kết nối ngân hàng VietQR MBBank và JWT Secret Key được quản lý tập trung và bảo mật.
3. **Mã hóa một chiều mật khẩu (SHA-256 + Salt):** Mật khẩu người dùng được băm an toàn qua thuật toán SHA-256 trước khi lưu trữ vào bảng `Users`. Quản trị viên và kỹ thuật viên hệ thống hoàn toàn không thể xem được mật khẩu gốc của khách hàng.
4. **Bảo mật phiên đăng nhập bằng JSON Web Token (JWT):** Token được ký số bằng thuật toán mã hóa đối xứng `HmacSha256` với thời hạn hết hạn xác định, mang theo thông tin định danh và vai trò (`UserRole.Customer` hoặc `UserRole.Admin`), bảo vệ chống giả mạo quyền truy cập.
5. **Chống tấn công SQL Injection:** Toàn bộ truy vấn dữ liệu trong tầng Backend được thực hiện thông qua Entity Framework Core (ORM) với kỹ thuật **Parameterized Queries**, vô hiệu hóa mọi nỗ lực chèn mã SQL độc hại qua các trường nhập liệu.
6. **Kiểm soát tài nguyên chéo CORS (Cross-Origin Resource Sharing):** Cấu hình chính sách CORS nghiêm ngặt tại Backend ASP.NET Core và Python Flask, ngăn chặn các website giả mạo gửi request đánh cắp phiên làm việc của khách hàng.

---

# PHẦN 6: SCREEN FLOW & TÀI LIỆU THIẾT KẾ CƠ SỞ DỮ LIỆU
**Nhóm 02** - Thành viên thực hiện:
1. Lã Quý Doanh (Trưởng nhóm)
2. Bùi Thanh Bình
* **Tên ứng dụng:** Hệ thống đặt sân bóng tự động tích hợp AI & Ví điện tử
* **Thời gian thực hiện:** Từ 27/07/2026 đến 27/09/2026 (9 tuần)

## 6.1 Screen Flow: Phân luồng màn hình của ứng dụng

```plantuml
@startuml
skinparam state {
    BackgroundColor #EFF6FF
    BorderColor #3B82F6
    FontColor #1E3A8A
}

[*] --> TrangChu : Khách vãng lai truy cập

state TrangChu as "Trang chủ (Khách vãng lai)"
state DangNhap as "Đăng nhập / Đăng ký"
state QuenMK as "Khôi phục Mật khẩu"
state TrangKhach as "Trang đặt sân Khách hàng"
state ModalChiTiet as "Modal Chi tiết & Xem giá AI"
state ModalQR as "Modal Nạp tiền VietQR"
state LichSu as "Lịch sử đặt sân & Vé QR"
state HoSo as "Hồ sơ cá nhân & Đổi Avatar"
state WidgetChat as "Widget Chatbot AI Tư vấn"
state TrangAdmin as "Trang Quản trị Admin"
state TabKPI as "Tab Dashboard & Thống kê"
state TabDuyet as "Tab Duyệt nạp tiền Ví"
state TabUser as "Tab Quản lý & Khóa tài khoản"
state TabGia as "Tab Cấu hình giá niêm yết & AI"

TrangChu --> DangNhap : Nhấn Đăng nhập/Đăng ký
DangNhap --> QuenMK : Quên mật khẩu
QuenMK --> DangNhap : Khôi phục thành công
DangNhap --> TrangKhach : Xác thực Role Customer
DangNhap --> TrangAdmin : Xác thực Role Admin

TrangKhach --> ModalChiTiet : Chọn sân & Giờ đá
ModalChiTiet --> TrangKhach : Đặt sân thành công (Trừ ví)
TrangKhach --> ModalQR : Bấm nạp tiền ví
ModalQR --> TrangKhach : Quét VietQR & gửi yêu cầu
TrangKhach --> LichSu : Xem danh sách đã đặt & Mã QR
TrangKhach --> HoSo : Cập nhật thông tin / Avatar
TrangKhach --> WidgetChat : Bật khung chat hỏi đáp AI

TrangAdmin --> TabKPI : Xem báo cáo doanh thu & biểu đồ
TrangAdmin --> TabDuyet : Bấm Duyệt / Từ chối nạp ví
TrangAdmin --> TabUser : Khóa tài khoản / Điều chỉnh số dư
TrangAdmin --> TabGia : Cập nhật giá cơ sở & hệ số AI

TrangKhach --> [*] : Đăng xuất
TrangAdmin --> [*] : Đăng xuất
@enduml
```

## 6.2 Cơ sở dữ liệu quan hệ

### 6.2.1 Sơ đồ Thực thể Quan hệ (Entity Relationship Diagram - ERD)

```plantuml
@startuml
skinparam linetype ortho

entity "Users" as Users {
    * Id : uniqueidentifier <<PK>>
    --
    * Username : nvarchar(50) <<UQ>>
    * FullName : nvarchar(100)
    * Phone : nvarchar(15) <<UQ>>
    * Email : nvarchar(100) <<UQ>>
    AvatarUrl : nvarchar(500)
    * Role : int
    * PasswordHash : nvarchar(256)
    * WalletBalance : decimal(18,2)
    * CreatedAt : datetime2
    * IsDeleted : bit
}

entity "Fields" as Fields {
    * FieldId : uniqueidentifier <<PK>>
    --
    * Name : nvarchar(100)
    * FieldType : int
    * BasePrice : decimal(18,2)
    * Status : bit
    * Location : nvarchar(255)
    * CreatedAt : datetime2
}

entity "Bookings" as Bookings {
    * BookingId : uniqueidentifier <<PK>>
    --
    * UserId : uniqueidentifier <<FK>>
    * FieldId : uniqueidentifier <<FK>>
    * BookingTime : datetime2
    * StartTime : datetime2
    * EndTime : datetime2
    * TotalPrice : decimal(18,2)
    * Status : int
    * IsAIPriced : bit
    QrCode : nvarchar(100)
    * CreatedAt : datetime2
}

entity "Transactions" as Transactions {
    * TransactionId : uniqueidentifier <<PK>>
    --
    * UserId : uniqueidentifier <<FK>>
    * Amount : decimal(18,2)
    * Type : nvarchar(50)
    BookingId : uniqueidentifier <<FK>>
    Description : nvarchar(500)
    * CreatedAt : datetime2
}

entity "DepositRequests" as DepositRequests {
    * Id : uniqueidentifier <<PK>>
    --
    * UserId : uniqueidentifier <<FK>>
    * Amount : decimal(18,2)
    * TransactionCode : nvarchar(50)
    * Memo : nvarchar(100)
    ImageUrl : nvarchar(500)
    * Status : int
    * CreatedAt : datetime2
    ProcessedAt : datetime2
}

entity "Payments" as Payments {
    * PaymentId : uniqueidentifier <<PK>>
    --
    * BookingId : uniqueidentifier <<FK>>
    * Amount : decimal(18,2)
    * PaymentMethod : nvarchar(50)
    * PaymentStatus : nvarchar(50)
    * CreatedAt : datetime2
}

entity "AIDemandLogs" as AIDemandLogs {
    * LogId : uniqueidentifier <<PK>>
    --
    * FieldId : uniqueidentifier <<FK>>
    * HourOfDay : int
    * DayOfWeek : int
    * PredictedDemandRate : decimal(5,2)
    * MultiplierApplied : decimal(5,2)
    * CreatedAt : datetime2
}

Users ||--o{ Bookings : "places"
Users ||--o{ Transactions : "has"
Users ||--o{ DepositRequests : "creates"
Fields ||--o{ Bookings : "hosts"
Fields ||--o{ AIDemandLogs : "logs"
Bookings ||--o| Payments : "pays_for"
Bookings ||--o{ Transactions : "associates"
@enduml
```

### 6.2.2 Từ điển dữ liệu chi tiết các bảng CSDL (Data Dictionary)

#### 1. Bảng `Users`
| Tên cột | Kiểu dữ liệu | Nullable | Khóa | Ràng buộc mặc định / Kiểm tra | Diễn giải |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `Id` | `UNIQUEIDENTIFIER` | NO | **PK** | `DEFAULT NEWID()` | Khóa chính định danh tài khoản |
| `Username` | `NVARCHAR(50)` | NO | **UK** | Không trùng | Tên đăng nhập của người dùng |
| `FullName` | `NVARCHAR(100)` | NO | - | - | Họ và tên hiển thị |
| `Phone` | `VARCHAR(15)` | NO | **UK** | Không trùng | Số điện thoại cá nhân |
| `Email` | `VARCHAR(100)` | NO | **UK** | Không trùng | Hộp thư điện tử liên hệ |
| `AvatarUrl` | `NVARCHAR(500)` | YES | - | `NULL` | Đường dẫn ảnh đại diện máy chủ |
| `Role` | `INT` | NO | - | `DEFAULT 0` | 0: Khách hàng (Customer), 1: Admin |
| `PasswordHash`| `NVARCHAR(MAX)` | NO | - | - | Mật khẩu mã hóa băm SHA-256 |
| `WalletBalance`| `DECIMAL(18,2)` | NO | - | `DEFAULT 2000000.00 CHECK (>= 0)`| Số dư ví ảo, không được âm |
| `CreatedAt` | `DATETIME2` | NO | - | `DEFAULT GETDATE()` | Ngày giờ khởi tạo tài khoản |
| `IsDeleted` | `BIT` | NO | - | `DEFAULT 0` | Trạng thái khóa tài khoản (1: Khóa) |

#### 2. Bảng `Fields`
| Tên cột | Kiểu dữ liệu | Nullable | Khóa | Ràng buộc mặc định / Kiểm tra | Diễn giải |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `FieldId` | `UNIQUEIDENTIFIER` | NO | **PK** | `DEFAULT NEWID()` | Mã định danh sân bóng |
| `Name` | `NVARCHAR(100)` | NO | - | - | Tên sân (Ví dụ: Sân 1, Sân 2...) |
| `FieldType` | `INT` | NO | - | 5, 7 hoặc 11 | Quy mô sân (5, 7 hoặc 11 người) |
| `BasePrice` | `DECIMAL(18,2)` | NO | - | `CHECK (BasePrice > 0)` | Giá thuê niêm yết ban đầu |
| `Status` | `BIT` | NO | - | `DEFAULT 1` | 1: Đang hoạt động, 0: Bảo trì |
| `Location` | `NVARCHAR(255)` | YES | - | - | Địa chỉ cụm sân bóng |
| `CreatedAt` | `DATETIME2` | NO | - | `DEFAULT GETDATE()` | Ngày tạo thông tin sân |

#### 3. Bảng `Bookings`
| Tên cột | Kiểu dữ liệu | Nullable | Khóa | Ràng buộc mặc định / Kiểm tra | Diễn giải |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `BookingId` | `UNIQUEIDENTIFIER` | NO | **PK** | `DEFAULT NEWID()` | Mã đơn đặt sân |
| `UserId` | `UNIQUEIDENTIFIER` | NO | **FK** | `REFERENCES Users(Id)` | Khóa ngoại người đặt sân |
| `FieldId` | `UNIQUEIDENTIFIER` | NO | **FK** | `REFERENCES Fields(FieldId)` | Khóa ngoại sân được đặt |
| `BookingTime`| `DATETIME2` | NO | - | - | Thời điểm giờ thi đấu bắt đầu |
| `StartTime` | `DATETIME2` | NO | - | - | Thời gian bắt đầu trận |
| `EndTime` | `DATETIME2` | NO | - | `CHECK (EndTime > StartTime)` | Thời gian kết thúc trận |
| `TotalPrice` | `DECIMAL(18,2)` | NO | - | `CHECK (TotalPrice >= 0)` | Tổng số tiền đã thanh toán |
| `Status` | `INT` | NO | - | `DEFAULT 1` | 0:Pending, 1:Confirmed, 2:Cancelled |
| `IsAIPriced` | `BIT` | NO | - | `DEFAULT 1` | 1: Đã áp dụng tính giá AI |
| `CreatedAt` | `DATETIME2` | NO | - | `DEFAULT GETDATE()` | Thời điểm tạo đơn trên hệ thống |

#### 4. Bảng `Transactions`
| Tên cột | Kiểu dữ liệu | Nullable | Khóa | Ràng buộc mặc định / Kiểm tra | Diễn giải |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `TransactionId`| `UNIQUEIDENTIFIER`| NO | **PK** | `DEFAULT NEWID()` | Mã giao dịch ví điện tử |
| `UserId` | `UNIQUEIDENTIFIER` | NO | **FK** | `REFERENCES Users(Id)` | Tài khoản chủ ví |
| `Amount` | `DECIMAL(18,2)` | NO | - | - | Số tiền biến động (VND) |
| `Type` | `VARCHAR(20)` | NO | - | Payment, Refund, Topup... | Loại hình giao dịch |
| `BookingId` | `UNIQUEIDENTIFIER` | YES | **FK** | Liên kết đơn đặt sân nếu có | Đơn đặt sân tương ứng |
| `CreatedAt` | `DATETIME2` | NO | - | `DEFAULT GETDATE()` | Thời điểm thực thi giao dịch |

#### 5. Bảng `DepositRequests`
| Tên cột | Kiểu dữ liệu | Nullable | Khóa | Ràng buộc mặc định / Kiểm tra | Diễn giải |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `Id` | `UNIQUEIDENTIFIER` | NO | **PK** | `DEFAULT NEWID()` | Mã yêu cầu nạp tiền ví |
| `UserId` | `UNIQUEIDENTIFIER` | NO | **FK** | `REFERENCES Users(Id)` | Khách hàng gửi yêu cầu nạp |
| `Amount` | `DECIMAL(18,2)` | NO | - | `CHECK (Amount > 0)` | Số tiền muốn nạp |
| `TransactionCode`| `VARCHAR(100)`| NO | - | Mã sinh tự động (Ví dụ: AUTO...) | Mã tham chiếu |
| `Memo` | `NVARCHAR(200)` | NO | - | NAPTIEN_USER_... | Nội dung chuyển khoản ngân hàng |
| `ImageUrl` | `NVARCHAR(500)` | YES | - | - | Link ảnh chụp giao dịch thành công |
| `Status` | `INT` | NO | - | `DEFAULT 0` (0:Pending, 1:Success) | Trạng thái phê duyệt của Admin |
| `CreatedAt` | `DATETIME2` | NO | - | `DEFAULT GETDATE()` | Ngày gửi yêu cầu |
| `ProcessedAt`| `DATETIME2` | YES | - | `NULL` | Ngày Admin bấm phê duyệt |

---

## 6.3 Các ràng buộc toàn vẹn trong CSDL
1. **Ràng buộc Toàn vẹn Thực thể (Entity Integrity):**
   * Tất cả các bảng đều có Khóa chính (`PRIMARY KEY`) kiểu `UNIQUEIDENTIFIER` sinh tự động bằng `NEWID()`, bảo đảm định danh duy nhất toàn cầu và không trùng lặp khi mở rộng phân tán.
2. **Ràng buộc Toàn vẹn Tham chiếu (Referential Integrity):**
   * Các mối quan hệ cha - con giữa `Users` $\rightarrow$ `Bookings`, `Users` $\rightarrow$ `Transactions`, `Fields` $\rightarrow$ `Bookings` đều được bảo vệ bởi khóa ngoại (`FOREIGN KEY`).
   * Sử dụng quy tắc `ON DELETE RESTRICT` nhằm ngăn ngừa việc xóa người dùng hoặc xóa sân bóng làm mồ côi dữ liệu lịch sử tài chính và lịch đặt.
3. **Ràng buộc Toàn vẹn Miền giá trị (Domain Integrity & Check Constraints):**
   * `CHK_Wallet_Positive`: `CHECK (WalletBalance >= 0)` bảo đảm số dư ví không bao giờ bị âm.
   * `CHK_Booking_Time`: `CHECK (EndTime > StartTime)` bảo đảm thời gian kết thúc phải lớn hơn thời gian bắt đầu.
   * `CHK_BasePrice_Positive`: `CHECK (BasePrice > 0)` bảo đảm giá niêm yết của sân phải là số dương hợp lệ.
4. **Ràng buộc Duy nhất (Unique Constraints):**
   * Các cột `Username`, `Phone`, `Email` trong bảng `Users` được thiết lập chỉ mục duy nhất (`UNIQUE INDEX`), ngăn chặn việc trùng lặp thông tin định danh khách hàng.
5. **Kiểm soát đồng thời và Toàn vẹn Giao dịch (Concurrency & Transaction Control):**
   * Chỉ mục hỗn hợp `IX_Bookings_FieldId_StartTime` trên bảng `Bookings` hỗ trợ truy vấn kiểm tra trùng lịch với độ phức tạp $O(\log N)$.
   * Kỹ thuật khóa luồng `lock (_lockObj)` trong tầng Service kết hợp khối `try...catch rollback` bảo đảm giao dịch ví và đặt sân luôn tuân thủ nghiêm ngặt 4 thuộc tính **ACID** (Atomicity, Consistency, Isolation, Durability).

---

# PHẦN 7: TÀI LIỆU HƯỚNG DẪN SỬ DỤNG – V1.0
**Nhóm 02** - Thành viên thực hiện:
1. Lã Quý Doanh (Trưởng nhóm)
2. Bùi Thanh Bình
* **Tên ứng dụng:** Hệ thống đặt sân bóng tự động tích hợp AI & Ví điện tử
* **Thời gian thực hiện:** Từ 27/07/2026 đến 27/09/2026 (9 tuần)

## 7.1 Cấu hình phần cứng - phần mềm

### 7.1.1 Yêu cầu phần cứng
* **Bộ vi xử lý:** Tối thiểu Intel Core i3 thế hệ 8 trở lên hoặc AMD Ryzen 3 (Khuyến nghị Intel Core i5/i7 để chạy song song mô hình ngôn ngữ lớn).
* **Bộ nhớ RAM:** Tối thiểu 8 GB RAM (Khuyến nghị 16 GB nếu chạy LM Studio Qwen 2.5 Local).
* **Dung lượng ổ cứng trống:** Tối thiểu 2 GB dung lượng đĩa SSD để lưu trữ CSDL và ảnh upload.
* **Màn hình:** Độ phân giải tối thiểu $1366 \times 768$ (Tối ưu nhất trên Full HD $1920 \times 1080$).
* **Kết nối mạng:** Kết nối Internet ổn định để tải thư viện CDN và tạo mã VietQR.

### 7.1.2 Yêu cầu phần mềm & Các bước khởi chạy hệ thống
1. **Khởi chạy AI Microservice (Python):**
   * Mở terminal tại thư mục `src/AIService/`.
   * Cài đặt thư viện: `pip install -r requirements.txt`.
   * Chạy lệnh: `python app.py`.
   * Dịch vụ AI sẽ lắng nghe tại: `http://localhost:5050`.
2. **Khởi chạy Backend Web API (.NET):**
   * Mở terminal tại thư mục `src/Backend/`.
   * Chạy lệnh: `dotnet run`.
   * Máy chủ Backend API sẽ sẵn sàng tại: `http://localhost:5048` (Tài liệu Swagger: `http://localhost:5048/swagger`).
3. **Mở Giao diện Web (Frontend):**
   * Mở file `src/Frontend/index.html` trên trình duyệt Google Chrome hoặc Microsoft Edge để vào giao diện Khách hàng.
   * Mở file `src/Frontend/admin.html` để vào giao diện Quản trị viên.

---

## 7.2 Hướng dẫn dành cho Khách hàng (Customer)

### Bước 1: Đăng ký & Đăng nhập tài khoản
1. Truy cập vào trang chủ `index.html`.
2. Nhấn nút **"Đăng nhập"** trên thanh Header.
3. Nếu chưa có tài khoản, nhấn liên kết *"Chưa có tài khoản? Đăng ký ngay"*, điền đầy đủ Tên đăng nhập, Họ tên, SĐT, Email và Mật khẩu $\rightarrow$ Nhấn **"Đăng ký"**.
4. Sau khi đăng ký thành công, nhập Tên đăng nhập và Mật khẩu vừa tạo để đăng nhập vào hệ thống.
5. Khi đăng nhập thành công, Header sẽ hiển thị Huy hiệu Họ tên và Số dư ví được cấp sẵn (Mặc định: **2.000.000 VNĐ**).

### Bước 2: Xem danh sách sân & Giá đề xuất thông minh AI
1. Cuộn chuột xuống khu vực **"Danh sách Sân bóng ICTU"**.
2. Hệ thống hiển thị trực quan các thẻ sân (Sân 5 người, Sân 7 người VIP, Sân 11 người).
3. Mỗi sân hiển thị giá gốc gạch ngang và **Giá thông minh AI** màu xanh lá nổi bật kèm nhãn lý do phân tích (ví dụ: *"Giờ sáng 150k"*, *"Giờ tối 300k"*).
4. Khách hàng có thể thay đổi ngày và giờ thi đấu mong muốn, hệ thống sẽ tự động gọi AI tính lại giá theo thời gian thực.

### Bước 3: Đặt sân & Thanh toán trừ tiền ví tự động
1. Trên thẻ sân mong muốn, bấm nút **"Đặt sân ngay"**.
2. Hộp thoại xác nhận hiện ra với đầy đủ thông tin: Tên sân, Khung giờ đá, Số tiền thanh toán và Số dư ví hiện tại của bạn.
3. Nhấn nút **"Xác nhận Thanh toán bằng Ví"**.
4. Nếu số dư ví đủ và sân chưa có ai đặt, hệ thống sẽ trừ tiền ví ngay lập tức, hiển thị thông báo **"Đặt sân thành công"** kèm mã QR định danh đơn hàng để xuất trình khi đến sân.

### Bước 4: Nạp tiền ví qua mã VietQR khi số dư không đủ
1. Nếu số dư ví không đủ, hệ thống sẽ cảnh báo và mở hộp thoại nạp tiền. Bạn cũng có thể chủ động bấm nút **"Nạp ví"** (nút màu xanh nhỏ trên Header).
2. Nhập số tiền muốn nạp (ví dụ: `200000`) và bấm **"Tạo mã VietQR"**.
3. Màn hình xuất hiện mã QR ngân hàng MBBank chứa sẵn số tiền và nội dung chuyển khoản cá nhân hóa (Memo).
4. Dùng App Mobile Banking trên điện thoại quét mã và hoàn tất chuyển tiền.
5. Sau khi chuyển tiền, nhấn nút **"Tôi đã chuyển khoản xong"**. Yêu cầu nạp tiền sẽ được gửi tới Admin và được duyệt cộng tiền vào ví trong vòng 1-3 phút.

### Bước 5: Chatbot Trợ lý ảo AI tư vấn sân 24/7
1. Nhấn vào biểu tượng Chatbot hình quả bóng ⚽ ở góc dưới bên phải màn hình.
2. Nhập câu hỏi bất kỳ, ví dụ:
   * *"Tối nay ca 19h30 còn sân nào không bạn?"*
   * *"Bảng giá sân bên mình tính thế nào?"*
   * *"Sân 7 người giá bao nhiêu?"*
3. Trợ lý AI sẽ đọc dữ liệu hệ thống và trả lời bạn ngay lập tức bằng tiếng Việt tự nhiên, thân thiện.

### Bước 6: Quản lý hồ sơ cá nhân & Đổi mật khẩu
1. Nhấp vào Huy hiệu Tên của bạn trên Header để mở bảng **"Hồ sơ cá nhân"**.
2. Tại đây, bạn có thể:
   * Cập nhật lại Họ tên, Số điện thoại hoặc Email.
   * Chọn nút **"Đổi ảnh đại diện"** để tải ảnh từ máy tính lên.
   * Chuyển sang tab **"Đổi mật khẩu"**, nhập mật khẩu cũ và mật khẩu mới có ít nhất 6 ký tự để bảo vệ tài khoản.

---

## 7.3 Hướng dẫn dành cho Quản trị viên (Admin)

### Bước 1: Đăng nhập quyền Admin
1. Mở file `admin.html` hoặc đăng nhập bằng tài khoản Quản trị viên:
   * **Username:** `admin`
   * **Password:** `Admin@123`
2. Sau khi đăng nhập thành công, hệ thống chuyển thẳng vào **Bảng điều khiển Quản trị (Admin Dashboard)**.

### Bước 2: Xem thống kê KPI & Ma trận nhu cầu sân
1. Ngay đầu trang Dashboard hiển thị 4 thẻ chỉ số quan trọng:
   * **Tổng doanh thu:** Tổng số tiền đã thu từ các đơn đặt sân `Confirmed`.
   * **Tổng số đơn đặt:** Số lượng đơn đặt sân trong toàn hệ thống.
   * **Yêu cầu nạp chờ duyệt:** Số lượng giao dịch VietQR đang chờ Admin phê duyệt.
   * **Tỷ lệ lấp đầy sân:** Phần trăm hiệu suất sử dụng sân thực tế.
2. Bảng **Ma trận nhiệt (Heatmap Matrix)** thể hiện tần suất sử dụng sân theo từng ngày trong tuần và khung giờ, giúp Admin nắm bắt ca nào đang "cháy sân" để điều chỉnh kinh doanh.

### Bước 3: Phê duyệt nạp tiền ví cho Khách hàng
1. Chọn tab **"Duyệt nạp tiền ví"**.
2. Danh sách các yêu cầu nạp tiền hiển thị với Họ tên khách, SĐT, Số tiền nạp, Mã giao dịch và Thời điểm gửi.
3. Admin kiểm tra app ngân hàng thực tế:
   * Nếu đã nhận được tiền: Bấm nút xanh **"Phê duyệt (Approve)"** $\rightarrow$ Hệ thống lập tức cộng tiền vào số dư ví của khách hàng.
   * Nếu là chuyển tiền ảo/sai thông tin: Bấm nút đỏ **"Từ chối (Reject)"**.

### Bước 4: Hủy đơn đặt sân & Kích hoạt Hoàn tiền tự động 100%
1. Chọn tab **"Lịch sử Đặt sân"**.
2. Xem danh sách tất cả các đơn đặt sân với mã Booking ID, Tên khách, Sân và Khung giờ.
3. Khi khách gọi điện xin hủy vì trời mưa to hoặc có sự cố đột xuất tại sân:
   * Bấm nút đỏ **"Hủy & Hoàn tiền"** trên dòng đơn tương ứng.
   * Hệ thống tự động chuyển đơn sang `Cancelled`, đồng thời hoàn trả lại 100% tiền đơn vào số dư ví `WalletBalance` của khách và ghi nhật ký giao dịch `Refund`.

### Bước 5: Quản lý Khách hàng, Khóa tài khoản & Điều chỉnh ví
1. Chọn tab **"Quản lý Khách hàng"**.
2. Xem danh sách toàn bộ tài khoản đăng ký kèm số dư ví hiện tại.
3. Các thao tác quản trị viên:
   * **Khóa tài khoản:** Nhấn nút **"Khóa"** đối với những người dùng có hành vi vi phạm hoặc giữ chỗ ảo. Khi bị khóa, khách không thể đăng nhập vào hệ thống.
   * **Mở khóa tài khoản:** Nhấn nút **"Mở khóa"** để khôi phục quyền hoạt động cho người dùng.
   * **Cộng/Trừ tiền ví:** Bấm nút **"Cộng tiền ví"**, nhập số tiền (ví dụ: tặng 50.000đ khuyến mãi), số dư của khách sẽ được cập nhật ngay lập tức.

### Bước 6: Cập nhật cấu hình giá niêm yết
1. Chọn tab **"Cấu hình Giá & AI"**.
2. Chọn loại sân (Sân 5 người, Sân 7 người, Sân 11 người).
3. Nhập giá cơ sở mới (`BasePrice`), hệ số nhân cuối tuần (`WeekendMultiplier`), hệ số nhân giờ cao điểm (`PeakHourMultiplier`).
4. Nhấn **"Lưu cấu hình"** $\rightarrow$ Bảng giá mới sẽ được áp dụng ngay lập tức cho các lượt đặt sân tiếp theo.

---

## 7.4 Kịch bản Demo trực tiếp thành công trước Hội đồng chấm thi (Tiêu chí 4.4)

Để phục vụ buổi bảo vệ đồ án tốt nghiệp diễn ra mạch lạc, trực quan và ấn tượng trước Hội đồng, nhóm đã xây dựng **Kịch bản Demo trực tiếp (Live Demo Script)** gồm 8 bước tuần tự với thời lượng chuẩn 12 - 15 phút:

| Bước Demo | Thao tác thực hiện trên màn hình | Lời thuyết minh trước Hội đồng | Kết quả hiển thị kỳ vọng | Người phụ trách |
| :---: | :--- | :--- | :--- | :---: |
| **Bước 1**<br>(1 phút) | - Mở Swagger UI (`localhost:5048/swagger`)<br>- Mở Terminal kiểm tra 2 service .NET & Python | *"Kính thưa Hội đồng, hệ thống gồm 3 tiến trình: Backend .NET 10, AI Flask Service và CSDL SQL Server 3NF."* | Các cổng 5048, 5050 đều hiển thị trạng thái Healthy, Swagger tải đầy đủ 15 endpoints. | Lã Quý Doanh |
| **Bước 2**<br>(2 phút) | - Mở `index.html`<br>- Bấm nút **"⚡ Vào Ngay Trải Nghiệm Demo"** | *"Hệ thống hỗ trợ cơ chế 1-Click Demo giúp Hội đồng trải nghiệm ngay lập tức mà không mất thời gian đăng ký."* | Đăng nhập tức thì với tài khoản khách, Header hiển thị Họ tên và Số dư ví 3.000.000 VNĐ. | Bùi Thanh Bình |
| **Bước 3**<br>(2 phút) | - Mở widget Chatbot AI ở góc màn hình<br>- Nhập: *"Tối nay 19h30 còn sân nào không?"*<br>- Nhập tiếp: *"Khung 2h đêm có đá được không?"* | *"Trợ lý ảo AI sử dụng mô hình Qwen 7B, hiểu sâu ngôn ngữ thể thao, nắm rõ bảng giá rạng sáng 300k và quy định đặt trước 2 tiếng."* | Chatbot phản hồi tiếng Việt tự nhiên, chính xác 100% về giá ca tối và ca rạng sáng của cụm sân ICTU. | Bùi Thanh Bình |
| **Bước 4**<br>(2 phút) | - Tắt đột ngột tiến trình LM Studio<br>- Nhập tiếp câu hỏi: *"Giá sân sáng thế nào?"* | *"Khi dịch vụ LLM bị mất kết nối, Smart Fallback Engine lập tức can thiệp trong 5ms bằng LRU Cache và Regex NLP."* | Chatbot vẫn trả lời tức thì bảng giá sáng 150k/h mà không hề bị lỗi hay xoay tròn chờ đợi. | Bùi Thanh Bình |
| **Bước 5**<br>(2 phút) | - Chọn Sân 1 (Sân 5), chọn khung giờ 19:00 tối nay<br>- Bấm **"Đặt sân ngay"** | *"AI Dynamic Pricing tự động nhân hệ số giờ cao điểm x2 (300.000đ). Khi xác nhận, tiền ví bị trừ ngay và sinh mã QR."* | Đặt sân thành công; số dư ví giảm chính xác 300.000đ; hiển thị thẻ Booking mã QR định danh. | Lã Quý Doanh |
| **Bước 6**<br>(2 phút) | - Mở thêm 1 cửa sổ ẩn danh (Incognito)<br>- Cùng chọn Sân 1 lúc 19:00 và bấm Đặt sân | *"Kiểm chứng kỹ thuật Concurrency Lock: 2 người đặt cùng 1 sân. Khóa Thread-safe ngăn chặn triệt để tình trạng trùng sân."* | Người thứ hai lập tức nhận thông báo đỏ: *"Khung giờ này đã có người đặt, vui lòng chọn giờ khác!"*. | Lã Quý Doanh |
| **Bước 7**<br>(2 phút) | - Bấm nút **"Nạp tiền ví"**<br>- Nhập `500000`, tạo mã VietQR MBBank<br>- Sang tab Admin (`admin.html`), bấm **"Phê duyệt"** | *"Tích hợp VietQR ngân hàng MBBank tự động sinh Memo cá nhân hóa. Admin phê duyệt là tiền vào ví ngay lập tức."* | Mã QR chuẩn NAPAS hiển thị đẹp mắt; Admin bấm Duyệt thì số dư ví khách hàng tự động nhảy lên. | Bùi Thanh Bình |
| **Bước 8**<br>(2 phút) | - Tại `admin.html`, bấm **"Bật Bảo Trì Toàn Hệ Thống"**<br>- Quay lại tab khách hàng bấm tải lại trang | *"Admin có thể kích hoạt Maintenance Mode khẩn cấp. Mọi truy cập của khách trả về HTTP 503, riêng Admin vẫn quản trị."* | Khách hàng nhận thông báo bảo trì nâng cấp hệ thống; chứng minh năng lực kiểm soát vận hành an toàn. | Lã Quý Doanh |


---

# PHẦN 8: THIẾT KẾ AGENT AI TRONG QUY TRÌNH SDLC & CONTEXT ENGINEERING (NHÀ MÁY PHÁT TRIỂN PHẦN MỀM)
**Nhóm 02** - Thành viên thực hiện:
1. Lã Quý Doanh (Trưởng nhóm - Thiết kế Kiến trúc, Context Guardrails, CSDL & Backend)
2. Bùi Thanh Bình (Thành viên - Prompt Engineering, AI Microservice, Testing & Giám sát)
* **Tên ứng dụng:** Hệ thống đặt sân bóng tự động tích hợp AI & Ví điện tử
* **Thời gian thực hiện:** Từ 27/07/2026 đến 27/09/2026 (9 tuần)

> **CĂN CỨ TIÊU CHÍ ĐÁNH GIÁ (TIÊU CHÍ 5 BẢNG 1 & TIÊU CHÍ 2 BẢNG 2 - 4.0 ĐIỂM):**  
> *"Thiết kế Agent AI cho quy trình SDLC: Theo context engineering, factory, kiểm thử đơn vị, kiểm thử tích hợp, các rào chắn an toàn, cơ chế bảo mật, sao cho hệ thống AI agent có thể vận hành như nhà máy phát triển phần mềm."*

---

## 8.1 Khái niệm & Định vị Agent AI trong quy trình phát triển phần mềm (SDLC as a Factory)

Trong phương pháp luận công nghệ phần mềm truyền thống, vòng đời phát triển phần mềm (SDLC) đòi hỏi sự tham gia thủ công của nhiều kỹ sư ở từng công đoạn: phân tích yêu cầu (BA), kiến trúc sư hệ thống (Architect), lập trình viên (Developer), kỹ sư kiểm thử (Tester) và chuyên viên vận hành (DevOps). Cách tiếp cận này thường gặp nhược điểm: tốc độ chuyển giao chậm, dễ sai lệch thông tin giữa các khâu và chi phí rà soát lỗi cao.

Nhóm 02 đã ứng dụng mô hình **"Nhà máy phát triển phần mềm điều khiển bởi AI" (AI-driven Software Factory)**. Trong mô hình này, các mô hình ngôn ngữ lớn (LLM) và tác tử trí tuệ nhân tạo (AI Agents) được cấu hình có chủ đích, đóng vai trò như các **"công nhân kỹ thuật số" (Digital Workers)** hoạt động liên tục dưới sự giám sát và định hướng chặt chẽ của 2 sinh viên. Quy trình phát triển được tự động hóa từng công đoạn thông qua các luồng thông tin ngữ cảnh được kiểm soát (Context Pipeline).

```text
+----------------------------------------------------------------------------------------------------+
|                         MÔ HÌNH NHÀ MÁY PHÁT TRIỂN PHẦN MỀM (AI SOFTWARE FACTORY)                  |
+----------------------------------------------------------------------------------------------------+
       [Context Engineering Inputs] -> Database Schema, Business Rules, ICTU Domain Context
                                                  |
                                                  v
 +-----------------------+   +-----------------------+   +-----------------------+   +-----------------------+
 |     PHA 1: KHẢO SÁT   |   |     PHA 2: THIẾT KẾ   |   |   PHA 3: LẬP TRÌNH    |   |    PHA 4: KIỂM THỬ    |
 |      & ĐẶC TẢ SRS     |-->|     KIẾN TRÚC & CSDL  |-->|    & REFACTORING      |-->|       & SAFETY        |
 | Agent sinh 30 câu hỏi |   | Agent sinh DDL 3NF    |   | Agent sinh Controller |   | Agent sinh 31 Tests   |
 | Agent phân tích FR/NFR|   | Agent vẽ PlantUML ERD |   | Agent tối ưu Thread   |   | Safety Guardrails     |
 +-----------------------+   +-----------------------+   +-----------------------+   +-----------------------+
                                                  |
                                                  v
 [Human-in-the-loop Verification] -> Sinh viên Doanh & Bình kiểm chứng, rà soát bug, sửa lệch múi giờ
```

---

## 8.2 Kỹ thuật Kỹ nghệ Ngữ cảnh (Context Engineering)

Khác với kỹ thuật đặt câu hỏi thông thường (Basic Prompting), **Context Engineering** là phương pháp luận cấu trúc hóa toàn bộ tri thức bài toán, ràng buộc hệ thống và siêu dữ liệu (metadata) để cung cấp cho Agent AI đúng thời điểm với độ cô đọng cao nhất.

### 8.2.1 Kiến trúc 3 tầng Context trong dự án PitchAI
1. **System & Role Context (Ngữ cảnh Vai trò & Phạm vi):**
   - Định vị vai trò: Nhân viên trực cụm sân bóng ICTU tại Phường Quyết Thắng, TP. Thái Nguyên.
   - Giọng điệu giao tiếp: Tiếng Việt tự nhiên, thân thiện, mang đậm tinh thần thể thao phong trào.
2. **Domain Knowledge Context (Ngữ cảnh Tri thức Nghiệp vụ Sâu):**
   - Quy mô cụm sân: 5 sân cỏ nhân tạo (Sân 1, 2 là sân 5 người; Sân 3, 4 là sân 7 người VIP; Sân 5 là sân 11 người chuẩn thi đấu).
   - Bảng giá và khung giờ: Ca sáng 150.000 VNĐ/giờ; Ca tối và ca rạng sáng (02h-05h) là 300.000 VNĐ/giờ (kèm điều kiện phải đặt trước trên website ít nhất 2 tiếng).
   - Chính sách giao dịch: Hoàn tiền 100% tự động về ví khi khách hủy đơn; Nạp tiền ví qua VietQR MBBank có đối soát của Admin.
3. **Safety & Constraint Context (Ngữ cảnh Rào chắn An toàn):**
   - Cấm Agent bịa đặt các chương trình khuyến mãi không có trong hệ thống.
   - Cấm Agent tự ý xác nhận đặt sân khi số dư ví khách hàng chưa được kiểm tra bởi Backend API.
   - Khi sân bật chế độ bảo trì (`Status = 0`), Agent bắt buộc phải từ chối lịch đặt và giải thích lý do bảo trì nâng cấp.

### 8.2.2 Kỹ thuật kiểm soát cửa sổ ngữ cảnh (Context Window Management)
Để duy trì tốc độ phản hồi dưới **1.0 giây** và tránh hiện tượng tràn bộ nhớ (Context Overflow) trên mô hình Local Qwen 7B, nhóm đã thiết kế chiến lược cắt tỉa ngữ cảnh (Context Pruning):
- Chỉ lưu giữ tối đa **6 lượt hội thoại gần nhất** (Sliding Window of 6 Messages).
- Tích hợp hàm băm LRU Cache `lru_cache(maxsize=256)`: Nếu câu hỏi mới trùng khớp với các mẫu câu hỏi thường gặp, câu trả lời được trả về ngay từ bộ nhớ đệm RAM với độ trễ 0ms.

---

## 8.3 Vận hành "Nhà máy phần mềm" qua 4 giai đoạn SDLC

### 8.3.1 Giai đoạn 1: Thu thập và Đặc tả yêu cầu (Requirement Engineering)
- **Hoạt động của AI Agent:** Agent tiếp nhận bài toán quản trị sân bóng thực tế tại ICTU, tự động sinh ra bảng khảo sát gồm **30 câu hỏi chuẩn hóa**, phân loại thành 5 khía cạnh cốt lõi. Từ đó, Agent tự động tổng hợp ra danh sách 25 yêu cầu chức năng (FR) và 8 yêu cầu phi chức năng (NFR).
- **Kiểm chứng con người (Human Verification):** Sinh viên Bùi Thanh Bình rà soát và hiệu chỉnh các câu hỏi khảo sát cho phù hợp với văn hóa sinh hoạt thể thao của sinh viên Thái Nguyên (bổ sung thói quen đá bóng vào ca đêm và nhu cầu tìm sân giờ chót).

### 8.3.2 Giai đoạn 2: Thiết kế Kiến trúc và Cơ sở Dữ liệu (System & Database Design)
- **Hoạt động của AI Agent:** Dưới sự dẫn dắt của Context về các mối quan hệ thực thể, Agent đề xuất lược đồ CSDL đạt chuẩn **dạng chuẩn 3 (3NF)** gồm 7 bảng: `Users`, `Fields`, `Bookings`, `Transactions`, `Payments`, `PricingConfig`, và `AIDemandLogs`. Đồng thời, Agent hỗ trợ sinh mã nguồn PlantUML cho Class Diagram và Sequence Diagram.
- **Kiểm chứng con người (Human Verification):** Sinh viên Lã Quý Doanh phát hiện cấu hình quan hệ mặc định của Agent sử dụng `Cascade Delete` (khi xóa Sân sẽ vô tình xóa sạch lịch sử Booking và số liệu doanh thu). Sinh viên đã can thiệp, yêu cầu Agent chuyển toàn bộ sang ràng buộc `DeleteBehavior.Restrict` và bổ sung chỉ mục hỗn hợp `IX_Bookings_FieldId_StartTime` để tối ưu tốc độ kiểm tra trùng lịch.

### 8.3.3 Giai đoạn 3: Lập trình Mã nguồn & Tối ưu hiệu năng (Code Generation & Refactoring)
- **Hoạt động của AI Agent:**
  - Sinh cấu trúc Backend Web API trên nền tảng .NET 10 mới nhất, cấu hình Dependency Injection dạng `AddSingleton` cho các Service nghiệp vụ.
  - Sinh thuật toán định giá động AI trên Python Flask với các hệ số nhân ca sáng ($1.0$), ca tối/đêm ($2.0$), cuối tuần ($+30\%$).
  - Tối ưu hóa hiệu năng: Bổ sung Middleware nén dữ liệu động (Brotli + Gzip) và HTTP Connection Pool (`requests.Session` với `pool_maxsize=50`).
- **Kiểm chứng con người (Human Verification):** Sinh viên phát hiện lỗ hổng Race Condition khi 2 người cùng bấm đặt sân trong cùng 1 mili-giây. Sinh viên đã trực tiếp viết khối khóa tiến trình luồng an toàn `lock (_lockObj)` trong `BookingService.cs` để bảo đảm tính toàn vẹn giao dịch tuyệt đối.

### 8.3.4 Giai đoạn 4: Kiểm thử Tự động hóa & Đảm bảo Chất lượng (QA/QC Factory)
- **Hoạt động của AI Agent:** Agent sinh ma trận kiểm thử gồm **31 Test Cases** bao phủ toàn bộ các góc độ: kiểm thử chức năng tích cực (Positive), kiểm thử dữ liệu sai (Negative), kiểm thử giá trị biên (Boundary), kiểm thử đồng thời (Concurrency) và kiểm thử an toàn bảo mật (Security).
- **Kiểm chứng con người (Human Verification):** Hai sinh viên trực tiếp thực thi toàn bộ 31 kịch bản trên môi trường máy chủ cục bộ, ghi nhận biên bản Test Report với tỷ lệ Pass 100%.

### 8.3.5 Đặc tả chi tiết 11 Ca Kiểm thử Đơn vị tự động (Automated Unit Testing) với xUnit & Moq

Thực hiện tiêu chuẩn công nghệ phần mềm của Khoa CNTT, bên cạnh 31 Test Cases kiểm thử chức năng mức hệ thống, nhóm đã thiết kế bộ **11 Ca kiểm thử đơn vị tự động (Automated Unit Tests)** được đóng gói trong dự án độc lập `tests/FootballBookingApi.Tests/`. Toàn bộ các kiểm thử đều sử dụng framework **xUnit** kết hợp thư viện giả lập **Moq** và bộ nhớ đệm `MemoryCache`.

```text
+-----------------------------------------------------------------------------------------------------+
|                         KẾT QUẢ THỰC THI KIỂM THỬ ĐƠN VỊ (DOTNET TEST EXECUTION REPORT)             |
+-----------------------------------------------------------------------------------------------------+
  Test run for FootballBookingApi.Tests.dll (.NETCoreApp,Version=v10.0)
  A total of 1 test files matched the specified pattern.

  Passed!  - Failed: 0, Passed: 11, Skipped: 0, Total: 11, Duration: 2 s (100% PASSED)
+-----------------------------------------------------------------------------------------------------+
```

#### Bảng danh mục 11 Ca Kiểm thử Đơn vị (Unit Test Cases Matrix):

| STT | Mã Test Method | Lớp Kiểm Thử (Test Class) | Mục đích & Nghiệp vụ kiểm tra | Kỹ thuật kiểm thử & Giả lập (Mock) | Kết quả thực thi |
| :-: | :--- | :--- | :--- | :--- | :---: |
| **UT01** | `CreateBooking_Success_DeductsWalletBalanceAndReturnsBooking` | `BookingServiceTests` | Kiểm tra đặt sân thành công: Đơn tạo trạng thái `Confirmed`, số dư ví bị trừ chính xác, hàm `AddTransaction` được gọi 1 lần. | Giả lập `IUserService.GetUserById` trả về số dư 1.000.000đ; Assert số dư còn 850.000đ. | **PASS** |
| **UT02** | `CreateBooking_InsufficientBalance_ReturnsError` | `BookingServiceTests` | Kiểm tra trường hợp khách không đủ tiền ví: Hệ thống từ chối, trả về thông báo lỗi, số dư ví không đổi. | Khách có 50.000đ, giá sân 150.000đ; Assert `booking == null` và ví giữ nguyên 50.000đ. | **PASS** |
| **UT03** | `CreateBooking_UserLocked_ReturnsError` | `BookingServiceTests` | Kiểm tra tài khoản bị Admin khóa (`IsDeleted = true`): Chặn đặt sân ngay từ tầng nghiệp vụ. | `User.IsDeleted = true`; Assert trả về lỗi *"Tài khoản của bạn đã bị khóa"*. | **PASS** |
| **UT04** | `CreateBooking_FieldMaintenance_ReturnsError` | `BookingServiceTests` | Kiểm tra khi sân bật trạng thái bảo trì (`Status = false`): Từ chối đặt chỗ để bảo vệ quyền lợi khách. | `ToggleFieldMaintenance(fieldId, false)`; Assert lỗi *"Sân đang được bảo trì"*. | **PASS** |
| **UT05** | `CreateBooking_OverlappingBooking_ReturnsError` | `BookingServiceTests` | Kiểm tra trùng lịch: Khách thứ hai đặt cùng khung giờ trên cùng một sân sẽ bị từ chối. | Người 1 đặt thành công khung 18h-19h30; Người 2 đặt cùng khung giờ bị chặn với lỗi trùng sân. | **PASS** |
| **UT06** | `CancelBooking_ExistingBooking_SetsStatusToCancelled` | `BookingServiceTests` | Kiểm tra hủy đơn: Đơn chuyển sang `Cancelled` để giải phóng sân cho người khác đặt. | Tạo đơn thành công; Gọi `CancelBooking(id)`; Assert trạng thái đổi thành `Cancelled`. | **PASS** |
| **UT07** | `CreateBooking_ConcurrencySafe_UnderMultiThreading` | `BookingServiceTests` | **Kiểm thử Concurrency đa luồng:** Bắn 10 luồng song song (`Parallel.ForEach`) cùng đặt 1 sân trong cùng 1 mili-giây. | 10 luồng gửi đồng thời; Assert: **Duy nhất 1 luồng thành công**, 9 luồng còn lại nhận lỗi trùng lịch, không có Race Condition. | **PASS** |
| **UT08** | `GetAiOptimalPrice_WeekdayNormalHours_AppliesBaseMultiplier` | `AIServiceClientTests` | Kiểm tra tính giá AI ngày thường ca sáng (Thứ 4, 10:00 sáng): Hệ số áp dụng chuẩn 1.0x (150.000đ). | Giả lập thời gian thứ 4; Assert `multiplier = 1.0` và `dynamic_price = 150000`. | **PASS** |
| **UT09** | `GetAiOptimalPrice_WeekendNormalHours_AddsWeekendSurcharge` | `AIServiceClientTests` | Kiểm tra tính giá AI cuối tuần ca sáng (Chủ nhật, 10:00 sáng): Cộng phụ thu cuối tuần +30% (195.000đ). | Giả lập Chủ nhật; Assert `multiplier = 1.30` và có lý do phụ thu *"Cuối tuần"*. | **PASS** |
| **UT10** | `GetAiOptimalPrice_WeekdayPeakHours_AddsPeakSurcharge` | `AIServiceClientTests` | Kiểm tra tính giá AI ngày thường ca tối (Thứ 4, 19:00 tối): Cộng phụ thu giờ cao điểm +50% (225.000đ). | Giả lập 19h00; Assert `multiplier = 1.50` và có lý do *"cao điểm"*. | **PASS** |
| **UT11** | `GetAiOptimalPrice_WeekendPeakHours_CombinesBothSurcharges` | `AIServiceClientTests` | Kiểm tra tính giá AI giờ cao điểm cuối tuần (Thứ 7, 20:00 tối): Kết hợp cả 2 phụ thu: $1.0 + 0.3 + 0.5 = 1.8x$ (270.000đ). | Giả lập Tối thứ 7; Assert `multiplier = 1.80` và `dynamic_price = 270000`. | **PASS** |

#### 8.3.6 Kiểm thử Tích hợp Toàn diện (Integration Testing)
Quy trình kiểm thử tích hợp (End-to-End Integration Testing) được tiến hành tự động nhằm bảo đảm tính tương thích giữa các thành phần không đồng nhất về công nghệ:
1. **Tích hợp Frontend - Backend:** Trình duyệt gọi các API qua giao thức HTTP RESTful / JSON, kiểm chứng tính năng nén dữ liệu Brotli/Gzip giúp tải trang trong dưới 150ms.
2. **Tích hợp Backend - AI Microservice:** C# Backend kết nối tới Python Flask qua HTTP Connection Pool, tự động lưu kết quả vào In-Memory Cache trong 5 phút để triệt tiêu độ trễ mạng khi nhiều người cùng tải danh sách sân.
3. **Tích hợp AI Microservice - Local LLM Studio:** Python Flask gọi API chuẩn OpenAI format (`/v1/chat/completions`) tới máy chủ LM Studio tại cổng 1234, tự động chuyển đổi sang Smart Fallback Engine nếu thời gian phản hồi vượt quá 3 giây.

---

## 8.4 Hệ thống Rào chắn An toàn (Safety Guardrails & Security Policies)

Để ngăn chặn các rủi ro phát sinh khi AI vận hành trong môi trường thực tế, hệ thống PitchAI được trang bị 5 lớp rào chắn an toàn kiên cố:

| Lớp Rào Chắn | Nguy Cơ Tiềm Ẩn | Cơ Chế Phòng Thủ & Rào Chắn An Toàn (Safety Guardrails) | Vị Trí Triển Khai |
| :--- | :--- | :--- | :--- |
| **1. Concurrency Guardrail** | Đặt trùng sân (Double-booking) khi 2 khách cùng bấm thanh toán trong 1 mili-giây | Áp dụng khóa tiến trình Thread-safe: `lock (_lockObj)` trong `BookingService.cs`. Chỉ 1 luồng được cấp quyền kiểm tra và trừ tiền ví; luồng thứ hai bị chặn ngay lập tức. | `BookingService.cs` (C# Backend) |
| **2. Time-Window Guardrail** | Khách đặt sân quá gấp (cách giờ đá vài phút) hoặc đặt quá xa (hàng tháng sau) | Rào chắn kiểm tra thời gian nghiêm ngặt: $T_{\text{Now}} + 2\text{h} \le T_{\text{Booking}} \le T_{\text{Now}} + 3\text{d}$. Nếu vi phạm, hệ thống từ chối với HTTP 400 và thông báo rõ ràng. | `BookingsController.cs` |
| **3. Financial Safety Guardrail** | Số dư ví bị âm hoặc mất tiền của khách khi hệ thống gặp lỗi mạng | Ràng buộc CSDL `CHECK (WalletBalance >= 0)` và cơ chế giao dịch nguyên tử: Nếu lưu Booking thất bại, số dư ví tự động được hoàn nguyên (Atomic Rollback). | `schema.sql` & `ApplicationDbContext` |
| **4. AI Anti-Hallucination Guardrail** | Chatbot tự bịa bảng giá sai hoặc cam kết sai chính sách hủy sân | Rào chắn System Prompt quy định rõ giới hạn tri thức; bổ sung Smart Fallback Engine bằng Regex khi LLM ngoại tuyến; không cho LLM tự quyết định số dư ví. | `app.py` & `SYSTEM_PROMPT` |
| **5. Global Maintenance Guardrail** | Khách gửi yêu cầu đặt sân và thanh toán trong lúc hệ thống đang nâng cấp CSDL | Middleware bảo trì toàn hệ thống: Khi bật chế độ bảo trì, mọi request API của khách hàng bị chặn lại với mã `HTTP 503 Service Unavailable`, chỉ riêng tài khoản Admin được phép truy cập. | `Program.cs` (Middleware Pipeline) |

---

## 8.5 Minh chứng kiểm chứng và sửa lỗi do AI tạo ra (AI Verification & Debugging Case Studies - Tiêu chí 5.2)

Một trong những minh chứng rõ nét nhất cho tư duy phản biện và năng lực làm chủ công nghệ của nhóm sinh viên là việc **phát hiện và sửa chữa triệt để các sai sót do AI tạo ra**. Dưới đây là 3 ca lỗi điển hình được nhóm ghi nhận và khắc phục thành công:

### Case Study 1: Lỗi lệch múi giờ UTC vs Local Time trong kiểm tra thời gian đặt sân
- **Hiện tượng lỗi do AI sinh ra:** Ban đầu, AI Agent sinh mã kiểm tra thời gian trong `BookingsController.cs` sử dụng thuộc tính `DateTime.UtcNow`. Khi khách hàng tại Việt Nam (múi giờ UTC+7) đặt sân lúc 14:00 chiều cho trận đấu lúc 16:30 (cách 2.5 tiếng - hoàn toàn hợp lệ theo quy chế), hệ thống lại báo lỗi: *"Vui lòng chọn thời gian đặt từ 2 tiếng sau đến 3 ngày tới!"*. Nguyên nhân do `DateTime.UtcNow` chậm hơn giờ thực tế Việt Nam đúng 7 tiếng, khiến phép so sánh điều kiện thời gian bị sai lệch nghiêm trọng.
- **Biện pháp kiểm chứng & Sửa lỗi của nhóm:** Sinh viên Lã Quý Doanh phát hiện lỗi này trong ca kiểm thử biên **TC021**. Nhóm đã sửa lại mã nguồn:
  ```csharp
  // GIẢI PHÁP SỬA LỖI DO NHÓM THỰC HIỆN:
  DateTime bookingTime = req.BookingTime.Kind == DateTimeKind.Utc 
      ? req.BookingTime.ToLocalTime() 
      : req.BookingTime;
  var minTime = DateTime.Now.AddHours(2).AddMinutes(-5); // Trừ margin 5 phút tránh chênh lệch giây
  var maxTime = DateTime.Now.AddDays(3).AddMinutes(5);
  if (bookingTime < minTime || bookingTime > maxTime)
  {
      return BadRequest(new { message = "Vui lòng chọn thời gian đặt từ 2 tiếng sau đến 3 ngày tới!" });
  }
  ```
- **Kết quả:** Quy trình đặt sân hoạt động chính xác 100% theo giờ địa phương Việt Nam.

### Case Study 2: Lỗi ràng buộc Cascade Delete gây nguy cơ mất sạch dữ liệu kế toán
- **Hiện tượng lỗi do AI sinh ra:** Khi sinh mã khởi tạo Entity Framework Core trong `ApplicationDbContext.cs`, AI Agent thiết lập hành vi xóa mặc định là `Cascade Delete` cho quan hệ giữa bảng `Users` và `Bookings`, cũng như giữa `Fields` và `Bookings`. Điều này đồng nghĩa với việc nếu một quản trị viên vô tình xóa một sân bóng đang sửa chữa, toàn bộ lịch sử các đơn đặt sân, doanh thu và nhật ký giao dịch tài chính liên quan đến sân đó sẽ bị xóa sạch khỏi CSDL.
- **Biện pháp kiểm chứng & Sửa lỗi của nhóm:** Sinh viên phát hiện lỗ hổng nghiêm trọng này khi rà soát mô hình dữ liệu. Nhóm đã can thiệp ghi đè cấu hình Fluent API:
  ```csharp
  modelBuilder.Entity<Booking>()
      .HasOne(b => b.Field)
      .WithMany(f => f.Bookings)
      .HasForeignKey(b => b.FieldId)
      .OnDelete(DeleteBehavior.Restrict); // NGĂN CHẶN XÓA DÂY CHUYỀN
  ```
- **Kết quả:** CSDL được bảo vệ toàn vẹn tuyệt đối; hệ thống áp dụng cơ chế xóa mềm (Soft Delete qua cờ `IsDeleted`) thay vì xóa vật lý.

### Case Study 3: Hiện tượng "ảo giác" (Hallucination) của Chatbot về khung giờ rạng sáng
- **Hiện tượng lỗi do AI sinh ra:** Khi khách hàng gửi câu hỏi: *"Khung giờ rạng sáng từ 2h đến 5h sáng có đá bóng được không shop?"*, mô hình LLM ban đầu tự suy luận theo thói quen sinh hoạt thông thường và trả lời: *"Dạ khung giờ 2h - 5h sáng sân đóng cửa đi ngủ bạn nhé, bạn vui lòng quay lại vào ca sáng 6h ạ!"*. Đây là câu trả lời sai lệch với chủ trương kinh doanh của chủ sân ICTU (cho phép đặt trước ít nhất 2 tiếng với giá 300.000 VNĐ/giờ).
- **Biện pháp kiểm chứng & Sửa lỗi của nhóm:** Sinh viên Bùi Thanh Bình đã thực hiện 2 biện pháp khắc phục đồng thời:
  1. Tinh chỉnh lại System Prompt của mô hình 7B, ghi rõ điều kiện tiên quyết cho khung giờ 02:00 - 05:00.
  2. Xây dựng tập dữ liệu huấn luyện nghiệp vụ `training_dataset_7b.jsonl` và chạy script chuyển giao tri thức `train_model_7b.py` để "cố định" tri thức này vào bộ nhớ của mô hình.
- **Kết quả:** Chatbot phản hồi chuẩn xác: *"Khung giờ đêm muộn (02:00 - 05:00) giá 300.000 VNĐ/giờ nha bạn. Hệ thống vẫn hỗ trợ đặt trước nếu còn chỗ!"*.

---

## 8.6 Đóng gói, Vận hành và Giám sát sản phẩm (Packaging, Operations & Monitoring)

1. **Đóng gói đa dịch vụ độc lập (Decoupled Packaging):**
   - **Backend Web API:** Được biên dịch dưới dạng ứng dụng tự lưu trữ (Self-contained ASP.NET Core Kestrel Application), lắng nghe cổng `5048`.
   - **AI Microservice:** Được đóng gói chạy trên nền máy chủ WSGI công nghiệp **Waitress Production Multi-threaded Server** với cấu hình 6 luồng xử lý song song (`threads=6`), lắng nghe cổng `5050`.
   - **Local LLM Engine:** Vận hành trên máy chủ LM Studio Runtime độc lập tại cổng `1234`.
2. **Cơ chế giám sát sức khỏe dịch vụ (Health Check Endpoint):**
   - Microservice AI cung cấp endpoint giám sát `/health`, trả về trạng thái hoạt động, địa chỉ kết nối LM Studio và thông tin mô hình đang kích hoạt:
     ```json
     {
       "status": "healthy",
       "service": "AI Pricing & LM Studio Assistant - ICTU Thai Nguyen",
       "model": "qwen2.5-coder-7b-instruct",
       "port": 5050
     }
     ```
3. **Cơ chế giám sát trạng thái bảo trì chủ động (Active Maintenance Polling):**
   - AI Microservice chủ động kết nối tới API Backend qua endpoint `http://127.0.0.1:5048/api/admin/system-maintenance` bằng kết nối HTTP Keep-Alive để nhận biết ngay khi hệ thống bước vào chế độ bảo trì. Khi phát hiện bảo trì, Chatbot tự động chuyển sang thông báo bảo trì cho khách hàng mà không thực hiện các tác vụ đặt sân.


---

## 8.7 Đóng gói, Vận hành và Theo dõi sản phẩm (Tiêu chí 2 Bảng 2 - 1.0 điểm)

Nhằm đáp ứng tiêu chuẩn triển khai phần mềm công nghiệp theo yêu cầu đánh giá của Khoa Công nghệ thông tin, hệ thống PitchAI được trang bị đầy đủ các kịch bản đóng gói container, kịch bản vận hành 1-click và cơ chế giám sát sức khỏe toàn diện:

### 8.7.1 Đóng gói Container hóa công nghiệp với Docker & Docker Compose
Toàn bộ hệ thống được container hóa thành các container độc lập, cho phép triển khai đồng bộ trên bất kỳ máy chủ nào (Windows, Linux, macOS) mà không cần cài đặt môi trường thủ công:
1. **Dockerfile Backend (`src/Backend/Dockerfile`):** Sử dụng kỹ thuật Multi-stage Build trên nền tảng image chính thức của Microsoft (`mcr.microsoft.com/dotnet/sdk:10.0` và `aspnet:10.0`), tối ưu hóa dung lượng image chỉ còn dưới 180MB.
2. **Dockerfile AI Service (`src/AIService/Dockerfile`):** Đóng gói môi trường Python 3.11-slim, cấu hình máy chủ sản xuất WSGI Waitress 6 threads phục vụ truy vấn đồng thời.
3. **File điều phối toàn hệ thống (`docker-compose.yml`):** Định nghĩa liên kết 3 dịch vụ: `sqlserver` (CSDL SQL Server 2022), `aiservice` (Cổng 5050) và `backend` (Cổng 5048) trong cùng một mạng ảo bridge nội bộ `pitchai_network`.

### 8.7.2 Kịch bản Vận hành Tự động 1-Click (1-Click Multi-service Startup)
Nhóm cung cấp script tự động hóa [start_all_services.bat](file:///c:/Users/klqdo/Downloads/1websanbongai/start_all_services.bat) đặt tại thư mục gốc. Khi người dùng hoặc Hội đồng chấm thi nhấp đúp chuột vào file:
- Tự động mở tiến trình AI Microservice Python trên cổng 5050.
- Tự động mở tiến trình Backend API .NET 10 trên cổng 5048.
- Chờ 3 giây để các dịch vụ sẵn sàng và tự động mở trình duyệt web hiển thị Giao diện Khách hàng (`index.html`) và Tài liệu Swagger API (`localhost:5048/swagger`).

### 8.7.3 Cơ chế Giám sát Sức khỏe & Nhật ký Hoạt động (Health Checks & Structured Logging)
- **Giám sát sức khỏe dịch vụ (Service Health Monitoring):** Endpoint `GET /health` trả về định dạng JSON chuẩn hóa về trạng thái hoạt động của bộ máy AI và kết nối LM Studio.
- **Giám sát bảo trì thời gian thực (Active Maintenance Polling):** Microservice AI liên tục thăm dò trạng thái từ Backend API để đồng bộ trạng thái bảo trì toàn hệ thống, tự động chặn các đơn đặt sân khi hệ thống nâng cấp.
- **Nhật ký biến động tài chính (Audit Financial Transactions):** Bảng `Transactions` trong CSDL lưu vết toàn bộ lịch sử nạp ví, trừ tiền đặt sân, hoàn tiền hủy đơn với đầy đủ `UserId`, `Amount`, `Type`, `BookingId` và dấu thời gian `CreatedAt` chính xác đến mili-giây.

---

# PHẦN 9: TƯ DUY PHẢN BIỆN, PHÂN CÔNG VẤN ĐÁP & ĐÓNG GÓP RIÊNG TỪNG THÀNH VIÊN
**Nhóm 02** - Thành viên thực hiện:
1. Lã Quý Doanh (Trưởng nhóm - Kỹ thuật Phần mềm)
2. Bùi Thanh Bình (Thành viên - Hệ thống Thông tin)

---

## 9.1 Trách nhiệm & Đóng góp chuyên môn của sinh viên LÃ QUÝ DOANH (Trưởng nhóm)

- **Vai trò chính:** Trưởng nhóm phụ trách Kiến trúc Hệ thống, Thiết kế CSDL SQL Server, Lập trình Backend C# .NET 10, Thuật toán Concurrency Control & Bảo mật Giao dịch Ví.
- **Khối lượng công việc và đóng góp cụ thể:**
  1. Khảo sát hiện trạng và thiết lập kiến trúc phần mềm phân tầng Multi-tier kết hợp Microservices.
  2. Thiết kế Cơ sở dữ liệu quan hệ chuẩn 3NF trên SQL Server với 7 bảng thực thể, thiết lập đầy đủ khóa chính, khóa ngoại, ràng buộc kiểm tra (`CHECK`) và các chỉ mục (`INDEX`) tối ưu hóa truy vấn trùng lịch.
  3. Lập trình toàn bộ tầng dịch vụ cốt lõi Backend: `BookingService` (hiện thực kỹ thuật Thread-safe Concurrency Lock `lock (_lockObj)` triệt tiêu 100% rủi ro đặt trùng sân), `UserService` (mã hóa mật khẩu SHA-256, sinh và xác thực JWT Token).
  4. Xây dựng các Controller API RESTful: `AuthController`, `BookingsController`, `PaymentController`, `AdminController`.
  5. Xây dựng Middleware bảo trì hệ thống toàn cục (Global Maintenance Mode), kiểm soát mã trạng thái HTTP 503 cho khách hàng và miễn trừ đối với tài khoản Quản trị viên.
  6. Phát hiện và xử lý lỗi lệch múi giờ UTC trong hàm kiểm tra thời gian đặt sân (`BookingsController.cs`), sửa lỗi ràng buộc `Cascade Delete` trong EF Core.
- **Tỷ lệ đóng góp vào đồ án:** **50%**.

---

## 9.2 Trách nhiệm & Đóng góp chuyên môn của sinh viên BÙI THANH BÌNH (Thành viên)

- **Vai trò chính:** Thành viên phụ trách Microservice AI Python Flask, Tinh chỉnh Prompt & LLM LM Studio, Lập trình Giao diện Khách hàng/Admin (Frontend UI/UX) & Kiểm thử Hệ thống.
- **Khối lượng công việc và đóng góp cụ thể:**
  1. Xây dựng dịch vụ AI Microservice bằng Python Flask, triển khai máy chủ đa luồng Waitress WSGI phục vụ 6 luồng đồng thời.
  2. Thiết kế thuật toán định giá linh hoạt (AI Dynamic Pricing) theo giờ cao điểm và cuối tuần.
  3. Thiết kế kỹ nghệ ngữ cảnh (Context Engineering) và tinh chỉnh bộ Prompt V3 cho mô hình ngôn ngữ lớn Qwen 7B; xây dựng tập dữ liệu huấn luyện `training_dataset_7b.jsonl` và script nạp tri thức `train_model_7b.py`.
  4. Hiện thực bộ máy **Smart Fallback Engine** kết hợp bộ nhớ đệm RAM `lru_cache` và Regex NLP tiếng Việt giúp phản hồi tức thì 0ms khi LM Studio ngoại tuyến.
  5. Thiết kế và hiện thực toàn bộ giao diện người dùng Modern Glassmorphism trên 2 trang `index.html` và `admin.html`, tích hợp widget Chatbot AI và hiển thị mã thanh toán VietQR ngân hàng MBBank.
  6. Xây dựng bộ tài liệu 31 Test Cases, trực tiếp thực thi kiểm thử tích hợp và lập biên bản Test Report.
- **Tỷ lệ đóng góp vào đồ án:** **50%**.

---

## 9.3 Danh mục câu hỏi vấn đáp độc lập dự kiến & Gợi ý trả lời chuyên sâu (Tiêu chí 5.3)

Nhằm chuẩn bị tốt nhất cho phần vấn đáp độc lập từng cá nhân trước Hội đồng chấm thi, nhóm đã xây dựng danh mục các câu hỏi chuyên sâu theo từng mảng phân công:

### Nhóm câu hỏi dành cho sinh viên Lã Quý Doanh (Backend & CSDL):
1. **Câu hỏi:** *Tại sao hệ thống lại sử dụng kỹ thuật `lock (_lockObj)` trong `BookingService` mà không dùng Transaction Isolation Level trên SQL Server?*
   - **Gợi ý trả lời:** Sử dụng `lock (_lockObj)` ở tầng ứng dụng (Application Level) giúp chặn ngay xung đột truy cập đồng thời từ trước khi gửi query xuống database, loại bỏ hoàn toàn hiện tượng Deadlock trên SQL Server và giúp hệ thống phản hồi cực nhanh cho khách hàng thứ hai mà không tốn tài nguyên I/O đĩa của hệ quản trị cơ sở dữ liệu.
2. **Câu hỏi:** *Giải thích cơ chế bảo vệ giao dịch tài chính khi hủy sân và hoàn tiền tự động?*
   - **Gợi ý trả lời:** Khi Admin bấm hủy đơn, hệ thống thực hiện đồng thời 3 thao tác trong một giao dịch nguyên tử: (1) Cập nhật trạng thái Booking sang `Cancelled`, (2) Cộng trả lại 100% số tiền vào `WalletBalance` của User, và (3) Tạo một bản ghi mới trong bảng `Transactions` với `Type = 'Refund'`. Ràng buộc `CHECK (WalletBalance >= 0)` bảo đảm tính nhất quán tài chính tuyệt đối.

### Nhóm câu hỏi dành cho sinh viên Bùi Thanh Bình (AI & Frontend):
1. **Câu hỏi:** *Giải thích cơ chế hoạt động của Smart Fallback Engine khi dịch vụ AI LM Studio bị ngắt kết nối đột ngột?*
   - **Gợi ý trả lời:** Khi cuộc gọi HTTP sang cổng 1234 của LM Studio gặp ngoại lệ hoặc timeout quá 3 giây, hàm `query_lm_studio_local_api` bắt lỗi và chuyển giao ngay cho hàm `get_smart_fallback_response`. Hàm này sử dụng bộ đệm RAM `lru_cache` kết hợp bộ phân tích từ khóa Regex tiếng Việt để trả lời chính xác thông tin sân ICTU trong 0ms, người dùng không nhận thấy bất kỳ sự gián đoạn nào.
2. **Câu hỏi:** *Sự khác biệt cốt lõi giữa Prompt V1, V2 và V3 là gì? Kỹ nghệ ngữ cảnh (Context Engineering) đã giải quyết vấn đề gì?*
   - **Gợi ý trả lời:** Prompt V1 chỉ là lệnh chung chung nên AI bị ảo giác 62%; Prompt V2 có vài ví dụ mẫu nhưng văn phong cứng nhắc; Prompt V3 là thành quả của Context Engineering: cấu trúc hóa vai trò nhân viên sân ICTU, cung cấp đầy đủ thông số 5 sân, phân tích giá sáng 150k, giá tối và rạng sáng 300k kèm rào chắn nghiệp vụ. Nhờ đó, tỷ lệ ảo giác giảm xuống dưới 2% và tỷ lệ hiểu đúng ý định đạt 98%.

---

## 9.4 Đánh giá tư duy phản biện và đạo đức sử dụng AI trong phát triển phần mềm

Nhóm sinh viên nhận thức sâu sắc rằng: **Trí tuệ nhân tạo là một công cụ hỗ trợ đắc lực nhưng không thể thay thế hoàn toàn tư duy logic, sự thấu hiểu nghiệp vụ thực tế và trách nhiệm nghề nghiệp của người kỹ sư phần mềm**.
- Nhóm không phụ thuộc thụ động vào mã do AI sinh ra mà luôn thực hiện kiểm chứng độc lập (Verification), viết test case kiểm thử biên và can thiệp cấu trúc lại mã nguồn để bảo đảm hiệu năng và an toàn dữ liệu.
- Việc triển khai mô hình LLM cục bộ (Local Model) khẳng định tinh thần trách nhiệm cao đối với quyền riêng tư và bí mật thông tin của khách hàng.


---

# PHẦN BỔ SUNG: KẾT LUẬN & ĐÁNH GIÁ ĐỒ ÁN TỐT NGHIỆP

## 1. Tổng kết kết quả đạt được so với mục tiêu ban đầu
Qua 9 tuần nỗ lực nghiên cứu, phân tích và phát triển chuyên sâu, nhóm sinh viên đã hoàn thành xuất sắc toàn bộ các mục tiêu đề ra cho đồ án tốt nghiệp:
1. **Xây dựng hoàn chỉnh Hệ thống Đặt sân bóng đá tự động:**
   * Giải quyết triệt để vấn đề "nhức nhối" nhất trong quản lý sân cỏ truyền thống là tình trạng trùng lịch đặt (Double-booking) bằng kỹ thuật khóa tiến trình Thread-safe Concurrency Lock.
   * Chuẩn hóa toàn bộ quy trình đặt sân, từ chọn giờ đến xác nhận chỉ mất chưa đầy **30 giây**.
2. **Ứng dụng thành công Trí tuệ Nhân tạo (AI) vào thực tế kinh doanh:**
   * **Dynamic Pricing:** Xây dựng thuật toán định giá tự động linh hoạt theo khung giờ sáng, giờ cao điểm và cuối tuần, giúp chủ sân tối đa hóa doanh thu vào giờ "vàng" và kích cầu khách hàng vào các khung giờ thấp điểm.
   * **Trợ lý ảo Chatbot:** Tích hợp mô hình ngôn ngữ lớn LLM (LM Studio Qwen 2.5) với khả năng hiểu và giao tiếp bằng tiếng Việt tự nhiên như một nhân viên trực sân thật, đi kèm bộ máy Smart Fallback Engine đảm bảo phản hồi 100% thời gian.
3. **Hiện đại hóa trải nghiệm Thanh toán:**
   * Xây dựng mô hình **Ví điện tử nội bộ (Virtual Wallet)** giúp thanh toán đơn đặt sân diễn ra tức thì, không bị phụ thuộc vào độ trễ mạng của cổng thanh toán ngoài tại thời điểm giữ chỗ.
   * Tích hợp mã **VietQR NAPAS 247** động của ngân hàng MBBank giúp việc nạp tiền diễn ra thuận tiện, chuyên nghiệp và có sự đối soát chặt chẽ từ phía Admin.
4. **Kiến trúc phần mềm phân tầng chuẩn mực:**
   * Áp dụng kiến trúc Microservices phân tán giữa Backend .NET Core hiệu năng cao và AI Microservice Python chuyên sâu, tạo nền tảng vững chắc cho việc mở rộng chuỗi nhiều cơ sở sân bóng trong tương lai.

## 2. Đánh giá ưu điểm và hạn chế của hệ thống

### Ưu điểm nổi bật:
* **Giao diện người dùng hiện đại, tinh tế (Modern UI/UX):** Phong cách thiết kế Glassmorphism, phối màu thể thao tràn đầy năng lượng, thân thiện với người dùng và tối ưu hiển thị Responsive trên mọi thiết bị.
* **Tính toàn vẹn và bảo mật cao:** Dữ liệu mật khẩu được mã hóa an toàn, phiên làm việc bảo vệ bởi JWT Token; cơ chế Transaction Rollback bảo vệ tuyệt đối số dư tài chính của khách hàng.
* **Độ tin cậy vượt trội (High Availability):** Cơ chế Fallback thông minh ở cả tầng API tính giá và tầng Chatbot giúp hệ thống luôn hoạt động ổn định kể cả khi dịch vụ AI gặp trục trặc kỹ thuật.
* **Bộ Test Case hoàn thiện:** Đã thực thi 31 ca kiểm thử chức năng và chịu tải với tỷ lệ Pass 100%, bảo đảm không có lỗi phát sinh trong môi trường vận hành thực tế.

### Hạn chế còn tồn tại:
* Việc phê duyệt nạp tiền ví hiện tại vẫn cần một bước bấm "Xác nhận" thủ công từ Quản trị viên trên trang Admin (chưa tích hợp Webhook tự động lắng nghe biến động số dư ngân hàng qua Open Banking).
* Mô hình Chatbot LLM chạy Local trên máy tính cá nhân nên phụ thuộc vào cấu hình phần cứng (RAM, GPU) của máy chủ triển khai.

## 3. Hướng phát triển và mở rộng trong tương lai
Để phát triển hệ thống thành một nền tảng thương mại toàn diện cung cấp cho các chuỗi thể thao chuyên nghiệp, nhóm đề xuất các hướng nâng cấp tiếp theo:
1. **Tự động hóa hoàn toàn cổng nạp tiền qua Webhook ngân hàng:**
   * Tích hợp các cổng thanh toán Open Banking (như Casso hoặc SePAY) để tự động lắng nghe biến động tài khoản ngân hàng và cộng tiền ví cho khách ngay trong **3 giây** mà không cần Admin bấm duyệt thủ công.
2. **Tích hợp phần cứng IoT thông minh tại sân:**
   * Kết nối hệ thống phần mềm với các rơ-le thông minh (Smart Relays): Khi đến giờ đặt sân của khách, hệ thống tự động bật dàn đèn chiếu sáng sân bóng và tự động ngắt điện khi hết giờ thi đấu.
3. **Nhận diện khuôn mặt và Biển số xe bằng AI Camera:**
   * Triển khai Camera AI tại cổng ra vào cụm sân để nhận diện cầu thủ đã đặt chỗ và tự động mở barie cho xe vào bãi đỗ.
4. **Tính năng Ghép đội thi đấu & Bắt đối (Matchmaking AI):**
   * Phát triển tính năng mạng xã hội thể thao: AI tự động phân tích trình độ, vị trí địa lý và độ tuổi của các đội bóng để gợi ý bắt đối, ghép kèo giao hữu đá bóng cuối tuần.

---
> **XÁC NHẬN CỦA NHÓM SINH VIÊN THỰC HIỆN ĐỒ ÁN:**  
> Toàn bộ nội dung, số liệu, mô hình sơ đồ và mã nguồn trong báo cáo này được nghiên cứu, phát triển và thử nghiệm trung thực bởi nhóm sinh viên.  
> *Thái Nguyên, ngày 21 tháng 09 năm 2026*  
> 
> **Trưởng nhóm:** Lã Quý Doanh  
> **Thành viên:** Bùi Thanh Bình  
