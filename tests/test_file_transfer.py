from pathlib import Path

import pytest

from pages.file_download_page import FileDownloadPage
from pages.file_upload_page import FileUploadPage


@pytest.mark.regression
# TC_FILE_HAPPY_001
# Verify a local file can be selected and submitted through the upload form.
def test_upload_file(page):
    upload_page = FileUploadPage(page)
    upload_file = Path(__file__).parent / "data" / "sample_upload.txt"

    upload_page.open_page()
    upload_page.verify_page_loaded()
    upload_page.upload_file(upload_file)
    upload_page.verify_file_selected("sample_upload.txt")
    upload_page.submit()


@pytest.mark.regression
# TC_FILE_HAPPY_002
# Verify the download link returns a successful downloadable response.
def test_download_file(page):
    download_page = FileDownloadPage(page)

    download_page.open_page()
    download_page.verify_page_loaded()
    download_link = download_page.get_download_link()
    response = page.goto(download_link)

    assert "/download/download-file/" in download_link
    assert response is not None
    assert response.ok
