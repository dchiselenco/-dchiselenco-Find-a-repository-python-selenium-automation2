from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


#SIGN_IN_BTN = (By.XPATH, "//a[@data-test='@web/AccountLink']")
#SIDE_NAV_SIGN_IN_BTN = (By.XPATH, "//a[@data-test='accountNav-signIn']")
#MESSAGE_TEXT = (By.XPATH,"//h1[contains(@class, 'styles__AuthHeading') and .//span[contains(text(), 'Sign into your Target account')]]")

@when('Click Sign In')
def click_sign_in(context):
    context.app.main_page.click_sign_in_button(context)


@when('From right side navigation menu click Sign In')
def click_sign_in_side_navigation(context):
    #context.wait.until(EC.element_to_be_clickable((SIDE_NAV_SIGN_IN_BTN)))
    #context.driver.find_element(*SIDE_NAV_SIGN_IN_BTN).click()
    #sleep(4)
    context.app.sign_in_page.click_sign_in_button_side_navigation(context)



@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    #context.wait.until(EC.presence_of_element_located((MESSAGE_TEXT)))
    #actual_text = context.driver.find_element(*MESSAGE_TEXT).text
    #print(actual_text)
    context.app.sign_in_page.verify_sign_in_form()
