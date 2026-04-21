from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.settings import BASE_URL


class ModalsPage(BasePage):
    URL = f"{BASE_URL}/modals/"
    SIMPLE_MODAL_BUTTON = "//button[normalize-space()='Simple Modal']"
    SIMPLE_MODAL_TEXT = "//*[contains(@class, 'pum-active')]//div[contains(@class, 'pum-content')]/p[1]"
    MODAL_CLOSE_BUTTON = "(//*[contains(@class, 'pum-active')]//button[contains(@class, 'pum-close')])[1]"
    FORM_MODAL_BUTTON = "//button[normalize-space()='Form Modal']"
    FORM_MODAL_NAME = "//*[contains(@class, 'pum-active')]//input[@id='g1051-name']"
    FORM_MODAL_EMAIL = "//*[contains(@class, 'pum-active')]//input[@id='g1051-email']"
    FORM_MODAL_MESSAGE = "//*[contains(@class, 'pum-active')]//textarea[@id='contact-form-comment-g1051-message']"
    FORM_MODAL_SUBMIT = "//*[contains(@class, 'pum-active')]//button[@type='submit' and normalize-space()='Submit']"
    FORM_MODAL_SUCCESS_HEADING = "//*[contains(@class, 'pum-active')]//div[contains(@class, 'contact-form-submission')]//h4[1]"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("Modals")

    def open_simple_modal(self) -> None:
        simple_modal_button = self.page.locator(self.SIMPLE_MODAL_BUTTON)
        simple_modal_button.click()

    def verify_simple_modal_visible(self) -> None:
        simple_modal_text = self.page.locator(self.SIMPLE_MODAL_TEXT)
        expect(simple_modal_text).to_be_visible()

    def verify_simple_modal_closed(self) -> None:
        simple_modal_text = self.page.locator(self.SIMPLE_MODAL_TEXT)
        expect(simple_modal_text).not_to_be_visible()

    def close_simple_modal(self) -> None:
        modal_close_button = self.page.locator(self.MODAL_CLOSE_BUTTON)
        modal_close_button.click()

    def open_form_modal(self) -> None:
        form_modal_button = self.page.locator(self.FORM_MODAL_BUTTON)
        form_modal_button.click()

    def verify_form_modal_opened(self) -> None:
        form_modal_name = self.page.locator(self.FORM_MODAL_NAME)
        expect(form_modal_name).to_be_visible()

    def fill_form_modal(self, name: str, email: str, message: str) -> None:
        form_modal_name = self.page.locator(self.FORM_MODAL_NAME)
        form_modal_email = self.page.locator(self.FORM_MODAL_EMAIL)
        form_modal_message = self.page.locator(self.FORM_MODAL_MESSAGE)

        form_modal_name.fill(name)
        form_modal_email.fill(email)
        form_modal_message.fill(message)

    def submit_form_modal(self) -> None:
        form_modal_submit = self.page.locator(self.FORM_MODAL_SUBMIT)
        form_modal_submit.click()

    def verify_form_modal_success(self) -> None:
        form_modal_success_heading = self.page.locator(self.FORM_MODAL_SUCCESS_HEADING)
        expect(form_modal_success_heading).to_contain_text("Thank you for your response")
