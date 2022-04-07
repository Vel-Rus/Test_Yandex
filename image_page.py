import time
from base_page import BasePage
from selenium.webdriver.common.by import By
from locators import MainPageLocators, ImagesPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class ImagesPage(BasePage):
    def image_click(self):
        image = self.browser.find_element(*ImagesPageLocators.IMAGES_LINK)
        image.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[1])

    def check_category(self):
        categories = self.browser.find_elements(*ImagesPageLocators.CATEGORIES_LINKS)
        category_text = categories[0].text
        category_link = categories[0].find_element_by_tag_name('a').get_attribute('href')
        # открываем первую категорию
        categories[0].click()
        return category_link, category_text

    def check_window_image(self):
        images = self.browser.find_elements(*ImagesPageLocators.SEARCH_RESULT_LINKS)
        # открываем первую картинку
        images[0].click()

    def check_media_viewer(self):
        media_viewer = self.browser.find_element(*ImagesPageLocators.MEDIA_VIEWER)
        return media_viewer.is_displayed()

    def press_forward_button(self):
        full_first_image_url = self.browser.current_url
        first_image_url = self.browser.find_element(*ImagesPageLocators.MEDIA_VIEWER_IMG).get_attribute('src')
        self.browser.find_element(*ImagesPageLocators.MEDIA_VIEWER_NEXT).click()
        WebDriverWait(self.browser, 10).until(EC.url_changes(full_first_image_url))
        second_image_url = self.browser.find_element(*ImagesPageLocators.MEDIA_VIEWER_IMG).get_attribute('src')
        return (first_image_url, second_image_url)

    def press_return_button(self):
        self.browser.find_element(*ImagesPageLocators.MEDIA_VIEWER_PREV).click()
        full_second_image_url = self.browser.current_url
        WebDriverWait(self.browser, 20).until(EC.url_changes(full_second_image_url))
        first_image_url_again = self.browser.find_element(*ImagesPageLocators.MEDIA_VIEWER_IMG).get_attribute('src')
        return first_image_url_again
