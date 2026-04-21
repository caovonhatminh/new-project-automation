from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.settings import BASE_URL


class AccordionsPage(BasePage):
    URL = f"{BASE_URL}/accordions/"
    ACCORDION_SUMMARY = "//summary[contains(@class, 'accordion-item__title')]"
    ACCORDION_CONTENT = "//div[contains(@class, 'accordion-item__content')]//p[1]"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("Accordions")

    def open_accordion(self) -> None:
        accordion_summary = self.page.locator(self.ACCORDION_SUMMARY)
        accordion_summary.click()

    def verify_accordion_content_hidden(self) -> None:
        accordion_content = self.page.locator(self.ACCORDION_CONTENT)
        expect(accordion_content).not_to_be_visible()

    def verify_accordion_text(self) -> None:
        accordion_content = self.page.locator(self.ACCORDION_CONTENT)
        expect(accordion_content).to_have_text("This is an accordion item.")
