import pytest

from pages.accordions_page import AccordionsPage
from pages.calendars_page import CalendarsPage
from pages.gestures_page import GesturesPage
from pages.home_page import HomePage
from pages.hover_page import HoverPage
from pages.javascript_delays_page import JavaScriptDelaysPage
from pages.slider_page import SliderPage
from pages.spinners_page import SpinnersPage
from pages.tables_page import TablesPage


@pytest.mark.e2e
@pytest.mark.e2e_regression
# TC_E2E_REG_001
# Verify a user can start at home, navigate to Calendars, and update the date value more than once.
def test_e2e_home_to_calendar_journey(page):
    home_page = HomePage(page)
    calendars_page = CalendarsPage(page)

    home_page.open_home_page()
    home_page.verify_home_page_loaded()
    home_page.open_practice_page("Calendars")

    calendars_page.verify_page_loaded()
    calendars_page.verify_date_empty()
    calendars_page.enter_date("2026-04-13")
    calendars_page.verify_date_value("2026-04-13")
    calendars_page.enter_date("2026-12-31")
    calendars_page.verify_date_value("2026-12-31")


@pytest.mark.e2e
@pytest.mark.e2e_regression
# TC_E2E_REG_002
# Verify a user can start at home, navigate to Tables, and validate both table sections in one journey.
def test_e2e_home_to_tables_journey(page):
    home_page = HomePage(page)
    tables_page = TablesPage(page)

    home_page.open_home_page()
    home_page.verify_home_page_loaded()
    home_page.open_practice_page("Tables")

    tables_page.verify_page_loaded()
    tables_page.verify_simple_table_visible()
    tables_page.verify_simple_table_value("Laptop", "$1200.00")
    tables_page.verify_sortable_table_visible()
    tables_page.verify_sortable_table_headers()
    tables_page.verify_sortable_table_contains_country("United States")


@pytest.mark.e2e
@pytest.mark.e2e_regression
# TC_E2E_REG_003
# Verify a user can start at home, navigate to Hover, and trigger the hover result.
def test_e2e_home_to_hover_journey(page):
    home_page = HomePage(page)
    hover_page = HoverPage(page)

    home_page.open_home_page()
    home_page.verify_home_page_loaded()
    home_page.open_practice_page("Hover")
    hover_page.verify_page_loaded()
    hover_page.verify_success_text_not_visible()
    hover_page.hover_target()
    hover_page.verify_success_text()


@pytest.mark.e2e
@pytest.mark.e2e_regression
# TC_E2E_REG_004
# Verify a user can start at home, navigate to Accordions, and reveal the hidden content.
def test_e2e_home_to_accordion_journey(page):
    home_page = HomePage(page)
    accordions_page = AccordionsPage(page)

    home_page.open_home_page()
    home_page.verify_home_page_loaded()
    home_page.open_practice_page("Accordions")
    accordions_page.verify_page_loaded()
    accordions_page.verify_accordion_content_hidden()
    accordions_page.open_accordion()
    accordions_page.verify_accordion_text()


@pytest.mark.e2e
@pytest.mark.e2e_regression
# TC_E2E_REG_005
# Verify a user can start at home, navigate to Sliders, and update the slider across normal and boundary values.
def test_e2e_home_to_slider_journey(page):
    home_page = HomePage(page)
    slider_page = SliderPage(page)

    home_page.open_home_page()
    home_page.verify_home_page_loaded()
    home_page.open_practice_page("Sliders")
    slider_page.verify_page_loaded()
    slider_page.verify_default_slider_value()
    slider_page.set_slider_value("80")
    slider_page.verify_slider_value("80")
    slider_page.set_slider_value("0")
    slider_page.verify_slider_value("0")
    slider_page.set_slider_value("100")
    slider_page.verify_slider_value("100")


@pytest.mark.e2e
@pytest.mark.e2e_regression
# TC_E2E_REG_006
# Verify a user can start at home, navigate to JavaScript Delays, and wait for the delayed result.
def test_e2e_home_to_delay_journey(page):
    home_page = HomePage(page)
    delays_page = JavaScriptDelaysPage(page)

    home_page.open_home_page()
    home_page.verify_home_page_loaded()
    home_page.open_practice_page("JavaScript Delays")
    delays_page.open_page()
    delays_page.verify_page_loaded()
    delays_page.start_countdown()
    delays_page.verify_liftoff_visible()


@pytest.mark.e2e
@pytest.mark.e2e_regression
# TC_E2E_REG_007
# Verify a user can start at home, navigate to Spinners, and observe the spinner transition.
def test_e2e_home_to_spinner_journey(page):
    home_page = HomePage(page)
    spinners_page = SpinnersPage(page)

    home_page.open_home_page()
    home_page.verify_home_page_loaded()
    home_page.open_practice_page("Spinners")
    spinners_page.verify_page_loaded()
    spinners_page.verify_spinner_visible_initially()
    spinners_page.verify_spinner_hidden()


@pytest.mark.e2e
@pytest.mark.e2e_regression
# TC_E2E_REG_008
# Verify a user can complete the drag-and-drop journey on the Gestures page.
def test_e2e_home_to_gestures_journey(page):
    home_page = HomePage(page)
    gestures_page = GesturesPage(page)

    home_page.open_home_page()
    home_page.verify_home_page_loaded()
    home_page.open_practice_page("Gestures")
    gestures_page.open_page()

    gestures_page.verify_page_loaded()
    gestures_page.verify_drag_source_present()
    gestures_page.verify_drop_target_present()

    source_children, target_children = gestures_page.drag_image_to_second_box()
    assert source_children == 0
    assert target_children == 1

    start_x, end_x = gestures_page.drag_moveable_box()
    assert start_x != end_x
