
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="E:\\Selenium\\driver\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "email").send_keys("vedprakash@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.NAME, "name").send_keys("Ved Prakash")
time.sleep(2)
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

driver.find_element(By.XPATH, "//input[@type='submit']").click()
# static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
message = driver.find_element(By.CLASS_NAME, "alert ").text
print(message)
assert "Success" in message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello again ")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
time.sleep(10)
