import json
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

import pytest


def _build_opener():
    return urllib.request.build_opener()


@pytest.fixture(scope="session")
def api_client():
    return _build_opener()


def api_get(opener, url: str):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 API Test Client",
            "Accept": "*/*",
        },
    )
    try:
        response = opener.open(request, timeout=30)
        body = response.read()
        return response.getcode(), dict(response.headers.items()), body, response.geturl()
    except urllib.error.HTTPError as error:
        body = error.read()
        return error.code, dict(error.headers.items()), body, error.geturl()


def api_get_text(opener, url: str) -> str:
    _, _, body, _ = api_get(opener, url)
    return body.decode("utf-8", errors="ignore")


def api_post_form(opener, url: str, form_data: dict[str, str]):
    encoded_data = urllib.parse.urlencode(form_data).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=encoded_data,
        headers={
            "User-Agent": "Mozilla/5.0 API Test Client",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        },
        method="POST",
    )
    try:
        response = opener.open(request, timeout=30)
        body = response.read()
        return response.getcode(), dict(response.headers.items()), body, response.geturl()
    except urllib.error.HTTPError as error:
        body = error.read()
        return error.code, dict(error.headers.items()), body, error.geturl()


def api_post_multipart(
    opener,
    url: str,
    fields: dict[str, str],
    files: list[tuple[str, str, bytes, str]],
    referer: str | None = None,
):
    boundary = f"----CodexBoundary{uuid.uuid4().hex}"
    body_parts: list[bytes] = []

    for key, value in fields.items():
        body_parts.append(f"--{boundary}\r\n".encode("utf-8"))
        body_parts.append(
            f'Content-Disposition: form-data; name="{key}"\r\n\r\n{value}\r\n'.encode("utf-8")
        )

    for field_name, file_name, file_bytes, mime_type in files:
        body_parts.append(f"--{boundary}\r\n".encode("utf-8"))
        body_parts.append(
            (
                f'Content-Disposition: form-data; name="{field_name}"; '
                f'filename="{file_name}"\r\n'
                f"Content-Type: {mime_type}\r\n\r\n"
            ).encode("utf-8")
        )
        body_parts.append(file_bytes)
        body_parts.append(b"\r\n")

    body_parts.append(f"--{boundary}--\r\n".encode("utf-8"))
    body = b"".join(body_parts)

    headers = {
        "User-Agent": "Mozilla/5.0 API Test Client",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": f"multipart/form-data; boundary={boundary}",
    }
    if referer:
        headers["Referer"] = referer

    request = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        response = opener.open(request, timeout=30)
        response_body = response.read()
        return response.getcode(), dict(response.headers.items()), response_body, response.geturl()
    except urllib.error.HTTPError as error:
        body = error.read()
        return error.code, dict(error.headers.items()), body, error.geturl()


def parse_json(body: bytes):
    return json.loads(body.decode("utf-8"))


def extract_hidden_input_value(html: str, input_name: str) -> str:
    import re

    pattern = rf"name=['\"]{re.escape(input_name)}['\"][^>]*value=['\"]([^'\"]*)['\"]"
    match = re.search(pattern, html)
    assert match is not None, f"Hidden input '{input_name}' not found"
    return match.group(1)


def current_millis() -> str:
    return str(int(time.time() * 1000))
