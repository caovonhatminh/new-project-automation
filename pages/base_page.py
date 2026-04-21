from playwright.sync_api import Page, expect
from playwright._impl._errors import TimeoutError as PlaywrightTimeoutError

from utils.settings import DEFAULT_TIMEOUT


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.page.set_default_timeout(DEFAULT_TIMEOUT)

    def open(self, url: str) -> None:
        try:
            self.page.goto(url, wait_until="domcontentloaded")
        except PlaywrightTimeoutError:
            self.page.goto(url, wait_until="domcontentloaded", timeout=DEFAULT_TIMEOUT * 2)

    @staticmethod
    def xpath_literal(value: str) -> str:
        if "'" not in value:
            return f"'{value}'"
        if '"' not in value:
            return f'"{value}"'
        parts = value.split("'")
        return "concat(" + ", \"'\", ".join(f"'{part}'" for part in parts) + ")"

    def expect_heading(self, heading_text: str) -> None:
        # Practical strategy: headings are usually stable enough by exact text.
        heading_literal = self.xpath_literal(heading_text)
        heading = self.page.locator(f"//h1[normalize-space()={heading_literal}]")
        expect(heading).to_be_visible()

    def click_link(self, link_text: str) -> None:
        # Practical strategy: use exact anchor text only for high-level navigation.
        link_literal = self.xpath_literal(link_text)
        link = self.page.locator(f"//a[normalize-space()={link_literal}]")
        link.click()
