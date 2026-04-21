from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.settings import BASE_URL


class AdsPage(BasePage):
    URL = f"{BASE_URL}/ads/"
    AD_MODAL_TEXT = "//*[contains(@class, 'pum-active')]//div[contains(@class, 'pum-content')]/p[1]"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("Ads")

    def verify_ad_modal_visible(self) -> None:
        ad_modal_text = self.page.locator(self.AD_MODAL_TEXT)
        expect(ad_modal_text).to_have_text("I am an ad.", timeout=10000)
