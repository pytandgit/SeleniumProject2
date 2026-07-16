from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email: str, password: str):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        reg_pswd = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        reg_repeat_pswd = self.browser.find_element(*LoginPageLocators.REGISTRATION_REPEAT_PASSWORD)
        reg_email.send_keys(email)
        reg_pswd.send_keys(password)
        reg_repeat_pswd.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, "Login url is correct"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is presented"
