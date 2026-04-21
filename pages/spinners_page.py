from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.settings import BASE_URL


class SpinnersPage(BasePage):
    URL = f"{BASE_URL}/spinners/"
    SPINNER = "(//*[contains(@class, 'spinner')])[1]"

    def open_page(self) -> None:
        self.page.goto(self.URL, wait_until="domcontentloaded")

    def verify_page_loaded(self) -> None:
        self.expect_heading("Spinners")

    def verify_spinner_visible_initially(self) -> None:
        spinner = self.page.locator(self.SPINNER)
        expect(spinner).to_have_class("spinner")

    def verify_spinner_hidden(self) -> None:
        spinner = self.page.locator(self.SPINNER)
        expect(spinner).to_have_class("spinner spinner-hidden", timeout=10000)
