import pytest

from pages.iframe_page import IframePage
from pages.window_operations_page import WindowOperationsPage


@pytest.mark.regression
# TC_IFRAME_HAPPY_001
# Verify the iframe page contains both expected embedded iframe sources.
def test_verify_iframe_content(page):
    iframe_page = IframePage(page)

    iframe_page.open_page()
    iframe_page.verify_page_loaded()
    iframe_page.verify_iframe_urls()


@pytest.mark.regression
# TC_WINDOW_HAPPY_001
# Verify the New Tab action opens a separate page successfully.
def test_open_new_tab(page):
    window_page = WindowOperationsPage(page)

    window_page.open_page()
    window_page.verify_page_loaded()
    new_page = window_page.open_new_tab()

    assert new_page.url != ""


@pytest.mark.regression
# TC_WINDOW_EDGE_001
# Verify the newly opened tab has a non-empty page title.
def test_new_tab_has_non_empty_title(page):
    window_page = WindowOperationsPage(page)

    window_page.open_page()
    window_page.verify_page_loaded()
    new_page = window_page.open_new_tab()
    assert new_page.title() != ""
