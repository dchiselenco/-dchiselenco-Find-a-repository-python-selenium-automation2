from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[data-test='orderPickupButton']")
MESSAGE_ADDED_TO_CART = (By.XPATH, '//span[text()="Added to cart"]')


@then('Select an item')
def select_an_item(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(6)


@then('Add item to cart')
def add_item_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()


@then('Cart message for added item')
def click_close_button(context):
    context.wait.until(EC.presence_of_element_located ((MESSAGE_ADDED_TO_CART)))
    context.driver.find_element(*MESSAGE_ADDED_TO_CART).text
