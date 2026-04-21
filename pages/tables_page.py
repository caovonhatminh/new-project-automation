from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.settings import BASE_URL


class TablesPage(BasePage):
    URL = f"{BASE_URL}/tables/"
    SIMPLE_TABLE_ROW_TEMPLATE = "(//table)[1]//tr[td[normalize-space()={item_name}]]"
    SORTABLE_TABLE = "//table[@id='tablepress-1']"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("Tables")

    def verify_simple_table_visible(self) -> None:
        simple_table = self.page.locator("(//table)[1]")
        expect(simple_table).to_be_visible()

    def verify_sortable_table_visible(self) -> None:
        sortable_table = self.page.locator(self.SORTABLE_TABLE)
        expect(sortable_table).to_be_visible()

    def verify_sortable_table_headers(self) -> None:
        country_header = self.page.locator(f"{self.SORTABLE_TABLE}//th[normalize-space()='Country']")
        population_header = self.page.locator(f"{self.SORTABLE_TABLE}//th[contains(normalize-space(), 'Population')]")
        expect(country_header).to_be_visible()
        expect(population_header).to_be_visible()

    def verify_simple_table_value(self, item_name: str, expected_price: str) -> None:
        item_literal = self.xpath_literal(item_name)
        table_row = self.page.locator(self.SIMPLE_TABLE_ROW_TEMPLATE.format(item_name=item_literal))
        expect(table_row).to_contain_text(expected_price)

    def verify_sortable_table_contains_country(self, country_name: str) -> None:
        sortable_table = self.page.locator(self.SORTABLE_TABLE)
        expect(sortable_table).to_contain_text(country_name)
