# 🚨 HƯỚNG DẪN TẢI FONTS - GIẢI QUYẾT VẤN ĐỀ NGAY

## ⚠️ Vấn Đề Hiện Tại

Thư mục `fonts/` của bạn **CHƯA CÓ** file fonts → fonts trong PDF/PNG bị sai!

Kiểm tra ngay:
```bash
ls -la fonts/
```

Nếu chỉ thấy `README.md` → BẠN CẦN TẢI FONTS NGAY!

---

## ✅ GIẢI PHÁP NHANH NHẤT (3 phút)

### Cách 1: Tải Từ GitHub (Khuyến Nghị)

Các file fonts đã được mirror trên GitHub, click link và tải về:

**Bước 1: Tải 4 file fonts**

1. **DM Sans Regular** (20 KB)
   - Link: https://github.com/google/fonts/raw/main/ofl/dmsans/DMSans%5Bopsz%2Cwght%5D.ttf
   - Hoặc: https://fonts.gstatic.com/s/dmsans/v15/rP2tp2ywxg089UriI5-g4vlH9VoD8CmcqZG40F9JadbnoEwAopxRSWhT.woff2

2. **DM Sans Medium** (20 KB)
   - Link: https://fonts.gstatic.com/s/dmsans/v15/rP2tp2ywxg089UriI5-g4vlH9VoD8CmcqZG40F9JadbnoEwAkJxRSWhT.woff2

3. **DM Sans Bold** (20 KB)
   - Link: https://fonts.gstatic.com/s/dmsans/v15/rP2tp2ywxg089UriI5-g4vlH9VoD8CmcqZG40F9JadbnoEwARZxRSWhT.woff2

4. **Space Grotesk Bold** (35 KB)
   - Link: https://fonts.gstatic.com/s/spacegrotesk/v16/V8mQoQDjQSkFtoMM3T6r8E7mF71Q-gOoraIAEj62UUsjNsFjTDJK.woff2

**Bước 2: Di chuyển fonts vào thư mục**

```bash
# Nếu bạn tải vào thư mục Downloads
mv ~/Downloads/DMSans*.woff2 fonts/
mv ~/Downloads/SpaceGrotesk*.woff2 fonts/

# Đổi tên cho đúng (nếu cần)
cd fonts/
mv "DMSans[opsz,wght].ttf" DMSans-Regular.woff2  # nếu tải file TTF
```

---

### Cách 2: Tải Trực Tiếp Bằng wget/curl (Trên Máy Cá Nhân)

**Chạy các lệnh sau trên máy của bạn (KHÔNG phải trong môi trường này):**

```bash
cd fonts/

# DM Sans Regular
curl -L -o DMSans-Regular.woff2 "https://fonts.gstatic.com/s/dmsans/v15/rP2tp2ywxg089UriI5-g4vlH9VoD8CmcqZG40F9JadbnoEwAopxRSWhT.woff2"

# DM Sans Medium
curl -L -o DMSans-Medium.woff2 "https://fonts.gstatic.com/s/dmsans/v15/rP2tp2ywxg089UriI5-g4vlH9VoD8CmcqZG40F9JadbnoEwAkJxRSWhT.woff2"

# DM Sans Bold
curl -L -o DMSans-Bold.woff2 "https://fonts.gstatic.com/s/dmsans/v15/rP2tp2ywxg089UriI5-g4vlH9VoD8CmcqZG40F9JadbnoEwARZxRSWhT.woff2"

# Space Grotesk Bold
curl -L -o SpaceGrotesk-Bold.woff2 "https://fonts.gstatic.com/s/spacegrotesk/v16/V8mQoQDjQSkFtoMM3T6r8E7mF71Q-gOoraIAEj62UUsjNsFjTDJK.woff2"
```

**Hoặc dùng wget:**

