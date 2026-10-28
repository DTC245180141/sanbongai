import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def set_cell_borders(cell, top=None, bottom=None, left=None, right=None, color="CBD5E1", sz="4"):
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="{top or 'single'}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:left w:val="{left or 'single'}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:bottom w:val="{bottom or 'single'}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:right w:val="{right or 'single'}" w:sz="{sz}" w:space="0" w:color="{color}"/>
        </w:tcBorders>
    ''')
    tcPr.append(tcBorders)

def add_header_footer(doc):
    section = doc.sections[0]
    section.different_first_page_header_footer = True
    
    # Header
    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("TRƯỜNG ĐẠI HỌC CNTT & TT THÁI NGUYÊN (ICTU) | ĐỒ ÁN TỐT NGHIỆP 2026")
    hrun.font.name = "Arial"
    hrun.font.size = Pt(8.5)
    hrun.font.color.rgb = RGBColor(100, 116, 139)
    
    # Footer
    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    frun = fp.add_run("Hệ Thống Đặt Sân Bóng Tự Động Tích Hợp AI & Ví Tiền Virtual Wallet")
    frun.font.name = "Arial"
    frun.font.size = Pt(9)
    frun.font.color.rgb = RGBColor(100, 116, 139)

def style_table(table, col_widths=None, align_center=True):
    if align_center:
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    for i, row in enumerate(table.rows):
        is_header = (i == 0)
        bg_color = "1E3A8A" if is_header else ("F8FAFC" if i % 2 == 1 else "FFFFFF")
        
        trPr = row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        if is_header:
            trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
            
        for j, cell in enumerate(row.cells):
            set_cell_background(cell, bg_color)
            set_cell_margins(cell, top=120, bottom=120, left=150, right=150)
            set_cell_borders(cell, color="CBD5E1", sz="4")
            
            if col_widths and j < len(col_widths):
                cell.width = Inches(col_widths[j])
                
            for paragraph in cell.paragraphs:
                paragraph.paragraph_format.space_before = Pt(2)
                paragraph.paragraph_format.space_after = Pt(2)
                paragraph.paragraph_format.line_spacing = 1.15
                for run in paragraph.runs:
                    run.font.name = "Arial"
                    if is_header:
                        run.font.bold = True
                        run.font.color.rgb = RGBColor(255, 255, 255)
                        run.font.size = Pt(9.5)
                    else:
                        run.font.size = Pt(9.5)
                        run.font.color.rgb = RGBColor(30, 41, 59)

def add_code_block(doc, code_text):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    set_cell_borders(cell, left="single", top="none", right="none", bottom="none", color="0284C7", sz="24")
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    
    run = p.add_run(code_text.strip())
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(30, 41, 59)
    
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(0)
    sp.paragraph_format.space_after = Pt(4)

def add_styled_heading(doc, text, level):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.bold = True
    
    if level == 1:
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run.font.size = Pt(15)
        run.font.color.rgb = RGBColor(30, 58, 138)
        
        pPr = p._p.get_or_add_pPr()
        pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="12" w:space="4" w:color="0284C7"/></w:pBdr>')
        pPr.append(pBdr)
        
    elif level == 2:
        p.paragraph_format.space_before = Pt(13)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run.font.size = Pt(13)
        run.font.color.rgb = RGBColor(2, 132, 199)
    elif level == 3:
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run.font.size = Pt(11.5)
        run.font.color.rgb = RGBColor(3, 105, 161)
    return p

def add_body_paragraph(doc, text, bold_prefix=None, italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.line_spacing = 1.15
    
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Arial"
        r_pre.font.size = Pt(10)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(30, 41, 59)
        
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(10)
    run.font.italic = italic
    run.font.color.rgb = RGBColor(51, 65, 85)
    return p

def add_bullet_point(doc, text, bold_prefix=None, level=0):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.left_indent = Inches(0.25 * (level + 1))
    
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Arial"
        r_pre.font.size = Pt(10)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(30, 41, 59)
        
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(51, 65, 85)
    return p

def add_toc_section(doc):
    add_styled_heading(doc, "MỤC LỤC TÀI LIỆU (TABLE OF CONTENTS)", level=1)
    
    note_p = doc.add_paragraph()
    note_p.paragraph_format.space_before = Pt(4)
    note_p.paragraph_format.space_after = Pt(14)
    r_note = note_p.add_run("💡 Trong Microsoft Word: Nhấp chuột phải chọn 'Update Field' hoặc nhấn phím F9 để cập nhật tự động số trang.")
    r_note.font.name = "Arial"
    r_note.font.size = Pt(9.5)
    r_note.font.italic = True
    r_note.font.color.rgb = RGBColor(2, 132, 199)
    
    # Embedded Word TOC Field (Dynamic Word TOC)
    p_toc_xml = doc.add_paragraph()
    p_toc_xml.paragraph_format.space_after = Pt(12)
    run_toc = p_toc_xml.add_run()
    fldChar1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
    instrText = parse_xml(r'<w:instrText %s xml:space="preserve"> TOC \o "1-3" \h \z \u </w:instrText>' % nsdecls('w'))
    fldChar2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
    fldChar3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
    run_toc._r.append(fldChar1)
    run_toc._r.append(instrText)
    run_toc._r.append(fldChar2)
    run_toc._r.append(fldChar3)
    
    # Styled Visual Table of Contents Block
    toc_structure = [
        ("NHIỆM VỤ 1: KẾ HOẠCH DỰ ÁN & THU THẬP YÊU CẦU", 1),
        ("1.1. Kế hoạch thực hiện dự án (Project Plan - 9 Tuần)", 2),
        ("1.2. Thu thập và làm rõ yêu cầu (20 Câu hỏi phỏng vấn)", 2),
        ("1.3. Sơ đồ phân cấp chức năng (PlantUML)", 2),
        ("NHIỆM VỤ 2: ĐẶC TẢ YÊU CẦU ỨNG DỤNG (SRS)", 1),
        ("2.1. Giới thiệu chung & Bảng 12 thuật ngữ hệ thống", 2),
        ("2.2. Mô tả tổng quan & Sơ đồ Use Case (PlantUML)", 2),
        ("2.2.1. Bảng danh sách các Tác nhân (Actors)", 3),
        ("2.2.2. Danh sách 12 Use Case chính", 3),
        ("2.3. Đặc tả chi tiết UC001: Đặt sân bóng tự động (Sequence Diagram)", 2),
        ("2.4. Đặc tả chi tiết UC002: Nạp tiền ví qua VietQR (Sequence Diagram)", 2),
        ("NHIỆM VỤ 3: THIẾT KẾ HƯỚNG ĐỐI TƯỢNG (OOD)", 1),
        ("3.1. Sơ đồ lớp tổng thể (Class Diagram - PlantUML)", 2),
        ("3.2. Đặc tả chi tiết các lớp dữ liệu & Business Services", 2),
        ("3.3. Phân tích thuật toán cốt lõi", 2),
        ("3.3.1. Thuật toán CreateBooking (BookingService.cs)", 3),
        ("3.3.2. Thuật toán GetAiOptimalPrice (AIServiceClient.cs)", 3),
        ("NHIỆM VỤ 4: SCREEN FLOW & CƠ SỞ DỮ LIỆU", 1),
        ("4.1. Mô tả luồng màn hình (Screen Flow & Mermaid Diagram)", 2),
        ("4.2. Cơ sở dữ liệu quan hệ (Database ERD & 8 Bảng chi tiết)", 2),
        ("4.3. Ràng buộc toàn vẹn & Đồng bộ giao dịch (Concurrency Lock)", 2),
        ("NHIỆM VỤ 5: KIỂM THỬ CHỨC NĂNG (TESTING REPORT)", 1),
        ("5.1. Yêu cầu tài nguyên & Môi trường thử nghiệm", 2),
        ("5.2. Bảng 16 Test Cases kiểm thử nghiệp vụ", 2),
        ("5.3. Báo cáo kết quả kiểm thử thực tế", 2),
        ("KẾT LUẬN CHUNG & TỔNG KẾT ĐỒ ÁN", 1)
    ]
    
    t_toc = doc.add_table(rows=len(toc_structure) + 1, cols=2)
    t_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_toc.cell(0, 0).paragraphs[0].text = "Danh mục Mục lục"
    t_toc.cell(0, 1).paragraphs[0].text = "Cấp độ"
    
    for idx, (item, lvl) in enumerate(toc_structure):
        c0 = t_toc.cell(idx + 1, 0)
        c1 = t_toc.cell(idx + 1, 1)
        
        p0 = c0.paragraphs[0]
        p0.paragraph_format.left_indent = Inches(0.2 * (lvl - 1))
        p0.paragraph_format.space_before = Pt(2)
        p0.paragraph_format.space_after = Pt(2)
        
        r0 = p0.add_run(item)
        r0.font.name = "Arial"
        if lvl == 1:
            r0.font.bold = True
            r0.font.size = Pt(10)
            r0.font.color.rgb = RGBColor(30, 58, 138)
        elif lvl == 2:
            r0.font.size = Pt(9.5)
            r0.font.bold = True
            r0.font.color.rgb = RGBColor(2, 132, 199)
        else:
            r0.font.size = Pt(9)
            r0.font.color.rgb = RGBColor(51, 65, 85)
            
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(2)
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(f"Hơi / Mục {lvl}")
        r1.font.name = "Arial"
        r1.font.size = Pt(9)
        r1.font.color.rgb = RGBColor(100, 116, 139)
        
    style_table(t_toc, col_widths=[5.2, 1.3])

def create_document():
    doc = docx.Document()
    
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)
        
    add_header_footer(doc)
    
    # ---------------------------------------------------------
    # COVER PAGE / TITLE BLOCK
    # ---------------------------------------------------------
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_p.paragraph_format.space_before = Pt(36)
    title_p.paragraph_format.space_after = Pt(6)
    
    r_inst = title_p.add_run("TRƯỜNG ĐẠI HỌC CNTT & TT THÁI NGUYÊN (ICTU)\n")
    r_inst.font.name = "Arial"
    r_inst.font.size = Pt(14)
    r_inst.font.bold = True
    r_inst.font.color.rgb = RGBColor(30, 58, 138)
    
    r_subinst = title_p.add_run("KHOA CÔNG NGHỆ THÔNG TIN — ĐỒ ÁN TỐT NGHIỆP\n\n")
    r_subinst.font.name = "Arial"
    r_subinst.font.size = Pt(11)
    r_subinst.font.color.rgb = RGBColor(100, 116, 139)
    
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "F1F5F9")
    set_cell_margins(cell, top=200, bottom=200, left=200, right=200)
    set_cell_borders(cell, top="single", bottom="single", left="single", right="single", color="1E3A8A", sz="12")
    
    cp = cell.paragraphs[0]
    cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp.paragraph_format.space_before = Pt(4)
    cp.paragraph_format.space_after = Pt(4)
    
    r_main = cp.add_run("BÁO CÁO TỔNG HỢP & ĐẶC TẢ DỰ ÁN\n")
    r_main.font.name = "Arial"
    r_main.font.size = Pt(13)
    r_main.font.bold = True
    r_main.font.color.rgb = RGBColor(2, 132, 199)
    
    r_title = cp.add_run("HỆ THỐNG QUẢN LÝ ĐẶT SÂN BÓNG TỰ ĐỘNG\nTÍCH HỢP AI & VÍ TIỀN VIRTUAL WALLET")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(16)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(30, 58, 138)
    
    meta_p = doc.add_paragraph()
    meta_p.paragraph_format.space_before = Pt(30)
    meta_p.paragraph_format.space_after = Pt(24)
    meta_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    r_meta = meta_p.add_run("Tài liệu đặc tả đầy đủ 5 Nhiệm vụ: Phân tích, SRS, OOD, Cơ sở dữ liệu & Kiểm thử\nTích hợp AI Dynamic Pricing & Trợ lý LM Studio (Qwen2.5-1.5B) & Thanh toán VietQR\n\nNăm học: 2025 - 2026")
    r_meta.font.name = "Arial"
    r_meta.font.size = Pt(10.5)
    r_meta.font.italic = True
    r_meta.font.color.rgb = RGBColor(71, 85, 105)
    
    doc.add_page_break()
    
    # ---------------------------------------------------------
    # TABLE OF CONTENTS PAGE
    # ---------------------------------------------------------
    add_toc_section(doc)
    doc.add_page_break()
    
    # ---------------------------------------------------------
    # NHIỆM VỤ 1: KẾ HOẠCH DỰ ÁN & THU THẬP YÊU CẦU
    # ---------------------------------------------------------
    add_styled_heading(doc, "NHIỆM VỤ 1: KẾ HOẠCH DỰ ÁN & THU THẬP YÊU CẦU", level=1)
    
    add_styled_heading(doc, "1. KẾ HOẠCH THỰC HIỆN (PROJECT PLAN)", level=2)
    add_body_paragraph(doc, "Bảng tiến độ thực hiện dự án trong thời gian 9 tuần từ khảo sát yêu cầu đến hoàn thiện bàn giao hệ thống:")
    
    t_plan = doc.add_table(rows=10, cols=5)
    headers_plan = ["Tuần", "Giai đoạn", "Công việc chi tiết", "Sản phẩm bàn giao", "Thành viên"]
    for j, h in enumerate(headers_plan):
        t_plan.cell(0, j).paragraphs[0].text = h
        
    data_plan = [
        ("1 (01/09 – 07/09)", "Khảo sát & Thu thập yêu cầu", "Họp khách hàng, phỏng vấn, khảo sát sân, phân tích đối thủ", "Biên bản họp, bảng câu hỏi, báo cáo sơ bộ", "PM, BA, Khách hàng"),
        ("2 (08/09 – 14/09)", "Phân tích yêu cầu & SRS", "Tổng hợp yêu cầu, sơ đồ phân cấp chức năng, use case, bảng thuật ngữ", "Sơ đồ PlantUML, SRS draft", "BA, SA, PM"),
        ("3 (15/09 – 21/09)", "Thiết kế CSDL & Kiến trúc", "ERD, các bảng, ràng buộc, kiến trúc tổng thể, công nghệ", "ERD, chi tiết bảng, sơ đồ kiến trúc", "SA, DBA, Backend Lead"),
        ("4 (22/09 – 28/09)", "Thiết kế hướng đối tượng (OOD)", "Class diagram, đặc tả class, mockup", "Sơ đồ lớp, bảng đặc tả, mockup", "SA, Dev Backend/Frontend"),
        ("5 (29/09 – 05/10)", "Phát triển Backend – Core API", "Project .NET 8, DbContext, Controllers, Services", "Mã nguồn Backend cơ bản, DB, API đăng nhập", "Backend Dev (2), DBA, Tester"),
        ("6 (06/10 – 12/10)", "Phát triển AI & Tích hợp", "Flask app, LM Studio, AIServiceClient, VietQR, Admin logic", "AI Microservice, tích hợp, VietQR", "AI Dev, Backend Dev, Tester"),
        ("7 (13/10 – 19/10)", "Phát triển Frontend & Tích hợp", "index.html, admin.html, CSS, JS gọi API, modal", "Giao diện hoàn chỉnh, chatbot, admin", "Frontend Dev, UI/UX, Backend Dev"),
        ("8 (20/10 – 26/10)", "Kiểm thử & Sửa lỗi", "Lập kế hoạch test, thực hiện unit/integration, ghi nhận lỗi", "Báo cáo test, hệ thống sửa lỗi", "Tester (2), All Dev, PM"),
        ("9 (27/10 – 02/11)", "Triển khai & Bàn giao", "Chuẩn bị môi trường, đóng gói source, hướng dẫn, đào tạo", "Source hoàn chỉnh, script, tài liệu, biên bản bàn giao", "Toàn bộ team, khách hàng")
    ]
    
    for i, row in enumerate(data_plan):
        for j, val in enumerate(row):
            t_plan.cell(i+1, j).paragraphs[0].text = val
            
    style_table(t_plan, col_widths=[1.1, 1.3, 1.8, 1.4, 0.9])
    
    add_styled_heading(doc, "2. THU THẬP VÀ LÀM RÕ YÊU CẦU", level=2)
    add_body_paragraph(doc, "Bảng 20 câu hỏi phỏng vấn khách hàng và khảo sát thực tế để làm rõ nghiệp vụ hệ thống:")
    
    t_q = doc.add_table(rows=21, cols=3)
    t_q.cell(0, 0).paragraphs[0].text = "STT"
    t_q.cell(0, 1).paragraphs[0].text = "Câu hỏi phỏng vấn"
    t_q.cell(0, 2).paragraphs[0].text = "Câu trả lời & Kết luận nghiệp vụ"
    
    data_q = [
        ("1", "Mục tiêu chính của hệ thống?", "Tự động hóa đặt sân, giảm tải nhân lực, tối ưu doanh thu bằng định giá AI, thanh toán VietQR 24/7."),
        ("2", "Quản lý bao nhiêu sân và loại?", "5 sân: 2 sân 5 người, 2 sân 7 người, 1 sân 11 người. Có thể mở rộng."),
        ("3", "Giá thuê hiện tại?", "Giá gốc 150.000đ/giờ; sáng (6h-17h) giữ nguyên, tối (17h-6h) x2 = 300k; cuối tuần tăng 30%."),
        ("4", "Quy trình đặt sân hiện tại?", "Khách gọi điện/nhắn tin, nhân viên ghi sổ, dễ trùng lịch. Cần tự động kiểm tra trùng lịch, xác nhận ngay."),
        ("5", "Phương thức thanh toán?", "Nạp tiền vào ví trước (tối thiểu 200k), thanh toán từ ví khi đặt. Nạp qua VietQR, Admin xác nhận."),
        ("6", "Tích hợp cổng thanh toán?", "Giai đoạn đầu chỉ VietQR, thiết kế dễ mở rộng MoMo/VNPay sau."),
        ("7", "AI dùng để làm gì?", "Định giá động và chatbot tư vấn, gợi ý khung giờ thấp điểm."),
        ("8", "Ai sử dụng? Phân quyền?", "Khách hàng (Customer) và Quản trị viên (Admin). Admin có quyền cao nhất."),
        ("9", "Yêu cầu bảo mật?", "Đăng nhập bằng tên/SĐT/email + mật khẩu (mã hóa SHA256), JWT thời gian sống 7 ngày."),
        ("10", "Quên mật khẩu/tên đăng nhập?", "Có, lấy lại tên qua SĐT/email, đổi mật khẩu cần OTP (mô phỏng)."),
        ("11", "Báo cáo thống kê cho admin?", "Tổng booking, doanh thu, số dư ví, yêu cầu nạp chờ, lịch trống của từng sân."),
        ("12", "Giới hạn thời gian đặt?", "Tối đa 3 ngày tới, tối thiểu 2 tiếng trước giờ đá, mỗi booking 1 giờ."),
        ("13", "Cho phép hủy booking?", "Khách có thể hủy nhưng không hoàn tiền; Admin có quyền hủy và hoàn tiền 100%."),
        ("14", "Đồng bộ lịch đặt giữa các sân?", "Kiểm tra xung đột dựa trên FieldId, StartTime, EndTime."),
        ("15", "Có thông báo nhắc nhở?", "Tạm bỏ qua, sẽ nâng cấp sau."),
        ("16", "Yêu cầu hiệu năng?", "API đặt sân <2s, tra cứu <1s, hỗ trợ 100 người đồng thời."),
        ("17", "Đa ngôn ngữ?", "Chỉ tiếng Việt, UTF-8."),
        ("18", "Lưu trữ dữ liệu lịch sử?", "Tối thiểu 2 năm, không xóa Transactions, Bookings, Payments."),
        ("19", "Xuất báo cáo Excel/PDF?", "Tạm thời chưa, có thể dùng API lấy JSON."),
        ("20", "Phương án dự phòng khi AI lỗi?", "Fallback: giá niêm yết + phụ thu cố định, ghi log.")
    ]
    
    for i, row in enumerate(data_q):
        for j, val in enumerate(row):
            t_q.cell(i+1, j).paragraphs[0].text = val
            
    style_table(t_q, col_widths=[0.5, 2.3, 3.7])
    
    add_styled_heading(doc, "3. SƠ ĐỒ PHÂN CẤP CHỨC NĂNG (PLANTUML)", level=2)
    add_body_paragraph(doc, "Mã nguồn PlantUML mô tả cấu trúc phân cấp chức năng toàn hệ thống:")
    
    plantuml_hierarchy = """@startuml
!define RECTANGLE class
skinparam componentStyle rectangle
package "Hệ thống Quản lý Đặt sân bóng tự động tích hợp AI & Ví Virtual Wallet" {
  component "Quản lý Đặt sân" as booking {
    component "Xem danh sách sân" as viewFields
    component "Xem lịch trống" as viewAvailability
    component "Đặt sân" as createBooking
    component "Hủy đặt sân" as cancelBooking
    component "Xem lịch sử đặt" as viewHistory
  }
  component "Quản lý Ví & Thanh toán" as wallet {
    component "Xem số dư ví" as viewBalance
    component "Nạp tiền vào ví" as deposit
    component "Tạo VietQR" as createQR
    component "Gửi yêu cầu nạp" as requestDeposit
    component "Xem lịch sử giao dịch" as viewTransactions
  }
  component "Trợ lý AI" as ai {
    component "Chat với AI (LM Studio)" as chat
    component "Định giá động (Dynamic Pricing)" as dynamicPricing
    component "Gợi ý khung giờ" as suggestTime
  }
  component "Quản trị Hệ thống (Admin)" as admin {
    component "Quản lý người dùng" as userMgmt {
      component "Xem danh sách" as listUsers
      component "Khóa/Mở khóa" as lockUser
      component "Điều chỉnh số dư" as adjustBalance
    }
    component "Quản lý đặt sân" as bookingMgmt {
      component "Xem tất cả booking" as allBookings
      component "Hủy & Hoàn tiền" as cancelRefund
    }
    component "Quản lý cấu hình giá" as priceMgmt {
      component "Cập nhật giá niêm yết" as updateBase
      component "Cập nhật hệ số" as updateMultiplier
    }
    component "Duyệt nạp tiền" as approveDeposit {
      component "Xem yêu cầu" as viewRequests
      component "Phê duyệt/Từ chối" as approveReject
    }
  }
  component "Báo cáo & Thống kê" as report {
    component "Thống kê doanh thu" as revenue
    component "Thống kê tần suất đặt" as frequency
  }
  booking -- viewFields
  booking -- viewAvailability
  booking -- createBooking
  booking -- cancelBooking
  booking -- viewHistory
  wallet -- viewBalance
  wallet -- deposit
  wallet -- createQR
  wallet -- requestDeposit
  wallet -- viewTransactions
  ai -- chat
  ai -- dynamicPricing
  ai -- suggestTime
  admin -- userMgmt
  admin -- bookingMgmt
  admin -- priceMgmt
  admin -- approveDeposit
  userMgmt -- listUsers
  userMgmt -- lockUser
  userMgmt -- adjustBalance
  bookingMgmt -- allBookings
  bookingMgmt -- cancelRefund
  priceMgmt -- updateBase
  priceMgmt -- updateMultiplier
  approveDeposit -- viewRequests
  approveDeposit -- approveReject
  report -- revenue
  report -- frequency
}
@enduml"""
    add_code_block(doc, plantuml_hierarchy)
    
    # ---------------------------------------------------------
    # NHIỆM VỤ 2: ĐẶC TẢ YÊU CẦU ỨNG DỤNG (SRS)
    # ---------------------------------------------------------
    doc.add_page_break()
    add_styled_heading(doc, "NHIỆM VỤ 2: ĐẶC TẢ YÊU CẦU ỨNG DỤNG (SRS)", level=1)
    
    add_styled_heading(doc, "1. GIỚI THIỆU CHUNG", level=2)
    add_body_paragraph(doc, "Tài liệu này đặc tả chi tiết các yêu cầu chức năng và phi chức năng của hệ thống, là cơ sở cho phát triển và kiểm thử.")
    add_bullet_point(doc, " Single Page Application (HTML/CSS/JS modern glassmorphism UI).", bold_prefix="Tầng Client:")
    add_bullet_point(doc, " .NET 8 / 10 RESTful Web API C#.", bold_prefix="Tầng Backend:")
    add_bullet_point(doc, " Python Flask Microservice + LM Studio (qwen2.5-1.5b-instruct).", bold_prefix="Tầng AI:")
    add_bullet_point(doc, " SQL Server (FootballBookingDB).", bold_prefix="Tầng Database:")
    
    add_styled_heading(doc, "Bảng thuật ngữ hệ thống (12 Thuật ngữ)", level=3)
    t_terms = doc.add_table(rows=13, cols=2)
    t_terms.cell(0, 0).paragraphs[0].text = "Thuật ngữ"
    t_terms.cell(0, 1).paragraphs[0].text = "Định nghĩa chi tiết"
    
    data_terms = [
        ("User", "Người dùng cuối (Customer hoặc Admin), có ví điện tử Virtual Wallet."),
        ("Wallet Balance", "Số dư ví ảo (VNĐ), dùng để thanh toán tiền thuê sân."),
        ("Dynamic Pricing", "Điều chỉnh giá thuê sân linh hoạt theo thời gian, do AI tính toán hoặc Fallback engine."),
        ("Booking", "Giao dịch đặt sân thành công với các trạng thái Confirmed, Cancelled, Completed."),
        ("Transaction", "Lịch sử biến động số dư ví (Payment, Refund, TopupApproved)."),
        ("VietQR", "Mã QR chuẩn ngân hàng để khách nạp tiền vào ví ảo."),
        ("Deposit Request", "Yêu cầu nạp tiền do khách tạo (đèm theo mã giao dịch), chờ Admin duyệt."),
        ("LM Studio", "Công cụ chạy LLM cục bộ (model qwen2.5-1.5b-instruct) đóng vai trò trợ lý tư vấn."),
        ("Fallback Engine", "Cơ chế tính giá và trả lời dự phòng khi AI microservice offline."),
        ("JWT Token", "JSON Web Token dùng để xác thực và phân quyền API, hết hạn sau 7 ngày."),
        ("Concurrency Lock", "Cơ chế khóa đồng bộ C# lock(_lockObj) ngăn ngừa xung đột đặt trùng lịch."),
        ("SHA256", "Thuật toán mã hóa băm mật khẩu người dùng trước khi lưu CSDL.")
    ]
    for i, row in enumerate(data_terms):
        for j, val in enumerate(row):
            t_terms.cell(i+1, j).paragraphs[0].text = val
    style_table(t_terms, col_widths=[1.8, 4.7])
    
    add_styled_heading(doc, "2. MÔ TẢ TỔNG QUAN & SƠ ĐỒ USE CASE", level=2)
    add_body_paragraph(doc, "Sơ đồ Use Case tổng quát thể hiện sự tương tác giữa tác nhân và các chức năng:")
    
    plantuml_uc = """@startuml
left to right direction
skinparam packageStyle rectangle
actor "Khách hàng (Customer)" as Customer
actor "Quản trị viên (Admin)" as Admin
actor "Hệ thống AI (AI System)" as AI <<system>>
rectangle "Hệ thống Quản lý Đặt sân bóng AI" {
  usecase "UC001: Đặt sân bóng tự động" as UC01
  usecase "UC002: Nạp tiền ví qua VietQR" as UC02
  usecase "UC003: Xem danh sách sân và giá AI" as UC03
  usecase "UC004: Xem lịch sử đặt sân & giao dịch" as UC04
  usecase "UC005: Hủy đặt sân" as UC05
  usecase "UC006: Trò chuyện với trợ lý AI" as UC06
  usecase "UC007: Quản lý người dùng (Khóa/Mở)" as UC07
  usecase "UC008: Duyệt yêu cầu nạp tiền" as UC08
  usecase "UC009: Hủy booking & Hoàn tiền" as UC09
  usecase "UC010: Cập nhật cấu hình giá" as UC10
  usecase "UC011: Xem báo cáo thống kê" as UC11
  usecase "UC012: Đăng nhập / Đăng ký" as UC12
}
Customer --> UC01
Customer --> UC02
Customer --> UC03
Customer --> UC04
Customer --> UC05
Customer --> UC06
Customer --> UC12
Admin --> UC07
Admin --> UC08
Admin --> UC09
Admin --> UC10
Admin --> UC11
Admin --> UC12
UC01 ..> AI : <<uses>>\n(định giá động)
UC06 ..> AI : <<uses>>\n(xử lý ngôn ngữ)
@enduml"""
    add_code_block(doc, plantuml_uc)
    
    add_styled_heading(doc, "Bảng danh sách các Tác nhân (Actors)", level=3)
    t_actors = doc.add_table(rows=4, cols=3)
    t_actors.cell(0, 0).paragraphs[0].text = "Tác nhân"
    t_actors.cell(0, 1).paragraphs[0].text = "Vai trò"
    t_actors.cell(0, 2).paragraphs[0].text = "Mô tả trách nhiệm"
    
    data_actors = [
        ("Khách hàng", "Người sử dụng dịch vụ", "Đăng ký, đăng nhập, xem sân, đặt sân, thanh toán từ ví, nạp tiền, chat AI, hủy đặt."),
        ("Quản trị viên", "Quản trị hệ thống", "Quản lý user, duyệt nạp tiền, quản lý booking, cập nhật giá, xem báo cáo."),
        ("Hệ thống AI", "Thành phần tự động", "Định giá động theo thời gian thực và xử lý ngôn ngữ tự nhiên (chatbot tư vấn).")
    ]
    for i, row in enumerate(data_actors):
        for j, val in enumerate(row):
            t_actors.cell(i+1, j).paragraphs[0].text = val
    style_table(t_actors, col_widths=[1.5, 1.8, 3.2])
    
    add_styled_heading(doc, "Danh sách 12 Use Case của hệ thống", level=3)
    t_12uc = doc.add_table(rows=13, cols=4)
    t_12uc.cell(0, 0).paragraphs[0].text = "Mã UC"
    t_12uc.cell(0, 1).paragraphs[0].text = "Tên Use Case"
    t_12uc.cell(0, 2).paragraphs[0].text = "Tác nhân chính"
    t_12uc.cell(0, 3).paragraphs[0].text = "Tóm tắt nghiệp vụ"
    
    data_12uc = [
        ("UC001", "Đặt sân bóng tự động", "Khách hàng", "Chọn sân, giờ, xem giá AI, xác nhận, trừ tiền ví, tạo booking."),
        ("UC002", "Nạp tiền ví qua VietQR", "Khách hàng, Admin", "Tạo mã QR, chuyển khoản, gửi yêu cầu, Admin duyệt, cộng tiền."),
        ("UC003", "Xem danh sách sân và giá AI", "Khách hàng", "Hiển thị danh sách sân và giá AI đề xuất theo khung giờ."),
        ("UC004", "Xem lịch sử đặt & giao dịch", "Khách hàng", "Xem danh sách booking và lịch sử biến động ví tiền."),
        ("UC005", "Hủy đặt sân", "Khách hàng", "Hủy booking, cập nhật status Cancelled (không hoàn tiền)."),
        ("UC006", "Trò chuyện với trợ lý AI", "Khách hàng", "Gửi câu hỏi, nhận phản hồi từ LM Studio hoặc fallback."),
        ("UC007", "Quản lý người dùng", "Admin", "Xem danh sách tài khoản, khóa/mở khóa tài khoản."),
        ("UC008", "Duyệt yêu cầu nạp tiền", "Admin", "Xem danh sách nạp, phê duyệt/từ chối yêu cầu nạp tiền."),
        ("UC009", "Hủy booking & Hoàn tiền", "Admin", "Hủy booking bất kỳ, hoàn tiền 100% vào ví khách."),
        ("UC010", "Cập nhật cấu hình giá", "Admin", "Cập nhật BasePrice, hệ số phụ thu cuối tuần / giờ cao điểm."),
        ("UC011", "Xem báo cáo thống kê", "Admin", "Xem doanh thu, tần suất đặt sân theo khoảng thời gian."),
        ("UC012", "Đăng nhập / Đăng ký", "Khách hàng, Admin", "Đăng ký tài khoản mới, đăng nhập nhận JWT Token.")
    ]
    for i, row in enumerate(data_12uc):
        for j, val in enumerate(row):
            t_12uc.cell(i+1, j).paragraphs[0].text = val
    style_table(t_12uc, col_widths=[0.8, 1.8, 1.4, 2.5])
    
    add_styled_heading(doc, "3. ĐẶC TẢ CHI TIẾT UC001: ĐẶT SÂN BÓNG TỰ ĐỘNG", level=2)
    add_body_paragraph(doc, "Khách hàng đặt sân, hệ thống tính giá AI, kiểm tra trùng lịch, kiểm tra số dư ví, trừ tiền và tạo booking.", bold_prefix="Mục đích: ")
    add_body_paragraph(doc, "Khách hàng (chính), Hệ thống AI (phụ).", bold_prefix="Tác nhân: ")
    add_body_paragraph(doc, "Khách hàng đã đăng nhập, sân đang hoạt động, có cấu hình giá.", bold_prefix="Điều kiện trước: ")
    add_body_paragraph(doc, "Tạo Booking Confirmed, trừ số dư ví, lưu Transaction Payment.", bold_prefix="Điều kiện sau: ")
    
    add_styled_heading(doc, "Luồng sự kiện chính (Main Flow):", level=3)
    add_bullet_point(doc, "Khách hàng truy cập giao diện, chọn sân bóng cần đặt.")
    add_bullet_point(doc, "Nhập khung giờ đá -> Hệ thống gọi AI Service lấy giá tối ưu (Dynamic Price).")
    add_bullet_point(doc, "Xác nhận đặt -> Hệ thống kiểm tra thời gian hợp lệ (≥2h sau, ≤3 ngày tới).")
    add_bullet_point(doc, "Gửi POST /bookings -> Hệ thống kiểm tra User, kiểm tra số dư ví, khóa lock(_lockObj) kiểm tra trùng lịch.")
    add_bullet_point(doc, "Nếu hợp lệ: Trừ tiền ví, tạo Booking status=Confirmed, lưu Transaction.")
    add_bullet_point(doc, "Trả về kết quả thành công kèm QR giả lập xác nhận.")
    
    add_styled_heading(doc, "Luồng ngoại lệ / Dự phòng (Alternative Flows):", level=3)
    add_bullet_point(doc, "A1: Số dư ví < Giá booking -> Báo lỗi 'Số dư ví không đủ, vui lòng nạp thêm!'.")
    add_bullet_point(doc, "A2: Khung giờ đã có Booking Confirmed -> Báo lỗi 'Khung giờ này đã có người đặt!'.")
    add_bullet_point(doc, "A3: AI Service offline -> Tự động chuyển qua Fallback Engine tính giá niêm yết + phụ thu.")
    add_bullet_point(doc, "A4: Lỗi hệ thống -> Rollback hoàn lại tiền ví và throw exception.")
    
    add_styled_heading(doc, "Biểu đồ Sequence cho UC001 (PlantUML)", level=3)
    puml_seq1 = """@startuml
actor KhachHang as K
participant "Frontend (UI)" as UI
participant "Backend API (BookingsController)" as B
participant "AIServiceClient" as AIC
participant "AI Microservice (Flask)" as AI
participant "BookingService" as BS
participant "UserService" as US
database "In-Memory Data" as DB

K -> UI: Chọn sân, nhập giờ
UI -> B: GET /fields
B -> DB: Lấy danh sách sân
DB --> B: Trả về Fields
B --> UI: Hiển thị danh sách

K -> UI: Chọn sân cụ thể
UI -> B: GET /fields/{id}/ai-price?time=...
B -> AIC: GetAiOptimalPrice(fieldId, time, basePrice)
AIC -> AI: POST /api/predict-price
alt AI Online
  AI --> AIC: dynamic_price
else AI Offline (Fallback)
  AIC --> AIC: Tính giá fallback (sáng/tối)
end
AIC --> B: AIPricingResult
B --> UI: Hiển thị giá AI

K -> UI: Xác nhận đặt
UI -> B: POST /bookings (UserId, FieldId, BookingTime, TotalPrice)
B -> BS: CreateBooking(userId, fieldId, startTime, endTime, price)
BS -> US: GetUserById(userId)
US --> BS: User object
alt User bị khóa
  BS --> B: error "Tài khoản bị khóa"
  B --> UI: error message
else User hợp lệ
  BS -> BS: Kiểm tra số dư ví (WalletBalance >= price)
  alt Số dư không đủ
    BS --> B: error "Số dư không đủ"
    B --> UI: error message
  else Số dư đủ
    BS -> BS: lock(_lockObj) { Kiểm tra trùng lịch }
    alt Bị trùng lịch
      BS --> B: error "Khung giờ đã có người đặt"
      B --> UI: error message
    else Không trùng
      BS -> BS: user.WalletBalance -= price
      BS -> BS: Tạo Booking (Status = Confirmed)
      BS -> US: AddTransaction(userId, price, "Payment", bookingId)
      US -> DB: Lưu Transaction
      BS --> B: Booking thành công
    end
  end
end
B --> UI: { status: "success", booking, qr_url }
UI --> K: Hiển thị thông báo thành công
@enduml"""
    add_code_block(doc, puml_seq1)
    
    add_styled_heading(doc, "4. ĐẶC TẢ CHI TIẾT UC002: NẠP TIỀN VÍ QUA VIETQR", level=2)
    add_body_paragraph(doc, "Khách hàng gửi yêu cầu nạp tiền qua mã VietQR, Admin duyệt và hệ thống cộng tiền vào ví ảo.", bold_prefix="Mục đích: ")
    add_body_paragraph(doc, "Khách hàng (người nạp), Admin (người phê duyệt).", bold_prefix="Tác nhân: ")
    add_body_paragraph(doc, "Đã đăng nhập, số tiền nạp > 0.", bold_prefix="Điều kiện trước: ")
    add_body_paragraph(doc, "Cộng tiền ví khách hàng, tạo Transaction TopupApproved nếu được duyệt.", bold_prefix="Điều kiện sau: ")
    
    add_styled_heading(doc, "Biểu đồ Sequence cho UC002 (PlantUML)", level=3)
    puml_seq2 = """@startuml
actor KhachHang as K
actor Admin as A
participant "Frontend (UI)" as UI
participant "PaymentController" as PC
participant "UserService" as US
database "In-Memory Data" as DB

K -> UI: Chọn nạp tiền, nhập Amount
UI -> PC: POST /generate-vietqr (UserId, Amount)
PC -> PC: Tạo QR URL (VietQR API giả lập)
PC --> UI: Trả về qr_url, bank_info, memo
UI --> K: Hiển thị QR và thông tin

K -> K: Quét QR, chuyển khoản (giả lập)
K -> UI: Nhập mã giao dịch, upload ảnh
UI -> PC: POST /create-deposit-request (UserId, Amount, TxnCode, Memo, ImageUrl)
PC -> US: CreateDepositRequest(...)
US -> DB: Lưu DepositRequest (Status=Pending)
US --> PC: depositId
PC --> UI: { status: "success", depositId }
UI --> K: "Yêu cầu nạp đã gửi, chờ Admin duyệt"

A -> UI: Đăng nhập Admin, vào trang duyệt nạp
UI -> PC: GET /deposit-requests
PC -> US: GetAllDepositRequests()
US -> DB: Lấy danh sách
US --> PC: Danh sách DepositRequests
PC --> UI: Hiển thị danh sách cho Admin

A -> UI: Chọn yêu cầu Pending và bấm "Phê duyệt"
UI -> PC: POST /deposit-requests/{id}/approve
PC -> US: ApproveDepositRequest(id)
US -> DB: Kiểm tra Status=Pending
alt Status không phải Pending
  US --> PC: error "Đã xử lý trước đó"
  PC --> UI: error message
else Status=Pending
  US -> US: Cập nhật Status=Success, ProcessedAt=Now
  US -> US: user.WalletBalance += Amount
  US -> US: AddTransaction(userId, Amount, "TopupApproved", null)
  US -> DB: Lưu Transaction và cập nhật User
  US --> PC: { success: true, message: "Đã cộng tiền", newBalance: X }
end
PC --> UI: Thông báo thành công
UI --> A: Hiển thị kết quả
@enduml"""
    add_code_block(doc, puml_seq2)
    
    # ---------------------------------------------------------
    # NHIỆM VỤ 3: THIẾT KẾ HƯỚNG ĐỐI TƯỢNG (OOD)
    # ---------------------------------------------------------
    doc.add_page_break()
    add_styled_heading(doc, "NHIỆM VỤ 3: THIẾT KẾ HƯỚNG ĐỐI TƯỢNG (OOD)", level=1)
    
    add_styled_heading(doc, "1. SƠ ĐỒ LỚP TỔNG THỂ (CLASS DIAGRAM — PLANTUML)", level=2)
    add_body_paragraph(doc, "Sơ đồ thể hiện toàn bộ các Data Entities, Enums, Interfaces và Business Logic Services:")
    
    puml_class = """@startuml
!define ENTITY class
!define ENUM enum
skinparam classAttributeIconSize 0

ENUM UserRole {
  + Customer = 0
  + Admin = 1
}
ENUM BookingStatus {
  + Pending = 0
  + Confirmed = 1
  + Cancelled = 2
  + Completed = 3
}
ENUM PaymentMethod {
  + MoMo = 0
  + VNPay = 1
  + ZaloPay = 2
  + Cash = 3
  + Wallet = 4
}
ENUM PaymentStatus {
  + Failed = 0
  + Success = 1
  + Refunded = 2
}
ENUM DepositStatus {
  + Pending = 0
  + Success = 1
  + Rejected = 2
}

ENTITY User {
  - Id : Guid
  - Username : string
  - FullName : string
  - Phone : string
  - Email : string
  - AvatarUrl : string
  - Role : UserRole
  - PasswordHash : string
  - WalletBalance : decimal
  - CreatedAt : DateTime
  - IsDeleted : bool
}

ENTITY FootballField {
  - FieldId : Guid
  - Name : string
  - FieldType : int
  - BasePrice : decimal
  - Status : bool
  - Location : string
  - CreatedAt : DateTime
}

ENTITY Booking {
  - BookingId : Guid
  - UserId : Guid
  - FieldId : Guid
  - BookingTime : DateTime
  - StartTime : DateTime
  - EndTime : DateTime
  - TotalPrice : decimal
  - Status : BookingStatus
  - IsAIPriced : bool
  - CreatedAt : DateTime
}

ENTITY Transaction {
  - TransactionId : Guid
  - UserId : Guid
  - Amount : decimal
  - Type : string
  - BookingId : Guid
  - CreatedAt : DateTime
}

ENTITY Payment {
  - PaymentId : Guid
  - BookingId : Guid
  - Amount : decimal
  - TransactionId : string
  - Method : PaymentMethod
  - Status : PaymentStatus
  - PaidAt : DateTime
}

ENTITY PricingConfig {
  - ConfigId : int
  - FieldType : int
  - BasePrice : decimal
  - WeekendMultiplier : decimal
  - PeakHourMultiplier : decimal
  - UpdatedAt : DateTime
}

ENTITY AIDemandLog {
  - LogId : Guid
  - FieldId : Guid
  - LogTime : DateTime
  - DemandScore : int
  - SuggestedMultiplier : decimal
  - IsOverridden : bool
}

ENTITY DepositRequest {
  - Id : Guid
  - UserId : Guid
  - Amount : decimal
  - TransactionCode : string
  - Memo : string
  - ImageUrl : string
  - Status : DepositStatus
  - CreatedAt : DateTime
  - ProcessedAt : DateTime
}

ENTITY IUserService <<interface>> {
  + Register(...) : User
  + Login(...) : (User, string)
  + GetUserById(Guid) : User
  + AddTransaction(...) : void
  + ApproveDepositRequest(Guid) : (bool, string)
}

ENTITY IBookingService <<interface>> {
  + GetFields() : List<FootballField>
  + CreateBooking(...) : (Booking, string)
  + CancelBooking(Guid) : bool
}

ENTITY IAIServiceClient <<interface>> {
  + GetAiOptimalPrice(Guid, DateTime, decimal) : AIPricingResult
}

User "1" --> "0..*" Booking : has
User "1" --> "0..*" Transaction : has
User "1" --> "0..*" DepositRequest : has
Booking "1" --> "1" User : belongs to
Booking "1" --> "1" FootballField : references
Booking "0..1" --> "0..1" Payment : has
FootballField "1" --> "0..*" Booking : has
FootballField "1" --> "0..*" AIDemandLog : has
Transaction "0..*" --> "1" User : belongs to
Payment "1" --> "1" Booking : belongs to
DepositRequest "0..*" --> "1" User : belongs to
BookingService --> IUserService : depends on
BookingService --> IAIServiceClient : depends on
@enduml"""
    add_code_block(doc, puml_class)
    
    add_styled_heading(doc, "2. ĐẶC TẢ CHI TIẾT CÁC LỚP DỮ LIỆU & SERVICE", level=2)
    add_bullet_point(doc, "Id (Guid), Username (string), FullName, Phone, Email, AvatarUrl, Role (UserRole), PasswordHash, WalletBalance (decimal), CreatedAt, IsDeleted.", bold_prefix="User: ")
    add_bullet_point(doc, "BookingId (Guid), UserId (FK), FieldId (FK), BookingTime, StartTime, EndTime, TotalPrice, Status (BookingStatus), IsAIPriced, CreatedAt.", bold_prefix="Booking: ")
    add_bullet_point(doc, "FieldId (Guid), Name (string), FieldType (5/7/11), BasePrice, Status (bool), Location, CreatedAt.", bold_prefix="FootballField: ")
    add_bullet_point(doc, "TransactionId (Guid), UserId (FK), Amount, Type ('Payment'/'Refund'/'TopupApproved'), BookingId, CreatedAt.", bold_prefix="Transaction: ")
    add_bullet_point(doc, "PaymentId (Guid), BookingId (FK), Amount, TransactionId, Method (PaymentMethod), Status, PaidAt.", bold_prefix="Payment: ")
    add_bullet_point(doc, "Id (Guid), UserId (FK), Amount, TransactionCode, Memo, ImageUrl, Status (DepositStatus), CreatedAt, ProcessedAt.", bold_prefix="DepositRequest: ")
    
    add_styled_heading(doc, "3. PHÂN TÍCH PHƯƠNG THỨC CỐT LÕI", level=2)
    add_styled_heading(doc, "A. CreateBooking (BookingService.cs)", level=3)
    add_body_paragraph(doc, "Luồng thực thi trong BookingService:")
    add_bullet_point(doc, "1. Lấy thông tin User theo UserId -> Kiểm tra tồn tại và không bị khóa (IsDeleted == false).")
    add_bullet_point(doc, "2. Kiểm tra số dư ví (user.WalletBalance >= price). Nếu không đủ -> Trả về lỗi.")
    add_bullet_point(doc, "3. Khóa đồng bộ lock(_lockObj) -> Kiểm tra xung đột lịch với các Booking Confirmed trên cùng FieldId.")
    add_bullet_point(doc, "4. Trừ tiền ví (user.WalletBalance -= price), khởi tạo đối tượng Booking mới.")
    add_bullet_point(doc, "5. Thêm Booking vào danh sách, gọi AddTransaction tạo lịch sử giao dịch Payment.")
    add_bullet_point(doc, "6. Nếu có ngoại lệ -> Catch và Rollback hoàn lại tiền ví (user.WalletBalance += price).")
    
    add_styled_heading(doc, "B. GetAiOptimalPrice (AIServiceClient.cs)", level=3)
    add_body_paragraph(doc, "Luồng thực thi trong AIServiceClient:")
    add_bullet_point(doc, "1. Chuyển đổi DayOfWeek C# sang chuẩn Python (Monday=0 ... Sunday=6).")
    add_bullet_point(doc, "2. Gửi HTTP POST tới http://localhost:5050/api/predict-price kèm payload JSON.")
    add_bullet_point(doc, "3. Nếu thành công -> Giải mã JSON trả về kết quả dynamic_price và lý do phụ thu.")
    add_bullet_point(doc, "4. Nếu thất bại / Timeout -> Chuyển sang Fallback Engine: Tự tính hệ số phụ thu cuối tuần (+30%) và giờ cao điểm 18h-21h (+50%).")
    
    # ---------------------------------------------------------
    # NHIỆM VỤ 4: SCREEN FLOW & CƠ SỞ DỮ LIỆU
    # ---------------------------------------------------------
    doc.add_page_break()
    add_styled_heading(doc, "NHIỆM VỤ 4: SCREEN FLOW & CƠ SỞ DỮ LIỆU", level=1)
    
    add_styled_heading(doc, "1. MÔ TẢ LUỒNG MÀN HÌNH (SCREEN FLOW)", level=2)
    
    add_styled_heading(doc, "Luồng trải nghiệm Khách hàng (Customer Flow)", level=3)
    t_flow_c = doc.add_table(rows=10, cols=4)
    t_flow_c.cell(0, 0).paragraphs[0].text = "Bước"
    t_flow_c.cell(0, 1).paragraphs[0].text = "Màn hình"
    t_flow_c.cell(0, 2).paragraphs[0].text = "Hành động người dùng"
    t_flow_c.cell(0, 3).paragraphs[0].text = "Phản hồi hệ thống"
    
    data_flow_c = [
        ("1", "Trang chủ", "Xem danh sách sân, bấm Đăng nhập/Đăng ký", "Hiển thị danh sách sân bóng, mở Modal Auth"),
        ("2", "Modal Đăng nhập", "Nhập username/password -> Bấm Đăng nhập", "Xác thực API, lưu JWT Token, cập nhật Header UI"),
        ("3", "Trang chủ (Đã login)", "Xem sân bóng, xem giá AI, nạp tiền, chat AI", "Tải số dư ví, hiển thị nút chức năng cá nhân"),
        ("4", "Modal Đặt sân", "Chọn khung giờ đá -> Bấm Xác nhận", "Gọi API tính giá AI, trừ tiền ví, tạo Booking Confirmed"),
        ("5", "Modal Nạp tiền", "Nhập số tiền nạp -> Bấm Tạo mã VietQR", "Tạo và hiển thị mã QR VietQR chuẩn kèm thông tin CK"),
        ("6", "Gửi Yêu cầu Nạp", "Nhập mã giao dịch -> Bấm Gửi yêu cầu", "Tạo DepositRequest trạng thái Pending chờ duyệt"),
        ("7", "Lịch sử Giao dịch", "Vào mục Lịch sử đặt sân & Ví tiền", "Hiển thị danh sách booking và biến động ví chi tiết"),
        ("8", "Trợ lý Chatbot AI", "Gửi câu hỏi tư vấn lịch/giá sân", "LM Studio (hoặc Fallback) phản hồi tiếng Việt tự nhiên"),
        ("9", "Đăng xuất", "Bấm nút Đăng xuất trên Header", "Xóa JWT Token khỏi localStorage, làm mới giao diện")
    ]
    for i, row in enumerate(data_flow_c):
        for j, val in enumerate(row):
            t_flow_c.cell(i+1, j).paragraphs[0].text = val
    style_table(t_flow_c, col_widths=[0.6, 1.4, 2.2, 2.3])
    
    add_styled_heading(doc, "Sơ đồ tổng hợp luồng ứng dụng (Mermaid)", level=3)
    mermaid_flow = """graph TD
    A[Trang chủ index.html] --> B{Đã đăng nhập?}
    B -->|Chưa| C[Modal Đăng nhập / Đăng ký]
    C --> D[Đăng nhập thành công JWT Token]
    D --> E[Trang chủ Customer - Hiện số dư ví]
    E --> F[Đặt sân bóng]
    E --> G[Nạp tiền vào ví]
    E --> H[Lịch sử đặt & Ví tiền]
    E --> I[Chatbot Trợ lý AI]
    E --> J[Đăng xuất]
    F --> K[Chọn sân, giờ -> Tính giá AI]
    K --> L[Thanh toán tự động từ Ví]
    L --> M[Thành công -> Tạo Booking Confirmed]
    G --> N[Nhập số tiền -> Tạo VietQR]
    N --> O[Chuyển khoản chuyển tiền]
    O --> P[Nhập mã GD -> Tạo DepositRequest]
    P --> Q[Trạng thái Pending chờ Admin duyệt]
    E --> R[Admin Dashboard admin.html]
    R --> S[Quản lý người dùng]
    R --> T[Phê duyệt Nạp ví VietQR]
    R --> U[Quản lý Booking & Hoàn tiền]
    R --> V[Cấu hình bảng giá Sân]
    R --> W[Báo cáo Doanh thu]"""
    add_code_block(doc, mermaid_flow)
    
    add_styled_heading(doc, "2. CƠ SỞ DỮ LIỆU QUAN HỆ (DATABASE ERD & TABLES)", level=2)
    add_styled_heading(doc, "Sơ đồ ERD Quan hệ Entities (Mermaid)", level=3)
    mermaid_erd = """erDiagram
    USERS ||--o{ BOOKINGS : "has"
    USERS ||--o{ TRANSACTIONS : "has"
    USERS ||--o{ DEPOSIT_REQUESTS : "has"
    FIELDS ||--o{ BOOKINGS : "has"
    FIELDS ||--o{ AI_DEMAND_LOGS : "has"
    BOOKINGS ||--|| PAYMENTS : "has one"
    USERS {
        GUID Id PK
        string Username UK
        string FullName
        string Phone UK
        string Email UK
        UserRole Role
        string PasswordHash
        decimal WalletBalance
        datetime CreatedAt
        bit IsDeleted
    }
    FIELDS {
        GUID FieldId PK
        string Name
        int FieldType
        decimal BasePrice
        bit Status
        string Location
        datetime CreatedAt
    }
    BOOKINGS {
        GUID BookingId PK
        GUID UserId FK
        GUID FieldId FK
        datetime BookingTime
        datetime StartTime
        datetime EndTime
        decimal TotalPrice
        BookingStatus Status
        bit IsAIPriced
        datetime CreatedAt
    }
    TRANSACTIONS {
        GUID TransactionId PK
        GUID UserId FK
        decimal Amount
        string Type
        GUID BookingId FK
        datetime CreatedAt
    }
    PAYMENTS {
        GUID PaymentId PK
        GUID BookingId FK
        decimal Amount
        string TransactionId
        PaymentMethod Method
        PaymentStatus Status
        datetime PaidAt
    }
    AI_DEMAND_LOGS {
        GUID LogId PK
        GUID FieldId FK
        datetime LogTime
        int DemandScore
        decimal SuggestedMultiplier
        bit IsOverridden
    }
    PRICING_CONFIG {
        int ConfigId PK
        int FieldType UK
        decimal BasePrice
        decimal WeekendMultiplier
        decimal PeakHourMultiplier
        datetime UpdatedAt
    }
    DEPOSIT_REQUESTS {
        GUID Id PK
        GUID UserId FK
        decimal Amount
        string TransactionCode
        string Memo
        string ImageUrl
        DepositStatus Status
        datetime CreatedAt
        datetime ProcessedAt
    }"""
    add_code_block(doc, mermaid_erd)
    
    add_styled_heading(doc, "3. RÀNG BUỘC TOÀN VẸN & ĐỒNG BỘ GIAO DỊCH", level=2)
    add_bullet_point(doc, "Users.WalletBalance >= 0, Fields.BasePrice > 0, Bookings.TotalPrice >= 0, Bookings.EndTime > StartTime, AI_DemandLogs.DemandScore BETWEEN 1 AND 10.", bold_prefix="Domain Checks: ")
    add_bullet_point(doc, "Users(Username, Phone, Email), PricingConfig(FieldType), Payments(BookingId).", bold_prefix="Unique Keys: ")
    add_bullet_point(doc, "Bookings -> Users & Fields (RESTRICT); Payments -> Bookings (CASCADE); Transactions -> Users (RESTRICT).", bold_prefix="Foreign Keys: ")
    add_bullet_point(doc, "IX_Bookings_FieldId_StartTime (FieldId, StartTime, EndTime) giúp tăng tốc 10x truy vấn kiểm tra trùng lịch.", bold_prefix="Performance Indexes: ")
    add_bullet_point(doc, "Sử dụng C# lock(_lockObj) ngăn ngừa race condition khi 2 khách hàng đặt cùng 1 sân tại cùng 1 milisecond.", bold_prefix="Concurrency Lock: ")
    
    # ---------------------------------------------------------
    # NHIỆM VỤ 5: KIỂM THỬ CHỨC NĂNG
    # ---------------------------------------------------------
    doc.add_page_break()
    add_styled_heading(doc, "NHIỆM VỤ 5: KIỂM THỬ CHỨC NĂNG (TESTING REPORT)", level=1)
    
    add_styled_heading(doc, "1. YÊU CẦU MÔI TRƯỜNG THỬ NGHIỆM", level=2)
    add_bullet_point(doc, "Backend (.NET 8): 2 Cores, 4GB RAM | AI Microservice (Python + LM Studio): 4 Cores, 8-16GB RAM | SQL Server 2019+.", bold_prefix="Phần cứng: ")
    add_bullet_point(doc, "Visual Studio 2022 / VS Code, Python 3.10+, LM Studio 0.2.0+, Postman, Google Chrome.", bold_prefix="Phần mềm: ")
    add_bullet_point(doc, "Tài khoản test: admin / Admin@123, khach1 / Customer@123, doanh / 123456. CSDLSat 5 sân bóng chuẩn.", bold_prefix="Dữ liệu mẫu: ")
    
    add_styled_heading(doc, "2. BẢNG 16 TEST CASE KIỂM THỬ NGHIỆP VỤ", level=2)
    t_test = doc.add_table(rows=17, cols=5)
    headers_t = ["Test ID", "Chức năng", "Mô tả kịch bản", "Dữ liệu thử nghiệm", "Kết quả mong đợi"]
    for j, h in enumerate(headers_t):
        t_test.cell(0, j).paragraphs[0].text = h
        
    data_test = [
        ("TC-001", "Đặt sân – đủ tiền", "Số dư ví vừa đủ giá booking", "UserId, FieldId, BookingTime=08:00, TotalPrice=150k", "Trừ đúng 150.000đ, booking Confirmed, Transaction Payment"),
        ("TC-002", "Đặt sân – không đủ tiền", "Số dư ví < giá booking", "User khach1 còn 50k, BookingTime=18:00 (300k)", "Lỗi 'Số dư ví không đủ', không tạo booking"),
        ("TC-003", "Trùng lịch đồng thời", "Hai luồng cùng đặt 1 sân tại 1 giờ", "Cùng FieldId, StartTime=10:00", "Một request thành công, một báo lỗi 'Đã có người đặt'"),
        ("TC-004", "Đặt sân quá gần", "BookingTime < Now + 2h", "BookingTime = Now + 1h", "Lỗi 'Vui lòng chọn thời gian đặt từ 2 tiếng sau'"),
        ("TC-005", "Đặt sân quá xa", "BookingTime > Now + 3 ngày", "BookingTime = Now + 4 ngày", "Lỗi 'Chỉ cho phép đặt trong vòng 3 ngày'"),
        ("TC-006", "AI offline fallback", "Tắt AI Service, vẫn đặt sân", "AI port 5050 offline, BookingTime=20:00", "Fallback tính giá niêm yết + phụ thu, đặt thành công"),
        ("TC-007", "Nạp tiền VietQR", "Tạo mã VietQR chuyển khoản", "Amount = 200.000 VNĐ", "Trả về URL mã QR VietQR chuẩn kèm bank info"),
        ("TC-008", "Gửi yêu cầu nạp", "Tạo DepositRequest Pending", "Amount=500k, TxnCode='MOCK123'", "Tạo request Pending, chưa cộng tiền vào ví"),
        ("TC-009", "Admin duyệt nạp", "Admin phê duyệt yêu cầu nạp", "DepositRequest Pending -> POST /approve", "Status=Success, cộng tiền ví, Transaction TopupApproved"),
        ("TC-010", "Admin từ chối nạp", "Admin từ chối yêu cầu nạp", "DepositRequest Pending -> POST /reject", "Status=Rejected, số dư ví giữ nguyên"),
        ("TC-011", "Admin hủy & hoàn tiền", "Admin hủy booking Confirmed", "DELETE /admin/bookings/{id}", "Booking Status=Cancelled, cộng lại 100% tiền ví"),
        ("TC-012", "Admin khóa tài khoản", "Admin khóa user", "PUT /admin/users/{id}/status {IsLocked:true}", "IsDeleted=true, user đăng nhập/đặt sân báo bị khóa"),
        ("TC-013", "Chat AI online", "Chatbot tư vấn bằng LM Studio", "Message: 'Sân 5 người giá bao nhiêu giờ tối?'", "LM Studio phản hồi đúng nội dung (300.000đ/h)"),
        ("TC-014", "Chat AI offline", "Fallback trả lời khi LM Studio tắt", "LM Studio offline, Message: 'Còn sân không?'", "Fallback engine trả lời thông tin dự phòng mượt mà"),
        ("TC-015", "JWT hết hạn", "Token cũ bị từ chối", "Gửi request với JWT đã quá 7 ngày", "Trả về HTTP 401 Unauthorized"),
        ("TC-016", "Khách hủy booking", "Customer tự hủy booking", "POST /bookings/{id}/cancel", "Status=Cancelled, không hoàn tiền ví")
    ]
    for i, row in enumerate(data_test):
        for j, val in enumerate(row):
            t_test.cell(i+1, j).paragraphs[0].text = val
    style_table(t_test, col_widths=[0.7, 1.3, 1.6, 1.4, 1.5])
    
    add_styled_heading(doc, "3. BÁO CÁO KẾT QUẢ KIỂM THỬ THỰC TẾ", level=2)
    t_res = doc.add_table(rows=17, cols=5)
    headers_r = ["Test ID", "Mô tả kịch bản", "Kết quả thực tế", "So với mong đợi", "Trạng thái"]
    for j, h in enumerate(headers_r):
        t_res.cell(0, j).paragraphs[0].text = h
        
    data_res = [
        ("TC-001", "Đặt sân – đủ tiền", "Trừ đúng 150k, booking Confirmed", "Khớp 100%", "PASS"),
        ("TC-002", "Đặt sân – không đủ tiền", "Báo lỗi 'Số dư không đủ'", "Khớp 100%", "PASS"),
        ("TC-003", "Trùng lịch đồng thời", "Một thành công, một báo lỗi", "Khớp (Lock OK)", "PASS"),
        ("TC-004", "Đặt sân quá gần", "Báo lỗi thời gian không hợp lệ", "Khớp 100%", "PASS"),
        ("TC-005", "Đặt sân quá xa", "Báo lỗi thời gian không hợp lệ", "Khớp 100%", "PASS"),
        ("TC-006", "AI offline fallback", "Fallback tính giá 300k, đặt thành công", "Khớp 100%", "PASS"),
        ("TC-007", "Nạp tiền VietQR", "Hiển thị QR code thành công", "Khớp 100%", "PASS"),
        ("TC-008", "Gửi yêu cầu nạp", "DepositRequest status=Pending", "Khớp 100%", "PASS"),
        ("TC-009", "Admin duyệt nạp", "Cộng tiền ví + Transaction mới", "Khớp 100%", "PASS"),
        ("TC-010", "Admin từ chối nạp", "DepositRequest status=Rejected", "Khớp 100%", "PASS"),
        ("TC-011", "Admin hủy & hoàn tiền", "Status=Cancelled, ví được hoàn 100%", "Khớp 100%", "PASS"),
        ("TC-012", "Admin khóa tài khoản", "Khóa tài khoản thành công", "Khớp 100%", "PASS"),
        ("TC-013", "Chat AI online", "Phản hồi thông minh từ LM Studio", "Khớp 100%", "PASS"),
        ("TC-014", "Chat AI offline", "Phản hồi tự nhiên từ Fallback Engine", "Khớp 100%", "PASS"),
        ("TC-015", "JWT hết hạn", "Trả về HTTP Status 401", "Khớp 100%", "PASS"),
        ("TC-016", "Khách hủy booking", "Booking Cancelled, không hoàn tiền", "Khớp 100%", "PASS")
    ]
    for i, row in enumerate(data_res):
        for j, val in enumerate(row):
            t_res.cell(i+1, j).paragraphs[0].text = val
    style_table(t_res, col_widths=[0.8, 1.8, 2.2, 1.0, 0.7])
    
    # ---------------------------------------------------------
    # KẾT LUẬN CHUNG
    # ---------------------------------------------------------
    doc.add_page_break()
    add_styled_heading(doc, "KẾT LUẬN CHUNG & TỔNG KẾT ĐỒ ÁN", level=1)
    
    add_body_paragraph(doc, "Tài liệu này đã tổng hợp toàn bộ 5 Nhiệm vụ trọng tâm của Đồ án Tốt nghiệp:")
    add_bullet_point(doc, " Lập kế hoạch 9 tuần, 20 câu hỏi phỏng vấn thực tế, Sơ đồ phân cấp chức năng.", bold_prefix="Nhiệm vụ 1: ")
    add_bullet_point(doc, " Bảng thuật ngữ 12 khái niệm, Sơ đồ Use Case, Đặc tả chi tiết 2 UC cốt lõi kèm Sequence Diagrams.", bold_prefix="Nhiệm vụ 2: ")
    add_bullet_point(doc, " Class Diagram tổng thể, Đặc tả 8 Data Entities & 3 Services, phân tích chuyên sâu thuật toán CreateBooking và GetAiOptimalPrice.", bold_prefix="Nhiệm vụ 3: ")
    add_bullet_point(doc, " Screen Flow chi tiết, ERD Mermaid, đặc tả 8 bảng CSDL, ràng buộc toàn vẹn và cơ chế Concurrency Lock.", bold_prefix="Nhiệm vụ 4: ")
    add_bullet_point(doc, " Ma trận 16 Test Cases kiểm thử nghiệp vụ nâng cao, báo cáo kết quả đạt 100% PASS.", bold_prefix="Nhiệm vụ 5: ")
    
    add_body_paragraph(doc, "Tất cả mã nguồn PlantUML và Mermaid trong tài liệu đều có thể render trực tiếp thành sơ đồ đồ họa minh họa cho báo cáo chính thức.")
    
    output_path = r"c:\1websanbongai\BAO_CAO_DU_AN_ICTU_VOI_MUC_LUC.docx"
    doc.save(output_path)
    print(f"Successfully updated docx with TOC at: {output_path}")

if __name__ == "__main__":
    create_document()
