from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.settings import BASE_URL


class SliderPage(BasePage):
    URL = f"{BASE_URL}/slider/"
    SLIDER_INPUT = "//input[@id='slideMe']"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("Slider")

    def verify_default_slider_value(self, expected_value: str = "25") -> None:
        slider_input = self.page.locator(self.SLIDER_INPUT)
        expect(slider_input).to_have_value(expected_value)

    def set_slider_value(self, value: str) -> None:
        slider_input = self.page.locator(self.SLIDER_INPUT)
        slider_input.fill(value)
        slider_input.evaluate("(element) => element.dispatchEvent(new Event('input', { bubbles: true }))")

    def verify_slider_value(self, expected_value: str) -> None:
        slider_input = self.page.locator(self.SLIDER_INPUT)
        expect(slider_input).to_have_value(expected_value)
