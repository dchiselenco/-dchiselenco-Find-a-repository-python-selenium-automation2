from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.XPATH, "//div[@data-test='@web/CartLink']")
SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")



@when("Search for {item}")
def search_product(context, item):
    context.driver.find_element(*SEARCH_INPUT).send_keys(item)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(6)


@then('Verify search results are shown for {expected_product}')
def verify_search_results(context, expected_product):
    actual_text = context.driver.find_element(*SEARCH_RESULT_HEADER).text
    assert expected_product in actual_text, f'Error! Text {expected_product} not in {actual_text}'
