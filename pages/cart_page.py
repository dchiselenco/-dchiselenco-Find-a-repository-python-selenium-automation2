from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class CartPage(Page):

    MESSAGE_CART_IS_EMPTY = (By.XPATH, '//h1[text()="Your cart is empty"]')
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[data-test='orderPickupButton']")
    MESSAGE_ADDED_TO_CART = (By.XPATH, '//span[text()="Added to cart"]')


    def verify_cart_is_empty(self):
        #actual_text = self.driver.find_element(*self.MESSAGE_CART_IS_EMPTY).text
        #expected_text = 'Your cart is empty'
        #assert expected_text == actual_text, f'Error! Text Your cart is empty not on {actual_text}'
        self.verify_text( 'Your cart is empty', *self.MESSAGE_CART_IS_EMPTY)

    def add_item_cart(self):
        self.wait_until_clickable(*self.SIDE_NAV_ADD_TO_CART_BTN)

    def message_added_item(self):
        self.verify_text( 'Added to cart',*self.MESSAGE_ADDED_TO_CART)
