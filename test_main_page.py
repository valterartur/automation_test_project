from .page.main_page import MainPage
from .page.login_page import LoginPage


def test_guest_can_go_to_login_page(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    login_page.should_be_register_form()
