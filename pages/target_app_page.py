from selenium.webdriver.common.by import By
from pages.base_page import Page



class TargetAppPage(Page):
    PP_LINK = (By.XPATH, "//a[contains(text(), 'Privacy policy')]")
    TC_LINK = (By.XPATH, "//a[contains(text(), 'Target terms and conditions')]")

    def open(self, url):
        self.driver.get(url)


    def open_target_app(self):
        self.open('https://www.target.com/c/target-app/')

    def open_sign_in_page(self):
        self.open('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')

    def click_pp_link(self):
        self.click(*self.PP_LINK)


    def verify_pp_opened(self):
        self.verify_partial_url('target-privacy-policy/')

    def click_tc_link(self):
        self.click(*self.TC_LINK)

    def verify_tc_opened(self):
        self.verify_partial_url('terms-conditions/')
