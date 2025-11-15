#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script chuyển đổi HTML sang PDF và tách thành các file PNG
Yêu cầu: playwright, PyMuPDF (fitz)

Cách sử dụng:
    python html_to_pdf_png.py                   # Tự động tìm file .html
    python html_to_pdf_png.py myslides.html    # Chỉ định file cụ thể
    python html_to_pdf_png.py -h               # Hiển thị help
"""

import os
import sys
import argparse
import glob
from pathlib import Path
from playwright.sync_api import sync_playwright
import fitz  # PyMuPDF


def find_html_files():
    """Tìm tất cả file .html trong thư mục hiện tại"""
    html_files = glob.glob("*.html")
    return sorted(html_files)


def select_html_file(html_files):
    """
    Cho phép user chọn file HTML từ danh sách

    Args:
        html_files (list): Danh sách các file HTML

    Returns:
        str: Tên file HTML được chọn
    """
    if len(html_files) == 1:
        print(f"✓ Tìm thấy file HTML: {html_files[0]}")
        return html_files[0]

    print(f"\n📋 Tìm thấy {len(html_files)} file HTML:")
    print("-" * 60)
    for i, filename in enumerate(html_files, 1):
        file_size = os.path.getsize(filename) / 1024  # KB
        print(f"  [{i}] {filename} ({file_size:.1f} KB)")
    print("-" * 60)

    while True:
        try:
            choice = input(f"\nChọn file (1-{len(html_files)}) hoặc 'q' để thoát: ").strip()

            if choice.lower() == 'q':
                print("Hủy bỏ.")
                sys.exit(0)

            index = int(choice) - 1
            if 0 <= index < len(html_files):
                selected_file = html_files[index]
                print(f"✓ Đã chọn: {selected_file}")
                return selected_file
            else:
                print(f"❌ Vui lòng chọn số từ 1 đến {len(html_files)}")
        except ValueError:
            print("❌ Vui lòng nhập số hợp lệ")
        except KeyboardInterrupt:
            print("\n\nHủy bỏ.")
            sys.exit(0)


def get_html_file(args_file=None):
    """
    Lấy file HTML để xử lý

    Args:
        args_file (str): File HTML từ command line argument

    Returns:
        str: Tên file HTML
    """
    # Nếu user chỉ định file qua argument
    if args_file:
        if not os.path.exists(args_file):
            print(f"❌ Lỗi: Không tìm thấy file '{args_file}'")
            sys.exit(1)

        if not args_file.lower().endswith('.html'):
            print(f"❌ Lỗi: File '{args_file}' không phải là file HTML")
            sys.exit(1)

        print(f"✓ Sử dụng file: {args_file}")
        return args_file

    # Tự động tìm file HTML
    html_files = find_html_files()

    if not html_files:
        print("❌ Lỗi: Không tìm thấy file HTML nào trong thư mục hiện tại")
        print("\nGợi ý:")
        print("  - Đảm bảo file HTML của bạn có extension .html")
        print("  - Hoặc chỉ định file cụ thể: python html_to_pdf_png.py myfile.html")
        sys.exit(1)

    return select_html_file(html_files)


def html_to_pdf(html_file, pdf_file):
    """
    Chuyển đổi file HTML thành PDF sử dụng Playwright

    Args:
        html_file (str): Đường dẫn tới file HTML
        pdf_file (str): Đường dẫn tới file PDF đầu ra
    """
    print(f"Bước 1: Đang chuyển đổi {html_file} sang PDF...")

    # Kiểm tra file HTML có tồn tại không
    if not os.path.exists(html_file):
        print(f"❌ Lỗi: Không tìm thấy file {html_file}")
        sys.exit(1)

    # Chuyển đổi sang đường dẫn tuyệt đối
    html_path = Path(html_file).resolve()
    html_url = f"file://{html_path}"

    with sync_playwright() as p:
        # Khởi chạy trình duyệt Chromium ở chế độ headless
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Mở file HTML
        page.goto(html_url)

        # Đợi page load xong
        page.wait_for_load_state('networkidle')

        # Xuất PDF với cấu hình chính xác
        page.pdf(
            path=pdf_file,
            width='1200px',
            height='1200px',
            print_background=True,
            margin={
                'top': '0',
                'bottom': '0',
                'left': '0',
                'right': '0'
            }
        )

        browser.close()

    print(f"✓ Đã tạo file PDF tạm thời: {pdf_file}")


def pdf_to_images(pdf_file, output_dir, zoom=2):
    """
    Tách file PDF thành các file ảnh PNG

    Args:
        pdf_file (str): Đường dẫn tới file PDF
        output_dir (str): Thư mục chứa các ảnh đầu ra
        zoom (int): Hệ số phóng đại (zoom=2 tạo ảnh 2400x2400px)
    """
    print(f"\nBước 2: Đang tách PDF thành ảnh PNG...")

    # Tạo thư mục output nếu chưa tồn tại
    os.makedirs(output_dir, exist_ok=True)

    # Mở file PDF
    pdf_document = fitz.open(pdf_file)
    total_pages = len(pdf_document)

    print(f"Tổng số trang: {total_pages}")

    # Ma trận phóng đại để tạo ảnh chất lượng cao
    matrix = fitz.Matrix(zoom, zoom)

    # Lặp qua từng trang
    for page_num in range(total_pages):
        # Lấy trang
        page = pdf_document[page_num]

        # Render trang thành pixmap (ảnh) với độ phóng đại
        pix = page.get_pixmap(matrix=matrix)

        # Tạo tên file với số thứ tự được đệm số 0
        # Tính số chữ số cần thiết dựa vào tổng số trang
        num_digits = len(str(total_pages))
        image_filename = f"slide_{str(page_num + 1).zfill(num_digits)}.png"
        image_path = os.path.join(output_dir, image_filename)

        # Lưu ảnh
        pix.save(image_path)

        # In tiến trình
        print(f"Đang xuất ảnh slide {page_num + 1}/{total_pages}...")

    # Đóng file PDF
    pdf_document.close()

    print(f"✓ Đã xuất {total_pages} ảnh vào thư mục '{output_dir}'")


def cleanup(temp_file):
    """
    Xóa file tạm thời

    Args:
        temp_file (str): Đường dẫn tới file cần xóa
    """
    if os.path.exists(temp_file):
        os.remove(temp_file)
        print(f"\n✓ Đã xóa file tạm: {temp_file}")


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Chuyển đổi file HTML thành PDF và tách thành các file PNG',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ:
  python html_to_pdf_png.py                   # Tự động tìm file .html
  python html_to_pdf_png.py slides.html       # Chuyển đổi file cụ thể
  python html_to_pdf_png.py -o output/        # Chỉ định thư mục output
  python html_to_pdf_png.py slides.html -z 3  # Zoom 3x (3600x3600px)
        """
    )

    parser.add_argument(
        'html_file',
        nargs='?',
        help='File HTML cần chuyển đổi (nếu không chỉ định, script sẽ tự động tìm)'
    )

    parser.add_argument(
        '-o', '--output',
        default='slides_images',
        help='Thư mục chứa ảnh PNG đầu ra (mặc định: slides_images)'
    )

    parser.add_argument(
        '-z', '--zoom',
        type=int,
        default=2,
        help='Hệ số phóng đại ảnh (mặc định: 2 = 2400x2400px)'
    )

    parser.add_argument(
        '-p', '--pdf',
        default='temp_slides.pdf',
        help='Tên file PDF tạm thời (mặc định: temp_slides.pdf)'
    )

    return parser.parse_args()


