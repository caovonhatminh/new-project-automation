PROJECT REQUIREMENTS

1. Project Goal
- Build an end-to-end UI automation test project for https://practice-automation.com/.
- Use Python for readability and easier onboarding.
- Use Playwright as the browser automation framework.
- Use Pytest as the test runner and assertion ecosystem.
- Organize the framework using Page Object Model (POM) for maintainability.

2. Technical Requirements
- The project must run with Python virtual environment support.
- The project must install dependencies from requirements.txt.
- The project must support Playwright browser installation and execution.
- The project must support local execution in headed mode and headless mode.
- The project must be runnable from terminal and from Visual Studio Code Testing panel.
- The project must use Pytest markers to separate smoke and regression execution.

3. Framework Structure
- The project must contain a pages/ directory for page object classes.
- Each page object class must keep locator constants at the top of the class.
- Page methods must contain reusable actions and verification methods.
- The project must contain a tests/ directory for test cases.
- The project must contain shared configuration through conftest.py and pytest.ini.
- The project must keep artifacts under artifacts/ for reports, logs, and screenshots.

4. Locator Strategy
- Locators must be easy to read and easy to update.
- XPath locators should be written directly with Playwright locator syntax, for example:
  page.locator("//td[text()='John Doe']/following-sibling::td[1]")
- Locator usage should prefer assigning an element to a variable first, then asserting or interacting with it.
- Dynamic or relation-based elements should use XPath axes such as following-sibling, preceding-sibling, ancestor, and descendant where appropriate.
- Locators should stay inside the corresponding page object class, not in a separate selector package.

5. Functional Test Coverage
- The framework must include smoke coverage for navigation to main pages.
- The framework must include regression coverage for the following features:
  Home page navigation
  Form Fields
  Modals
  Popups
  File Upload
  File Download
  Iframes
  Window Operations
  JavaScript Delays
  Slider
  Click Events
  Accordions
  Calendars
  Ads
  Hover
  Spinners
  Gestures
  Tables
  Broken Images
  Broken Links

6. Verification Requirements
- Each page object should expose clear verify_* methods where practical.
- Tests must validate important UI states such as visibility, text, value, open/close state, selected state, and navigation state.
- Tests should avoid hard sleep and instead rely on Playwright waiting and Pytest expectations.
- The framework should support both action-based tests and verification-only test functions for baseline regression confidence.

7. Reporting and Debugging
- The framework must generate HTML reports for smoke and regression runs.
- The framework must save screenshots when tests fail.
- The framework must save per-test logs for easier debugging.
- Artifacts must be suitable for local review and GitHub Actions upload.

8. CI/CD Requirements
- The project must include GitHub Actions workflow configuration.
- The CI pipeline must separate smoke and regression jobs.
- Regression should run after smoke passes.
- CI must install Python dependencies and Playwright browser binaries.
- CI must publish reports, screenshots, and logs as workflow artifacts.

9. Visual Studio Code Requirements
- The workspace must be configured to use the local .venv interpreter.
- VS Code must be able to discover and run Pytest tests from the Testing panel.
- The project should remain simple enough for manual review and maintenance inside VS Code.

10. Quality Expectations
- The framework should be readable for beginners.
- The design should favor maintainability over overly clever abstractions.
- The suite should provide a stable baseline regression pack for practice-automation.com.
- Current implemented baseline includes smoke and regression coverage with passing automated tests.
