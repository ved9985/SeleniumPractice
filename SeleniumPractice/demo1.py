from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="E:\\Selenium\\driver\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.google.com/")
print(driver.title)
driver.find_element(By.NAME, 'q').send_keys("naveen automationlab")
option_count = driver.find_elements(By.CSS_SELECTOR, "ul[jsname = 'bw4e9b'] li")

for i in option_count:
    if i.text == "s youtube":
        i.click()
        print(i.get_attribute("value"))
        time.sleep(4)
time.sleep(4)

#print(driver.find_element(By.NAME, 'q').get_attribute("value"))

