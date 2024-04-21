from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Cart(Page):
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    MESSAGE_CART_IS_EMPTY = (By.XPATH, '//h1[text()="Your cart is empty"]')

    def click_cart(self):
        self.click(*self.CART_ICON)

    def verify_cart_is_empty(self, expected_text):
        actual_text = self.find_element(*self.MESSAGE_CART_IS_EMPTY).text
        assert expected_text in actual_text, f'Error! Expected text "{expected_text}" not found in "{actual_text}"'
