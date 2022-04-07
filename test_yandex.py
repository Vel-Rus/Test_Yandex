from main_page import MainPage
from image_page import ImagesPage
from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException
from locators import MainPageLocators, ImagesPageLocators


class TestYandex(unittest.TestCase):
    link = "https://yandex.ru"
    link2 = "https://yandex.ru/images/"

    def setUp(self):
        self.browser = webdriver.Chrome()
        MainPage(self.browser, self.link).open()

    def test_search(self):
        page = MainPage(self.browser, self.link)
        # Проверяем поле поиска
        self.assertTrue(page.check_search_field(), "Поле поиска не отображается")

        # Проверяем suggest
        self.assertTrue(page.check_suggest(), "suggest не отображается")

        # Проверяем отсутствие таблицы результатов
        self.assertRaises(NoSuchElementException, self.browser.find_element, *MainPageLocators.SEARCH_RESULT)

        # Проверяем поиск
        self.assertTrue(page.check_search(), "Нет таблицы поиска")

        # Проверяем, что Тензор в первых пяти
        self.assertIn('https://tensor.ru/', page.check_tensor_ru()[:5], "tensor.ru не в первых пяти результатах поиска")

    def test_images(self):
        page = ImagesPage(self.browser, self.link2)
        # кликаем на ссылку "Картинки"
        page.image_click()

        # проверяем что перешли на url https://yandex.ru/images/
        self.assertEqual('https://yandex.ru/images/', self.browser.current_url.split('?')[0], 'перешли на другой url')

        # проверяем что открылась первая категория
        category_link, category_text = page.check_category()
        self.assertEqual(category_link, self.browser.current_url, 'Открылась не та категория')

        # проверяем, что в поиске нужный текст
        self.assertEqual(category_text, self.browser.find_element(*ImagesPageLocators.SEARCH_FIELD).
                         get_attribute("value"), 'в поиске не тот текст')

        # открываем первую картинку
        page.check_window_image()
        # проверяем что появилось окно с изображением
        self.assertTrue(page.check_media_viewer(), 'Нет окна с изображением')

        # проверяем что картинка меняется
        first_image_url, second_image_url = page.press_forward_button()
        self.assertNotEqual(first_image_url, second_image_url, 'картинка не изменилась')

        # проверяем, что изображение то же что и изначально
        self.assertEqual(first_image_url, page.press_return_button(), 'картинки отличаются')

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
