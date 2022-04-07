import time
from base_page import BasePage
from locators import MainPageLocators, ImagesPageLocators
from selenium.webdriver.common.keys import Keys

class MainPage(BasePage):
    def check_search_field(self):
        search_field = self.browser.find_element(*MainPageLocators.SEARCH_FIELD)
        return search_field.is_displayed()

    def check_suggest(self):
        search_field = self.browser.find_element(*MainPageLocators.SEARCH_FIELD)
        search_field.send_keys('Тензор')
        time.sleep(1)
        suggest = self.browser.find_element(*MainPageLocators.SUGGEST)
        return suggest.is_displayed()

    def check_search(self):
        button = self.browser.find_element(*MainPageLocators.BUTTON)
        button.send_keys(Keys.RETURN)
        search_table = self.browser.find_element(*MainPageLocators.SEARCH_RESULT)
        return search_table.is_displayed()

    def check_tensor_ru(self):
        result_items = self.browser.find_elements(*MainPageLocators.RESULT_ITEMS)
        hrefs = [el.get_attribute('href') for el in result_items]
        return hrefs



