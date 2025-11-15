#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tải fonts cho HTML to PDF converter
Chạy script này trên máy tính cá nhân để tải fonts từ Google Fonts
"""

import urllib.request
import os
import sys

def download_font(url, filename):
    """Tải một font file từ URL"""
    try:
        req = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
        )

        with urllib.request.urlopen(req, timeout=30) as response:
            data = response.read()

        # Kiểm tra xem có phải file font hợp lệ không
        if len(data) < 1000:  # Font file thường > 1KB
            return False, f"File quá nhỏ ({len(data)} bytes)"

        # Lưu file
        with open(filename, 'wb') as f:
            f.write(data)

        return True, len(data)

    except Exception as e:
        return False, str(e)

def main():
    print("=" * 70)
    print("SCRIPT TẢI FONTS CHO HTML TO PDF CONVERTER")
    print("=" * 70)
    print()

    # Tạo thư mục fonts
    os.makedirs('fonts', exist_ok=True)
    print("✓ Đã tạo/kiểm tra thư mục fonts/\n")

    # Danh sách fonts cần tải từ CDN
    fonts_to_download = [
        {
            'name': 'DM Sans Regular',
            'file': 'fonts/DMSans-Regular.woff2',
            'url': 'https://cdn.jsdelivr.net/fontsource/fonts/dm-sans@latest/latin-400-normal.woff2'
        },
        {
            'name': 'DM Sans Medium',
            'file': 'fonts/DMSans-Medium.woff2',
            'url': 'https://cdn.jsdelivr.net/fontsource/fonts/dm-sans@latest/latin-500-normal.woff2'
        },
        {
            'name': 'DM Sans Bold',
            'file': 'fonts/DMSans-Bold.woff2',
            'url': 'https://cdn.jsdelivr.net/fontsource/fonts/dm-sans@latest/latin-700-normal.woff2'
        },
        {
            'name': 'Space Grotesk Bold',
            'file': 'fonts/SpaceGrotesk-Bold.woff2',
            'url': 'https://cdn.jsdelivr.net/fontsource/fonts/space-grotesk@latest/latin-700-normal.woff2'
        },
    ]

    success_count = 0
    fail_count = 0

    print("Đang tải fonts...")
    print("-" * 70)

    for font_info in fonts_to_download:
        print(f"📥 {font_info['name']}...", end=" ", flush=True)

        success, result = download_font(font_info['url'], font_info['file'])

        if success:
            size_kb = result / 1024
            print(f"✓ ({size_kb:.1f} KB)")
            success_count += 1
        else:
            print(f"✗ Lỗi: {result}")
            fail_count += 1

    print("-" * 70)
    print()

    # Kết quả
    print("KẾT QUẢ:")
    print(f"  ✓ Thành công: {success_count}/{len(fonts_to_download)}")
    if fail_count > 0:
        print(f"  ✗ Thất bại: {fail_count}/{len(fonts_to_download)}")
    print()

    # Kiểm tra files
    print("FONTS ĐÃ TẢI:")
    all_fonts_ready = True
    for font_info in fonts_to_download:
        if os.path.exists(font_info['file']):
            size = os.path.getsize(font_info['file']) / 1024
            if size > 1:
                print(f"  ✓ {os.path.basename(font_info['file'])} ({size:.1f} KB)")
            else:
                print(f"  ⚠ {os.path.basename(font_info['file'])} ({size:.1f} KB - có thể bị lỗi)")
                all_fonts_ready = False
        else:
            print(f"  ✗ {os.path.basename(font_info['file'])} (chưa có)")
            all_fonts_ready = False

    print()
    print("=" * 70)

    if all_fonts_ready:
        print("🎉 HOÀN TẤT! Tất cả fonts đã sẵn sàng.")
        print("Bây giờ bạn có thể chạy: python html_to_pdf_png.py")
    else:
        print("⚠ MỘT SỐ FONTS CHƯA TẢI THÀNH CÔNG")
        print("\nHƯỚNG DẪN TẢI THỦ CÔNG:")
        print("1. Truy cập: https://fontsource.org/fonts/dm-sans")
        print("2. Truy cập: https://fontsource.org/fonts/space-grotesk")
        print("3. Tải file .woff2 và đặt vào thư mục fonts/")
        print("\nHoặc tham khảo file FONTS_SETUP.md để biết thêm chi tiết")

    print("=" * 70)

    return 0 if all_fonts_ready else 1

if __name__ == "__main__":
    sys.exit(main())
