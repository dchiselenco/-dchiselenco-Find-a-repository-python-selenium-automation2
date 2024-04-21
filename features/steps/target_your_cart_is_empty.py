from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR, 'a[href="/cart?prehydrateClick=true"]')
MESSAGE_CART_IS_EMPTY = (By.XPATH, '//h1[text()="Your cart is empty"]')


#@when('Click on Cart icon')
#def click_on_cart_icon(context):
    #context.wait.until(EC.element_to_be_clickable((CART_ICON)))
    #context.driver.find_element(*CART_ICON).click()


@then('Verify Your cart is empty message is shown')
def verify_cart_is_empty(context):
    #context.wait.until(EC.presence_of_element_located((MESSAGE_CART_IS_EMPTY)))
    #actual_text = context.driver.find_element(*MESSAGE_CART_IS_EMPTY).text
    #assert 'Your cart is empty' in actual_text, f'Error! Text Your cart is empty not on {actual_text}'

    expected_text = 'Your cart is empty'
    context.app.cart_page.verify_cart_is_empty(expected_text)