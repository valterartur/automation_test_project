from .page.main_page import MainPage
from .page.login_page import LoginPage
from .page.book_page import BookPage
import time


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


def test_guest_can_add_product_to_basket(browser, language):
    link = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = BookPage(browser, link)
    page.open()
    page.add_book_to_busket()
    page.check_discount()
    time.sleep(2)
    page.check_name_of_book()
    page.check_book_and_busket_price()



def test_guest_can_add_product_to_basket2(browser, language):
    link = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/?promo=newYear2019'
    page = BookPage(browser, link)
    page.open()
    page.add_book_to_busket()
    page.check_discount()
    time.sleep(2)
    page.check_name_of_book()
    page.check_book_and_busket_price()


