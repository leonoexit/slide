#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script chuyển đổi HTML sang PDF và tách thành các file PNG
Yêu cầu: playwright, PyMuPDF (fitz)
"""

import os
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
import fitz  # PyMuPDF


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


def main():
    """Hàm chính"""
    # Cấu hình
    HTML_FILE = "name.html"
    TEMP_PDF_FILE = "temp_slides.pdf"
    OUTPUT_DIR = "slides_images"
    ZOOM_FACTOR = 2  # Tạo ảnh 2400x2400px (gấp đôi 1200x1200px)

    print("=" * 60)
    print("SCRIPT CHUYỂN ĐỔI HTML SANG PDF VÀ PNG")
    print("=" * 60)

    try:
        # Bước 1: Chuyển HTML sang PDF
        html_to_pdf(HTML_FILE, TEMP_PDF_FILE)

        # Bước 2: Tách PDF thành ảnh PNG
        pdf_to_images(TEMP_PDF_FILE, OUTPUT_DIR, zoom=ZOOM_FACTOR)

        # Bước 3: Dọn dẹp file tạm
        cleanup(TEMP_PDF_FILE)

        print("\n" + "=" * 60)
        print("✓ HOÀN TẤT!")
        print(f"Các ảnh slide đã được lưu trong thư mục: {OUTPUT_DIR}/")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Lỗi: {str(e)}")
        # Dọn dẹp ngay cả khi có lỗi
        if os.path.exists(TEMP_PDF_FILE):
            cleanup(TEMP_PDF_FILE)
        sys.exit(1)


if __name__ == "__main__":
    main()
