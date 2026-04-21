from pathlib import Path

import pytest

from api_tests.conftest import (
    api_get_text,
    api_post_form,
    api_post_multipart,
    current_millis,
    extract_hidden_input_value,
    parse_json,
)


FILE_UPLOAD_PAGE_URL = "https://practice-automation.com/file-upload/"
FILE_UPLOAD_API_URL = "https://practice-automation.com/wp-json/contact-form-7/v1/contact-forms/13587/feedback"
MODALS_PAGE_URL = "https://practice-automation.com/modals/"
MODAL_API_URL = "https://practice-automation.com/wp-admin/admin-ajax.php?action=grunion-contact-form"


@pytest.mark.api
# TC_API_UPLOAD_HAPPY_001
# Verify the file upload API returns a completed JSON response for a supported file with the real CF7 form contract.
def test_file_upload_api_accepts_valid_text_file(api_client):
    html = api_get_text(api_client, FILE_UPLOAD_PAGE_URL)
    sample_file = Path("tests/data/sample_upload.txt").read_bytes()

    fields = {
        "_wpcf7": extract_hidden_input_value(html, "_wpcf7"),
        "_wpcf7_version": extract_hidden_input_value(html, "_wpcf7_version"),
        "_wpcf7_locale": extract_hidden_input_value(html, "_wpcf7_locale"),
        "_wpcf7_unit_tag": extract_hidden_input_value(html, "_wpcf7_unit_tag"),
        "_wpcf7_container_post": extract_hidden_input_value(html, "_wpcf7_container_post"),
        "_wpcf7_posted_data_hash": extract_hidden_input_value(html, "_wpcf7_posted_data_hash"),
        "_wpcf7_ak_js": current_millis(),
        "_wpcf7_ak_hp_textarea": "",
    }
    files = [("file-941", "sample_upload.txt", sample_file, "text/plain")]

    status_code, headers, body, _ = api_post_multipart(
        api_client,
        FILE_UPLOAD_API_URL,
        fields,
        files,
        referer=FILE_UPLOAD_PAGE_URL,
    )

    assert status_code == 200
    assert "application/json" in headers.get("Content-Type", "")

    payload = parse_json(body)
    assert isinstance(payload, dict)
    assert payload.get("status") in {"mail_sent", "mail_failed", "validation_failed"}
    assert "message" in payload
    assert "thank you" in payload["message"].lower()


@pytest.mark.api
# TC_API_UPLOAD_NEGATIVE_001
# Verify the file upload API returns a handled JSON response when no file is provided.
def test_file_upload_api_rejects_missing_file(api_client):
    html = api_get_text(api_client, FILE_UPLOAD_PAGE_URL)

    fields = {
        "_wpcf7": extract_hidden_input_value(html, "_wpcf7"),
        "_wpcf7_version": extract_hidden_input_value(html, "_wpcf7_version"),
        "_wpcf7_locale": extract_hidden_input_value(html, "_wpcf7_locale"),
        "_wpcf7_unit_tag": extract_hidden_input_value(html, "_wpcf7_unit_tag"),
        "_wpcf7_container_post": extract_hidden_input_value(html, "_wpcf7_container_post"),
        "_wpcf7_posted_data_hash": extract_hidden_input_value(html, "_wpcf7_posted_data_hash"),
        "_wpcf7_ak_js": current_millis(),
        "_wpcf7_ak_hp_textarea": "",
    }

    status_code, headers, body, _ = api_post_multipart(
        api_client,
        FILE_UPLOAD_API_URL,
        fields,
        [],
        referer=FILE_UPLOAD_PAGE_URL,
    )

    assert status_code == 200
    assert "application/json" in headers.get("Content-Type", "")

    payload = parse_json(body)
    assert isinstance(payload, dict)
    assert payload.get("status") in {"validation_failed", "mail_failed"}
    assert "message" in payload


@pytest.mark.api
# TC_API_MODAL_HAPPY_001
# Verify the modal form API accepts a valid payload using the live Jetpack token and hidden fields.
def test_modal_form_api_accepts_valid_payload(api_client):
    html = api_get_text(api_client, MODALS_PAGE_URL)

    form_data = {
        "jetpack_contact_form_jwt": extract_hidden_input_value(html, "jetpack_contact_form_jwt"),
        "g1051-name": "Minh",
        "g1051-email": "minh@example.com",
        "g1051-message": "Modal API submission from automated test.",
        "contact-form-id": extract_hidden_input_value(html, "contact-form-id"),
        "action": extract_hidden_input_value(html, "action"),
        "contact-form-hash": extract_hidden_input_value(html, "contact-form-hash"),
        "ak_hp_textarea": "",
        "ak_js": current_millis(),
    }

    status_code, headers, body, _ = api_post_form(api_client, MODAL_API_URL, form_data)

    assert status_code == 200
    content_type = headers.get("Content-Type", "").lower()
    assert "text/html" in content_type or "application/json" in content_type
    assert len(body) > 0


@pytest.mark.api
# TC_API_MODAL_NEGATIVE_001
# Verify the modal form API rejects a blank required name with an error HTTP response.
def test_modal_form_api_rejects_blank_required_name(api_client):
    html = api_get_text(api_client, MODALS_PAGE_URL)

    form_data = {
        "jetpack_contact_form_jwt": extract_hidden_input_value(html, "jetpack_contact_form_jwt"),
        "g1051-name": "",
        "g1051-email": "minh@example.com",
        "g1051-message": "Blank name contract check.",
        "contact-form-id": extract_hidden_input_value(html, "contact-form-id"),
        "action": extract_hidden_input_value(html, "action"),
        "contact-form-hash": extract_hidden_input_value(html, "contact-form-hash"),
        "ak_hp_textarea": "",
        "ak_js": current_millis(),
    }

    status_code, _, body, _ = api_post_form(api_client, MODAL_API_URL, form_data)

    assert status_code == 400
    assert len(body) > 0
