from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element ((By.ID, "price"), "100")
    )
button= browser.find_element_by_id("book").click()

#считаем Х
x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
#считаем формулу
calc(x)

input1 = browser.find_element_by_id("answer").send_keys(calc(x))
submit = browser.find_element_by_id("solve").click()

time.sleep(10)
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text