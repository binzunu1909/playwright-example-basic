import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='session')
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()
        yield page
        browser.close()