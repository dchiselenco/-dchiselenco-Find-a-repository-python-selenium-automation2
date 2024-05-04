from pages.base_page import Page
from selenium.webdriver.common.by import By

class SigninPage(Page):

    SIDE_NAV_SIGN_IN_BTN = (By.XPATH, "//a[@data-test='accountNav-signIn']")
    MESSAGE_TEXT = (By.XPATH, '//span[text()="Sign into your Target account"]')

    def click_sign_in_button_side_navigation(self, context):
        self.wait_until_clickable(*self.SIDE_NAV_SIGN_IN_BTN)


    def verify_sign_in_form(self):
        actual_text = self.driver.find_element(*self.MESSAGE_TEXT).text
        expected_text = 'Sign into your Target account'
        assert actual_text in expected_text, f'Error! Text {expected_text} not in {actual_text}'
