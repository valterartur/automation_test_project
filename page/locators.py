from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BookPageLocators:
    ADD_TO_BUSKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.XPATH, '//div[contains (@class, "product_main")]/h1')
    SUCCESFUL_ADDED_ALERT = (
        By.XPATH, '//div[contains (@class, "alertinner")]/strong')
    BOOK_PRICE = (
        By.XPATH, '//p[contains (@class, "price_color")]')
    BUSKET_TOTAL_SUM = (By.XPATH, '//div[contains (@class, "alertinner")]/strong')


