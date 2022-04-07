from selenium.webdriver.common.by import By


class MainPageLocators(object):
    SEARCH_FIELD = (By.CSS_SELECTOR, "#text")
    SUGGEST = (By.CSS_SELECTOR, '.mini-suggest__popup')
    SEARCH_RESULT = (By.CSS_SELECTOR, "#search-result")
    BUTTON = (By.CSS_SELECTOR, "button.button")
    RESULT_ITEMS = (By.CSS_SELECTOR, "a.OrganicTitle-Link")


class ImagesPageLocators(object):
    CATEGORIES_LINKS = (By.CSS_SELECTOR, '.PopularRequestList-Item')
    SEARCH_FIELD = (By.NAME, 'text')
    SEARCH_RESULT_LINKS = (By.CSS_SELECTOR, '.serp-item')
    MEDIA_VIEWER = (By.CSS_SELECTOR, '.MediaViewer')
    MEDIA_VIEWER_NEXT = (By.CSS_SELECTOR, '.MediaViewer-ButtonNext')
    MEDIA_VIEWER_PREV = (By.CSS_SELECTOR, '.MediaViewer-ButtonPrev')
    MEDIA_VIEWER_IMG = (By.CSS_SELECTOR, '.MMImage-Origin')
    IMAGES_LINK = (By.LINK_TEXT, 'Картинки')