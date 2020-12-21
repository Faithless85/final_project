import pytest
import time
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


@pytest.mark.basket_guest
class TestGuestAddToBasketFromProductPage():
    @pytest.mark.parametrize('offer', ["0", "1", "2", "3", "4", "5", "6",
                                       pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
    def test_guest_can_add_product_to_basket(self, browser, offer):
        product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.name_in_basket()
        page.basket_price()

    @pytest.mark.xfail(reason="message have to appear after adding product to basket")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_basket()
        page.should_be_no_success_message()

    def test_guest_cant_see_success_message(self, browser):
        product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, product_link)
        page.open()
        page.should_be_no_success_message()

    @pytest.mark.xfail(reason="message does not disappear")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_basket()
        page.success_message_should_disappear()


@pytest.mark.login_guest
class TestLoginFromProductPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_no_products_in_basket()
    page.should_be_text_that_basket_is_empty()


@pytest.mark.basket_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, login_link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "PaSsWoRd"
        page.register_new_user(email=email, password=password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, product_link)
        page.open()
        page.should_be_no_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_basket()
        page.name_in_basket()
        page.basket_price()
