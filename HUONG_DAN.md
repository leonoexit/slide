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

### Bước 3: Cài đặt Fonts (QUAN TRỌNG!)

⚠️ **BƯỚC NÀY RẤT QUAN TRỌNG** - Nếu không cài fonts, chữ trong PDF/PNG sẽ bị đổi sang font khác!

**Cách nhanh nhất:**
```bash
python download_fonts_final.py
```

**Nếu script trên không hoạt động:**
- Xem hướng dẫn chi tiết trong file [FONTS_SETUP.md](FONTS_SETUP.md)
- Tải fonts thủ công từ Google Fonts và đặt vào thư mục `fonts/`

**Kiểm tra fonts đã cài đặt chưa:**
```bash
ls fonts/
```

Bạn cần có 4 file:
- `DMSans-Regular.woff2`
- `DMSans-Medium.woff2`
- `DMSans-Bold.woff2`
- `SpaceGrotesk-Bold.woff2`

## 📁 Chuẩn bị

Đảm bảo:
1. File HTML của bạn (tên bất kỳ, có extension `.html`)
2. Thư mục `fonts/` đã có đủ 4 file fonts (xem bước 3 ở trên)
3. File HTML và script nằm trong cùng thư mục

**Lưu ý:** Bạn **KHÔNG CẦN** đổi tên file HTML thành `name.html` nữa!

## ▶️ Chạy script

### Cách 1: Tự động tìm file HTML

```bash
python html_to_pdf_png.py
```

Script sẽ tự động:
- Tìm tất cả file `.html` trong thư mục
- Nếu chỉ có 1 file: sử dụng file đó
- Nếu có nhiều file: hiển thị menu để bạn chọn

### Cách 2: Chỉ định file cụ thể

```bash
python html_to_pdf_png.py myslides.html
```

### Cách 3: Tùy chỉnh options

```bash
# Chỉ định thư mục output
python html_to_pdf_png.py -o my_images/

# Tăng chất lượng ảnh (zoom 3x)
python html_to_pdf_png.py myslides.html -z 3

# Xem tất cả options
python html_to_pdf_png.py -h
```

**Các options có sẵn:**
- `-o, --output`: Thư mục chứa ảnh PNG (mặc định: `slides_images`)
- `-z, --zoom`: Hệ số phóng đại (mặc định: 2)
- `-p, --pdf`: Tên file PDF tạm (mặc định: `temp_slides.pdf`)
- `-h, --help`: Hiển thị help

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

**Không cần chỉnh sửa code!** Tất cả cấu hình được thực hiện qua command line:

```bash
# Thay đổi thư mục output
python html_to_pdf_png.py -o my_output/

# Thay đổi zoom factor
python html_to_pdf_png.py -z 3  # Tạo ảnh 3600x3600px

# Thay đổi tên file PDF tạm
python html_to_pdf_png.py -p custom_temp.pdf

# Kết hợp tất cả
python html_to_pdf_png.py myslides.html -o output/ -z 2 -p temp.pdf
```

**Bảng zoom factor:**
| Zoom | Kích thước ảnh | Kích thước file | Khuyến nghị |
|------|----------------|-----------------|-------------|
| 1    | 1200x1200px    | ~50-100 KB      | Web nhỏ     |
| 2    | 2400x2400px    | ~200-400 KB     | ✅ Mặc định |
| 3    | 3600x3600px    | ~500-800 KB     | In ấn       |
| 4    | 4800x4800px    | ~1-2 MB         | Poster      |

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

### Lỗi: "Font chữ trong PDF/PNG không đúng"
- **Nguyên nhân:** Fonts chưa được cài đặt hoặc file fonts bị lỗi
- **Giải pháp:**
  1. Kiểm tra thư mục `fonts/` có đủ 4 file không: `ls fonts/`
  2. Chạy lại: `python download_fonts_final.py`
  3. Nếu vẫn lỗi, xem [FONTS_SETUP.md](FONTS_SETUP.md) để tải thủ công

### Lỗi: "HTTP Error 403: Forbidden" khi tải fonts
- **Nguyên nhân:** Mạng hoặc firewall chặn kết nối
- **Giải pháp:** Tải fonts thủ công theo hướng dẫn trong [FONTS_SETUP.md](FONTS_SETUP.md)

## 📧 Hỗ trợ

Nếu gặp vấn đề, hãy kiểm tra:
1. Đã cài đặt đầy đủ các thư viện chưa
2. File HTML có tồn tại và đúng định dạng không
3. Có đủ dung lượng ổ cứng để lưu ảnh không
