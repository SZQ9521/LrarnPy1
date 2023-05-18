# -*- encoding: utf-8 -*-
# @ModuleName: add_member
# @Author: SZQ
# @Time: 2023/4/21 18:13
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from learn.wework.logined.base_page import BasePage


class AddMember(BasePage):


    def add_member(self):
        self.find_element(By.CSS_SELECTOR, '#username').send_keys('李四1')
        self.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys('li_si1')
        self.find_element(By.CSS_SELECTOR, '#memberAdd_biz_mail').send_keys('li_si1')
        self.find_element(By.CSS_SELECTOR, '#memberAdd_phone').send_keys('16600000001')
        self.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        return True
