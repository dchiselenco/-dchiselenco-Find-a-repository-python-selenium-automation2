from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then
from time import sleep

WAIT_TIME = 10

COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonSelectorImage']")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='StyledHeaderWrapperDiv']")

@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')

    sleep(15)

@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['dark khaki', 'black/gum', 'stone/grey', 'white/gum']
    actual_colors = []

    WebDriverWait(context.driver, WAIT_TIME).until(
        EC.presence_of_all_elements_located(COLOR_OPTIONS)
    )

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()

        WebDriverWait(context.driver, WAIT_TIME).until(
            EC.visibility_of_element_located(SELECTED_COLOR)
        )

        selected_color = context.driver.find_element(*SELECTED_COLOR).text.strip()  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'