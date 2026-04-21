# E2E Test Flows

## 1. Purpose

This document defines the end-to-end test flows for the current Playwright + Pytest automation project built for [practice-automation.com](https://practice-automation.com/).

Unlike page-level UI tests, these E2E flows combine multiple actions into user-like journeys.  
The goal is to validate that important features work together from entry point to final result.

## 2. E2E Scope

The site is a practice sandbox, so "business" flows are limited.  
Because of that, E2E should focus on:

- navigation from home page
- completing representative user journeys
- verifying browser interactions across multiple pages
- validating combined behavior between UI and server-backed actions

## 3. E2E Flow Classification

### P0 Critical E2E Flows

These are the most useful baseline end-to-end journeys:

1. Home -> Form Fields -> Submit form
2. Home -> File Upload -> Upload supported file
3. Home -> File Download -> Open download endpoint
4. Home -> Modals -> Open modal -> Submit modal form
5. Home -> Window Operations -> Open new tab
6. Home -> Popups -> Handle alert/confirm/prompt

### P1 Secondary E2E Flows

These validate interactive journeys that span multiple steps but are not true server-backed submissions:

1. Home -> Calendars -> Enter and overwrite date
2. Home -> Tables -> Validate simple table + sortable table
3. Home -> Hover -> Trigger hover result
4. Home -> Accordion -> Expand content
5. Home -> Slider -> Change value to boundary and normal values
6. Home -> Gestures -> Drag image and move box
7. Home -> JavaScript Delays -> Start and wait for final result
8. Home -> Spinners -> Observe visible to hidden transition

### P2 Monitoring / Integration E2E Flows

These are useful for environment confidence but lower in business value:

1. Home -> Iframes -> Validate external sources
2. Home -> Broken Links -> Confirm broken target behavior
3. Home -> Broken Images -> Confirm broken assets are still detected
4. Home -> Ads -> Wait for popup ad to appear

## 4. Recommended E2E Journeys

### E2E_001 Home To Form Submission

Priority:
- P0

Goal:
- Validate the user can navigate from the home page to the form page and complete a valid form submission flow.

Steps:
1. Open home page
2. Verify home page is visible
3. Click `Form Fields`
4. Verify `Form Fields` page heading
5. Fill text fields
6. Select checkbox, radio, and dropdown values
7. Submit the form
8. Accept browser dialog if shown

Expected result:
- Target page opens correctly
- Fields accept input
- Submit action completes without UI failure

Related existing coverage:
- `tests/test_smoke_navigation.py`
- `tests/test_forms.py`

### E2E_002 Home To File Upload

Priority:
- P0

Goal:
- Validate the user can navigate to the upload page, select a supported file, and submit it.

Steps:
1. Open home page
2. Open `File Upload`
3. Verify upload page heading
4. Select supported file
5. Verify file name is populated
6. Submit upload

Expected result:
- File input accepts the file
- Submit action completes
- No blocking UI error appears

Related existing coverage:
- `tests/test_smoke_navigation.py`
- `tests/test_file_transfer.py`
- `api_tests/test_submission_api.py`

### E2E_003 Home To File Download

Priority:
- P0

Goal:
- Validate the user can navigate to the download page and reach the public download endpoint.

Steps:
1. Open home page
2. Open `File Download`
3. Verify page heading
4. Read or click the download link
5. Confirm the target endpoint is reachable

Expected result:
- Download page loads
- Download endpoint returns a valid HTTP response

Related existing coverage:
- `tests/test_file_transfer.py`
- `api_tests/test_download_and_links_api.py`

### E2E_004 Home To Modal Submission

Priority:
- P0

Goal:
- Validate the user can open the modal page, launch the form modal, and submit valid data.

Steps:
1. Open home page
2. Open `Modals`
3. Verify page heading
4. Open `Form Modal`
5. Fill name, email, and message
6. Submit form
7. Verify success state

Expected result:
- Modal opens correctly
- Fields accept input
- Submit completes successfully

Related existing coverage:
- `tests/test_modals.py`
- `api_tests/test_submission_api.py`

### E2E_005 Home To Popup Interaction

Priority:
- P0

Goal:
- Validate the user can trigger and handle all major browser popup types from one flow family.

Steps:
1. Open home page
2. Open `Popups`
3. Trigger alert and accept it
4. Trigger confirm and accept it
5. Trigger confirm and dismiss it
6. Trigger prompt and send input

Expected result:
- All popup types are handled without page failure
- Dialog messages are correct

Related existing coverage:
- `tests/test_popups.py`

### E2E_006 Home To New Tab Flow

Priority:
- P0

Goal:
- Validate the user can navigate to window operations and open a new browser tab successfully.

Steps:
1. Open home page
2. Open `Window Operations`
3. Click `New Tab`
4. Switch to new page
5. Verify URL/title is valid

Expected result:
- New tab opens
- New page is reachable

Related existing coverage:
- `tests/test_iframe_and_window.py`
- `tests/test_additional_verifications.py`

### E2E_007 Home To Calendar Data Entry

Priority:
- P1

Goal:
- Validate date entry flow including overwrite behavior.

Steps:
1. Open home page
2. Open `Calendars`
3. Verify field is empty
4. Enter first valid date
5. Overwrite with second valid date

Expected result:
- Date field stores expected value after each update

Related existing coverage:
- `tests/test_dynamic_features.py`
- `tests/test_additional_verifications.py`

### E2E_008 Home To Data Table Verification

Priority:
- P1

Goal:
- Validate that both simple and sortable tables are present and contain expected content.

Steps:
1. Open home page
2. Open `Tables`
3. Verify simple table is visible
4. Verify expected product price
5. Verify sortable table is visible
6. Verify headers and expected country content

Expected result:
- Both table sections load correctly
- Known content is present

Related existing coverage:
- `tests/test_content_features.py`
- `tests/test_additional_verifications.py`

### E2E_009 Home To Dynamic Interaction Journey

Priority:
- P1

Goal:
- Validate representative dynamic interactions from separate interactive pages.

Recommended grouped scenarios:
- Home -> Hover -> verify hover result
- Home -> Accordion -> expand and verify text
- Home -> Slider -> verify default, change to `80`, then boundaries `0` and `100`
- Home -> JavaScript Delays -> trigger delayed result
- Home -> Spinners -> verify transition from visible to hidden

Expected result:
- UI state changes correctly after each interaction

Related existing coverage:
- `tests/test_dynamic_features.py`

### E2E_010 Home To Gesture Journey

Priority:
- P1

Goal:
- Validate drag-and-drop interactions across the gestures page.

Steps:
1. Open home page
2. Open `Gestures`
3. Verify source and target are visible
4. Drag image to second box
5. Drag movable box to new position

Expected result:
- Drag image relocates to second target
- Movable box changes position

Related existing coverage:
- `tests/test_dynamic_features.py`
- `tests/test_additional_verifications.py`

### E2E_011 Home To External Content Verification

Priority:
- P2

Goal:
- Validate embedded external resources are still available.

Steps:
1. Open home page
2. Open `Iframes`
3. Verify both iframe sources exist and point to expected domains

Expected result:
- Top and bottom iframe sources are present

Related existing coverage:
- `tests/test_iframe_and_window.py`

### E2E_012 Home To Error Content Monitoring

Priority:
- P2

Goal:
- Validate expected error-oriented demo pages still behave as designed.

Grouped scenarios:
- Home -> Broken Links -> broken target returns error
- Home -> Broken Images -> broken assets detected
- Home -> Ads -> delayed ad popup appears

Expected result:
- Error demo pages continue to expose their intended conditions

Related existing coverage:
- `tests/test_content_features.py`
- `tests/test_dynamic_features.py`
- `api_tests/test_download_and_links_api.py`

## 5. Recommended E2E Suite Split

### E2E Smoke

Suggested contents:
- E2E_001 Home To Form Submission
- E2E_002 Home To File Upload
- E2E_003 Home To File Download
- E2E_004 Home To Modal Submission
- E2E_005 Home To Popup Interaction
- E2E_006 Home To New Tab Flow

Purpose:
- Fast confidence that the main user journeys still work

### E2E Regression

Suggested contents:
- All P0 flows
- All P1 flows
- Selected P2 flows

Purpose:
- Broader validation for CI or scheduled regression runs

### E2E Monitoring

Suggested contents:
- Iframes
- Broken Links
- Broken Images
- Ads

Purpose:
- Detect environment or third-party content changes

## 6. Mapping To Current Project

Current project already contains page-level coverage for almost all defined E2E steps.  
What is still missing is a dedicated `e2e/` layer that chains multiple pages into longer journeys.

Suggested future structure:

```text
e2e_tests/
  test_e2e_smoke.py
  test_e2e_core_journeys.py
  test_e2e_interactions.py
```

Suggested markers:

```text
@pytest.mark.e2e
@pytest.mark.e2e_smoke
@pytest.mark.e2e_regression
```

## 7. Recommended Next Implementation Order

1. Create E2E smoke tests for:
   - Form submission
   - File upload
   - Modal submission
   - Popup flow
   - New tab flow
2. Add E2E regression tests for:
   - Calendar
   - Tables
   - Slider / Hover / Accordion / Delay / Spinner
   - Gestures
3. Add optional monitoring E2E for:
   - Iframes
   - Broken links
   - Broken images
   - Ads

## 8. Important Note

This site is a feature sandbox, so many flows are intentionally isolated.  
Because of that, E2E here means:

- start from a user entry point
- navigate to the feature
- perform the full interaction path
- verify final observable outcome

It does not mean deep cross-module business workflow like a real product with accounts, orders, payments, or dashboards.
