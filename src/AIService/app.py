import os
import sys
import json
from datetime import datetime
from functools import lru_cache
from flask import Flask, request, jsonify
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

app = Flask(__name__)

# TỐI ƯU HIỆU NĂNG: Khởi tạo HTTP Connection Pool tái sử dụng kết nối TCP Keep-Alive
http_session = requests.Session()
adapter = HTTPAdapter(pool_connections=20, pool_maxsize=50, max_retries=Retry(total=1, backoff_factor=0.05))
http_session.mount("http://", adapter)
http_session.mount("https://", adapter)

# CẤU HÌNH CORS TOÀN DIỆN
try:
    from flask_cors import CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})
except Exception:
    @app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        return response

# CẤU HÌNH LM STUDIO LOCAL SERVER ENDPOINT (MÔ HÌNH 7B: QWEN2.5-CODER-7B-INSTRUCT)
LM_STUDIO_API_URL = "http://127.0.0.1:1234/v1/chat/completions"
LM_STUDIO_MODEL = "qwen2.5-coder-7b-instruct"

# SYSTEM PROMPT CHO MÔ HÌNH 7B TRỢ LÝ SÂN BÓNG ICTU THÁI NGUYÊN (ĐÃ HUẤN LUYỆN TOÀN BỘ TRI THỨC TỪ 1.5B)
SYSTEM_PROMPT = """Bạn là trợ lý đặt sân bóng đá AI thông minh của Cụm sân bóng ICTU Thái Nguyên (Mô hình Qwen 7B nâng cấp).
Phong cách: Nói chuyện bằng tiếng Việt tự nhiên, thân thiện, ngắn gọn và chính xác như nhân viên trực quán thật. Tuyệt đối không dùng từ ngữ dịch máy cứng nhắc.

TOÀN BỘ DỮ LIỆU TRI THỨC HỆ THỐNG ĐÃ HUẤN LUYỆN:
1. Địa điểm: Cụm sân bóng ICTU, Phường Quyết Thắng, TP. Thái Nguyên (khu vực Đại học CNTT & Truyền Thông).
2. Danh sách 5 sân:
   - Sân 1 & Sân 2: Sân 5 người cỏ nhân tạo tiêu chuẩn.
   - Sân 3 & Sân 4: Sân 7 người VIP chất lượng cao.
   - Sân 5: Sân 11 người chuẩn thi đấu Quốc tế.
3. Bảng giá niêm yết:
   - Khung giờ sáng (06:00 - 17:00): 150.000 VNĐ/giờ.
   - Khung giờ tối & đêm (ngoài 06:00 - 17:00): 300.000 VNĐ/giờ (x2 giá gốc do chi phí chiếu sáng cao áp).
   - Khung rạng sáng (02:00 - 05:00): 300.000 VNĐ/giờ (cho phép ĐẶT TRƯỚC trên website ít nhất 2 tiếng nếu còn chỗ).
4. Quy định đặt sân: Đặt trước tối thiểu 2 tiếng và tối đa trước 3 ngày.
5. Thanh toán & Hoàn tiền:
   - Thanh toán tự động qua Ví ảo (Virtual Wallet) hoặc quét mã VietQR MBBank.
   - HỦY SÂN: Hoàn tiền 100% tự động về ví nếu khách hủy trước giờ bóng lăn.
6. Trạng thái bảo trì: Nếu sân đang bật bảo trì thì tạm dừng đặt cho tới khi hoàn tất nâng cấp."""

