---
name: dynamic-pricing-ai-engine
description: >-
  Chuyên gia tính toán định giá linh hoạt theo thời gian thực (AI Dynamic Pricing) và kiến trúc phòng thủ chịu lỗi 3 tầng
  (Three-tier Fallback Architecture) cho dịch vụ AI Flask và Backend .NET. Sử dụng kỹ năng này khi phát triển, điều chỉnh
  hoặc xử lý sự cố liên quan đến dự đoán giá sân bóng và Chatbot trợ lý ảo.
---

# Kỹ Năng Định Giá AI Linh Hoạt & Phòng Thủ Chịu Lỗi 3 Tầng (Dynamic Pricing AI Engine)

Kỹ năng này bảo đảm hệ thống định giá sân bóng luôn hoạt động liên tục 24/7 với độ trễ thấp nhất, tự động thích ứng với thời tiết, ngày trong tuần, khung giờ cao điểm và tuyệt đối không bao giờ làm gián đoạn website khi mô hình AI gặp sự cố.

---

## 1. Ràng Buộc Nghiệp Vụ Định Giá (Pricing Rules & Formulas)

1. **Bảng giá cơ sở (Base Price Matrix):**
   - Khung giờ tiêu chuẩn (06:00 - 17:00): Giá gốc cơ bản (ví dụ 150.000 VNĐ/giờ sân 5).
   - Khung giờ cao điểm / Đèn đêm (17:00 - 23:00): Hệ số tăng cường $\times 1.25$ đến $1.5$.
   - Cuối tuần (Thứ 7 & Chủ Nhật): Phụ thu thêm 15% - 20% do nhu cầu tăng cao.

2. **Yếu tố thích ứng thời tiết (Weather & Demand Multipliers):**
   - Trời mưa bão / Nhiệt độ cực đoan: Tự động áp dụng chiết khấu hỗ trợ cầu thủ (giảm 10% - 20%).
   - Tỷ lệ lấp đầy sân (Occupancy Rate): Khi cụm sân đạt trên 80% công suất trong ngày, áp dụng hệ số phụ thu giờ vàng.

---

## 2. Kiến Trúc Phòng Thủ 3 Tầng (Three-Tier Defense Architecture)

Mọi yêu cầu dự đoán giá và trò chuyện AI đều phải tuân thủ nghiêm ngặt mô hình dự phòng đa tầng sau:

```
[Client / Backend Gọi API AI]
            │
            ▼
┌──────────────────────────────────────┐
│  TẦNG 1: BỘ ĐỆM RAM (lru_cache)      │ ───(Hit)───> Trả kết quả tức thì (0ms)
└──────────────────┬───────────────────┘
                   │ (Miss)
                   ▼
┌──────────────────────────────────────┐
│  TẦNG 2: LOCAL LLM / MODEL (PORT 1234)│ ───(Thành công)───> Cập nhật cache & Trả về (< 500ms)
└──────────────────┬───────────────────┘
                   │ (Mất kết nối / Timeout / Lỗi model)
                   ▼
┌──────────────────────────────────────┐
│  TẦNG 3: SMART REGEX FALLBACK NLP    │ ───(Khớp quy tắc)─> Phân tích từ khóa nội bộ (< 5ms)
└──────────────────┬───────────────────┘
                   │ (AI Service Offline hoàn toàn)
                   ▼
┌──────────────────────────────────────┐
│  TẦNG DỰ PHÒNG CUỐI: C# GRACEFUL     │ ───(Backend .NET)─> Tự tính phụ thu theo bảng giá cứng
└──────────────────────────────────────┘
```

---

## 3. Quy Chuẩn Vận Hành Mô Hình Ngôn Ngữ Lớn (LLM Guardrails)

- **Zero Cloud Leakage:** Toàn bộ quá trình suy luận (Inference) của mô hình Qwen 2.5 7B Instruct phải thực thi tại máy chủ cục bộ (LM Studio `http://127.0.0.1:1234/v1`), tuyệt đối không gửi API Key hoặc dữ liệu người dùng ra dịch vụ đám mây công cộng.
- **Circuit Breaker:** Client phía Backend .NET (`AIServiceClient.cs`) phải đặt thời gian chờ tối đa (Timeout $\le 5$ giây). Nếu quá 3 lần lỗi liên tiếp, tự động chuyển trạng thái Circuit Breaker sang OPEN để không chặn luồng đặt sân của khách.
