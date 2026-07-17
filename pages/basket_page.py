from .locators import BasketPageLocators
from .main_page import MainPage


class BasketPage(MainPage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), \
            "Products is presented, but should not be"

    def should_be_text_basket_is_empty(self):
        assert not self.is_disappeared(*BasketPageLocators.BASKET_MESSAGE), \
            "Message is disappeared, but should not be"