@lru_cache(maxsize=256)
def get_smart_fallback_response(user_message):
    """
    SMART FALLBACK RESPONSE ENGINE CHO KHU VỰC ICTU THÁI NGUYÊN (TỰ NHIÊN & KHÔNG RẬP KHUÔN)
    Tối ưu hóa: LRU Cache trong RAM giúp phản hồi ngay lập tức 0ms với các câu hỏi trùng lặp.
    """
    msg = user_message.lower().strip()

    # Xử lý câu chào hỏi tự nhiên
    if msg in ["hi", "hello", "chào", "chào bạn", "chào bot", "xin chào", "alo", "bot ơi", "helo"]:
        return "Chào bạn! Mình là trợ lý AI sân bóng ICTU Thái Nguyên. Bạn cần tìm sân hay hỏi giá lúc nào thế?"

    if "2h" in msg or "02:" in msg or "3h" in msg or "03:" in msg or "4h" in msg or "04:" in msg or "5h" in msg or "05:" in msg or "đêm" in msg or "rạng sáng" in msg:
        return ("Khung giờ đêm muộn (02:00 - 05:00) giá 300.000 VNĐ/giờ nha bạn. Giờ này không có sân trực sẵn nhưng hệ thống vẫn hỗ trợ **đặt trước** nếu còn chỗ. Bạn muốn kiểm tra slot mấy giờ?")

    elif "giá" in msg or "nhiêu" in msg or "tiền" in msg or "bảng giá" in msg or "bao nhiêu" in msg:
        return ("Giá sân bên mình cực ưu đãi:\n* Ca sáng (06h - 17h): **150.000đ/giờ**\n* Ca tối & đêm (sau 17h): **300.000đ/giờ**\nBạn định đá khung giờ nào để mình check cho?")

    elif "sân nào trống" in msg or "trống" in msg or "lịch trống" in msg or "còn sân" in msg:
        return ("Hôm nay bên mình còn trống vài khung giờ đẹp:\n* Ca sáng: 08:00, 10:00, 15:00 (150k/h)\n* Ca tối: 18:00, 19:30 (300k/h)\nBạn muốn giữ chỗ slot nào?")

    elif "cảm ơn" in msg or "thanks" in msg or "ok" in msg or "thanhks" in msg:
        return "Dạ không có gì ạ! Cần chốt sân lúc nào bạn cứ nhắn mình nhé ⚽"

    else:
        return ("Dạ bạn cần hỏi về lịch sân trống, bảng giá hay đặt chỗ khung giờ nào cứ nhắn mình hỗ trợ ngay nhé!")

def query_lm_studio_local_api(messages_history, last_user_message=""):
    """
    Gửi HTTP POST Request trực tiếp sang LM Studio Local Server (http://127.0.0.1:1234/v1/chat/completions)
    kèm theo toàn bộ lịch sử trò chuyện (Context Memory), sử dụng connection pool.
    """
    try:
        formatted_messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        if isinstance(messages_history, list) and len(messages_history) > 0:
            for item in messages_history:
                if isinstance(item, dict) and "role" in item and "content" in item:
                    formatted_messages.append({
                        "role": item["role"],
                        "content": item["content"]
                    })
        elif last_user_message:
            formatted_messages.append({"role": "user", "content": last_user_message})

        payload = {
            "model": LM_STUDIO_MODEL,
            "messages": formatted_messages,
            "temperature": 0.7,
            "max_tokens": 300,
            "stream": False
        }
        
        headers = {"Content-Type": "application/json"}
        res = http_session.post(LM_STUDIO_API_URL, json=payload, headers=headers, timeout=3)
        
        if res.status_code == 200:
            data = res.json()
            if "choices" in data and len(data["choices"]) > 0:
                reply = data["choices"][0]["message"]["content"].strip()
                if reply:
                    return reply, f"LM-Studio ({LM_STUDIO_MODEL})"
    except Exception:
        pass

    # Fallback mượt mà nếu LM Studio chưa bật
    return get_smart_fallback_response(last_user_message), "Instant-Smart-Fallback-Engine"

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "service": "AI Pricing & LM Studio Assistant - ICTU Thai Nguyen",
        "lm_studio_url": LM_STUDIO_API_URL,
        "model": LM_STUDIO_MODEL,
        "port": 5050
    })

