from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == self.url, "Urls didn't match"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        new_user_email_input = self.browser.find_element(
            *LoginPageLocators.NEW_USER_EMAIL_INPUT)
        new_user_email_input.send_keys(email)
        
        new_user_password_input = self.browser.find_element(
            *LoginPageLocators.NEW_USER_PASSWORD_INPUT)
        repeat_password_input = self.browser.find_element(
            *LoginPageLocators.NEW_USER_REPEAT_PASSWORD_INPUT)
        new_user_password_input.send_keys(password)
        repeat_password_input.send_keys(password)
        
        register_button = self.browser.find_element(
            *LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
