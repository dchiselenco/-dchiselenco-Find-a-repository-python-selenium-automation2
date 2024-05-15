from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep



class SearchResultsPage(Page):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
    FAVORITES_BTN = (By.CSS_SELECTOR, '[data-test="FavoritesButton"]')
    FAVORITES_TOOLTIP_TXT = (By.XPATH, "//*[text()='Click to sign in and save']")

    def hover_fav_icon(self):
        fav_btn = self.find_element(*self.FAVORITES_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(fav_btn)
        actions.perform()


    def verify_fav_tooltip(self):
        self.verify_text('Click to sign in and save', *self.FAVORITES_TOOLTIP_TXT)


    def verify_search_results(self, expected_product):
        actual_text = self.find_element(*self.SEARCH_RESULT_HEADER).text
        assert expected_product in actual_text, f'Error! Text {expected_product} not in {actual_text}'


    def select_an_item(self):
        self.wait_until_clickable(*self.ADD_TO_CART_BTN)




