from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
import allure
class OrderPage(BasePage):

    @allure.step('Клик на кнопку "Заказать" в шапке главной')
    def click_header_order_btn(self):
        self.click_to_element(HomePageLocators.order_header)


    @allure.step('Клик на кнопку "Заказать" в середине главной страницы')
    def click_main_order_btn(self):
        self.click_to_element(HomePageLocators.order_page)


    @allure.step('Заполнение поля "Имя"')
    def set_name(self, name):
        self.set_text(OrderPageLocators.name_field, name)


    @allure.step('Заполнение поля "Фамилия"')
    def set_last_name(self, last_name):
        self.set_text(OrderPageLocators.last_name_field, last_name)


    @allure.step('Заполнение поля "Адрес"')
    def set_address(self, address):
        self.set_text(OrderPageLocators.address_field, address)


    @allure.step('Выбор станции метро')
    def set_metro(self, station):
        self.find_element(OrderPageLocators.metro_station_field)
        self.click_to_element(OrderPageLocators.metro_station_field)
        self.click_to_element(station)


    @allure.step('Заполнение поля "Телефон"')
    def set_phone(self, phone):
        self.set_text(OrderPageLocators.phone_field, phone)


    @allure.step('Клик по кнопке "Далее"')
    def click_next_btn(self):
        self.click_to_element(OrderPageLocators.next_button)


    @allure.step('Выбор даты доставки')
    def set_date(self, date):
        self.click_to_element(OrderPageLocators.date_field)
        self.find_element(date)
        self.click_to_element(date)


    @allure.step('Выбор продолжительности срока аренды')
    def set_term(self, term):
        self.click_to_element(OrderPageLocators.rental_period_field)
        self.find_element(term)
        self.click_to_element(term)


    @allure.step('Выбор цвета')
    def set_color(self, color):
        self.click_to_element(color)


    @allure.step('Заполнение поля "Комментарии"')
    def set_comments(self, comments):
        self.set_text(OrderPageLocators.comments_field, comments)


    @allure.step('Появление модального окна "Заказ оформлен"')
    def check_success_order(self):
        return self.find_element(OrderPageLocators.order_success_window).text


    def create_order(self, name, last_name, address, station, phone, date, term, color, comments):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(station)
        self.set_phone(phone)
        self.click_next_btn()
        self.set_date(date)
        self.set_term(term)
        self.set_color(color)
        self.set_comments(comments)
        self.click_to_element(OrderPageLocators.order_button)
        self.click_to_element(OrderPageLocators.yes_button)