from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')
    #считаем Х
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    #считаем формулу
    calc(x)
    #скроллим
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    
    button.click()

    select = Select(browser.find_element_by_css_selector('#dropdown'))
    select.select_by_value(str(sum)) 

    button = browser.find_element_by_css_selector('.btn.btn-default').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()