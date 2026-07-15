from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOKNAME_IN_CARD = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    BOOKNAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success strong")
    PRICE_IN_CARD = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
