from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.settings import BASE_URL


class HomePage(BasePage):
    HOME_HEADING = "//h1[contains(normalize-space(), 'Welcome to your software automation practice website!')]"

    def open_home_page(self) -> None:
        self.open(BASE_URL)

    def verify_home_page_loaded(self) -> None:
        home_heading = self.page.locator(self.HOME_HEADING)
        expect(home_heading).to_be_visible()

    def open_practice_page(self, page_name: str) -> None:
        page_literal = self.xpath_literal(page_name)
        practice_page_link = self.page.locator(f"//a[normalize-space()={page_literal}]")
        practice_page_link.click()
