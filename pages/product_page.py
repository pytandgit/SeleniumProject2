from .locators import ProductPageLocators, BasketPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()

    def get_book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOKNAME_IN_CARD).text

    def get_book_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_IN_CARD).text

    def should_be_basket_button(self):
        # проверка на наличие кнопки "Добавить в корзину"
        assert self.browser.find_element(*ProductPageLocators.BASKET_BUTTON), "Кнопка 'Добавить в корзину' отсутствует"

    def should_be_same_bookname(self, book_name_in_card: str):
        # проверка на совпадение имени добавленной книги с именем в информационном сообщении, после добавления в корзину
        assert book_name_in_card == self.browser.find_element(
            *ProductPageLocators.BOOKNAME_IN_MESSAGE).text, "Название книги на карточке и в информационном сообщении не совпадают"

    def should_be_same_bookprice(self, book_price_in_card: str):
        # проверка на совпадение цены добавленной книги с ценой в информационном сообщении, после добавления в корзину
        assert book_price_in_card == self.browser.find_element(
            *ProductPageLocators.PRICE_IN_MESSAGE).text, "Цена книги на карточке и в информационном сообщении не совпадают"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), \
            "Products is presented, but should not be"

    def should_be_text_basket_is_empty(self):
        assert not self.is_disappeared(*BasketPageLocators.BASKET_MESSAGE), \
            "Message is disappeared, but should not be"
