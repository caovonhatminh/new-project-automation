import pytest

from api_tests.conftest import api_get, parse_json


CF7_FORM_ID = "13587"
CF7_BASE = f"https://practice-automation.com/wp-json/contact-form-7/v1/contact-forms/{CF7_FORM_ID}"


@pytest.mark.api
# TC_API_CF7_HAPPY_001
# Verify the Contact Form 7 schema endpoint is reachable and returns JSON.
def test_cf7_schema_endpoint_returns_json(api_client):
    status_code, headers, body, final_url = api_get(api_client, f"{CF7_BASE}/feedback/schema")

    assert status_code == 200
    assert "application/json" in headers.get("Content-Type", "")
    assert final_url.endswith("/feedback/schema")

    payload = parse_json(body)
    assert isinstance(payload, dict)


@pytest.mark.api
# TC_API_CF7_HAPPY_002
# Verify the Contact Form 7 refill endpoint is reachable and returns JSON content.
def test_cf7_refill_endpoint_returns_json(api_client):
    status_code, headers, body, final_url = api_get(api_client, f"{CF7_BASE}/refill")

    assert status_code == 200
    assert "application/json" in headers.get("Content-Type", "")
    assert final_url.endswith("/refill")

    payload = parse_json(body)
    assert isinstance(payload, (dict, list))


@pytest.mark.api
# TC_API_CF7_EDGE_001
# Verify the schema endpoint remains stable across repeated requests.
def test_cf7_schema_endpoint_is_repeatable(api_client):
    first_status, _, first_body, _ = api_get(api_client, f"{CF7_BASE}/feedback/schema")
    second_status, _, second_body, _ = api_get(api_client, f"{CF7_BASE}/feedback/schema")

    assert first_status == 200
    assert second_status == 200
    assert first_body == second_body
