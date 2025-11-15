# Hướng Dẫn Sử Dụng Script Chuyển Đổi HTML sang PDF và PNG

## 📋 Mô tả

Script này giúp bạn:
1. Chuyển đổi file HTML thành PDF với chất lượng cao
2. Tách mỗi trang PDF thành file ảnh PNG riêng biệt

## 🔧 Cài đặt

### Bước 1: Cài đặt các thư viện Python

```bash
pip install -r requirements.txt
```

### Bước 2: Cài đặt trình duyệt cho Playwright

```bash
playwright install chromium
```

Hoặc cài đặt tất cả các trình duyệt:

```bash
playwright install
```

## 📁 Chuẩn bị

Đảm bảo file `name.html` của bạn nằm trong cùng thư mục với script `html_to_pdf_png.py`.

## ▶️ Chạy script

```bash
python html_to_pdf_png.py
```

Hoặc:

```bash
python3 html_to_pdf_png.py
```

## 📤 Kết quả

Sau khi chạy script, bạn sẽ có:
- Thư mục `slides_images/` chứa các file PNG:
  - `slide_01.png`
  - `slide_02.png`
  - `slide_03.png`
  - ...
  - `slide_67.png`

Mỗi ảnh có kích thước **2400x2400 pixels** (chất lượng cao, phóng đại 2x từ kích thước gốc 1200x1200px).

## ⚙️ Cấu hình

Bạn có thể chỉnh sửa các thông số trong file `html_to_pdf_png.py`:

```python
HTML_FILE = "name.html"           # Tên file HTML đầu vào
TEMP_PDF_FILE = "temp_slides.pdf" # Tên file PDF tạm thời
OUTPUT_DIR = "slides_images"      # Thư mục chứa ảnh đầu ra
ZOOM_FACTOR = 2                   # Hệ số phóng đại (2 = ảnh 2400x2400px)
```

## 📝 Lưu ý

- Script sẽ tự động xóa file PDF tạm thời sau khi hoàn thành
- Nếu thư mục `slides_images` đã tồn tại, các ảnh mới sẽ ghi đè lên ảnh cũ
- Thời gian chạy phụ thuộc vào số lượng slide trong file HTML

## ❌ Xử lý lỗi

### Lỗi: "Không tìm thấy file name.html"
- Đảm bảo file `name.html` nằm trong cùng thư mục với script

### Lỗi: "playwright not found"
- Chạy: `pip install playwright` và `playwright install chromium`

### Lỗi: "fitz not found" hoặc "PyMuPDF not found"
- Chạy: `pip install PyMuPDF`

## 📧 Hỗ trợ

Nếu gặp vấn đề, hãy kiểm tra:
1. Đã cài đặt đầy đủ các thư viện chưa
2. File HTML có tồn tại và đúng định dạng không
3. Có đủ dung lượng ổ cứng để lưu ảnh không
