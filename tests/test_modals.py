import pytest

from pages.modals_page import ModalsPage


@pytest.mark.regression
# TC_MODAL_HAPPY_001
# Verify the simple modal can be opened and closed successfully.
def test_open_and_close_simple_modal(page):
    modals_page = ModalsPage(page)

    modals_page.open_page()
    modals_page.verify_page_loaded()
    modals_page.open_simple_modal()
    modals_page.verify_simple_modal_visible()
    modals_page.close_simple_modal()


@pytest.mark.regression
# TC_MODAL_HAPPY_002
# Verify the form modal accepts valid input and shows a success message after submit.
def test_submit_form_inside_modal(page):
    modals_page = ModalsPage(page)

    modals_page.open_page()
    modals_page.verify_page_loaded()
    modals_page.open_form_modal()
    modals_page.fill_form_modal(
        name="Minh",
        email="minh@example.com",
        message="Testing form modal with Playwright.",
    )
    modals_page.submit_form_modal()
    modals_page.verify_form_modal_success()


@pytest.mark.regression
# TC_MODAL_EDGE_003
# Verify the form modal still submits and shows success even when left blank.
def test_form_modal_blank_submit_still_shows_success(page):
    modals_page = ModalsPage(page)

    modals_page.open_page()
    modals_page.verify_page_loaded()
    modals_page.open_form_modal()
    modals_page.verify_form_modal_opened()
    modals_page.submit_form_modal()
    modals_page.verify_form_modal_success()
