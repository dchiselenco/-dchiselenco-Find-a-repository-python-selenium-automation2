

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.com/?ref_=nav_ya_signin&prevRID=NSNYH47K5HXR4P7DCCSJ&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&pageId=usflex&openid.ns=http://specs.openid.net/auth/2.0')

#Amazon logo
# $$(".a-icon-logo")
driver.find_element(By.CSS_SELECTOR, ".a-icon-logo")

#Create account text
# $$("h1.a-spacing-small")
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
#Your name insert text field
# $$("input#ap_customer_name")
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")

#Email insert text field
# $$("input#ap_email")
driver.find_element(By.CSS_SELECTOR, "input#ap_email")
#Passord insert text field
# $$("#ap_password")
driver.find_element(By.CSS_SELECTOR, "#ap_password")
#"Passords must be at least 6 chatacters." text
# $x("//text()[contains(., 'Passwords must be at least 6 characters.')]")
driver.find_element(By.XPATH, "//text()[contains(., 'Passwords must be at least 6 characters.')]")
#Re enter password insert text field
#$$("#ap_password_check")
driver.find_element(By.CSS_SELECTOR, ".a-icon-logo")

#Create your Amazon account button
# $$("#continue")
driver.find_element(By.CSS_SELECTOR, "#continue")
#Condition of Use link
# $x("//*[text()='Conditions of Use']")
driver.find_element(By.XPATH, "//*[text()='Conditions of Use']")

#Privacy Notice link
# $x("//*[text()='Privacy Notice']")
driver.find_element(By.XPATH, "//*[text()='Privacy Notice']")

#Sign in link
# $$(".a-link-emphasis")
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")

