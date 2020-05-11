# SYSTEM TESTING USING SELENIUM
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time


driver = Chrome()
driver.implicitly_wait(10)
driver.get("http://localhost:8080")

# name = "Charles"
# driver.find_element(By.NAME, "name").send_keys(name)

# Contanins 6 whitespaces and 8 tabs
test_cases = ["rubbish","!$%*#&","      ","clustering","neural","123321","compu71ter","sp{}am","netw0r1<","                             ","analysis","processing"]

input_field = driver.find_element(By.ID,"forWidth")

# input_field.send_keys("neural")
# time.sleep(5)
# def document_initialised(driver):
#     return driver.execute_script("return initialised")

# driver.navigate("file:///race_condition.html")
# WebDriverWait(driver).until(document_initialised)
# el = driver.find_element(By.TAG_NAME, "p")
# assert el.text == "Hello from JavaScript!"


for test_case in test_cases:
    input_field.clear()
    print("TESTING for:",test_cases)
    time.sleep(3)
    input_field.send_keys(test_case)
    time.sleep(10)
    year_stat_button = driver.find_element(By.ID,"yearStat").click()
    time.sleep(6)
    author_stat_button = driver.find_element(By.ID,"authorStat").click()
    time.sleep(6)
    print("Successfull!(200 OK)")



print("OPENING HTML LINK")
html_link = driver.find_element(By.ID,"html_link").click()
print("HTML LINK SUCCESSFULLY OPENED!")
time.sleep(4)
print("OPENING PDF LINK")
pdf_link = driver.find_element(By.ID,"pdf_link").click()
print("PDF LINK SUCCESSFULLY OPENED!")

# driver.close()
