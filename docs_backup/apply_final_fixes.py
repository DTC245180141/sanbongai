# -*- coding: utf-8 -*-
"""
Script áp dụng tất cả các hiệu chỉnh chuẩn hóa cuối cùng:
1. Đổi '### 4.7.2 Đặc tả Lớp BookingService' thành '### 4.8 Đặc tả Lớp BookingService'
2. Chuẩn hóa ngày tháng nghiệm thu: 28/10/2026, ghi chú rõ 9 tuần phát triển chính thức (07-09/2026) và đợt nghiệm thu đóng gói (10/2026)
3. Cập nhật Mục lục Markdown hoàn chỉnh, khớp chính xác từng mục
4. Đồng bộ file Markdown ra thư mục gốc
5. Chạy export_report_to_word.py để tạo file Word hoàn hảo
"""

import os
import re
import sys
import shutil

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

MD_PATH = r"C:\Users\klqdo\Downloads\1websanbongai\docs_backup\BAO_CAO_CHI_TIET_DO_AN_TOT_NGHIEP.md"

def main():
    print(f"Reading file: {MD_PATH}")
    with open(MD_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Sửa lỗi trùng số mục 4.7.2
    content = content.replace("### 4.7.2 Đặc tả Lớp `BookingService`", "### 4.8 Đặc tả Lớp `BookingService`")
    print("Fixed duplicate section number 4.7.2 -> 4.8.")

    # 2. Chuẩn hóa ngày tháng và mốc thời gian
    old_sign = r"""*Thái Nguyên, ngày 21 tháng 09 năm 2026*  
> 
> **Trưởng nhóm:** Lã Quý Doanh  
> **Thành viên:** Bùi Thanh Bình"""

    new_sign = r"""*Thái Nguyên, ngày 28 tháng 10 năm 2026*  
> *(Giai đoạn phát triển chính khóa theo đề cương: 27/07/2026 - 27/09/2026; Giai đoạn kiểm thử tự động hóa, đóng gói container và nghiệm thu hoàn thiện: Tháng 10/2026)*  
> 
> **Trưởng nhóm:** Lã Quý Doanh  
> **Thành viên:** Bùi Thanh Bình"""

    if old_sign in content:
        content = content.replace(old_sign, new_sign)
        print("Harmonized project dates and sign-off block.")
    else:
        # Match pattern
        content = re.sub(r'\*Thái Nguyên, ngày 21 tháng 09 năm 2026\*', 
                         r'*Thái Nguyên, ngày 28 tháng 10 năm 2026*\n> *(Giai đoạn phát triển chính khóa: 27/07/2026 - 27/09/2026; Giai đoạn kiểm thử tự động hóa, đóng gói container và nghiệm thu hoàn thiện: Tháng 10/2026)*', 
                         content)

    # 3. Cập nhật Mục lục (Table of Contents) chuẩn hóa
    TOC_COMPLETE = """## MỤC LỤC TỔNG THỂ BÁO CÁO

* [PHẦN 1: KẾ HOẠCH THỰC HIỆN – PHÁT TRIỂN ỨNG DỤNG CHUYÊN SÂU (9 TUẦN)](#phần-1-kế-hoạch-thực-hiện--phát-triển-ứng-dụng-chuyên-sâu)
* [PHẦN 2: THU THẬP VÀ LÀM RÕ YÊU CẦU ỨNG DỤNG](#phần-2-thu-thập-và-làm-rõ-yêu-cầu-ứng-dụng)
  * [2.1 Danh sách câu hỏi thu thập & làm rõ yêu cầu (Khảo sát thực tế 30 câu)](#21-danh-sách-câu-hỏi-thu-thập--làm-rõ-yêu-cầu-khảo-sát-thực-tế-30-câu)
  * [2.2 Yêu cầu chức năng và phi chức năng](#22-yêu-cầu-chức-năng-và-phi-chức-năng)
  * [2.3 Sơ đồ phân cấp chức năng (Functional Hierarchy Diagram)](#23-sơ-đồ-phân-cấp-chức-năng-của-ứng-dụng)
* [PHẦN 3: ĐẶC TẢ YÊU CẦU ỨNG DỤNG – V1.0 (SRS)](#phần-3-đặc-tả-yêu-cầu-ứng-dụng--v10-srs)
  * [3.1 Giới thiệu chung](#31-giới-thiệu-chung)
  * [3.2 Mô tả tổng quan ứng dụng & Mô hình Use Case](#32-mô-tả-tổng-quan-ứng-dụng)
  * [3.3 Đặc tả chi tiết các yêu cầu chức năng (15 Use Cases theo chuẩn UML 2.5)](#33-đặc-tả-các-yêu-cầu-chức-năng-functional)
  * [3.4 Các thông tin hỗ trợ khác](#34-các-thông-tin-hỗ-trợ-khác)
  * [3.5 Lý giải vị trí ứng dụng AI trong kiến trúc hệ thống (Tiêu chí 1.4)](#35-lý-giải-vị-trí-ứng-dụng-ai-trong-kiến-trúc-hệ-thống-tiêu-chí-14)
* [PHẦN 4: TÀI LIỆU THIẾT KẾ HƯỚNG ĐỐI TƯỢNG (MÔ HÌNH LỚP CHI TIẾT)](#phần-4-tài-liệu-thiết-kế-hướng-đối-tượng-mô-hình-lớp)
  * [4.1 Mô hình lớp chi tiết (Class Diagram UML)](#41-mô-hình-lớp-class-diagram)
  * [4.2 Đặc tả chi tiết từng Lớp đối tượng](#42-đặc-tả-class-chi-tiết)
  * [4.8 Đặc tả Lớp BookingService](#48-đặc-tả-lớp-bookingservice)
* [PHẦN 5: KIỂM THỬ CHỨC NĂNG ỨNG DỤNG (TEST CASES & REPORT)](#phần-5-kiểm-thử-chức-năng-ứng-dụng)
  * [5.1 Những yêu cầu về tài nguyên cho kiểm thử ứng dụng](#51-những-yêu-cầu-về-tài-nguyên-cho-kiểm-thử-ứng-dụng)
  * [5.2 Danh sách toàn bộ các tình huống kiểm tra (31 Test Cases)](#52-danh-sách-toàn-bộ-các-tình-huống-kiểm-tra-test-cases)
  * [5.3 Báo cáo kết quả kiểm thử (Test Report)](#53-báo-cáo-kết-quả-test-test-report)
  * [5.4 Thực nghiệm so sánh các phiên bản Prompt & Mô hình AI (Tiêu chí 3.2)](#54-thực-nghiệm-so-sánh-các-phiên-bản-prompt--mô-hình-ai-tiêu-chí-32)
  * [5.5 Cơ chế xử lý lỗi AI & Khả năng chịu lỗi Fault Tolerance (Tiêu chí 3.3)](#55-cơ-chế-xử-lý-lỗi-ai--khả-năng-chịu-lỗi-fault-tolerance-tiêu-chí-33)
  * [5.6 Bảo mật dữ liệu & Quản lý API Key (Tiêu chí 3.4)](#56-bảo-mật-dữ-liệu--quản-lý-api-key-tiêu-chí-34)
* [PHẦN 6: SCREEN FLOW & TÀI LIỆU THIẾT KẾ CƠ SỞ DỮ LIỆU](#phần-6-screen-flow--tài-liệu-thiết-kế-cơ-sở-dữ-liệu)
  * [6.1 Luồng phân chuyển màn hình (Screen Flow Diagram)](#61-screen-flow-phân-luồng-màn-hình-của-ứng-dụng)
  * [6.2 Thiết kế Cơ sở dữ liệu quan hệ (ERD & Data Dictionary)](#62-cơ-sở-dữ-liệu-quan-hệ)
  * [6.3 Các ràng buộc toàn vẹn & Concurrency Control](#63-các-ràng-buộc-toàn-vẹn-trong-csdl)
* [PHẦN 7: TÀI LIỆU HƯỚNG DẪN SỬ DỤNG – V1.0](#phần-7-tài-liệu-hướng-dẫn-sử-dụng--v10)
  * [7.1 Cấu hình phần cứng - phần mềm & khởi chạy hệ thống](#71-cấu-hình-phần-cứng---phần-mềm)
  * [7.2 Hướng dẫn dành cho Khách hàng (Customer)](#72-hướng-dẫn-dành-cho-khách-hàng-customer)
  * [7.3 Hướng dẫn dành cho Quản trị viên (Admin)](#73-hướng-dẫn-dành-cho-quản-trị-viên-admin)
  * [7.4 Kịch bản Demo trực tiếp trước Hội đồng chấm thi (Tiêu chí 4.4)](#74-kịch-bản-demo-trực-tiếp-thành-công-trước-hội-đồng-chấm-thi-tiêu-chí-44)
* [PHẦN 8: THIẾT KẾ AGENT AI TRONG QUY TRÌNH PHÁT TRIỂN PHẦN MỀM (SDLC AGENT SOFTWARE FACTORY)](#phần-8-thiết-kế-agent-ai-trong-quy-trình-sdlc--context-engineering-nhà-máy-phát-triển-phần-mềm)
  * [8.1 Danh mục Công cụ AI, Vai trò Agent và Tệp Luật điều khiển (.agentrules)](#81-khái-niệm--định-vị-agent-ai-trong-quy-trình-phát-triển-phần-mềm-sdlc-as-a-factory)
  * [8.2 Kỹ nghệ Ngữ cảnh (Context Engineering) cho Agent viết code](#82-kỹ-thuật-kỹ-nghệ-ngữ-cảnh-context-engineering)
  * [8.3 Vận hành "Nhà máy phát triển phần mềm" qua 4 pha SDLC](#83-vận-hành-nhà-máy-phần-mềm-qua-4-giai-đoạn-sdlc)
  * [8.4 Kiểm thử Đơn vị (Unit Tests) và Kiểm thử Tích hợp (Integration Tests) tự động](#84-hệ-thống-rào-chắn-an-toàn-safety-guardrails--security-policies)
  * [8.5 Các Rào chắn An toàn cho Agent trong quy trình SDLC (Agent Safety Guardrails)](#85-minh-chứng-kiểm-chứng-và-sửa-lỗi-do-ai-tạo-ra-ai-verification--debugging-case-studies---tiêu-chí-52)
  * [8.6 Minh chứng kiểm chứng và sửa lỗi do AI tạo ra (AI Verification & Debugging Case Studies)](#86-đóng-gói-vận-hành-và-giám-sát-sản-phẩm-packaging-operations--monitoring)
  * [8.7 Đóng gói, Vận hành và Theo dõi sản phẩm (Packaging, Operations & Monitoring)](#87-đóng-gói-vận-hành-và-theo-dõi-sản-phẩm)
* [PHẦN 9: TƯ DUY PHẢN BIỆN, PHÂN CÔNG VẤN ĐÁP & ĐÓNG GÓP RIÊNG TỪNG THÀNH VIÊN](#phần-9-tư-duy-phản-biện-phân-công-vấn-đáp--đóng-góp-riêng-từng-thành-viên)
  * [9.1 Trách nhiệm & Đóng góp chuyên môn của sinh viên Lã Quý Doanh](#91-trách-nhiệm--đóng-góp-chuyên-môn-của-sinh-viên-lã-quý-doanh-trưởng-nhóm)
  * [9.2 Trách nhiệm & Đóng góp chuyên môn của sinh viên Bùi Thanh Bình](#92-trách-nhiệm--đóng-góp-chuyên-môn-của-sinh-viên-bùi-thanh-bình-thành-viên)
  * [9.3 Danh mục câu hỏi vấn đáp độc lập dự kiến & Gợi ý trả lời chuyên sâu (Phân tích khóa in-process và kiến trúc phân tán Redis/SQL UPDLOCK)](#93-danh-mục-câu-hỏi-vấn-đáp-độc-lập-dự-kiến--gợi-ý-trả-lời-chuyên-sâu-tiêu-chí-53)
  * [9.4 Đánh giá tư duy phản biện và đạo đức sử dụng AI trong phát triển phần mềm](#94-đánh-giá-tư-duy-phản-biện-và-đạo-đức-sử-dụng-ai-trong-phát-triển-phần-mềm)
* [PHẦN BỔ SUNG: KẾT LUẬN & ĐÁNH GIÁ ĐỒ ÁN TỐT NGHIỆP](#phần-bổ-sung-kết-luận--đánh-giá-đồ-án-tốt-nghiệp)"""

    toc_pattern = re.compile(r'## MỤC LỤC TỔNG THỂ BÁO CÁO.*?(?=\n---\n\n# PHẦN 1: KẾ HOẠCH THỰC HIỆN)', re.DOTALL)
    if toc_pattern.search(content):
        content = toc_pattern.sub(TOC_COMPLETE, content)
        print("Updated Table of Contents with complete, matching section hierarchy.")

    # Ghi lại file Markdown
    with open(MD_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved: {MD_PATH}")

    # Đồng bộ sang root
    root_md = r"C:\Users\klqdo\Downloads\1websanbongai\BAO_CAO_CHI_TIET_DO_AN_TOT_NGHIEP.md"
    shutil.copyfile(MD_PATH, root_md)
    print(f"Synced: {root_md}")

    # Chạy export_report_to_word.py để tạo file Word
    print("Re-compiling Word DOCX report...")
    export_py = r"C:\Users\klqdo\Downloads\1websanbongai\docs_backup\export_report_to_word.py"
    os.system(f'python "{export_py}"')

if __name__ == '__main__':
    main()
