import pytest

from pages.popups_page import PopupsPage


@pytest.mark.regression
# TC_POPUP_HAPPY_001
# Verify the alert popup can be opened and accepted.
def test_handle_alert_popup(page):
    popups_page = PopupsPage(page)

    popups_page.open_page()
    popups_page.verify_page_loaded()

    page.once("dialog", lambda dialog: dialog.accept())
    popups_page.click_alert()


@pytest.mark.regression
# TC_POPUP_HAPPY_002
# Verify the confirm popup can be opened and accepted.
def test_handle_confirm_popup(page):
    popups_page = PopupsPage(page)

    popups_page.open_page()
    popups_page.verify_page_loaded()

    page.once("dialog", lambda dialog: dialog.accept())
    popups_page.click_confirm()


@pytest.mark.regression
# TC_POPUP_HAPPY_003
# Verify the prompt popup accepts input text and can be confirmed.
def test_handle_prompt_popup(page):
    popups_page = PopupsPage(page)

    popups_page.open_page()
    popups_page.verify_page_loaded()

    page.once("dialog", lambda dialog: dialog.accept("Minh"))
    popups_page.click_prompt()


@pytest.mark.regression
# TC_POPUP_NEGATIVE_001
# Verify the confirm popup can be dismissed without breaking the page flow.
def test_handle_confirm_popup_dismiss(page):
    popups_page = PopupsPage(page)

    popups_page.open_page()
    popups_page.verify_page_loaded()

    page.once("dialog", lambda dialog: dialog.dismiss())
    popups_page.click_confirm()


@pytest.mark.regression
# TC_POPUP_EDGE_001
# Verify each popup shows the expected browser dialog message.
def test_popup_dialog_messages_are_correct(page):
    popups_page = PopupsPage(page)

    popups_page.open_page()
    popups_page.verify_page_loaded()

    received_messages = []

    def handle_dialog(dialog):
        received_messages.append(dialog.message)
        dialog.dismiss()

    page.once("dialog", handle_dialog)
    popups_page.click_alert()
    assert received_messages[-1] == "Hi there, pal!"

    page.once("dialog", handle_dialog)
    popups_page.click_confirm()
    assert received_messages[-1] == "OK or Cancel, which will it be?"

    page.once("dialog", handle_dialog)
    popups_page.click_prompt()
    assert received_messages[-1] == "Hi there, what's your name?"
