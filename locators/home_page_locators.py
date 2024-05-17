from selenium.webdriver.common.by import By

class HomePageLocators:

    order_header = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']") #кнопка заказа в шапке лединга
    order_page = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']") #кнопка заказа по середине страницы
    yandex_logo = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]") #логотип "Яндекс" в шапке лединга
    samokat_logo = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]") #логотип "Самокат" в шапке лединга
    cookies_button = (By.ID, "rcc-confirm-button")  #кнопка "Да, мы все привыкли" в сообщении о куках
    question_list = (By.XPATH, "//div[@id = 'accordion__heading-{}']")  #локатор вопросов выпадющего списка
    answer_list = (By.XPATH, '//div[@id="accordion__panel-{}"]/p') #локатор ответов выпадающего списка
    last_question = (By.XPATH, "(//div[contains(@id,'accordion__heading-')])[last()]") #локатор последнего вопроса

