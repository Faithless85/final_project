from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        button.click()

    def name_in_basket(self):
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        product_name_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_STORE)
        assert product_name_in_basket.text == product_name_in_store.text, "product name does not match"

    def basket_price(self):
        price_in_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        price_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert price_in_basket.text == price_in_store.text, "price is not correct"