def main():
    """Hàm chính"""
    # Parse arguments
    args = parse_arguments()

    print("=" * 60)
    print("SCRIPT CHUYỂN ĐỔI HTML SANG PDF VÀ PNG")
    print("=" * 60)
    print()

    try:
        # Lấy file HTML (từ argument hoặc tự động tìm)
        html_file = get_html_file(args.html_file)

        # Cấu hình từ arguments
        temp_pdf_file = args.pdf
        output_dir = args.output
        zoom_factor = args.zoom

        # Hiển thị cấu hình
        print()
        print("📝 Cấu hình:")
        print(f"  - File HTML: {html_file}")
        print(f"  - Thư mục output: {output_dir}/")
        print(f"  - Zoom factor: {zoom_factor}x")
        print(f"  - Kích thước ảnh: {1200 * zoom_factor}x{1200 * zoom_factor}px")
        print()

        # Bước 1: Chuyển HTML sang PDF
        html_to_pdf(html_file, temp_pdf_file)

        # Bước 2: Tách PDF thành ảnh PNG
        pdf_to_images(temp_pdf_file, output_dir, zoom=zoom_factor)

        # Bước 3: Dọn dẹp file tạm
        cleanup(temp_pdf_file)

        print("\n" + "=" * 60)
        print("✓ HOÀN TẤT!")
        print(f"Các ảnh slide đã được lưu trong thư mục: {output_dir}/")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Lỗi: {str(e)}")
        # Dọn dẹp ngay cả khi có lỗi
        if 'temp_pdf_file' in locals() and os.path.exists(temp_pdf_file):
            cleanup(temp_pdf_file)
        sys.exit(1)


if __name__ == "__main__":
    main()
