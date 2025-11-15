# 📁 Thư Mục Fonts

Thư mục này chứa các font files cần thiết để render HTML thành PDF/PNG với font chữ chính xác.

## 📋 Fonts Cần Thiết

Bạn cần có 4 file fonts sau đây trong thư mục này:

- ✅ `DMSans-Regular.woff2` (~20-30 KB)
- ✅ `DMSans-Medium.woff2` (~20-30 KB)
- ✅ `DMSans-Bold.woff2` (~20-30 KB)
- ✅ `SpaceGrotesk-Bold.woff2` (~30-40 KB)

## ⚡ Cách Tải Fonts

### Phương Pháp 1: Tự Động (Khuyến Nghị)

Từ thư mục gốc của project, chạy:

```bash
python download_fonts_final.py
```

Script sẽ tự động tải tất cả fonts vào thư mục này.

### Phương Pháp 2: Thủ Công

Nếu script tự động không hoạt động:

1. Xem hướng dẫn chi tiết trong [FONTS_SETUP.md](../FONTS_SETUP.md)
2. Tải fonts từ Google Fonts
3. Chuyển đổi sang định dạng WOFF2
4. Đặt vào thư mục này với tên file chính xác như trên

## ⚠️ Lưu Ý

- **KHÔNG** commit file fonts vào Git (file lớn, không cần thiết)
- Mỗi developer cần tự tải fonts về máy của họ
- Kiểm tra kích thước file - nếu < 10 KB có thể bị lỗi

## ✅ Kiểm Tra

Chạy lệnh sau để kiểm tra:

```bash
ls -lh
```

Bạn sẽ thấy 4 file .woff2 với kích thước hợp lý.

---

Nếu gặp vấn đề, xem [FONTS_SETUP.md](../FONTS_SETUP.md) để biết thêm chi tiết.
