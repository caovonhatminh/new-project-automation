from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.settings import BASE_URL


class JavaScriptDelaysPage(BasePage):
    URL = f"{BASE_URL}/javascript-delays/"
    START_BUTTON = "//button[@id='start']"
    DELAY_RESULT = "//div[@id='delay']"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("JavaScript Delays")

    def start_countdown(self) -> None:
        start_button = self.page.locator(self.START_BUTTON)
        start_button.click()

    def verify_liftoff_visible(self) -> None:
        delay_result = self.page.locator(self.DELAY_RESULT)
        expect(delay_result).to_have_text("Liftoff!", timeout=20000)
