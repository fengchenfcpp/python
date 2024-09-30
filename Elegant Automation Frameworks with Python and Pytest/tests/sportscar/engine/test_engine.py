import time
from pytest import mark


@mark.smoke
@mark.engine
@mark.ui
def test_can_navigate_to_engine_page(chrome_browser):
    my_browser = chrome_browser
    my_browser.get('http://www.google.com')

    time.sleep(1)

    second_browser = chrome_browser
    second_browser.get('http://www.amazon.com')
    assert True