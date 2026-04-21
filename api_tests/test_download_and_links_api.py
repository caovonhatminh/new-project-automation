import pytest

from api_tests.conftest import api_get


DOWNLOAD_URL = "https://practice-automation.com/download/download-file/"
BROKEN_LINK_URL = "https://practice-automation.com/broken-links/missing-page.html"


@pytest.mark.api
# TC_API_DOWNLOAD_HAPPY_001
# Verify the public download endpoint is reachable and returns a successful response.
def test_public_download_endpoint_eventually_succeeds(api_client):
    first_status, first_headers, first_body, _ = api_get(api_client, DOWNLOAD_URL)

    if first_status == 429:
        second_status, second_headers, second_body, _ = api_get(api_client, DOWNLOAD_URL)
        assert second_status == 200
        assert len(second_body) > 0
        assert "text/html" in second_headers.get("Content-Type", "").lower()
        return

    assert first_status == 200
    assert len(first_body) > 0
    assert "text/html" in first_headers.get("Content-Type", "").lower()


@pytest.mark.api
# TC_API_LINK_NEGATIVE_001
# Verify the known broken link returns an error response and does not resolve as 200.
def test_broken_link_endpoint_returns_error(api_client):
    first_status, _, _, _ = api_get(api_client, BROKEN_LINK_URL)

    if first_status == 429:
        second_status, _, second_body, _ = api_get(api_client, BROKEN_LINK_URL)
        assert second_status == 404
        assert len(second_body) > 0
        return

    assert first_status == 404


@pytest.mark.api
# TC_API_LINK_EDGE_001
# Verify the broken link target remains in the 4xx range on repeated requests.
def test_broken_link_endpoint_stays_in_client_error_range(api_client):
    first_status, _, _, _ = api_get(api_client, BROKEN_LINK_URL)
    second_status, _, _, _ = api_get(api_client, BROKEN_LINK_URL)

    assert first_status in {404, 429}
    assert second_status in {404, 429}
