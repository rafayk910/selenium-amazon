from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import time
import urls
import info

class AmazonWebAutomation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.ChromeOptions()

    def test_amazon_web_app(self):
        driver = self.driver

print("Amazon Web Automation using Selenium with Python")
ser = Service(urls.Chrome)
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=opt)

# maximize the window size
driver.maximize_window()

# Launch the Amazon Web App
print('Launching Amazon Web App')
driver.get(urls.Amazon)
print('Amazon Web App launched successfully')
driver.get_screenshot_as_file("AmazonWeb.png")

# Search TV
print('Searching for TV')
driver.find_element(by=By.ID, value="twotabsearchtextbox").send_keys("Samsung TV")
driver.find_element(by=By.ID, value="nav-search-submit-button").click()
driver.get_screenshot_as_file("TVSearched.png")
tvElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span")))
tvElement.click()
driver.get_screenshot_as_file("ProductDetail.png")
driver.find_element(by=By.ID, value="buybox-see-all-buying-choices").click()
print('TV searched and page opened successfully')


# Add it to the Cart
print('Adding TV to Cart')
addToCart = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/span/span/span/div/div/div[4]/div/div[2]/div/div/div[2]/div/div/div[2]/span/span/span/span/input")))
addToCart.click()
time.sleep(10)
driver.get_screenshot_as_file("AddedtoCart.png")
time.sleep(5)
closeAddToCart = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/span/div/span/span/i")))
closeAddToCart.click()
print('TV added successfully to the Cart')


# Proceed to Checkout page with an Authenticated User
print('Proceeding to Checkout page')
driver.find_element(by=By.ID, value="nav-cart").click()
driver.find_element(by=By.ID, value="sc-buy-box-ptc-button").click()
print('Logging-in to the account')
driver.get_screenshot_as_file("Accountlogin.png")
driver.find_element(by=By.ID, value="ap_email").send_keys(info.ID)
driver.find_element(by=By.ID, value="continue").click()
driver.find_element(by=By.ID, value="ap_password").send_keys(info.Pass)
driver.find_element(by=By.ID, value="signInSubmit").click()
time.sleep(10)
print('Proceeded to checkout page successfully with an authenticated user')
driver.get_screenshot_as_file("ProceededtoCheckout.png")

# Verifying title for shipping page after successful login
print('Verifying title of the page after successful login')
time.sleep(15)
title = driver.title
assert title == "Enter the shipping address for this order"
print('Title verified!!')
print('Test Case Passed Successfully!')
driver.get_screenshot_as_file("TestcasePassed.png")

# close the browser once done
driver.close()
