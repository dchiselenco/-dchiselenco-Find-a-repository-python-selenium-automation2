from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



CART_ICON = (By.XPATH, "//div[@data-test='@web/CartLink']")
SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")



@then('Verify search results are shown for {expected_product}')
def verify_search_results(context, expected_product):

    context.app.search_results_page.verify_search_results(expected_product)



@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4,  ......]

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        product.find_element(*PRODUCT_IMG)