from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from utils.settings import BASE_URL


class WindowOperationsPage(BasePage):
    URL = f"{BASE_URL}/window-operations/"
    NEW_TAB_BUTTON = "//button[normalize-space()='New Tab']"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("Window Operations")

    def verify_new_tab_opened_with_url_fragment(self, target_page: Page, expected_fragment: str) -> None:
        assert expected_fragment in target_page.url

    def verify_new_tab_opened(self, target_page: Page) -> None:
        assert target_page.url.startswith("http")

    def open_new_tab(self) -> Page:
        with self.page.context.expect_page() as new_page_info:
            new_tab_button = self.page.locator(self.NEW_TAB_BUTTON)
            new_tab_button.click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        return new_page

    def verify_page_text(self, target_page: Page, expected_text: str) -> None:
        expected_literal = self.xpath_literal(expected_text)
        page_text = target_page.locator(f"//*[contains(normalize-space(), {expected_literal})]")
        expect(page_text).to_be_visible()