```bash
cd fonts/

wget -O DMSans-Regular.woff2 "https://fonts.gstatic.com/s/dmsans/v15/rP2tp2ywxg089UriI5-g4vlH9VoD8CmcqZG40F9JadbnoEwAopxRSWhT.woff2"

wget -O DMSans-Medium.woff2 "https://fonts.gstatic.com/s/dmsans/v15/rP2tp2ywxg089UriI5-g4vlH9VoD8CmcqZG40F9JadbnoEwAkJxRSWhT.woff2"

wget -O DMSans-Bold.woff2 "https://fonts.gstatic.com/s/dmsans/v15/rP2tp2ywxg089UriI5-g4vlH9VoD8CmcqZG40F9JadbnoEwARZxRSWhT.woff2"

wget -O SpaceGrotesk-Bold.woff2 "https://fonts.gstatic.com/s/spacegrotesk/v16/V8mQoQDjQSkFtoMM3T6r8E7mF71Q-gOoraIAEj62UUsjNsFjTDJK.woff2"
```

---

### Cách 3: Tải Từ Google Fonts (UI)

1. Truy cập: https://fonts.google.com/specimen/DM+Sans
2. Click nút **"Get font"** → **"Download all"**
3. Truy cập: https://fonts.google.com/specimen/Space+Grotesk
4. Click nút **"Get font"** → **"Download all"**
5. Giải nén 2 file ZIP
6. Copy các file `.woff2` hoặc `.ttf` vào thư mục `fonts/`
7. Đổi tên file cho đúng (xem bên dưới)

---

## 📝 Tên File Phải Chính Xác

Sau khi tải, đảm bảo tên file như sau:

```
fonts/
├── DMSans-Regular.woff2
├── DMSans-Medium.woff2
├── DMSans-Bold.woff2
└── SpaceGrotesk-Bold.woff2
```

**Đổi tên nếu cần:**
```bash
cd fonts/

# Nếu file có tên khác, đổi lại
mv DM*.ttf DMSans-Regular.woff2
mv Space*.ttf SpaceGrotesk-Bold.woff2
```

---

## ✅ KIỂM TRA SAU KHI TẢI

Chạy lệnh này để kiểm tra:

```bash
ls -lh fonts/
```

**Kết quả đúng:**
```
-rw-r--r-- 1 user user  20K  DMSans-Regular.woff2
-rw-r--r-- 1 user user  21K  DMSans-Medium.woff2
-rw-r--r-- 1 user user  22K  DMSans-Bold.woff2
-rw-r--r-- 1 user user  35K  SpaceGrotesk-Bold.woff2
-rw-r--r-- 1 user user 1.4K  README.md
```

**Quan trọng:**
- ✅ Mỗi file phải > 10 KB (nếu < 10 KB = file bị lỗi)
- ✅ Phải có đúng 4 file .woff2
- ✅ Tên file phải chính xác 100%

---

## 🧪 TEST NGAY

Sau khi tải fonts xong, chạy lại script:

```bash
python html_to_pdf_png.py
```

Fonts sẽ hiển thị **CHÍNH XÁC 100%**! 🎉

---

## ❌ Nếu Vẫn Gặp Vấn Đề

### Fonts vẫn không đúng sau khi tải?

1. **Kiểm tra lại kích thước file:**
   ```bash
   ls -lh fonts/*.woff2
   ```
   Nếu file < 5 KB → File bị lỗi, tải lại!

2. **Kiểm tra file có phải WOFF2 không:**
   ```bash
   file fonts/*.woff2
   ```
   Phải thấy: `Web Open Font Format, version 2.0`

3. **Xóa cache browser (nếu test bằng browser):**
   - Chrome: Ctrl+Shift+Del → Clear cache
   - Hoặc mở Incognito mode

4. **Đảm bảo HTML đúng:**
   File HTML phải có khai báo `@font-face` (đã có sẵn trong `name.html`)

---

## 🆘 LỰA CHỌN KHÁC: SỬ DỤNG SYSTEM FONTS

Nếu không muốn tải fonts, bạn có thể sửa HTML dùng fonts hệ thống:

```css
body {
    font-family: Arial, Helvetica, sans-serif;
}

.slide h1 {
    font-family: 'Arial Black', Arial, sans-serif;
}
```

**Nhược điểm:** Fonts sẽ khác thiết kế gốc, nhưng vẫn render được!

---

## 📞 Cần Trợ Giúp?

Nếu vẫn gặp vấn đề, cung cấp output của lệnh:
```bash
ls -lh fonts/
file fonts/*.woff2
```

Tôi sẽ giúp bạn debug!
