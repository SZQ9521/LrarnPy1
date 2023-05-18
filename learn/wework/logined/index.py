# -*- encoding: utf-8 -*-
# @ModuleName: index
# @Author: SZQ
# @Time: 2023/4/21 18:13
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from learn.wework.logined.add_member import AddMember
from learn.wework.logined.base_page import BasePage


class Index(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def go_to_add_member(self):
        self.find_element(By.CSS_SELECTOR, '#_hmt_click > div.index_colLeft > div.index_service > div.index_service_cnt.js_service_list > a:nth-child(1) > div > span.index_service_cnt_item_title').click()
        return AddMember(self._driver)
