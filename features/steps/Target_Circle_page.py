
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFITS = (By.CSS_SELECTOR, "[class*='CellItemContainer']")


@given('Open the Target Circle page')
def open_target(context):
    context.driver.get('https://www.target.com/circle')
    sleep(10)

@then('{expected_amount} benefit cells are shown')
def verify_amount_cells_benefit(context, expected_amount):
    expected_amount = int(expected_amount)
    cells = context.driver.find_elements(*BENEFITS)
    #print(cells)
    assert len(cells) == expected_amount
    for cell in cells:
        print(cell.text)