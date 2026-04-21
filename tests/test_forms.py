import pytest

from pages.form_fields_page import FormFieldsPage


@pytest.mark.regression
# TC_FORM_HAPPY_001
# Verify the form can be submitted successfully with valid input data.
def test_submit_form_fields_successfully(page):
    form_page = FormFieldsPage(page)

    form_page.open_page()
    form_page.verify_page_loaded()
    form_page.fill_name("Minh")
    form_page.fill_password("Password123!")
    form_page.select_drink("Milk")
    form_page.select_color("Yellow")
    form_page.select_automation_option("yes")
    form_page.fill_email("minh@example.com")
    form_page.fill_message("Practice Automation form submission.")

    page.once("dialog", lambda dialog: dialog.accept())
    form_page.submit()


@pytest.mark.regression
# TC_FORM_EDGE_001
# Verify multiple drink checkboxes can be selected at the same time.
def test_form_fields_allow_multiple_drink_selection(page):
    form_page = FormFieldsPage(page)

    form_page.open_page()
    form_page.verify_page_loaded()
    form_page.select_drink("Milk")
    form_page.select_drink("Coffee")
    form_page.verify_drink_selected("Milk")
    form_page.verify_drink_selected("Coffee")
