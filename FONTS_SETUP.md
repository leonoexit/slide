# 🔤 Hướng Dẫn Cài Đặt Fonts

## ❓ Tại Sao Cần Self-Host Fonts?

Khi sử dụng Playwright để render HTML thành PDF, môi trường headless browser **KHÔNG** có quyền truy cập vào:
- Fonts đã cài đặt trên máy tính của bạn
- Fonts từ Google Fonts (có thể bị chặn hoặc load chậm)

**Giải pháp:** Đặt file fonts ngay trong thư mục dự án để đảm bảo 100% fonts được render đúng.

---

## 🚀 Cách 1: Tự Động (Khuyến Nghị)

### Chạy Script Tải Fonts

```bash
python download_fonts_final.py
```

Script này sẽ:
- ✅ Tự động tạo thư mục `fonts/`
- ✅ Tải 4 file fonts từ CDN (jsDelivr)
- ✅ Kiểm tra tính hợp lệ của fonts
- ✅ Báo cáo kết quả chi tiết

### Fonts Sẽ Được Tải:

| Font File                  | Font Family    | Weight | Kích Thước |
|----------------------------|----------------|--------|------------|
| DMSans-Regular.woff2       | DM Sans        | 400    | ~20-30 KB  |
| DMSans-Medium.woff2        | DM Sans        | 500    | ~20-30 KB  |
| DMSans-Bold.woff2          | DM Sans        | 700    | ~20-30 KB  |
| SpaceGrotesk-Bold.woff2    | Space Grotesk  | 700    | ~30-40 KB  |

---

## 🔧 Cách 2: Tải Thủ Công

Nếu script tự động không hoạt động (do firewall, proxy, v.v.), hãy tải thủ công:

### Bước 1: Tải Fonts Từ Google Fonts

#### DM Sans:
1. Truy cập: https://fonts.google.com/specimen/DM+Sans
2. Click nút **"Download family"**
3. Giải nén file ZIP

#### Space Grotesk:
1. Truy cập: https://fonts.google.com/specimen/Space+Grotesk
2. Click nút **"Download family"**
3. Giải nén file ZIP

### Bước 2: Chuyển Đổi TTF sang WOFF2

Google Fonts cung cấp file `.ttf`, nhưng web sử dụng `.woff2` (nhỏ hơn, load nhanh hơn).

**Công cụ chuyển đổi online:**
- https://cloudconvert.com/ttf-to-woff2
- https://convertio.co/ttf-woff2/

**Hoặc dùng CLI (nếu đã cài `fonttools`):**
```bash
pip install fonttools brotli
pyftsubset font.ttf --output-file=font.woff2 --flavor=woff2
```

### Bước 3: Đổi Tên và Sắp Xếp Files

Sau khi chuyển đổi, đổi tên các file và đặt vào thư mục `fonts/`:

```
slide/
└── fonts/
    ├── DMSans-Regular.woff2      (từ: DMSans-Regular.ttf)
    ├── DMSans-Medium.woff2       (từ: DMSans-Medium.ttf)
    ├── DMSans-Bold.woff2         (từ: DMSans-Bold.ttf)
    └── SpaceGrotesk-Bold.woff2   (từ: SpaceGrotesk-Bold.ttf)
```

---

## 🔍 Kiểm Tra Fonts Đã Cài Đặt Đúng

### Kiểm Tra Cấu Trúc Thư Mục:

```bash
ls -lh fonts/
```

**Kết quả mong đợi:**
```
DMSans-Regular.woff2       (~20-30 KB)
DMSans-Medium.woff2        (~20-30 KB)
DMSans-Bold.woff2          (~20-30 KB)
SpaceGrotesk-Bold.woff2    (~30-40 KB)
```

### Kiểm Tra File Có Hợp Lệ Không:

```bash
file fonts/*.woff2
```

**Kết quả mong đợi:**
```
fonts/DMSans-Regular.woff2: Web Open Font Format, version 2.0
fonts/DMSans-Medium.woff2: Web Open Font Format, version 2.0
...
```

---

## 📋 Checklist Trước Khi Chạy Script

- [ ] Thư mục `fonts/` đã tồn tại
- [ ] Có đủ 4 file `.woff2` trong thư mục `fonts/`
- [ ] Mỗi file có kích thước > 10 KB (không phải file lỗi)
- [ ] File `name.html` đã có khai báo `@font-face` (✓ đã cập nhật)

---

## ❌ Xử Lý Sự Cố

### Lỗi: "Font không hiển thị đúng trong PDF"

**Nguyên nhân:** Fonts chưa được tải hoặc đường dẫn sai.

**Giải pháp:**
1. Kiểm tra fonts đã tồn tại: `ls fonts/*.woff2`
2. Kiểm tra `name.html` có chứa `@font-face` declarations
3. Đảm bảo đường dẫn trong HTML là `fonts/TenFont.woff2` (relative path)

### Lỗi: "HTTP Error 403: Forbidden" khi tải fonts

**Nguyên nhân:** CDN chặn request từ script.

**Giải pháp:**
1. Thử tải từ nguồn khác (xem Cách 2 - Tải Thủ Công)
2. Sử dụng VPN hoặc thay đổi mạng
3. Tải trực tiếp từ Google Fonts website

### File fonts chỉ có vài KB (< 10 KB)

**Nguyên nhân:** Tải về trang lỗi thay vì file font thực.

**Giải pháp:**
1. Xóa file lỗi: `rm fonts/*.woff2`
2. Tải lại bằng Cách 2 (thủ công)
3. Kiểm tra kích thước file sau khi tải

---

## 🎓 Giải Thích Kỹ Thuật

### Tại sao dùng WOFF2 thay vì TTF hoặc OTF?

| Format | Kích Thước | Browser Support | Load Speed |
|--------|------------|-----------------|------------|
| TTF    | 100%       | ✅ Tốt          | Chậm       |
| WOFF   | ~40%       | ✅ Tốt          | Nhanh      |
| WOFF2  | ~30%       | ✅ Rất tốt      | Rất nhanh  |

**WOFF2** = Web Open Font Format 2.0
- Nén Brotli → nhỏ nhất
- Load nhanh nhất
- Được tất cả trình duyệt hiện đại hỗ trợ

### Thuộc tính `font-display: swap`

```css
@font-face {
    font-family: 'DM Sans';
    src: url('fonts/DMSans-Regular.woff2') format('woff2');
    font-display: swap;  /* ← Dòng này */
}
```

- **swap:** Hiển thị font hệ thống ngay, đổi sang custom font khi đã load xong
- Ngăn chặn "FOIT" (Flash of Invisible Text)
- Tốt cho UX nhưng không quan trọng trong PDF generation

---

## 📚 Nguồn Fonts Thay Thế

Nếu không thể tải DM Sans hoặc Space Grotesk, bạn có thể dùng fonts tương tự:

| Font Gốc        | Font Thay Thế Miễn Phí         |
|-----------------|--------------------------------|
| DM Sans         | Inter, Open Sans, Roboto       |
| Space Grotesk   | Outfit, Manrope, Plus Jakarta  |

**Lưu ý:** Nếu đổi fonts, cần cập nhật `@font-face` declarations trong `name.html`.

---

## ✅ Kết Luận

Sau khi hoàn tất setup fonts:

```bash
# Chạy script chuyển đổi
python html_to_pdf_png.py
```

Fonts sẽ được render **100% chính xác** trong cả PDF và PNG! 🎉
