from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.settings import BASE_URL


class CalendarsPage(BasePage):
    URL = f"{BASE_URL}/calendars/"
    DATE_INPUT = "//input[@id='g1065-1-selectorenteradate']"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("Calendars")

    def verify_date_empty(self) -> None:
        date_input = self.page.locator(self.DATE_INPUT)
        expect(date_input).to_have_value("")

    def enter_date(self, date_value: str) -> None:
        date_input = self.page.locator(self.DATE_INPUT)
        date_input.fill(date_value)

    def verify_date_value(self, expected_value: str) -> None:
        date_input = self.page.locator(self.DATE_INPUT)
        expect(date_input).to_have_value(expected_value)
