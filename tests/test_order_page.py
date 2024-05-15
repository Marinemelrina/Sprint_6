from conftest import driver
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
from utils.test_data import YaScooterOrderHeaderBtn, YaScooterOrderMainBtn
import allure


class TestOrderPage:
    @allure.title('Оформление заказа через кнопку "Заказать" в шапке лэдинга')
    def test_create_order_header_btn(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        order_page = OrderPage(driver)
        home_page.get_cookies(HomePageLocators.cookies_button)
        order_page.click_header_order_btn()
        order_page.create_order(YaScooterOrderHeaderBtn.first_name,
                                YaScooterOrderHeaderBtn.last_name,
                                YaScooterOrderHeaderBtn.address,
                                OrderPageLocators.station_1,
                                YaScooterOrderHeaderBtn.phone,
                                OrderPageLocators.date_1,
                                OrderPageLocators.term_1,
                                OrderPageLocators.black_checkbox,
                                YaScooterOrderHeaderBtn.comment)
        text = order_page.check_success_order()
        assert 'Заказ оформлен' in text


    @allure.title('Проверка оформления заказа через кнопку "Заказать" в середине главной страницы')
    def test_create_order_main_page_btn(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        order_page = OrderPage(driver)
        home_page.get_cookies(HomePageLocators.cookies_button)
        order_page.click_main_order_btn()
        order_page.create_order(YaScooterOrderMainBtn.first_name,
                                YaScooterOrderMainBtn.last_name,
                                YaScooterOrderMainBtn.address,
                                OrderPageLocators.station_2,
                                YaScooterOrderMainBtn.phone,
                                OrderPageLocators.date_2,
                                OrderPageLocators.term_1,
                                OrderPageLocators.grey_checkbox,
                                YaScooterOrderMainBtn.comment)
        text = order_page.check_success_order()
        assert 'Заказ оформлен' in text