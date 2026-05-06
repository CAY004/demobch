# Migration to `https://github.com/CAY004/totnghiep`

Không thể clone repo đích trong môi trường hiện tại do lỗi mạng 403 từ GitHub.

## Các bước chuyển môi trường
1. Trên máy có quyền truy cập GitHub:
   ```bash
   git clone https://github.com/CAY004/totnghiep.git
   cd totnghiep
   ```
2. Copy các thành phần app từ repo này sang repo đích:
   - `expense_tracker/`
   - `Dockerfile`
   - `docker-compose.yml`
   - `builds/`
   - cập nhật `requirements.txt` thêm `streamlit pandas plotly openai`
3. Tạo biến môi trường trong repo đích:
   - `OPENAI_API_KEY`
   - `APP_PASSWORD_PEPPER`
4. Chạy local:
   ```bash
   pip install -r requirements.txt
   streamlit run expense_tracker/app.py
   ```
5. Chạy Docker:
   ```bash
   docker compose up --build
   ```

## Ghi chú bảo mật
- Không commit API key vào repo.
- Nếu key đã lộ, revoke và tạo key mới.

## Script tự động đổi môi trường
Bạn có thể chạy script:
```bash
./switch_environment.sh https://github.com/CAY004/totnghiep.git /workspace/totnghiep
```
Nếu mạng cho phép, script sẽ clone repo đích và bạn có thể làm việc trực tiếp trong thư mục mới.
