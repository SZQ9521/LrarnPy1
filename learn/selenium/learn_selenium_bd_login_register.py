# -*- encoding: utf-8 -*-
# @ModuleName: learn_selenium_bd_login_register
# @Author: SZQ
# @Time: 2023/4/18 12:52
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestBdLoginRegister:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    # def teardown(self):
    #     self.driver.quit()
    # def get_ele_time(self, driver, times, fun):
    #     return WebDriverWait(driver, times).until(fun)

    def test_login_register(self):
        self.driver.find_element(By.LINK_TEXT, '登录').click()

        self.driver.find_element(By.LINK_TEXT, '立即注册').click()

        # 获取所有窗口
        windows = self.driver.window_handles
        # 切换到第二个窗口
        self.driver.switch_to.window(windows[1])

        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__userName').send_keys('username')
