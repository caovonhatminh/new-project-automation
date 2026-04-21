from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.settings import BASE_URL


class FileDownloadPage(BasePage):
    URL = f"{BASE_URL}/file-download/"
    DOWNLOAD_LINK = "//a[contains(@href, 'download/download-file')]"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("File Download")

    def verify_download_link_visible(self) -> None:
        download_link = self.page.locator(self.DOWNLOAD_LINK).first
        expect(download_link).to_be_visible()

    def get_download_link(self) -> str:
        download_link = self.page.locator(self.DOWNLOAD_LINK).first
        href = download_link.get_attribute("href")
        assert href is not None
        return href
