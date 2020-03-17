from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, '//span[contains (@class, "btn-group")]/a')
    BUSKET_IS_EMPTY = (By.XPATH, '//div[contains (@id, "content_inner")]/p')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    NEW_USER_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    NEW_USER_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    NEW_USER_REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, '//button[contains (@name, "registration_submit")]')


class BookPageLocators:
    ADD_TO_BUSKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.XPATH, '//div[contains (@class, "product_main")]/h1')
    SUCCESFUL_ADDED_ALERT = (
        By.XPATH, '//div[contains (@class, "alertinner")]/strong')
    BOOK_PRICE = (
        By.XPATH, '//p[contains (@class, "price_color")]')
    BUSKET_TOTAL_SUM = (By.XPATH, '//div[contains (@class, "alertinner")]/strong')
    SUCCESFUL_ADDED_ALERT_DIV = (By.XPATH, '//div[contains (@class, "alertinner")]')


    

