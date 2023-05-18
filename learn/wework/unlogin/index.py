# -*- encoding: utf-8 -*-
# @ModuleName: index
# @Author: SZQ
# @Time: 2023/4/21 16:59

from selenium import webdriver
from selenium.webdriver.common.by import By

from learn.wework.unlogin.login import Login
from learn.wework.unlogin.register import Register


class Index:
    """
    未登录情况，首页的po
    """

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/')
        self.driver.implicitly_wait(3)

    def go_to_register(self):
        """
        点击注册
        跳转到注册页面的po
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Register(self.driver)

    def go_to_login(self):
        """
        点击登录
        跳转到登录页面的po
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Login(self.driver)
