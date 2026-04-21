from pages.base_page import BasePage
from utils.settings import BASE_URL


class IframePage(BasePage):
    URL = f"{BASE_URL}/iframes/"
    TOP_IFRAME = "//iframe[@name='top-iframe']"
    BOTTOM_IFRAME = "//iframe[@name='bottom-iframe']"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("Iframes")

    def verify_iframe_urls(self) -> None:
        top_iframe = self.page.locator(self.TOP_IFRAME)
        bottom_iframe = self.page.locator(self.BOTTOM_IFRAME)

        assert top_iframe.count() == 1
        assert bottom_iframe.count() == 1
        assert "playwright.dev" in (top_iframe.get_attribute("src") or "")
        assert "selenium.dev" in (bottom_iframe.get_attribute("src") or "")
