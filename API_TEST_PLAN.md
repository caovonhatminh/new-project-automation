# API Test Plan

## 1. Scope

Website [practice-automation.com](https://practice-automation.com/) is primarily a UI practice site, not a public API product.  
Because of that, API testing in this project should focus on flows that clearly involve HTTP request/response behavior instead of forcing every UI page into API coverage.

The most relevant API/integration targets are:

- Form submission on [Form Fields](https://practice-automation.com/form-fields/)
- Form submission inside [Modals](https://practice-automation.com/modals/)
- File transfer behavior on [File Upload](https://practice-automation.com/file-upload/) and [File Download](https://practice-automation.com/file-download/)
- Error response behavior on [Broken Links](https://practice-automation.com/broken-links/)
- External resource availability on [Iframes](https://practice-automation.com/iframes/)

## 2. Out Of Scope

These pages are mainly browser-side interaction demos and are better covered by UI automation, not API automation:

- Popups
- Slider
- Hover
- Accordions
- Click Events
- Spinners
- Gestures
- Ads

## 3. API Test Strategy

- Prefer testing real HTTP behavior only where the page clearly depends on server response.
- Keep API validation separate from UI assertions.
- Validate status code, headers, payload shape, file metadata, and error handling where applicable.
- Do not assume strict backend validation unless it is confirmed by real behavior.
- If a page behavior is mostly front-end only, keep it in UI suite and do not duplicate it as API test.

## 4. Candidate API Areas And Test Cases

### 4.1 Form Fields Submission

Reference:
- [Form Fields](https://practice-automation.com/form-fields/)

Why this matters:
- This page contains a real submission flow and is the strongest candidate for request payload and response validation.

Happy cases:
- Submit form with valid required and optional fields.
- Submit form with all supported field types populated.
- Submit form with valid email format.
- Submit form with one valid automation selection.

Negative cases:
- Submit with missing required name.
- Submit with invalid email format.
- Submit with empty payload.
- Submit with only whitespace values.
- Submit with malformed request body.

Edge cases:
- Submit with long name/message values.
- Submit with special characters and Unicode.
- Submit with HTML-like or script-like content.
- Submit multiple times in quick succession.
- Submit with multiple checkbox values selected.

Verify:
- HTTP status code
- Response body or response message
- Response content-type
- Error payload shape when request is invalid
- Server behavior consistency across repeated submissions

### 4.2 Modal Form Submission

Reference:
- [Modals](https://practice-automation.com/modals/)

Why this matters:
- The modal contains a second form flow that may behave differently from the main form.

Known UI observation from current automation:
- Blank modal form submit still shows success in UI.
- This suggests backend validation may be minimal or absent.

Happy cases:
- Submit modal form with valid name, email, and message.
- Submit modal form with minimum valid payload.

Negative cases:
- Submit with missing name.
- Submit with invalid email.
- Submit with empty message if the endpoint is expected to validate it.

Edge cases:
- Submit fully blank payload and confirm actual server behavior.
- Submit special characters and Unicode.
- Submit repeated requests in the same session.
- Submit after reopening the modal.

Verify:
- HTTP status code
- Whether blank payload is accepted or rejected
- Response message consistency
- Session/cookie dependency if any

### 4.3 File Upload

Reference:
- [File Upload](https://practice-automation.com/file-upload/)

Public page constraints:
- Max file size: `1 MB`
- Supported file types: `txt, docx, pdf, jpeg, png, jpg, gif`

Happy cases:
- Upload supported file type below 1 MB.
- Upload each supported file type successfully.
- Upload valid file with normal ASCII filename.

Negative cases:
- Upload unsupported extension.
- Upload file larger than 1 MB.
- Submit without selecting a file.
- Upload file with mismatched extension and mime type.

Edge cases:
- Upload file exactly 1 MB.
- Upload file 1 MB + 1 byte.
- Upload zero-byte file.
- Upload filename with spaces.
- Upload filename with Unicode characters.
- Upload very long filename.
- Upload same file repeatedly.

Verify:
- HTTP status code
- Validation/error response
- Accepted file type handling
- Size-limit enforcement
- Returned file metadata if present

### 4.4 File Download

Reference:
- [File Download](https://practice-automation.com/file-download/)

Public page hints:
- Normal download exists
- Password protected download exists
- Password shown on page: `automateNow`

Happy cases:
- Download normal file successfully.
- Download password-protected file with correct password.
- Validate file response headers for successful download.

Negative cases:
- Download protected file without password.
- Download protected file with wrong password.
- Request invalid download URL.

Edge cases:
- Download same file multiple times in one session.
- Download protected file after previous failed password attempt.
- Validate behavior for HEAD request if endpoint supports it.

Verify:
- HTTP status code
- `Content-Disposition`
- `Content-Type`
- file size greater than zero
- access control behavior on protected download

### 4.5 Broken Links

Reference:
- [Broken Links](https://practice-automation.com/broken-links/)

Public page explicitly states:
- Clicking the broken link returns `404`

Happy cases:
- Verify the known broken link returns expected error code.

Negative cases:
- Verify the broken target does not silently return `200`.

Edge cases:
- Verify error response still returns valid HTML body.
- Verify response time is reasonable and does not hang.

Verify:
- HTTP status code is `404` or expected `4xx`
- target URL is the expected broken resource
- response body exists

### 4.6 Iframe Resource Availability

Reference:
- [Iframes](https://practice-automation.com/iframes/)

Why this matters:
- This is more of an integration/availability check than an API business flow.
- It is still useful to validate embedded source availability.

Happy cases:
- Top iframe source returns successful response.
- Bottom iframe source returns successful response.

Negative cases:
- Embedded resource unavailable or timeout.

Edge cases:
- Redirect behavior changes.
- Cross-domain headers prevent expected rendering behavior.

Verify:
- HTTP status code
- final URL after redirects
- content availability

## 5. Recommended Execution Priority

Recommended order for implementation:

1. File Download
2. Broken Links
3. File Upload
4. Form Fields Submission
5. Modal Form Submission
6. Iframe Resource Availability

Reason:
- Download and broken-link checks are the most deterministic.
- Upload and form submission are more useful but may require discovering the actual request endpoints first.
- Iframe availability is lower business value and closer to integration monitoring.

## 6. Recommended Test Structure

Suggested structure for future API tests:

```text
api_tests/
  test_download_api.py
  test_broken_links_api.py
  test_upload_api.py
  test_form_submission_api.py
  test_modal_form_api.py
  test_iframe_resources_api.py
```

Suggested support modules:

```text
api_clients/
  base_client.py
  download_client.py
  upload_client.py
  forms_client.py
```

## 7. Risks And Assumptions

- This site does not publish a formal API contract on the public pages reviewed.
- Some flows may be handled by WordPress plugins or form services rather than a clean REST API.
- Some validations may happen only on the client side or may not exist at all.
- Before implementation, actual network requests should be inspected in browser devtools or by Playwright network capture.

## 8. Next Step

Next recommended action:

- Discover real request endpoints and payload formats for:
  - Form Fields submit
  - Modal form submit
  - File Upload
  - Password-protected File Download

After that, API automation can be scaffolded with `pytest + requests` in a separate `api_tests/` suite.
