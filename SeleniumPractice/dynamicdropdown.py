
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="E:\\Selenium\\driver\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")


for i in countries:
    if i.text == "India":
        i.click()
        break
time.sleep(2)

assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"
