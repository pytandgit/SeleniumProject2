from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_basket_button(self):
        # проверка на наличие кнопки "Добавить в корзину"
        assert self.browser.find_element(*ProductPageLocators.BASKET_BUTTON), "Кнопка 'Добавить в корзину' отсутствует"

    def should_be_same_bookname(self):
        # проверка на совпадение имени добавленной книги с именем в информационном сообщении, после добавления в корзину
        assert self.browser.find_element(*ProductPageLocators.BOOKNAME_IN_CARD).text == self.browser.find_element(*ProductPageLocators.BOOKNAME_IN_MESSAGE).text, "Название книги на карточке и в информационном сообщении не совпадают"
    def should_be_same_bookprice(self):
        # проверка на совпадение цены добавленной книги с ценой в информационном сообщении, после добавления в корзину
        assert self.browser.find_element(*ProductPageLocators.PRICE_IN_CARD).text == self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text, "Цена книги на карточке и в информационном сообщении не совпадают"
