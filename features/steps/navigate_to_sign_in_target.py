from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target.com')
def open_target_page(context):
    context.driver.get('https://www.target.com/')
    sleep(6)
@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
    sleep(4)
@when('From right side navigation menu click Sign In')
def click_sign_in_side_navigation(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(4)
@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    actual_text = context.driver.find_element(By.XPATH,"//h1[contains(@class, 'styles__AuthHeading') and .//span[contains(text(), 'Sign into your Target account')]]").text
    print(actual_text)
