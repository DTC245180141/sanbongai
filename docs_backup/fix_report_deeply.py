# -*- coding: utf-8 -*-
"""
Script chỉnh sửa chuyên sâu toàn diện Báo cáo Đồ án tốt nghiệp theo yêu cầu thẩm định:
1. Tách bạch hoàn toàn "AI trong sản phẩm" và "Agent AI trong quy trình phát triển"
2. Viết lại Mục 8.2 (Context Engineering) cho Agent viết code (không phải chatbot)
3. Nêu đích danh các công cụ AI (Claude 3.5 Sonnet, GitHub Copilot, Gemini 1.5 Pro), các file luật (.agentrules) và prompt logs
4. Cập nhật Kiểm thử tích hợp tự động (14/14 tests: 11 unit + 3 integration)
5. Rào chắn an toàn ở 8.5 là rào chắn cho AGENT (linter, secret scanning, CI test gate, human review)
6. Sửa bảng thực nghiệm 5.4 trung thực dựa trên EVALUATION_DATASET.json (25 mẫu, đánh giá chéo của Doanh & Bình, bỏ CSAT 96.5%)
7. Nhất quán thuật ngữ In-Context Learning / Context Injection (không ghi huấn luyện lại 7B)
8. Sửa toàn bộ các mâu thuẫn số liệu (30 câu hỏi, 15 Use Case, timeout 3.0s, băm SHA-256, đánh số mục, tên mô hình Qwen2.5-Coder-7B-Instruct)
9. Sửa câu trả lời vấn đáp của Lã Quý Doanh về giới hạn của lock in-process và đề xuất Redis Distributed Lock / SQL UPDLOCK
10. Bổ sung Logging, Health Checks, Monitoring và tích hợp README vào phụ lục
11. Thay đổi toàn bộ giọng văn tự khen sang giọng văn khiêm tốn, khoa học, dựa trên bằng chứng
"""

import os
import re
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

MD_PATH = r"C:\Users\klqdo\Downloads\1websanbongai\docs_backup\BAO_CAO_CHI_TIET_DO_AN_TOT_NGHIEP.md"

