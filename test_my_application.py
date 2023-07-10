def test_search(page):
    page.goto('https://www.google.com')
    page.fill('[name="q"]', 'OpenAI')
    page.press('[name="q"]', 'Enter')
    assert 'OpenAI' in page.title()