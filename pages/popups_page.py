from playwright.sync_api import Dialog, expect

from pages.base_page import BasePage
from utils.settings import BASE_URL


class PopupsPage(BasePage):
    URL = f"{BASE_URL}/popups/"
    ALERT_BUTTON = "//button[normalize-space()='Alert Popup']"
    CONFIRM_BUTTON = "//button[normalize-space()='Confirm Popup']"
    PROMPT_BUTTON = "//button[normalize-space()='Prompt Popup']"
    TOOLTIP_TEXT = "//*[contains(normalize-space(), 'Cool text')]"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("Popups")

    def verify_alert_button_visible(self) -> None:
        alert_button = self.page.locator(self.ALERT_BUTTON)
        expect(alert_button).to_be_visible()

    def verify_confirm_button_visible(self) -> None:
        confirm_button = self.page.locator(self.CONFIRM_BUTTON)
        expect(confirm_button).to_be_visible()

    def verify_prompt_button_visible(self) -> None:
        prompt_button = self.page.locator(self.PROMPT_BUTTON)
        expect(prompt_button).to_be_visible()

    def click_alert(self) -> None:
        alert_button = self.page.locator(self.ALERT_BUTTON)
        alert_button.click()

    def click_confirm(self) -> None:
        confirm_button = self.page.locator(self.CONFIRM_BUTTON)
        confirm_button.click()

    def click_prompt(self) -> None:
        prompt_button = self.page.locator(self.PROMPT_BUTTON)
        prompt_button.click()

    @staticmethod
    def verify_dialog_message(dialog: Dialog, expected_message: str) -> None:
        assert dialog.message == expected_message

    def verify_tooltip_visible(self) -> None:
        tooltip_text = self.page.locator(self.TOOLTIP_TEXT)
        expect(tooltip_text).to_be_visible()