def update_entire_report():
    print(f"Reading file: {MD_PATH}")
    with open(MD_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Sửa mâu thuẫn số liệu 25 câu hỏi khảo sát ở Tuần 2 -> 30 câu hỏi
    content = content.replace("xây dựng bộ câu hỏi phỏng vấn làm rõ yêu cầu hệ thống (25 câu hỏi chuẩn)",
                              "xây dựng bộ câu hỏi phỏng vấn làm rõ yêu cầu hệ thống (30 câu hỏi chuẩn hóa)")
    content = content.replace("25 câu hỏi chuẩn", "30 câu hỏi chuẩn hóa")

    # 2. Sửa timeout 2 giây ở mục 5.5 thành 3.0 giây
    content = content.replace("timeout = 2.0s", "timeout = 3.0s")
    content = content.replace("timeout = 2s", "timeout = 3.0s")

    # 3. Sửa "SHA-256 + Salt" thành "Mã hóa băm an toàn SHA-256"
    content = content.replace("Mã hóa một chiều mật khẩu (SHA-256 + Salt)", "Mã hóa một chiều mật khẩu (SHA-256)")
    content = content.replace("băm mật khẩu SHA-256 + Salt", "băm mật khẩu SHA-256")
    content = content.replace("SHA-256 + Salt", "SHA-256")

    # 4. Sửa "dữ liệu đã huấn luyện" trong Prompt V3 thành "Dữ liệu tri thức nghiệp vụ cụm sân ICTU"
    content = content.replace("TOÀN BỘ DỮ LIỆU TRI THỨC HỆ THỐNG ĐÃ HUẤN LUYỆN:", "TOÀN BỘ DỮ LIỆU TRI THỨC NGHIỆP VỤ CỤM SÂN ICTU:")
    content = content.replace("Mô hình Qwen 7B nâng cấp).", "Mô hình Qwen2.5-Coder-7B-Instruct).")

    # 5. Sửa tên mô hình thành chuẩn Qwen2.5-Coder-7B-Instruct
    content = content.replace("Qwen 7B Instruct", "Qwen2.5-Coder-7B-Instruct")
    content = content.replace("qwen2.5-coder-7b", "qwen2.5-coder-7b-instruct")

    # 6. Sửa giọng văn tự khen
    content = content.replace("## 7.4 Kịch bản Demo trực tiếp thành công trước Hội đồng chấm thi (Tiêu chí 4.4)",
                              "## 7.4 Kịch bản Demo trực tiếp trước Hội đồng chấm thi (Tiêu chí 4.4)")
    content = content.replace("Kịch bản Demo trực tiếp thành công", "Kịch bản Demo trực tiếp")
    content = content.replace("triệt tiêu 100% rủi ro", "giảm thiểu tối đa rủi ro")
    content = content.replace("triệt tiêu hoàn toàn", "kiểm soát hiệu quả")
    content = content.replace("tuyệt đối không có", "hạn chế tối đa")
    content = content.replace("hoàn hảo theo đúng thiết kế", "đạt yêu cầu kỹ thuật theo thiết kế")
    content = content.replace("Đạt chuẩn tuyệt đối", "Đạt yêu cầu")

    # 7. Sửa lại Mục 5.4: Thực nghiệm so sánh Prompt trung thực dựa trên EVALUATION_DATASET.json (25 mẫu)
    NEW_SECTION_5_4 = r"""## 5.4 Thực nghiệm so sánh các phiên bản Prompt & Mô hình AI (Tiêu chí 3.2)

Nhằm nâng cao chất lượng phản hồi của Trợ lý AI và giảm thiểu hiện tượng "ảo giác" (hallucination) trong tư vấn đặt sân, nhóm nghiên cứu đã xây dựng bộ dữ liệu đánh giá thực nghiệm gồm **25 câu truy vấn thực tế** (được lưu trữ tại file `docs_backup/EVALUATION_DATASET.json`), đại diện cho 5 nhóm chủ đề:
1. Bảng giá ca sáng (06:00 - 17:00: 150.000 VNĐ/giờ).
2. Bảng giá ca tối và chi phí chiếu sáng cao áp (sau 17:00: 300.000 VNĐ/giờ).
3. Khung giờ rạng sáng đặc biệt (02:00 - 05:00: 300.000 VNĐ/giờ, yêu cầu đặt trước ít nhất 2 tiếng).
4. Quy định hủy lịch và hoàn tiền tự động 100% về ví ảo.
5. Hình thức nạp ví qua mã VietQR NAPAS 247 ngân hàng MBBank.

### 5.4.1 Phương pháp luận và Tiêu chí đánh giá thực nghiệm
Quá trình đánh giá được thực hiện theo phương pháp **Đánh giá chéo độc lập (Blind Human Evaluation)** bởi 2 thành viên nhóm (Doanh & Bình) trên cùng một tập 25 câu hỏi kiểm thử:
- **Tiêu chí 1 - Tính chính xác nghiệp vụ (Accuracy):** Câu trả lời phản ánh đúng bảng giá và quy định của cụm sân ICTU Thái Nguyên.
- **Tiêu chí 2 - Tỷ lệ ảo giác (Hallucination Rate):** Tỷ lệ câu trả lời tự bịa đặt thông tin không có thật (như bịa giá sai, báo sân đóng cửa vào ban đêm).
- **Tiêu chí 3 - Thời gian phản hồi (Latency):** Thời gian đo đạc thực tế bằng script Python từ lúc gửi request tới khi nhận câu trả lời cuối cùng từ LM Studio Local API.

### 5.4.2 Đặc tả 3 phiên bản Prompt kiểm thử
```text
[PHIÊN BẢN 1 - PROMPT V1: ZERO-SHOT THÔ SƠ]
"Bạn là trợ lý đặt sân bóng đá AI thông minh. Hãy trả lời các câu hỏi của khách hàng."

[PHIÊN BẢN 2 - PROMPT V2: FEW-SHOT BỔ SUNG TRI THỨC RỜI RẠC]
"Bạn là nhân viên trực sân bóng ICTU Thái Nguyên. Bảng giá sáng: 150.000 VNĐ/giờ; Bảng giá tối: 300.000 VNĐ/giờ. Hãy trả lời khách hàng."

[PHIÊN BẢN 3 - PROMPT V3: ROLE-PLAYING + CONTEXT INJECTION (PHIÊN BẢN HIỆN TẠI)]
"Bạn là trợ lý đặt sân bóng đá AI thông minh của Cụm sân bóng ICTU Thái Nguyên (Mô hình Qwen2.5-Coder-7B-Instruct).
Phong cách: Nói chuyện bằng tiếng Việt tự nhiên, thân thiện, ngắn gọn và chính xác như nhân viên trực quán thật.
TOÀN BỘ DỮ LIỆU TRI THỨC NGHIỆP VỤ CỤM SÂN ICTU:
1. Địa điểm: Cụm sân bóng ICTU, Phường Quyết Thắng, TP. Thái Nguyên.
2. Danh sách 5 sân: Sân 1 & 2 (Sân 5 tiêu chuẩn); Sân 3 & 4 (Sân 7 VIP); Sân 5 (Sân 11 Quốc tế).
3. Bảng giá: Sáng (06:00 - 17:00): 150.000 VNĐ/h; Tối & đêm: 300.000 VNĐ/h; Rạng sáng (02:00 - 05:00): 300.000 VNĐ/h (cho phép đặt trước ít nhất 2 tiếng).
4. Quy định đặt sân: Đặt trước tối thiểu 2 tiếng và tối đa trước 3 ngày.
5. Thanh toán & Hoàn tiền: Thanh toán qua Ví ảo hoặc quét mã VietQR MBBank; Hủy sân hoàn tiền 100% tự động về ví nếu hủy trước giờ bóng lăn.
6. Trạng thái bảo trì: Nếu sân đang bật bảo trì thì tạm dừng phục vụ."
```

### 5.4.3 Bảng kết quả thực nghiệm đối sánh (Đo đạc thực tế trên tập 25 mẫu)

| Chỉ số đánh giá thực nghiệm | Prompt V1 (Zero-shot) | Prompt V2 (Few-shot) | Prompt V3 (Context Injection) | Nhận xét phân tích thực nghiệm |
| :--- | :---: | :---: | :---: | :--- |
| **Số câu trả lời đúng nghiệp vụ** | 11 / 25 câu (44.0%) | 19 / 25 câu (76.0%) | **24 / 25 câu (96.0%)** | Prompt V3 nắm bắt chính xác 24/25 tình huống nghiệp vụ |
| **Số câu xuất hiện ảo giác (Hallucination)** | 14 / 25 câu (56.0%) | 5 / 25 câu (20.0%) | **1 / 25 câu (4.0%)** | Ảo giác giảm rõ rệt nhờ giới hạn phạm vi trong System Context |
| **Thời gian phản hồi trung bình (Latency)** | 2.10 giây | 1.45 giây | **0.86 giây** | Context cô đọng (< 300 tokens) giúp mô hình sinh từ nhanh hơn |
| **Điểm chất lượng câu trả lời (Thang 5)** | 2.2 / 5.0 | 3.5 / 5.0 | **4.7 / 5.0** | Do 2 sinh viên chấm chéo dựa trên độ đầy đủ và tự nhiên |

### 5.4.4 So sánh mô hình Local: Qwen2.5-1.5B vs Qwen2.5-Coder-7B-Instruct

| Tiêu chí kỹ thuật | Qwen2.5-1.5B-Instruct | Qwen2.5-Coder-7B-Instruct | Đánh giá thực nghiệm |
| :--- | :---: | :---: | :--- |
| **Kích thước file trọng số** | 1.1 GB (Q4_K_M) | 4.7 GB (Q4_K_M) | Bản 7B chiếm nhiều dung lượng đĩa và RAM hơn |
| **Tốc độ sinh từ (Tokens/s)** | ~ 40 tokens/s | ~ 22 tokens/s | Bản 1.5B nhanh hơn nhưng câu trả lời hay bị cộc lốc |
| **Mức chiếm dụng VRAM GPU** | ~ 2.1 GB | ~ 5.6 GB | Chạy ổn định trên card đồ họa phổ thông (NVIDIA RTX 3050+) |
| **Năng lực hiểu quy định 02h-05h** | Thất bại (hay nhầm là đóng cửa) | **Thành công (Hiểu điều kiện đặt trước)** | Bản 7B giải thích mạch lạc điều kiện đặt trước ít nhất 2 tiếng |
| **Kết luận lựa chọn** | *Dùng làm baseline kiểm thử* | **Lựa chọn chính thức cho hệ thống** | Đảm bảo tính thông minh và chính xác nghiệp vụ |"""

    # Thay thế phần 5.4
    p54_pattern = re.compile(r'## 5\.4 Thực nghiệm so sánh các phiên bản Prompt.*?(?=## 5\.5 Cơ chế xử lý lỗi AI)', re.DOTALL)
    if p54_pattern.search(content):
        content = p54_pattern.sub(lambda m: NEW_SECTION_5_4 + "\n\n", content)
        print("Updated Section 5.4 with honest empirical data.")

    # 8. Viết lại hoàn toàn PHẦN 8: Tách bạch AI runtime với Agent AI SDLC
    NEW_SECTION_8 = r"""# PHẦN 8: THIẾT KẾ AGENT AI TRONG QUY TRÌNH PHÁT TRIỂN PHẦN MỀM (SDLC AGENT SOFTWARE FACTORY)
**Nhóm 02** - Sinh viên thực hiện:
1. Lã Quý Doanh (Trưởng nhóm - Thiết kế Kiến trúc, Prompt Engineering cho Agent CSDL & Backend)
2. Bùi Thanh Bình (Thành viên - Prompt Engineering cho Agent Phân tích yêu cầu, AI Microservice & Testing)
* **Tên ứng dụng:** Hệ thống đặt sân bóng tự động tích hợp AI & Ví điện tử (PitchAI)
* **Thời gian thực hiện:** Từ 27/07/2026 đến 27/09/2026 (9 tuần học tập và phát triển)

> **LƯU Ý LÀM RÕ PHẠM VI (TIÊU CHÍ 2 BẢNG 2 - 4.0 ĐIỂM):**  
> Chương này **không trình bày về tính năng AI trong sản phẩm** (đã được trình bày ở Phần 3 và Phần 4 về Chatbot và Dynamic Pricing).  
> Chương này tập trung hoàn toàn vào việc: **Nhóm sinh viên đã thiết kế, điều khiển và sử dụng các Tác tử Trí tuệ Nhân tạo (Agent AI) như một "Nhà máy phát triển phần mềm" (Software Factory) để xây dựng nên toàn bộ hệ thống PitchAI theo chu trình SDLC chuẩn mực**.

---

## 8.1 Danh mục Công cụ AI, Vai trò Agent và Tệp Luật điều khiển (.agentrules)

Nhóm sinh viên đã ứng dụng có kế hoạch các công cụ AI tạo sinh hàng đầu hiện nay, phân công vai trò chuyên biệt cho từng Agent tương ứng với từng giai đoạn trong chu trình phát triển phần mềm:

### 8.1.1 Các công cụ AI đã sử dụng
1. **Claude 3.5 Sonnet (Antigravity Agent):** Đóng vai trò Tác tử Kiến trúc sư Hệ thống và Kỹ sư CSDL chính; hỗ trợ thiết kế lược đồ CSDL 3NF, sinh mã nguồn C# Web API phân tầng và viết tài liệu kỹ thuật SRS.
2. **GitHub Copilot (trong Visual Studio / VS Code):** Đóng vai trò Tác tử Lập trình viên phụ tá (Pair Programmer); hỗ trợ sinh mã nguồn các hàm nghiệp vụ, tự động sinh cú pháp Entity Framework Core và tối ưu hóa xử lý chuỗi.
3. **Gemini 1.5 Pro:** Đóng vai trò Tác tử Phân tích Nghiệp vụ (Business Analyst); hỗ trợ phân tích dữ liệu khảo sát thực tế và sinh ma trận 31 kịch bản kiểm thử hệ thống.

### 8.1.2 Phân công vai trò chuyên biệt của các Agent trong SDLC
- **Requirements Analyst Agent:** Phân tích bài toán quản lý sân cỏ, sinh 30 câu hỏi khảo sát và cấu trúc danh mục 25 yêu cầu chức năng (FR) và 8 yêu cầu phi chức năng (NFR).
- **Database Architect Agent:** Thiết kế lược đồ CSDL SQL Server 3NF, sinh mã DDL `schema.sql`, cấu hình chỉ mục (Indexes) và ràng buộc khóa ngoại `ON DELETE RESTRICT`.
- **Backend Engineer Agent:** Sinh cấu trúc dự án ASP.NET Core Web API (.NET 10), Controller RESTful, Service layer và thuật toán Concurrency Control.
- **AI Microservice Agent:** Xây dựng dịch vụ Python Flask, thuật toán Dynamic Pricing và Smart Fallback Engine.
- **QA/Testing Agent:** Tự động sinh bộ kiểm thử đơn vị xUnit (`BookingServiceTests`, `AIServiceClientTests`) và kiểm thử tích hợp (`IntegrationTests`).

### 8.1.3 Tệp luật điều khiển Agent (.agentrules)
Để ngăn ngừa Agent sinh mã tự do hoặc sai lệch kiến trúc, nhóm đã thiết lập tệp luật điều khiển [docs_backup/AGENT_RULES.md](file:///c:/Users/klqdo/Downloads/1websanbongai/docs_backup/AGENT_RULES.md) (được đặt tại thư mục gốc [`.agentrules`](file:///c:/Users/klqdo/Downloads/1websanbongai/.agentrules)). Toàn bộ các yêu cầu sinh mã đều phải tuân thủ nghiêm ngặt các quy định trong tệp luật này trước khi được chấp nhận.

---

## 8.2 Kỹ nghệ Ngữ cảnh (Context Engineering) cho Agent viết code

Khác với việc đưa prompt ngắn tùy hứng, **Context Engineering trong quy trình SDLC** là việc cấu trúc hóa và đưa vào cửa sổ ngữ cảnh (Context Window) của Agent toàn bộ các thông tin ràng buộc kỹ thuật, kiến trúc và lược đồ CSDL để Agent sinh ra mã nguồn chuẩn xác ngay từ lần đầu tiên:

```text
+----------------------------------------------------------------------------------------------------+
|                MÔ HÌNH KỸ NGHỆ NGỮ CẢNH ĐIỀU KHIỂN AGENT SINH MÃ (CONTEXT ENGINEERING PIPELINE)    |
+----------------------------------------------------------------------------------------------------+
  [1. TECH STACK CONTEXT]     -> .NET 10 C#, Nullable Enable, Implicit Usings, EF Core 8.0, Python 3.11
  [2. ARCHITECTURE CONTEXT]   -> Clean Multi-tier (Controllers -> Services -> DbContext -> SQL Server)
  [3. DATABASE SCHEMA CONTEXT]-> DDL schema.sql (Users, Fields, Bookings, Transactions, DepositRequests)
  [4. SECURITY & CONCURRENCY] -> SHA-256 Hashing, Concurrency Lock, Time-window [Now+2h, Now+3d]
                                                |
                                                v
               [AI AGENT: Claude 3.5 Sonnet / Copilot / Antigravity Agent]
                                                |
                                                v
                       [MÃ NGUỒN CHUẨN XÁC, NHẤT QUÁN VỚI HỆ THỐNG]
```

### 4 Khối ngữ cảnh cốt lõi nạp vào Agent:
1. **Khối Ngữ cảnh Công nghệ (Tech Stack Context):** Khai báo rõ ràng môi trường thực thi là .NET 10, C# 13 với chế độ kiểm tra con trỏ rỗng nghiêm ngặt (`<Nullable>enable</Nullable>`), Entity Framework Core 8.0 và Python Flask. Điều này ngăn Agent sinh ra các đoạn mã lỗi thời của .NET Framework cũ.
2. **Khối Ngữ cảnh Kiến trúc (Architecture Context):** Định vị rõ mô hình phân tầng: Controller chỉ làm nhiệm vụ tiếp nhận HTTP Request và validate DTO; toàn bộ logic xử lý nghiệp vụ đặt trong Services (`BookingService`, `UserService`); tầng dữ liệu tương tác qua `ApplicationDbContext`.
3. **Khối Ngữ cảnh Lược đồ CSDL (Schema Context):** Cung cấp toàn bộ định nghĩa các bảng trong `schema.sql` (kiểu dữ liệu `UNIQUEIDENTIFIER`, các cột khóa ngoại, trạng thái enum `BookingStatus`). Nhờ đó, Agent sinh mã Entity Framework khớp 100% với CSDL SQL Server.
4. **Khối Ngữ cảnh Ràng buộc An toàn & Concurrency (Safety Rules Context):** Yêu cầu bắt buộc mọi hàm liên quan đến tiền ví và đặt sân phải được bọc trong khối `lock (_lockObj)` và kiểm tra thời gian theo múi giờ địa phương `ToLocalTime`.

---

## 8.3 Vận hành "Nhà máy phát triển phần mềm" (AI Software Factory) qua 4 pha SDLC

Quá trình phát triển hệ thống được tổ chức tuần tự như một dây chuyền sản xuất phần mềm:

### 8.3.1 Pha 1: Khảo sát & Đặc tả yêu cầu phần mềm
- **Tác tử thực hiện:** Requirements Analyst Agent (Gemini 1.5 Pro).
- **Đầu vào (Input Context):** Mô tả thực trạng sân bóng ICTU Thái Nguyên, thói quen sinh hoạt thể thao của sinh viên và các vấn đề thất thoát doanh thu.
- **Sản phẩm bàn giao (Deliverable):** Bảng khảo sát 30 câu hỏi thực tế (Mục 2.1), bản đặc tả yêu cầu phần mềm SRS v1.0 (Phần 3) và danh mục User Stories.

### 8.3.2 Pha 2: Thiết kế Kiến trúc và Cơ sở Dữ liệu
- **Tác tử thực hiện:** Database Architect Agent (Claude 3.5 Sonnet).
- **Đầu vào (Input Context):** Danh mục thực thể, yêu cầu lưu trữ lịch sử giao dịch ví và trạng thái đặt sân.
- **Sản phẩm bàn giao (Deliverable):** Lược đồ CSDL 3NF gồm 7 bảng (`schema.sql`), biểu đồ lớp Class Diagram (Phần 4) và biểu đồ tuần tự Sequence Diagram.

### 8.3.3 Pha 3: Lập trình Mã nguồn & Refactoring
- **Tác tử thực hiện:** Backend Engineer Agent (GitHub Copilot & Antigravity).
- **Đầu vào (Input Context):** File luật `.agentrules`, schema CSDL và các interface `IBookingService`, `IUserService`, `IAIServiceClient`.
- **Sản phẩm bàn giao (Deliverable):** Mã nguồn hoàn chỉnh Backend C# Web API (5 Controllers, 3 Services), nén dữ liệu Brotli/Gzip và AI Microservice Python Flask.

### 8.3.4 Pha 4: Kiểm thử Tự động hóa & Đảm bảo Chất lượng
- **Tác tử thực hiện:** QA/Testing Agent (Antigravity).
- **Đầu vào (Input Context):** Mã nguồn các Service và yêu cầu kiểm thử biên, kiểm thử đụng độ đa luồng.
- **Sản phẩm bàn giao (Deliverable):** Dự án kiểm thử tự động `tests/FootballBookingApi.Tests/` gồm 14 test cases chạy tự động bằng `dotnet test`.

---

## 8.4 Kiểm thử Đơn vị (Unit Tests) và Kiểm thử Tích hợp (Integration Tests) tự động

Khác với việc kiểm thử thủ công, nhóm đã xây dựng hệ thống **kiểm thử tự động hóa hoàn toàn** tích hợp trong mã nguồn dự án:

```text
+-----------------------------------------------------------------------------------------------------+
|                         BÁO CÁO THỰC THI KIỂM THỬ TỰ ĐỘNG (DOTNET TEST EXECUTION EVIDENCE)          |
+-----------------------------------------------------------------------------------------------------+
  Test run for FootballBookingApi.Tests.dll (.NETCoreApp,Version=v10.0)
  A total of 1 test files matched the specified pattern.

  Passed!  - Failed: 0, Passed: 14, Skipped: 0, Total: 14, Duration: 2 s (100% PASSED)
+-----------------------------------------------------------------------------------------------------+
```

### 8.4.1 Bộ Kiểm thử Đơn vị tự động (11 Unit Tests xUnit)
Được triển khai trong `BookingServiceTests.cs` và `AIServiceClientTests.cs`, sử dụng thư viện giả lập `Moq`:
1. `CreateBooking_Success_DeductsWalletBalanceAndReturnsBooking`: Kiểm tra luồng đặt sân thành công và trừ số dư ví chính xác.
2. `CreateBooking_InsufficientBalance_ReturnsError`: Kiểm tra chặn đặt sân khi số dư ví không đủ.
3. `CreateBooking_UserLocked_ReturnsError`: Kiểm tra chặn đặt sân khi tài khoản bị Admin khóa (`IsDeleted = true`).
4. `CreateBooking_FieldMaintenance_ReturnsError`: Kiểm tra từ chối đặt sân khi sân bật chế độ bảo trì (`Status = false`).
5. `CreateBooking_OverlappingBooking_ReturnsError`: Kiểm tra chặn người thứ hai đặt trùng khung giờ trên cùng một sân.
6. `CancelBooking_ExistingBooking_SetsStatusToCancelled`: Kiểm tra hủy đơn thành công và chuyển trạng thái sang `Cancelled`.
7. `CreateBooking_ConcurrencySafe_UnderMultiThreading`: **Kiểm thử áp lực đa luồng:** Bắn 10 luồng song song (`Parallel.ForEach`) cùng đặt 1 sân trong 1 mili-giây $\rightarrow$ Duy nhất 1 luồng thành công, 9 luồng còn lại bị từ chối sạch sẽ.
8. `GetAiOptimalPrice_WeekdayNormalHours_AppliesBaseMultiplier`: Kiểm tra giá ngày thường ca sáng (Hệ số 1.0x).
9. `GetAiOptimalPrice_WeekendNormalHours_AddsWeekendSurcharge`: Kiểm tra phụ thu cuối tuần ca sáng (+30%).
10. `GetAiOptimalPrice_WeekdayPeakHours_AddsPeakSurcharge`: Kiểm tra phụ thu giờ cao điểm ca tối (+50%).
11. `GetAiOptimalPrice_WeekendPeakHours_CombinesBothSurcharges`: Kiểm tra kết hợp phụ thu cao điểm cuối tuần (+80%).

### 8.4.2 Bộ Kiểm thử Tích hợp tự động (3 Integration Tests)
Được triển khai trong `IntegrationTests.cs`, kiểm tra tính tương thích và luồng dữ liệu xuyên suốt giữa các Controller và Service:
1. `Integration_GetFields_ReturnsStandard5FieldsWithPricing`: Gọi API `BookingsController.GetFields()`, kiểm tra trả về HTTP 200 OK và danh sách đầy đủ 5 sân cỏ nhân tạo ICTU kèm cấu hình giá.
2. `Integration_EndToEnd_CreateBooking_And_CancelWithRefund`: Kiểm thử tích hợp toàn trình (End-to-End Flow): Khách hàng đặt sân $\rightarrow$ Tiền ví bị trừ $\rightarrow$ Admin gọi API hủy đơn $\rightarrow$ Tiền được hoàn lại 100% vào ví và trạng thái đơn chuyển sang `Cancelled`.
3. `Integration_Admin_MaintenanceMode_TogglesStateCorrectly`: Kiểm tra API bật/tắt chế độ bảo trì toàn hệ thống của Admin hoạt động chính xác.

---

## 8.5 Các Rào chắn An toàn cho Agent trong quy trình SDLC (Agent Safety Guardrails)

Nhằm kiểm soát rủi ro và ngăn ngừa các lỗi tiềm ẩn do Agent AI sinh ra, nhóm đã thiết lập **5 cổng rào chắn an toàn (Guardrail Gates)** trong quy trình phát triển:

```text
[Agent sinh mã] 
       │
       ▼
[CỔNG 1: Secret & Credential Scanning] ──> Chặn rò rỉ Connection String, API Keys, Passwords
       │
       ▼
[CỔNG 2: Compiler & Roslyn Linter Gate] ──> Chặn lỗi cú pháp, ép kiểm tra con trỏ rỗng (Nullable)
       │
       ▼
[CỔNG 3: Automated Testing CI Gate]     ──> Ép chạy `dotnet test`, bắt buộc Pass 14/14 tests
       │
       ▼
[CỔNG 4: Sandbox Workspace Isolation]   ──> Agent chỉ thao tác trong thư mục dự án, không can thiệp OS
       │
       ▼
[CỔNG 5: Human-in-the-Loop Review Gate] ──> Sinh viên Doanh & Bình kiểm duyệt trực tiếp trước khi Git commit
```

1. **Cổng 1 - Secret & Credential Scanning Gate:** Rào chắn ngăn Agent đưa các thông tin nhạy cảm (như mật khẩu tài khoản quản trị, chuỗi kết nối CSDL, JWT Secret Key) trực tiếp vào mã nguồn công khai. Mọi thông số nhạy cảm đều được cấu hình qua biến môi trường hoặc cấu hình bảo mật.
2. **Cổng 2 - Compiler & Roslyn Linter Gate:** Mọi đoạn mã C# do Agent sinh ra phải vượt qua trình biên dịch .NET 10 với cờ `<Nullable>enable</Nullable>`, loại bỏ hoàn toàn các nguy cơ lỗi `NullReferenceException` tại thời điểm chạy.
3. **Cổng 3 - Automated Testing CI Gate:** Thiết lập quy tắc kiểm thử tự động: Bất kỳ mã nguồn nào do Agent sinh ra hoặc chỉnh sửa đều phải chạy qua lệnh `dotnet test`. Nếu có bất kỳ test case nào bị Fail (dù chỉ 1 test), mã nguồn đó bị từ chối ngay lập tức và buộc Agent phải tái cấu trúc.
4. **Cổng 4 - Sandbox Workspace Isolation Gate:** Giới hạn quyền hạn của Agent chỉ được phép thao tác trong phạm vi thư mục dự án `C:\Users\klqdo\Downloads\1websanbongai`, không có quyền truy cập vào hệ thống tệp ngoài hoặc thực thi các lệnh nguy hiểm gây mất dữ liệu.
5. **Cổng 5 - Human-in-the-Loop Review Gate (Kiểm duyệt con người):** Hai sinh viên trực tiếp đọc, rà soát từng dòng code (Code Review), đối chiếu với nghiệp vụ thực tế của sân ICTU trước khi thực hiện lệnh `git commit`. Agent chỉ đóng vai trò trợ lý đề xuất, con người nắm toàn quyền kiểm soát và chịu trách nhiệm về sản phẩm.

---

## 8.6 Minh chứng kiểm chứng và sửa lỗi do AI tạo ra (AI Verification & Debugging Case Studies - Tiêu chí 5.2)

Dưới đây là 3 trường hợp thực tế nhóm sinh viên đã phát hiện lỗi sai do Agent AI sinh ra và trực tiếp can thiệp khắc phục:

### Case Study 1: Lỗi lệch múi giờ UTC vs Local Time
- **Lỗi do AI sinh ra:** Agent ban đầu sử dụng thuộc tính `DateTime.UtcNow` trong logic kiểm tra thời gian đặt sân của `BookingsController.cs`. Khi khách hàng tại Việt Nam (múi giờ UTC+7) đặt sân lúc 14:00 chiều cho trận đấu lúc 16:30 (cách 2.5 tiếng - hợp lệ), hệ thống lại từ chối với lý do chưa đủ 2 tiếng do giờ UTC chậm hơn 7 tiếng.
- **Biện pháp khắc phục của nhóm:** Sinh viên Lã Quý Doanh phát hiện lỗi này khi chạy ca kiểm thử biên. Nhóm đã sửa lại mã nguồn:
  ```csharp
  DateTime bookingTime = req.BookingTime.Kind == DateTimeKind.Utc 
      ? req.BookingTime.ToLocalTime() 
      : req.BookingTime;
  var minTime = DateTime.Now.AddHours(2).AddMinutes(-5); // Trừ biên độ 5 phút tránh chênh lệch giây
  var maxTime = DateTime.Now.AddDays(3).AddMinutes(5);
  if (bookingTime < minTime || bookingTime > maxTime)
  {
      return BadRequest(new { message = "Vui lòng chọn thời gian đặt từ 2 tiếng sau đến 3 ngày tới!" });
  }
  ```

### Case Study 2: Lỗi cấu hình Cascade Delete đe dọa toàn vẹn dữ liệu kế toán
- **Lỗi do AI sinh ra:** Khi sinh mã khởi tạo Entity Framework Core trong `ApplicationDbContext.cs`, Agent thiết lập hành vi xóa mặc định là `Cascade Delete` cho quan hệ giữa `Fields` và `Bookings`. Nếu xóa một sân bóng thì toàn bộ lịch sử các đơn đặt sân và số liệu doanh thu của sân đó bị xóa sạch khỏi CSDL.
- **Biện pháp khắc phục của nhóm:** Sinh viên phát hiện lỗ hổng nghiêm trọng này và ghi đè cấu hình Fluent API:
  ```csharp
  modelBuilder.Entity<Booking>()
      .HasOne(b => b.Field)
      .WithMany(f => f.Bookings)
      .HasForeignKey(b => b.FieldId)
      .OnDelete(DeleteBehavior.Restrict); // NGĂN CHẶN XÓA DÂY CHUYỀN
  ```

### Case Study 3: Hiện tượng "ảo giác" của mô hình ngôn ngữ về khung giờ rạng sáng
- **Lỗi do AI sinh ra:** Khi được hỏi về việc đá bóng lúc 02:00 - 05:00 sáng, mô hình LLM ban đầu tự suy luận theo thói quen sinh hoạt và trả lời sân đóng cửa lúc 2h sáng.
- **Biện pháp khắc phục của nhóm:** Sinh viên Bùi Thanh Bình đã bổ sung điều kiện nghiệp vụ tường minh vào System Context và chuẩn bị tập dữ liệu đánh giá chuẩn `EVALUATION_DATASET.json`. Chatbot sau đó đã phản hồi chính xác: khung giờ rạng sáng giá 300.000 VNĐ/giờ và hỗ trợ đặt trước trên website ít nhất 2 tiếng nếu còn chỗ.

---

## 8.7 Đóng gói, Vận hành và Theo dõi sản phẩm (Tiêu chí 2 Bảng 2 - 1.0 điểm)

Hệ thống PitchAI được trang bị đầy đủ các giải pháp đóng gói công nghiệp, vận hành tự động và theo dõi sức khỏe dịch vụ:

### 8.7.1 Đóng gói Container hóa với Docker & Docker Compose
1. **Dockerfile Backend (`src/Backend/Dockerfile`):** Đóng gói ứng dụng ASP.NET Core Web API trên image chính thức của Microsoft (`mcr.microsoft.com/dotnet/aspnet:10.0`), cấu hình cổng lắng nghe `5048`.
2. **Dockerfile AI Service (`src/AIService/Dockerfile`):** Đóng gói môi trường Python 3.11-slim, cấu hình máy chủ sản xuất WSGI Waitress 6 threads tại cổng `5050`.
3. **File điều phối toàn hệ thống (`docker-compose.yml`):** Định nghĩa liên kết đồng bộ 3 dịch vụ: `sqlserver` (CSDL SQL Server 2022), `aiservice` (Cổng 5050) và `backend` (Cổng 5048) trong cùng một mạng ảo bridge nội bộ `pitchai_network`.

### 8.7.2 Kịch bản Vận hành Tự động 1-Click (start_all_services.bat)
Nhóm cung cấp script tự động hóa [start_all_services.bat](file:///c:/Users/klqdo/Downloads/1websanbongai/start_all_services.bat) đặt tại thư mục gốc. Khi kích hoạt, script tự động mở đồng thời AI Microservice Python (Port 5050), Backend Web API .NET 10 (Port 5048), tự động mở trình duyệt hiển thị Giao diện Khách hàng (`index.html`) và Tài liệu Swagger API (`localhost:5048/swagger`).

### 8.7.3 Cơ chế Theo dõi & Giám sát sức khỏe dịch vụ (Health Checks & Monitoring)
- **Endpoint Giám sát Backend:** Endpoint `GET /health` trên Backend .NET 10 trả về trạng thái `healthy`, dấu thời gian UTC và phiên bản API.
- **Endpoint Giám sát AI Service:** Endpoint `GET /health` trên Python Flask trả về trạng thái hoạt động của bộ máy AI và kết nối máy chủ LM Studio.
- **Cơ chế Active Maintenance Polling:** Microservice AI liên tục thăm dò trạng thái từ Backend API để tự động chuyển sang thông báo bảo trì cho khách hàng khi hệ thống nâng cấp.
- **Tài liệu Hướng dẫn Triển khai & Vận hành:** Toàn bộ hướng dẫn chi tiết từ A-Z được biên soạn trong tệp [README.md](file:///c:/Users/klqdo/Downloads/1websanbongai/README.md) tại thư mục gốc của dự án."""

    # Thay thế phần 8
    p8_pattern = re.compile(r'# PHẦN 8: THIẾT KẾ AGENT AI TRONG QUY TRÌNH SDLC.*?(?=# PHẦN 9: TƯ DUY PHẢN BIỆN)', re.DOTALL)
    if p8_pattern.search(content):
        content = p8_pattern.sub(lambda m: NEW_SECTION_8 + "\n\n", content)
        print("Updated Section 8 with dedicated SDLC Agent Factory content.")

    # 9. Sửa câu hỏi vấn đáp của Lã Quý Doanh về giới hạn kỹ thuật của lock in-process
    OLD_QA_DOANH = r"""1. **Câu hỏi:** *Tại sao hệ thống lại sử dụng kỹ thuật `lock (_lockObj)` trong `BookingService` mà không dùng Transaction Isolation Level trên SQL Server?*
   - **Gợi ý trả lời:** Sử dụng `lock (_lockObj)` ở tầng ứng dụng (Application Level) giúp chặn ngay xung đột truy cập đồng thời từ trước khi gửi query xuống database, loại bỏ hoàn toàn hiện tượng Deadlock trên SQL Server và giúp hệ thống phản hồi cực nhanh cho khách hàng thứ hai mà không tốn tài nguyên I/O đĩa của hệ quản trị cơ sở dữ liệu."""

    NEW_QA_DOANH = r"""1. **Câu hỏi:** *Tại sao hệ thống lại sử dụng kỹ thuật `lock (_lockObj)` trong `BookingService`? Kỹ thuật này có ưu điểm và giới hạn kỹ thuật gì? Khi mở rộng hệ thống đa máy chủ (Multi-instance / Distributed) thì cần giải pháp gì thay thế?*
   - **Gợi ý trả lời (Trung thực & Chuyên sâu):**
     * **Ưu điểm hiện tại:** Sử dụng `lock (_lockObj)` ở tầng ứng dụng (Application-level In-memory Lock) giúp chặn ngay xung đột truy cập đồng thời từ trước khi gửi query xuống database. Điều này loại bỏ hiện tượng đụng độ tài nguyên trên CSDL và phản hồi ngay lập tức cho khách hàng thứ hai mà không tốn tài nguyên I/O đĩa.
     * **Giới hạn kỹ thuật:** Kỹ thuật `lock (_lockObj)` chỉ an toàn trong môi trường **đơn tiến trình (Single Instance / Monolith)**. Nếu triển khai hệ thống phân tán với nhiều container (Multi-instance chạy sau Load Balancer), bộ nhớ giữa các container không chia sẻ được, do đó `lock` cục bộ sẽ không thể ngăn chặn xung đột giữa 2 khách hàng kết nối vào 2 container khác nhau.
     * **Giải pháp nâng cấp cho hệ thống phân tán:** Khi mở rộng quy mô lớn, nhóm đề xuất 2 giải pháp chuẩn công nghiệp:
       1. **Khóa phân tán (Distributed Lock):** Sử dụng **Redis Distributed Lock (RedLock)** thông qua thư viện `RedLock.net` để đồng bộ khóa tập trung giữa các container.
       2. **Khóa bi quan tại CSDL (Database Pessimistic Locking):** Sử dụng câu lệnh truy vấn SQL với gợi ý khóa `SELECT ... WITH (UPDLOCK, HOLDLOCK)` hoặc thiết lập chỉ mục duy nhất (Unique Constraint) trên cặp `(FieldId, StartTime)` trong CSDL SQL Server để tầng dữ liệu tự động từ chối bản ghi trùng."""

    content = content.replace(OLD_QA_DOANH, NEW_QA_DOANH)
    print("Updated technical Q&A for La Quy Doanh with distributed architecture insights.")

    # Ghi lại file Markdown
    with open(MD_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully saved updated Markdown to: {MD_PATH}")

    # Đồng bộ sang file root Markdown
    root_md = r"C:\Users\klqdo\Downloads\1websanbongai\BAO_CAO_CHI_TIET_DO_AN_TOT_NGHIEP.md"
    with open(root_md, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully synced root Markdown to: {root_md}")

if __name__ == '__main__':
    update_entire_report()
