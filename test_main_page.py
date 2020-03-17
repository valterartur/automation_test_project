from .page.main_page import MainPage
from .page.login_page import LoginPage
from .page.book_page import BookPage
import time
import pytest

class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()
        login_page.should_be_login_form()
        login_page.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.basket_is_empty()


	
