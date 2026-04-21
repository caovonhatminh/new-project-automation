import pytest

from pages.calendars_page import CalendarsPage
from pages.file_download_page import FileDownloadPage
from pages.file_upload_page import FileUploadPage
from pages.form_fields_page import FormFieldsPage
from pages.gestures_page import GesturesPage
from pages.modals_page import ModalsPage
from pages.popups_page import PopupsPage
from pages.slider_page import SliderPage
from pages.tables_page import TablesPage
from pages.window_operations_page import WindowOperationsPage


@pytest.mark.regression
# TC_FORM_NEGATIVE_001
# Verify the form fields page starts with empty text inputs and default automation selection.
def test_form_fields_default_state(page):
    form_page = FormFieldsPage(page)

    form_page.open_page()
    form_page.verify_page_loaded()
    form_page.verify_name_empty()
    form_page.verify_password_empty()
    form_page.verify_automation_default_empty()


@pytest.mark.regression
# TC_FORM_HAPPY_002
# Verify selecting one color radio option marks that option as checked.
def test_form_fields_radio_selection(page):
    form_page = FormFieldsPage(page)

    form_page.open_page()
    form_page.verify_page_loaded()
    form_page.select_color("Yellow")
    form_page.verify_color_selected("Yellow")


@pytest.mark.regression
# TC_CALENDAR_NEGATIVE_001
# Verify the calendar field is empty on initial page load.
def test_calendar_default_state(page):
    calendars_page = CalendarsPage(page)

    calendars_page.open_page()
    calendars_page.verify_page_loaded()
    calendars_page.verify_date_empty()


@pytest.mark.regression
# TC_MODAL_EDGE_001
# Verify the simple modal is no longer visible after close action.
def test_simple_modal_can_be_closed(page):
    modals_page = ModalsPage(page)

    modals_page.open_page()
    modals_page.verify_page_loaded()
    modals_page.open_simple_modal()
    modals_page.verify_simple_modal_visible()
    modals_page.close_simple_modal()
    modals_page.verify_simple_modal_closed()


@pytest.mark.regression
# TC_MODAL_EDGE_002
# Verify the form modal open action exposes the input fields.
def test_form_modal_open_state(page):
    modals_page = ModalsPage(page)

    modals_page.open_page()
    modals_page.verify_page_loaded()
    modals_page.open_form_modal()
    modals_page.verify_form_modal_opened()


@pytest.mark.regression
# TC_POPUP_NEGATIVE_002
# Verify all popup trigger buttons are visible before interaction.
def test_popup_buttons_visible(page):
    popups_page = PopupsPage(page)

    popups_page.open_page()
    popups_page.verify_page_loaded()
    popups_page.verify_alert_button_visible()
    popups_page.verify_confirm_button_visible()
    popups_page.verify_prompt_button_visible()


@pytest.mark.regression
# TC_SLIDER_NEGATIVE_001
# Verify the slider starts with the default value before user interaction.
def test_slider_default_value(page):
    slider_page = SliderPage(page)

    slider_page.open_page()
    slider_page.verify_page_loaded()
    slider_page.verify_default_slider_value()


@pytest.mark.regression
# TC_TABLE_EDGE_001
# Verify both table sections and important headers are visible on the page.
def test_table_sections_visible(page):
    tables_page = TablesPage(page)

    tables_page.open_page()
    tables_page.verify_page_loaded()
    tables_page.verify_simple_table_visible()
    tables_page.verify_sortable_table_visible()
    tables_page.verify_sortable_table_headers()


@pytest.mark.regression
# TC_FILE_NEGATIVE_001
# Verify upload and download controls are visible before any file action.
def test_upload_and_download_controls_visible(page):
    upload_page = FileUploadPage(page)
    download_page = FileDownloadPage(page)

    upload_page.open_page()
    upload_page.verify_page_loaded()
    upload_page.verify_upload_button_visible()

    download_page.open_page()
    download_page.verify_page_loaded()
    download_page.verify_download_link_visible()


@pytest.mark.regression
# TC_GESTURE_NEGATIVE_001
# Verify the drag source and drop target are visible before gesture actions.
def test_gesture_areas_visible(page):
    gestures_page = GesturesPage(page)

    gestures_page.open_page()
    gestures_page.verify_page_loaded()
    gestures_page.verify_drag_source_present()
    gestures_page.verify_drop_target_present()


@pytest.mark.regression
# TC_WINDOW_EDGE_002
# Verify the newly opened tab has the expected URL pattern.
def test_new_tab_has_expected_url_fragment(page):
    window_page = WindowOperationsPage(page)

    window_page.open_page()
    window_page.verify_page_loaded()
    new_page = window_page.open_new_tab()
    window_page.verify_new_tab_opened(new_page)
