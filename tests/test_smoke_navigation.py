import pytest

from pages.home_page import HomePage


@pytest.mark.smoke
# TC_HOME_HAPPY_001
# Verify the home page loads successfully and the main welcome heading is visible.
def test_home_page_loads(page):
    home_page = HomePage(page)

    home_page.open_home_page()
    home_page.verify_home_page_loaded()


@pytest.mark.smoke
@pytest.mark.parametrize(
    "menu_name, expected_heading",
    [
        ("Form Fields", "Form Fields"),
        ("Calendars", "Calendars"),
        ("Modals", "Modals"),
        ("Popups", "Popups"),
        ("Tables", "Tables"),
        ("File Upload", "File Upload"),
        ("File Download", "File Download"),
        ("Iframes", "Iframes"),
        ("Window Operations", "Window Operations"),
    ],
)
# TC_HOME_HAPPY_002
# Verify each main practice page can be opened from the home page navigation.
def test_main_pages_are_reachable(page, menu_name, expected_heading):
    home_page = HomePage(page)

    home_page.open_home_page()
    home_page.open_practice_page(menu_name)
    home_page.expect_heading(expected_heading)
