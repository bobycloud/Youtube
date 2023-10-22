import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

url = "https://leetcode.com/"
driver.get(url)

login_link = driver.find_element(By.XPATH, "//div[@class='nav-menu']//a[@href='/accounts/login/']")
login_link.click()

time.sleep(5)

username_input = driver.find_element(By.XPATH, "//input[contains(@class, 'input__2o8B') and @data-cy='username']")
password_input = driver.find_element(By.XPATH, "//input[contains(@class, 'input__2o8B') and @data-cy='password']")

username_input.send_keys('test-video-boby')
password_input.send_keys(os.getenv("PASSWORD"))

login_button = driver.find_element(By.XPATH, "//button[contains(@class, 'fancy-btn__2prB') and @data-cy='sign-in-btn']")
login_button.click()

time.sleep(5)

try:
    driver.find_element(By.ID, "headlessui-menu-button-5")
    print("Yay, Test passed!")
except NoSuchElementException:
    print("Sorry, Test failed!")


driver.quit()