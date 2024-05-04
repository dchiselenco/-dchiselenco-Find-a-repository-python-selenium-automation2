from pages.base_page import Page
from selenium.webdriver.common.by import By



class MainPage(Page):
    SIGN_IN_BTN = (By.XPATH, "//a[@data-test='@web/AccountLink']")

    def open_main(self):
        self.driver.get('https://www.target.com/')


    def click_sign_in_button(self,context):
        self.wait_until_clickable(*self.SIGN_IN_BTN)