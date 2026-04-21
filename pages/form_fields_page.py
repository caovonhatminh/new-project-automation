from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.settings import BASE_URL


class FormFieldsPage(BasePage):
    URL = f"{BASE_URL}/form-fields/"
    FORM = "//form[@id='feedbackForm']"
    NAME_INPUT = f"{FORM}//input[@data-testid='name-input']"
    PASSWORD_INPUT = f"{FORM}//input[@type='password']"
    AUTOMATION_SELECT = f"{FORM}//select[@id='automation']"
    EMAIL_INPUT = f"{FORM}//input[@data-testid='email']"
    MESSAGE_TEXTAREA = f"{FORM}//textarea[@data-testid='message']"
    SUBMIT_BUTTON = f"{FORM}//button[@data-testid='submit-btn']"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("Form Fields")

    def verify_name_empty(self) -> None:
        name_input = self.page.locator(self.NAME_INPUT)
        expect(name_input).to_have_value("")

    def verify_password_empty(self) -> None:
        password_input = self.page.locator(self.PASSWORD_INPUT)
        expect(password_input).to_have_value("")

    def verify_automation_default_empty(self) -> None:
        automation_select = self.page.locator(self.AUTOMATION_SELECT)
        expect(automation_select).to_have_value("default")

    def fill_name(self, value: str) -> None:
        name_input = self.page.locator(self.NAME_INPUT)
        name_input.fill(value)

    def fill_password(self, value: str) -> None:
        password_input = self.page.locator(self.PASSWORD_INPUT)
        password_input.fill(value)

    def select_drink(self, drink_name: str) -> None:
        drink_literal = self.xpath_literal(drink_name)
        drink_checkbox = self.page.locator(
            f"{self.FORM}//label[normalize-space()={drink_literal}]/preceding-sibling::input[1]"
        )
        drink_checkbox.check()

    def verify_drink_selected(self, drink_name: str) -> None:
        drink_literal = self.xpath_literal(drink_name)
        drink_checkbox = self.page.locator(
            f"{self.FORM}//label[normalize-space()={drink_literal}]/preceding-sibling::input[1]"
        )
        expect(drink_checkbox).to_be_checked()

    def select_color(self, color_name: str) -> None:
        color_literal = self.xpath_literal(color_name)
        color_radio = self.page.locator(
            f"{self.FORM}//label[normalize-space()={color_literal}]/preceding-sibling::input[1]"
        )
        color_radio.check()

    def verify_color_selected(self, color_name: str) -> None:
        color_literal = self.xpath_literal(color_name)
        color_radio = self.page.locator(
            f"{self.FORM}//label[normalize-space()={color_literal}]/preceding-sibling::input[1]"
        )
        expect(color_radio).to_be_checked()

    def select_automation_option(self, value: str) -> None:
        automation_select = self.page.locator(self.AUTOMATION_SELECT)
        automation_select.select_option(value=value)

    def fill_email(self, value: str) -> None:
        email_input = self.page.locator(self.EMAIL_INPUT)
        email_input.fill(value)

    def fill_message(self, value: str) -> None:
        message_textarea = self.page.locator(self.MESSAGE_TEXTAREA)
        message_textarea.fill(value)

    def submit(self) -> None:
        submit_button = self.page.locator(self.SUBMIT_BUTTON)
        submit_button.click()
