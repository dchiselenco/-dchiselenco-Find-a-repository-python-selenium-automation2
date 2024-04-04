from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')
@when('Click on Cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[href="/cart?prehydrateClick=true"]').click()
    sleep(6)
@then('Verify Your cart is empty message is shown')
def verify_cart_is_empty(context):
    actual_text = context.driver.find_element(By.XPATH, '//h1[text()="Your cart is empty"]').text
    assert 'Your cart is empty' in actual_text, f'Error! Text Your cart is empty not on {actual_text}'