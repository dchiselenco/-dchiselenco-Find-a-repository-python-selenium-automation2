from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")



    def search_product(self, item):
        self.input_text(item, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_cart(self):
        self.wait_until_clickable(*self.CART_ICON)
        self.save_screenshot('clicked_cart')