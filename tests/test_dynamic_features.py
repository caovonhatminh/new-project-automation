import pytest

from pages.accordions_page import AccordionsPage
from pages.ads_page import AdsPage
from pages.calendars_page import CalendarsPage
from pages.click_events_page import ClickEventsPage
from pages.gestures_page import GesturesPage
from pages.hover_page import HoverPage
from pages.javascript_delays_page import JavaScriptDelaysPage
from pages.slider_page import SliderPage
from pages.spinners_page import SpinnersPage


@pytest.mark.regression
# TC_DELAY_HAPPY_001
# Verify the delayed action eventually shows the Liftoff message.
def test_javascript_delay_shows_liftoff(page):
    delays_page = JavaScriptDelaysPage(page)

    delays_page.open_page()
    delays_page.verify_page_loaded()
    delays_page.start_countdown()
    delays_page.verify_liftoff_visible()


@pytest.mark.regression
# TC_SLIDER_HAPPY_001
# Verify the slider value can be changed to a valid in-range value.
def test_slider_value_can_be_changed(page):
    slider_page = SliderPage(page)

    slider_page.open_page()
    slider_page.verify_page_loaded()
    slider_page.set_slider_value("80")
    slider_page.verify_slider_value("80")


@pytest.mark.regression
@pytest.mark.parametrize(
    "animal_name, expected_sound",
    [
        ("Cat", "Meow!"),
        ("Dog", "Woof!"),
        ("Pig", "Oink!"),
        ("Cow", "Moo!"),
    ],
)
# TC_CLICK_HAPPY_001
# Verify each animal button displays the expected sound text after click.
def test_click_events_show_expected_text(page, animal_name, expected_sound):
    click_events_page = ClickEventsPage(page)

    click_events_page.open_page()
    click_events_page.verify_page_loaded()
    click_events_page.click_animal(animal_name)
    click_events_page.verify_animal_sound(expected_sound)


@pytest.mark.regression
# TC_ACCORDION_HAPPY_001
# Verify the accordion reveals the hidden content after expansion.
def test_accordion_reveals_hidden_content(page):
    accordions_page = AccordionsPage(page)

    accordions_page.open_page()
    accordions_page.verify_page_loaded()
    accordions_page.open_accordion()
    accordions_page.verify_accordion_text()


@pytest.mark.regression
# TC_CALENDAR_HAPPY_001
# Verify the calendar input accepts a valid date string.
def test_calendar_input_accepts_date(page):
    calendars_page = CalendarsPage(page)

    calendars_page.open_page()
    calendars_page.verify_page_loaded()
    calendars_page.enter_date("2026-04-13")
    calendars_page.verify_date_value("2026-04-13")


@pytest.mark.regression
# TC_ADS_HAPPY_001
# Verify the ad modal appears after the configured delay.
def test_ad_modal_appears_after_countdown(page):
    ads_page = AdsPage(page)

    ads_page.open_page()
    ads_page.verify_page_loaded()
    ads_page.verify_ad_modal_visible()


@pytest.mark.regression
# TC_HOVER_HAPPY_001
# Verify hovering over the target changes the text to the success message.
def test_hover_displays_success_message(page):
    hover_page = HoverPage(page)

    hover_page.open_page()
    hover_page.verify_page_loaded()
    hover_page.hover_target()
    hover_page.verify_success_text()


@pytest.mark.regression
# TC_SPINNER_HAPPY_001
# Verify the spinner eventually transitions to the hidden state.
def test_spinner_becomes_hidden(page):
    spinners_page = SpinnersPage(page)

    spinners_page.open_page()
    spinners_page.verify_page_loaded()
    spinners_page.verify_spinner_hidden()


@pytest.mark.regression
# TC_GESTURE_HAPPY_001
# Verify the draggable image can be moved from the first box to the second box.
def test_drag_and_drop_image_to_second_box(page):
    gestures_page = GesturesPage(page)

    gestures_page.open_page()
    gestures_page.verify_page_loaded()
    source_children, target_children = gestures_page.drag_image_to_second_box()

    assert source_children == 0
    assert target_children == 1


@pytest.mark.regression
# TC_GESTURE_HAPPY_002
# Verify the movable box changes position after drag action.
def test_moveable_box_can_be_dragged(page):
    gestures_page = GesturesPage(page)

    gestures_page.open_page()
    gestures_page.verify_page_loaded()
    start_x, end_x = gestures_page.drag_moveable_box()

    assert start_x != end_x


@pytest.mark.regression
# TC_SLIDER_EDGE_001
# Verify the slider accepts both lower and upper boundary values.
def test_slider_accepts_boundary_values(page):
    slider_page = SliderPage(page)

    slider_page.open_page()
    slider_page.verify_page_loaded()
    slider_page.set_slider_value("0")
    slider_page.verify_slider_value("0")
    slider_page.set_slider_value("100")
    slider_page.verify_slider_value("100")


@pytest.mark.regression
# TC_ACCORDION_NEGATIVE_001
# Verify accordion content is hidden before the user expands it.
def test_accordion_content_is_hidden_before_expand(page):
    accordions_page = AccordionsPage(page)

    accordions_page.open_page()
    accordions_page.verify_page_loaded()
    accordions_page.verify_accordion_content_hidden()


@pytest.mark.regression
# TC_CALENDAR_EDGE_001
# Verify the date input can be overwritten with a different valid date.
def test_calendar_value_can_be_overwritten(page):
    calendars_page = CalendarsPage(page)

    calendars_page.open_page()
    calendars_page.verify_page_loaded()
    calendars_page.enter_date("2026-04-13")
    calendars_page.verify_date_value("2026-04-13")
    calendars_page.enter_date("2026-12-31")
    calendars_page.verify_date_value("2026-12-31")


@pytest.mark.regression
# TC_HOVER_NEGATIVE_001
# Verify the hover success message is not shown before any hover action.
def test_hover_success_message_is_hidden_initially(page):
    hover_page = HoverPage(page)

    hover_page.open_page()
    hover_page.verify_page_loaded()
    hover_page.verify_success_text_not_visible()


@pytest.mark.regression
# TC_SPINNER_EDGE_001
# Verify the spinner is visible first and then becomes hidden.
def test_spinner_transitions_from_visible_to_hidden(page):
    spinners_page = SpinnersPage(page)

    spinners_page.open_page()
    spinners_page.verify_page_loaded()
    spinners_page.verify_spinner_visible_initially()
    spinners_page.verify_spinner_hidden()