@app.route('/api/predict-price', methods=['POST', 'OPTIONS'])
def predict_price():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200

    data = request.get_json() or {}
    field_id = data.get('field_id', '')
    hour = int(data.get('hour', datetime.now().hour))

    reasons = []
    if 6 <= hour < 17:
        base_price = 150000
        multiplier = 1.0
        reasons.append("Khung giờ sáng 06:00-17:00 (150.000 VNĐ)")
    else:
        base_price = 150000
        multiplier = 2.0
        reasons.append("Khung giờ tối/đêm ngoài 06:00-17:00 (x2 giá gốc = 300.000 VNĐ)")

    if 2 <= hour < 5:
        reasons.append("Khung giờ đặc biệt 02:00-05:00 (Cho phép đặt trước nếu còn chỗ)")

    dynamic_price = base_price * multiplier

    return jsonify({
        "status": "success",
        "field_id": field_id,
        "base_price": base_price,
        "dynamic_price": dynamic_price,
        "multiplier": multiplier,
        "reasons": reasons,
        "timestamp": datetime.now().isoformat()
    })

BACKEND_SYSTEM_MAINTENANCE_URL = "http://127.0.0.1:5048/api/admin/system-maintenance"

def check_backend_system_maintenance():
    """Kiểm tra xem Backend C# có đang ở Chế độ Bảo trì Hệ thống hay không bằng persistent connection"""
    try:
        res = http_session.get(BACKEND_SYSTEM_MAINTENANCE_URL, timeout=1.5)
        if res.status_code == 200:
            return res.json().get('isMaintenance', False)
    except Exception:
        pass
    return False

@app.route('/api/chat-assistant', methods=['POST', 'OPTIONS'])
def chat_assistant():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200

    # Kiểm tra trạng thái Bảo Trì Toàn Hệ Thống từ C# Backend
    if check_backend_system_maintenance():
        maint_msg = "🛠️ **THÔNG BÁO BẢO TRÌ:** Hệ thống đang bảo trì để nâng cấp, vui lòng quay lại sau! Mọi chức năng đặt sân và thanh toán tạm thời ngừng phục vụ."
        return jsonify({
            "status": "success",
            "is_maintenance": True,
            "response": maint_msg,
            "reply": maint_msg,
            "provider": "System-Maintenance-Notice",
            "timestamp": datetime.now().isoformat()
        })

    data = request.get_json() or {}
    messages_history = data.get('messages', [])
    user_message = data.get('message', '') or data.get('prompt', '')

    if not user_message and isinstance(messages_history, list) and len(messages_history) > 0:
        last_item = messages_history[-1]
        if isinstance(last_item, dict) and last_item.get('role') == 'user':
            user_message = last_item.get('content', '')

    if not user_message and not messages_history:
        return jsonify({"status": "error", "response": "Vui lòng nhập câu hỏi!"}), 400

    response_text, provider = query_lm_studio_local_api(messages_history, user_message)

    return jsonify({
        "status": "success",
        "response": response_text,
        "reply": response_text,
        "provider": provider,
        "model": LM_STUDIO_MODEL,
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("=================================================")
    print("[AI SERVICE] Starting AI Pricing & LM Studio Local Server Assistant")
    print(f"[AI SERVICE] LM Studio Endpoint: {LM_STUDIO_API_URL}")
    print(f"[AI SERVICE] Active Model: {LM_STUDIO_MODEL}")
    print("[AI SERVICE] Listening Port: http://localhost:5050")
    print("=================================================")
    try:
        from waitress import serve
        print("[AI SERVICE] Engine: Waitress Production Multi-threaded WSGI Server (6 threads)")
        serve(app, host='0.0.0.0', port=5050, threads=6)
    except ImportError:
        print("[AI SERVICE] Engine: Flask Built-in Multi-threaded Server")
        app.run(host='0.0.0.0', port=5050, threaded=True, debug=False)

