import re
from pathlib import Path

from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.settings import BASE_URL


class FileUploadPage(BasePage):
    URL = f"{BASE_URL}/file-upload/"
    FILE_INPUT = "//input[@id='file-upload']"
    SUBMIT_BUTTON = "//input[@id='upload-btn']"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("File Upload")

    def verify_upload_button_visible(self) -> None:
        upload_button = self.page.locator(self.SUBMIT_BUTTON)
        expect(upload_button).to_be_visible()

    def upload_file(self, file_path: Path) -> None:
        file_input = self.page.locator(self.FILE_INPUT)
        file_input.set_input_files(str(file_path))

    def submit(self) -> None:
        upload_button = self.page.locator(self.SUBMIT_BUTTON)
        upload_button.click()

    def verify_file_selected(self, file_name: str) -> None:
        file_input = self.page.locator(self.FILE_INPUT)
        expect(file_input).to_have_value(re.compile(rf".*{re.escape(file_name)}$"))
