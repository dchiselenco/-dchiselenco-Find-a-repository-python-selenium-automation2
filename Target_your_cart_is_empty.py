import drive
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

# Open https://www.target.com/
driver.get('https://www.target.com/')
sleep(6)
# Click on Cart icon
#driver.find_element(By.XPATH, '//div[@data-test="@web/CartIcon"]').click()
driver.find_element(By.CSS_SELECTOR, 'a[href="/cart?prehydrateClick=true"]').click()
sleep(6)
# Verify “Your cart is empty” message is shown


actual_text = driver.find_element(By.XPATH, '//h1[text()="Your cart is empty"]').text

print(actual_text)
driver.quit()