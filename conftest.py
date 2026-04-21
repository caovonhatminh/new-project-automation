import os
from pathlib import Path

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright
from playwright._impl._errors import Error as PlaywrightError

ARTIFACTS_DIR = Path("artifacts")
SCREENSHOTS_DIR = ARTIFACTS_DIR / "screenshots"
LOGS_DIR = ARTIFACTS_DIR / "logs"


def _safe_test_name(nodeid: str) -> str:
    invalid_chars = "\\/:*?\"<>|"
    safe_name = nodeid
    for char in invalid_chars:
        safe_name = safe_name.replace(char, "_")
    return safe_name.replace("::", "__")


@pytest.fixture(scope="session")
def playwright_instance() -> Playwright:
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def browser(playwright_instance: Playwright) -> Browser:
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    browser = playwright_instance.chromium.launch(headless=headless)
    yield browser
    browser.close()


@pytest.fixture
def context(browser: Browser) -> BrowserContext:
    context = browser.new_context(accept_downloads=True)
    yield context
    context.close()


@pytest.fixture
def page(context: BrowserContext, request: pytest.FixtureRequest) -> Page:
    page = context.new_page()
    test_name = _safe_test_name(request.node.nodeid)
    console_log_path = LOGS_DIR / f"{test_name}.log"

    def save_console_message(message) -> None:
        with console_log_path.open("a", encoding="utf-8") as log_file:
            log_file.write(f"[{message.type.upper()}] {message.text}\n")

    page.on("console", save_console_message)
    yield page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(autouse=True)
def capture_failure_artifacts(request: pytest.FixtureRequest):
    yield
    page_fixture = request.node.funcargs.get("page")
    if page_fixture and getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        screenshot_name = _safe_test_name(request.node.nodeid)
        screenshot_path = SCREENSHOTS_DIR / f"{screenshot_name}.png"
        try:
            page_fixture.screenshot(path=str(screenshot_path), full_page=True)
        except PlaywrightError:
            pass
