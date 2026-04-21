from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.settings import BASE_URL


class HoverPage(BasePage):
    URL = f"{BASE_URL}/hover/"
    HOVER_TARGET = "//h3[@id='mouse_over']"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("Hover")

    def hover_target(self) -> None:
        hover_target = self.page.locator(self.HOVER_TARGET)
        hover_target.hover()

    def verify_success_text_not_visible(self) -> None:
        hover_target = self.page.locator(self.HOVER_TARGET)
        expect(hover_target).not_to_have_text("You did it!")

    def verify_success_text(self) -> None:
        hover_target = self.page.locator(self.HOVER_TARGET)
        expect(hover_target).to_have_text("You did it!")
