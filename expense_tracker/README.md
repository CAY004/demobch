# KA Smart Expense System

Kiến trúc đã tách lớp rõ ràng:

Frontend  
↓  
Backend  
↓  
Database  
↓  
AI Assistant

## Tính năng
- Giao diện hiện đại (glass style) + logo **KA**.
- Đổi ngôn ngữ toàn hệ thống qua icon 🌐 (Việt/Anh).
- Đăng ký/đăng nhập người dùng.
- Giao dịch lưu theo từng user, data được giữ trong thư mục `data/`.
- Nút **Reset hệ thống (giữ data)**: reset trạng thái sử dụng, không xóa DB.

## Chạy app
```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your_key"
streamlit run expense_tracker/app.py
```

## Cấu trúc
- `expense_tracker/frontend.py`: UI, charts, i18n text.
- `expense_tracker/backend.py`: điều phối nghiệp vụ.
- `expense_tracker/database.py`: SQLite + users/transactions.
- `expense_tracker/ai_assistant.py`: gọi OpenAI để parse giao dịch.
- `expense_tracker/theme.py`: CSS theme hiện đại.

## Bảo mật API key
- Không hardcode `sk-...` trong code.
- Nhập API key ở sidebar (chỉ giữ trong phiên) hoặc dùng biến môi trường `OPENAI_API_KEY`.
- Nếu key từng lộ, hãy revoke key cũ và tạo key mới ngay.
