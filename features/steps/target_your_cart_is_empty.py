from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep



#@when('Click on Cart icon')
#def click_on_cart_icon(context):
    #context.wait.until(EC.element_to_be_clickable((CART_ICON)))
    #context.driver.find_element(*CART_ICON).click()


@then('Verify Your cart is empty message is shown')
def verify_cart_is_empty(context):

    context.app.cart_page.verify_cart_is_empty()