# -*- encoding: utf-8 -*-
# @ModuleName: web_driver_manager
# @Author: SZQ
# @Time: 2023/4/17 15:02
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    ChromeDriverManager(
        url="https://registry.npmmirror.com/-/binary/chromedriver",
        latest_release_url="https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE",
        cache_valid_range=365).install(),
    options=None)
