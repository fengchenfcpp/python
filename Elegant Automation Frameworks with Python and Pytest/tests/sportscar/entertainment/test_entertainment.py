from pytest import mark


@mark.entertainment
@mark.ui
def test_can_navigate_to_entertainment_page(chrome_browser):
    chrome_browser.get('http://www.sas.com/')
    assert True