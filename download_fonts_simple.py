#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Font Downloader - Tải fonts từ Google Fonts CDN
Chạy script này TRÊN MÁY CÁ NHÂN của bạn (không phải trong Docker/Container)
"""

import urllib.request
import os
import sys

def download_font(url, filename):
    """Tải một font file"""
    print(f"📥 Đang tải {filename}...", end=" ", flush=True)

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

        req = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req, timeout=30) as response:
            data = response.read()

        if len(data) < 5000:  # Font file phải > 5KB
            print(f"❌ File quá nhỏ ({len(data)} bytes)")
            return False

        with open(filename, 'wb') as f:
            f.write(data)

        size_kb = len(data) / 1024
        print(f"✅ OK ({size_kb:.1f} KB)")
        return True

    except Exception as e:
        print(f"❌ Lỗi: {e}")
        return False

def main():
    print("=" * 70)
    print("🔤 FONT DOWNLOADER - DM Sans & Space Grotesk")
    print("=" * 70)
    print()

    # Tạo thư mục fonts
    os.makedirs('fonts', exist_ok=True)

    # URLs từ Google Fonts CDN
    fonts = {
        'fonts/DMSans-Regular.woff2': 'https://fonts.gstatic.com/s/dmsans/v15/rP2tp2ywxg089UriI5-g4vlH9VoD8CmcqZG40F9JadbnoEwAopxRSWhT.woff2',
        'fonts/DMSans-Medium.woff2': 'https://fonts.gstatic.com/s/dmsans/v15/rP2tp2ywxg089UriI5-g4vlH9VoD8CmcqZG40F9JadbnoEwAkJxRSWhT.woff2',
        'fonts/DMSans-Bold.woff2': 'https://fonts.gstatic.com/s/dmsans/v15/rP2tp2ywxg089UriI5-g4vlH9VoD8CmcqZG40F9JadbnoEwARZxRSWhT.woff2',
        'fonts/SpaceGrotesk-Bold.woff2': 'https://fonts.gstatic.com/s/spacegrotesk/v16/V8mQoQDjQSkFtoMM3T6r8E7mF71Q-gOoraIAEj62UUsjNsFjTDJK.woff2',
    }

    success_count = 0
    failed = []

    for filename, url in fonts.items():
        if download_font(url, filename):
            success_count += 1
        else:
            failed.append(os.path.basename(filename))

    print()
    print("=" * 70)
    print(f"KẾT QUẢ: {success_count}/{len(fonts)} fonts tải thành công")

    if failed:
        print(f"\n⚠️  CÁC FONT THẤT BẠI: {', '.join(failed)}")
        print("\n💡 GIẢI PHÁP:")
        print("   1. Kiểm tra kết nối Internet")
        print("   2. Tắt VPN/Proxy nếu đang dùng")
        print("   3. Tải thủ công theo hướng dẫn trong FONTS_DOWNLOAD_GUIDE.md")
        print()
        print("   📄 Xem chi tiết: FONTS_DOWNLOAD_GUIDE.md")
    else:
        print("\n✅ HOÀN TẤT! Tất cả fonts đã sẵn sàng.")
        print("   Bây giờ bạn có thể chạy: python html_to_pdf_png.py")

    print("=" * 70)

    return 0 if success_count == len(fonts) else 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Đã hủy bởi người dùng")
        sys.exit(1)
