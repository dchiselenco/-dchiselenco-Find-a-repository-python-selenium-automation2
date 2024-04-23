from pages.base_page import Page
from selenium.webdriver.common.by import By

class SigninPage(Page):

    SIDE_NAV_SIGN_IN_BTN = (By.XPATH, "//a[@data-test='accountNav-signIn']")
    MESSAGE_TEXT = (By.XPATH,"//h1[contains(@class, 'styles__AuthHeading') and .//span[contains(text(), 'Sign into your Target account')]]")


    def click_sign_in_button_side_navigation(self, context):
        self.wait_until_clickable(*self.SIDE_NAV_SIGN_IN_BTN)




    def verify_sign_in_form(self, expected_text, *MESSAGE_TEXT):
        actual_text = self.driver.find_element(*MESSAGE_TEXT).text
        assert actual_text == expected_text, f'Error! Expected {expected_text}, but got {actual_text}'