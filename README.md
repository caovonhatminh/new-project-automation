# Playwright Python Automation - Practice Automation

Project nay dung `Playwright + Pytest` va duoc to chuc theo `Page Object Model (POM)` de de doc va de mo rong.

## 1. Cai dat

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install
```

## 2. Chay test

Chay toan bo:

```bash
pytest --html=artifacts\reports\report.html --self-contained-html
```

Chay smoke:

```bash
pytest -m smoke --html=artifacts\reports\smoke-report.html --self-contained-html
```

Chay 1 file:

```bash
pytest tests/test_forms.py
```

Artifacts sau khi chay test:

```text
artifacts/
  logs/
  reports/
  screenshots/
```

## 3. Cau truc project

```text
pages/       Page Object classes
tests/       Test cases
utils/       Dung chung cho config va helper
conftest.py  Pytest fixtures
```

## 4. Luu y

- `base_url` dang tro toi `https://practice-automation.com`
- Locator uu tien cach de doc: `get_by_role`, `get_by_label`, `get_by_text`
- Han che `sleep`; uu tien `expect(...)`
- Mac dinh browser chay co giao dien de ban de quan sat. Neu muon headless:

```bash
set HEADLESS=true
pytest --html=artifacts\reports\report.html --self-contained-html
```
