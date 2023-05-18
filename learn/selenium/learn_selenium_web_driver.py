# -*- encoding: utf-8 -*-
# @ModuleName: learn_selenium_web_driver
# @Author: SZQ
# @Time: 2023/4/17 15:58
import time
from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get("https://www.baidu.com")
# browser.find_element('kw').clear()
# browser.find_element('kw').send_keys('九江')
# browser.find_element('su').click()
# time.sleep(20)
# browser.quit()

driver = webdriver.Firefox()
print(driver)
driver.get("https://www.baidu.com")
driver.maximize_window()
# driver.quit()
