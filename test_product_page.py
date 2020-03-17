from .page.main_page import MainPage
from .page.login_page import LoginPage
from .page.book_page import BookPage
from .page.book_page import BasePage
import time
import pytest
import random   

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser,language):
        def generete_email_and_password():
            email = str(random.random()) + "@gmail.com"
            password = str(random.random())
            return email, password
        self.link = f"http://selenium1py.pythonanywhere.com/{language}"
        page = MainPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email, password = generete_email_and_password()
        login_page.register_new_user(email, password)
        login_page.should_be_loggined()


    def test_user_cant_see_success_message(self, browser, language):
        self.link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/the-city-and-the-stars_95/"
        book_page = BookPage(browser, self.link)
        book_page.open()
        book_page.no_succes_message_by_default()
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, language):
        self.link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/the-city-and-the-stars_95/"
        page = BookPage(browser, self.link)
        page.open()
        page.add_book_to_busket()
        page.check_name_of_book()
        page.check_book_and_busket_price()


def test_guest_should_see_login_link_on_product_page(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/the-city-and-the-stars_95/"
    page = BookPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/the-city-and-the-stars_95/"
    page = BookPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, language):
    link = f" http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    page = BookPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.basket_is_empty()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, language):
    link = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = BookPage(browser, link)
    page.open()
    page.add_book_to_busket()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.check_name_of_book()
    page.check_book_and_busket_price()


def test_guest_can_add_product_to_basket2(browser, language):
    link = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/?promo=newYear2019'
    page = BookPage(browser, link)
    page.open()
    page.add_book_to_busket()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.check_name_of_book()
    page.check_book_and_busket_price()


@pytest.mark.parametrize('offer_No', ["1", "2", "3", "4", "5", "6",
                                      pytest.param(
                                          "7", marks=pytest.mark.xfail),
                                      "8", "9"])
def test_promo_offers(browser, language, offer_No):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/?promo=offer{str(offer_No)}"
    page = BookPage(browser, link)
    page.open()
    page.add_book_to_busket()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    time.sleep(4)
    page.check_name_of_book()
    page.check_book_and_busket_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, language):
    link = f" http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    page = BookPage(browser, link)
    page.open()
    page.add_book_to_busket()
    page.no_succes_message_after_adding()


def test_guest_cant_see_success_message(browser, language):
    link = f" http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    page = BookPage(browser, link)
    page.open()
    page.no_succes_message_by_default()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, language):
    link = f" http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    page = BookPage(browser, link)
    page.open()
    page.add_book_to_busket()
    page.succes_message_disapeared()
