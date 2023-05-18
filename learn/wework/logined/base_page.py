# -*- encoding: utf-8 -*-
# @ModuleName: base_page
# @Author: SZQ
# @Time: 2023/4/22 11:07
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        _driver = None
        _base_url = ''

        if driver is None:
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=options)
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver

        if _base_url != '':
            self._driver.get(_base_url)

    def find_element(self, by, way):
        return self._driver.find_element(by, way)
