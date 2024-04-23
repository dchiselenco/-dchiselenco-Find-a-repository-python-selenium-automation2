from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage(Page):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[id*="addToCartButton"]')


    def verify_search_results(self, expected_product):
        actual_text = self.find_element(*self.SEARCH_RESULT_HEADER).text
        assert expected_product in actual_text, f'Error! Text {expected_product} not in {actual_text}'


    def select_an_item(self):
        self.wait_until_clickable(*self.ADD_TO_CART_BTN)




