from selenium.webdriver.common.by import By

class OrderPageLocators:
    name_field = (By.XPATH, "//input[@placeholder='* Имя']")#поле "Имя" на странице "Для кого самокат"
    last_name_field = (By.XPATH, "//input[@placeholder='* Фамилия']") #поле "Фамилия" на странице "Для кого самокат"
    address_field = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") #поле "Адрес:куда привезти заказ" на странице "Для кого самокат"
    metro_station_field = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']") #поле "Станция метро" на странице "Для кого самокат"
    station_1 = (By.XPATH, "//li[@class='select-search__row' and @data-index='0' and @data-value='1']") #станции метро
    station_2 = (By.XPATH, "//li[@class='select-search__row' and @data-index='3' and @data-value='4']") #станции метро
    phone_field = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']") #поле "Телефон: на него позвонит курьер" на странице "Для кого самокат"
    next_button = (By.XPATH, "//button[text()='Далее']") #кнопка "Далее" на странице на странице "Для кого самокат"
    date_field = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']") #поле "Когда привезти самокат" на странице "Про аренду"
    date_1 = (By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--010']") #выбранная дата
    date_2 = (By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--021']") #выбранная дата
    rental_period_field = (By.XPATH, "//div[text()='* Срок аренды']") #поле "Срок аренды" на странице "Про аренду"
    term_1 = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']") #продолжительность аренды
    term_2 = (By.XPATH, "//div[@class='Dropdown-option' and text()='пятеро суток']") #продолжительность аренды
    black_checkbox = (By.ID, "black") #чекбокс чёрного цвета на станице "Про аренду"
    grey_checkbox = (By.ID, "grey") #чекбокс серого цвета на станице "Про аренду"
    comments_field = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") #поле "Комментарий для курьера" на странице "Про аренду"
    order_button = (By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]') #кнопка "Заказать" на странице "Про аренду"
    yes_button = (By.XPATH, "//button[text()='Да']") #кнопка подтверждения в всплывающем окне "Хотите оформить заказ?"
    order_success_window = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]") #окно успешного заказа