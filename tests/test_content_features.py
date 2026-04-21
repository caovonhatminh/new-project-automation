import pytest

from pages.broken_images_page import BrokenImagesPage
from pages.broken_links_page import BrokenLinksPage
from pages.tables_page import TablesPage


@pytest.mark.regression
# TC_TABLE_HAPPY_001
# Verify the simple table shows the expected price for a known product.
def test_simple_table_displays_expected_price(page):
    tables_page = TablesPage(page)

    tables_page.open_page()
    tables_page.verify_page_loaded()
    tables_page.verify_simple_table_value("Laptop", "$1200.00")


@pytest.mark.regression
# TC_TABLE_HAPPY_002
# Verify the sortable table contains the expected country entry.
def test_sortable_table_contains_expected_country(page):
    tables_page = TablesPage(page)

    tables_page.open_page()
    tables_page.verify_page_loaded()
    tables_page.verify_sortable_table_contains_country("United States")


@pytest.mark.regression
# TC_IMAGE_NEGATIVE_001
# Verify the broken images page still contains broken image assets as intended.
def test_broken_images_page_contains_broken_images(page):
    broken_images_page = BrokenImagesPage(page)

    broken_images_page.open_page()
    broken_images_page.verify_page_loaded()

    assert broken_images_page.get_broken_image_count() >= 2


@pytest.mark.regression
# TC_LINK_NEGATIVE_001
# Verify the broken link target returns an HTTP error response.
def test_broken_link_returns_404(page):
    broken_links_page = BrokenLinksPage(page)

    broken_links_page.open_page()
    broken_links_page.verify_page_loaded()

    href = broken_links_page.get_broken_link_href()
    response = broken_links_page.fetch_broken_link()

    assert href.endswith("missing-page.html")
    assert response.status >= 400
