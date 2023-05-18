# -*- encoding: utf-8 -*-
# @ModuleName: register
# @Author: SZQ
# @Time: 2023/4/21 17:03
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    """
    注册的po
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        """
        注册的方法
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, '#corp_name').send_keys('我的企业')
        self.driver.find_element(By.CSS_SELECTOR, '#manager_name').send_keys('我的管理员')

        return True
