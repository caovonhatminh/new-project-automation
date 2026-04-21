from pathlib import Path

import pytest

from pages.file_download_page import FileDownloadPage
from pages.file_upload_page import FileUploadPage
from pages.form_fields_page import FormFieldsPage
from pages.home_page import HomePage
from pages.modals_page import ModalsPage
from pages.popups_page import PopupsPage
from pages.window_operations_page import WindowOperationsPage


@pytest.mark.e2e
@pytest.mark.e2e_smoke
# TC_E2E_SMOKE_001
# Verify a user can start at home, navigate to Form Fields, and complete the form submission journey.
def test_e2e_home_to_form_submission(page):
    home_page = HomePage(page)
    form_page = FormFieldsPage(page)

    home_page.open_home_page()
    home_page.verify_home_page_loaded()
    home_page.open_practice_page("Form Fields")

    form_page.verify_page_loaded()
    form_page.fill_name("Minh")
    form_page.fill_password("Password123!")
    form_page.select_drink("Milk")
    form_page.select_color("Yellow")
    form_page.select_automation_option("yes")
    form_page.fill_email("minh@example.com")
    form_page.fill_message("End-to-end form submission flow.")

    page.once("dialog", lambda dialog: dialog.accept())
    form_page.submit()


@pytest.mark.e2e
@pytest.mark.e2e_smoke
# TC_E2E_SMOKE_002
# Verify a user can start at home, navigate to File Upload, select a supported file, and submit it.
def test_e2e_home_to_file_upload(page):
    home_page = HomePage(page)
    upload_page = FileUploadPage(page)
    upload_file = Path(__file__).parents[1] / "tests" / "data" / "sample_upload.txt"

    home_page.open_home_page()
    home_page.verify_home_page_loaded()
    home_page.open_practice_page("File Upload")

    upload_page.verify_page_loaded()
    upload_page.upload_file(upload_file)
    upload_page.verify_file_selected("sample_upload.txt")
    upload_page.submit()


@pytest.mark.e2e
@pytest.mark.e2e_smoke
# TC_E2E_SMOKE_003
# Verify a user can start at home, navigate to File Download, and reach the public download endpoint with a handled HTTP response.
def test_e2e_home_to_file_download(page):
    home_page = HomePage(page)
    download_page = FileDownloadPage(page)

    home_page.open_home_page()
    home_page.verify_home_page_loaded()
    home_page.open_practice_page("File Download")

    download_page.verify_page_loaded()
    download_link = download_page.get_download_link()
    response = page.goto(download_link)

    assert response is not None
    assert response.status in {200, 429}


@pytest.mark.e2e
@pytest.mark.e2e_smoke
# TC_E2E_SMOKE_004
# Verify a user can start at home, navigate to Modals, open the form modal, and submit valid data.
def test_e2e_home_to_modal_submission(page):
    home_page = HomePage(page)
    modals_page = ModalsPage(page)

    home_page.open_home_page()
    home_page.verify_home_page_loaded()
    home_page.open_practice_page("Modals")

    modals_page.verify_page_loaded()
    modals_page.open_form_modal()
    modals_page.verify_form_modal_opened()
    modals_page.fill_form_modal(
        name="Minh",
        email="minh@example.com",
        message="End-to-end modal submission flow.",
    )
    modals_page.submit_form_modal()
    modals_page.verify_form_modal_success()


@pytest.mark.e2e
@pytest.mark.e2e_smoke
# TC_E2E_SMOKE_005
# Verify a user can start at home, navigate to Popups, and handle alert, confirm, and prompt dialogs in one journey.
def test_e2e_home_to_popup_interactions(page):
    home_page = HomePage(page)
    popups_page = PopupsPage(page)

    home_page.open_home_page()
    home_page.verify_home_page_loaded()
    home_page.open_practice_page("Popups")

    popups_page.verify_page_loaded()

    page.once("dialog", lambda dialog: dialog.accept())
    popups_page.click_alert()

    page.once("dialog", lambda dialog: dialog.accept())
    popups_page.click_confirm()

    page.once("dialog", lambda dialog: dialog.accept("Minh"))
    popups_page.click_prompt()


@pytest.mark.e2e
@pytest.mark.e2e_smoke
# TC_E2E_SMOKE_006
# Verify a user can start at home, navigate to Window Operations, and open a valid new tab.
def test_e2e_home_to_new_tab(page):
    home_page = HomePage(page)
    window_page = WindowOperationsPage(page)

    home_page.open_home_page()
    home_page.verify_home_page_loaded()
    home_page.open_practice_page("Window Operations")

    window_page.verify_page_loaded()
    new_page = window_page.open_new_tab()
    window_page.verify_new_tab_opened(new_page)
