from locators.main_page_locators import MainPageLocators as Main
from pages.main_page import BasePage, MainPage


class TestListQuestions:
    def test_first_question(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_site()
        main_page.scroll()
        driver.find_element(*Main.QUESTION_1).click()
        text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

        assert driver.find_element(*Main.ANSWER_1).text == text

    def test_second_question(self, scroll, driver):
        base_page = BasePage(driver)
        base_page.go_to_site()
        driver = scroll
        driver.find_element(*Main.QUESTION_2).click()
        text = "Пока что у нас так: один заказ — один самокат. " \
               "Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

        assert driver.find_element(*Main.ANSWER_2).text == text

    def test_third_question(self, scroll):
        driver = scroll
        driver.find_element(*Main.QUESTION_3).click()
        text = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. " \
               "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. " \
               "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

        assert driver.find_element(*Main.ANSWER_3).text == text

    def test_fourth_question(self, scroll):
        driver = scroll
        driver.find_element(*Main.QUESTION_4).click()
        text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

        assert driver.find_element(*Main.ANSWER_4).text == text

    def test_fifth_question(self, scroll):
        driver = scroll
        driver.find_element(*Main.QUESTION_5).click()
        text = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

        assert driver.find_element(*Main.ANSWER_5).text == text

    def test_sixth_question(self, scroll):
        driver = scroll
        driver.find_element(*Main.QUESTION_6).click()
        text = "Самокат приезжает к вам с полной зарядкой. " \
               "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. " \
               "Зарядка не понадобится."

        assert driver.find_element(*Main.ANSWER_6).text == text

    def test_seventh_question(self, scroll):
        driver = scroll
        driver.find_element(*Main.QUESTION_7).click()
        text = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

        assert driver.find_element(*Main.ANSWER_7).text == text

    def test_eighth_question(self, scroll):
        driver = scroll
        driver.find_element(*Main.QUESTION_8).click()
        text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

        assert driver.find_element(*Main.ANSWER_8).text == text


