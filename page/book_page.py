from .base_page import BasePage
from .locators import BookPageLocators


class BookPage(BasePage):
    def add_book_to_busket(self):
        assert self.is_element_present(
            *BookPageLocators.ADD_TO_BUSKET_LINK), "There is not 'Add to busket' button"
        add_to_busket_button = self.browser.find_element(
            *BookPageLocators.ADD_TO_BUSKET_LINK)
        add_to_busket_button.click()

    def check_name_of_book(self):
        book_name = self.browser.find_element(
            *BookPageLocators.BOOK_NAME).text
        succesful_alert_book_name = self.browser.find_element(
            *BookPageLocators.SUCCESFUL_ADDED_ALERT).text
        assert book_name == succesful_alert_book_name, "Book names don't match"

    def check_book_and_busket_price(self):
        def clear_price(price):
            for letter in price:
                if letter.isdigit() == False and letter != '.':
                    price.replace(letter, '')
        book_price = self.browser.find_element(
            *BookPageLocators.BOOK_PRICE).text
        busket_total_sum = self.browser.find_element(
            *BookPageLocators.BUSKET_TOTAL_SUM).text
        assert clear_price(book_price) == clear_price(
            busket_total_sum), "Book names don't match"

    def no_succes_message_after_adding(self):
        assert self.is_not_element_present(
            *BookPageLocators.SUCCESFUL_ADDED_ALERT_DIV
        ) == True, ("Succes message is present")

    def no_succes_message_by_default(self):
        assert self.is_not_element_present(
            *BookPageLocators.SUCCESFUL_ADDED_ALERT_DIV
        ) == True, ("Succes message is present on start page")

    def succes_message_disapeared(self):
        assert self.is_disappeared(
            *BookPageLocators.SUCCESFUL_ADDED_ALERT_DIV
        ) == True, ("Succes message doesn't disappear")
