from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@given('Open Target maiin page')
def open_target(context):
    context.driver.get("https://www.target.com/")
@when("Search for 'coffe'")
def search_coffe(context):
    context.driver
    context.driver
    sleep(6)

@then("Verify search results are shown")
def verify_search_results(context):
    actual_text = context.driver.element
    assert