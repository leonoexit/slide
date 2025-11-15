# HTML to PDF & PNG Converter

Công cụ chuyển đổi file HTML thành PDF và tách thành các file PNG chất lượng cao.

## ✨ Tính năng

- ✅ Chuyển đổi HTML sang PDF với rendering chính xác 100% (giữ nguyên CSS, fonts, backgrounds)
- ✅ Tách mỗi trang PDF thành file PNG riêng biệt
- ✅ Xuất ảnh chất lượng cao (2400x2400px từ slide 1200x1200px)
- ✅ Self-hosted fonts để đảm bảo font hiển thị đúng 100%
- ✅ Tự động dọn dẹp file tạm
- ✅ Hiển thị tiến trình xử lý

## ⚡ Bắt Đầu Nhanh

### 1️⃣ Cài Đặt Dependencies

```bash
# Cài đặt thư viện Python
pip install -r requirements.txt

# Cài đặt trình duyệt Chromium cho Playwright
playwright install chromium
```

### 2️⃣ Cài Đặt Fonts (QUAN TRỌNG!)

**Tự động (khuyến nghị):**
```bash
python download_fonts_final.py
```

**Thủ công:**
- Xem hướng dẫn chi tiết trong [FONTS_SETUP.md](FONTS_SETUP.md)

### 3️⃣ Chạy Script

**Cách đơn giản nhất** (tự động tìm file .html):
```bash
python html_to_pdf_png.py
```

**Chỉ định file cụ thể:**
```bash
python html_to_pdf_png.py myslides.html
```

**Tùy chọn nâng cao:**
```bash
# Chỉ định thư mục output
python html_to_pdf_png.py -o my_images/

# Tăng chất lượng ảnh (zoom 3x = 3600x3600px)
python html_to_pdf_png.py myslides.html -z 3

# Xem tất cả options
python html_to_pdf_png.py -h
```

---

## 📦 Cài đặt Chi tiết

```bash
# Cài đặt thư viện Python
pip install -r requirements.txt

# Cài đặt trình duyệt Chromium cho Playwright
playwright install chromium
```

## 🚀 Sử dụng

### Cách Sử Dụng Cơ Bản

```bash
# Tự động tìm file .html trong thư mục
python html_to_pdf_png.py

# Hoặc chỉ định file cụ thể
python html_to_pdf_png.py myslides.html
```

### Options Nâng Cao

```bash
# Xem tất cả options
python html_to_pdf_png.py -h

# Chỉ định thư mục output
python html_to_pdf_png.py -o my_output/

# Tùy chỉnh zoom factor (chất lượng ảnh)
python html_to_pdf_png.py -z 3  # Tạo ảnh 3600x3600px

# Kết hợp nhiều options
python html_to_pdf_png.py slides.html -o output/ -z 2
```

### Script Sẽ:
1. Tự động tìm hoặc nhận file HTML được chỉ định
2. Tạo file PDF tạm thời
3. Tách PDF thành các file PNG trong thư mục output
4. Tự động xóa file PDF tạm

### Tính Năng Thông Minh:
- ✅ Không cần đổi tên file HTML thành `name.html` nữa
- ✅ Nếu có nhiều file .html, script sẽ hiển thị menu để chọn
- ✅ Tự động validate file tồn tại và đúng định dạng
- ✅ Hiển thị cấu hình trước khi chạy

## 📁 Cấu trúc file

```
slide/
├── html_to_pdf_png.py         # Script chính
├── download_fonts_final.py    # Script tải fonts
├── requirements.txt           # Danh sách thư viện
├── README.md                  # Hướng dẫn tổng quan
├── HUONG_DAN.md              # Hướng dẫn chi tiết (tiếng Việt)
├── FONTS_SETUP.md            # Hướng dẫn cài đặt fonts
├── name.html                 # File HTML đầu vào (ví dụ)
├── fonts/                    # Thư mục chứa self-hosted fonts
│   ├── DMSans-Regular.woff2
│   ├── DMSans-Medium.woff2
│   ├── DMSans-Bold.woff2
│   └── SpaceGrotesk-Bold.woff2
└── slides_images/            # Thư mục chứa ảnh PNG (tự động tạo)
    ├── slide_01.png
    ├── slide_02.png
    └── ...
```

## 🔧 Yêu cầu

- Python 3.7+
- Playwright
- PyMuPDF (fitz)

## 📖 Tài liệu

- **[HUONG_DAN.md](HUONG_DAN.md)** - Hướng dẫn sử dụng chi tiết
  - Cách cấu hình
  - Xử lý lỗi
  - Tùy chỉnh kích thước ảnh

- **[FONTS_SETUP.md](FONTS_SETUP.md)** - Hướng dẫn cài đặt fonts (QUAN TRỌNG!)
  - Tại sao cần self-host fonts
  - Cách tải fonts tự động
  - Cách tải fonts thủ công
  - Xử lý sự cố fonts

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
