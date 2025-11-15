# HTML to PDF & PNG Converter

Công cụ chuyển đổi file HTML thành PDF và tách thành các file PNG chất lượng cao.

## ✨ Tính năng

- ✅ Chuyển đổi HTML sang PDF với rendering chính xác 100% (giữ nguyên CSS, fonts, backgrounds)
- ✅ Tách mỗi trang PDF thành file PNG riêng biệt
- ✅ Xuất ảnh chất lượng cao (2400x2400px từ slide 1200x1200px)
- ✅ Tự động dọn dẹp file tạm
- ✅ Hiển thị tiến trình xử lý

## 📦 Cài đặt

```bash
# Cài đặt thư viện Python
pip install -r requirements.txt

# Cài đặt trình duyệt Chromium cho Playwright
playwright install chromium
```

## 🚀 Sử dụng

```bash
python html_to_pdf_png.py
```

Script sẽ:
1. Đọc file `name.html`
2. Tạo file PDF tạm thời
3. Tách PDF thành các file PNG trong thư mục `slides_images/`
4. Xóa file PDF tạm

## 📁 Cấu trúc file

```
slide/
├── html_to_pdf_png.py    # Script chính
├── requirements.txt       # Danh sách thư viện
├── HUONG_DAN.md          # Hướng dẫn chi tiết (tiếng Việt)
├── name.html             # File HTML đầu vào (ví dụ)
└── slides_images/        # Thư mục chứa ảnh PNG (tự động tạo)
    ├── slide_01.png
    ├── slide_02.png
    └── ...
```

## 🔧 Yêu cầu

- Python 3.7+
- Playwright
- PyMuPDF (fitz)

## 📖 Hướng dẫn chi tiết

Xem file [HUONG_DAN.md](HUONG_DAN.md) để biết thêm chi tiết về:
- Cách cấu hình
- Xử lý lỗi
- Tùy chỉnh kích thước ảnh

## 🎯 Ví dụ

File `name.html` bao gồm 5 slide demo với:
- Kích thước: 1200x1200 pixels mỗi slide
- Màu nền gradient đẹp mắt
- Font chữ rõ ràng, dễ đọc
- Số thứ tự slide ở góc dưới phải

Kết quả: 5 file PNG (2400x2400px) trong thư mục `slides_images/`

## 📝 License

MIT License

## 👤 Author

Created with ❤️ for easy HTML to image conversion
