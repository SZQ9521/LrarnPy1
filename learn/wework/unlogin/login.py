# -*- encoding: utf-8 -*-
# @ModuleName: login
# @Author: SZQ
# @Time: 2023/4/21 17:04
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from learn.wework.unlogin.register import Register


class Login:
    """
    登录的po
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_by_scan(self):
        """
        扫码登录的方法
        :return:
        """
        pass

    def go_to_register(self):
        """
        点击企业注册
        跳转到注册的po
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link')
        return Register(self.driver)
