from playwright.sync_api import APIResponse

from pages.base_page import BasePage
from utils.settings import BASE_URL


class BrokenLinksPage(BasePage):
    URL = f"{BASE_URL}/broken-links/"
    BROKEN_LINK = "//a[normalize-space()='broken link']"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("Broken Links")

    def get_broken_link_href(self) -> str:
        href = self.page.locator(self.BROKEN_LINK).get_attribute("href")
        assert href is not None
        return href

    def fetch_broken_link(self) -> APIResponse:
        return self.page.context.request.get(f"{self.URL}missing-page.html")
