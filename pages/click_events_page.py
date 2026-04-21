from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.settings import BASE_URL


class ClickEventsPage(BasePage):
    URL = f"{BASE_URL}/click-events/"
    RESULT_HEADING = "//h2[@id='demo']"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("Click Events")

    def click_animal(self, animal_name: str) -> None:
        animal_literal = self.xpath_literal(animal_name)
        animal_button = self.page.locator(f"//button[normalize-space()={animal_literal}]")
        animal_button.click()

    def verify_animal_sound(self, sound_text: str) -> None:
        result_heading = self.page.locator(self.RESULT_HEADING)
        expect(result_heading).to_have_text(sound_text)
