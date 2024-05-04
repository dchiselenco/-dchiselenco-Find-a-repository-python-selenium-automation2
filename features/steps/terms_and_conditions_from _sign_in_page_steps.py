from pages.base_page import Page
from pages.target_app_page import TargetAppPage


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep



@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.target_app_page.get_current_window()
    sleep(5)

@when('Click on Target terms and conditions link')
def click_tc_link(context):
    context.app.target_app_page.click_tc_link()


@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.target_app_page.verify_tc_opened()

    sleep(5)