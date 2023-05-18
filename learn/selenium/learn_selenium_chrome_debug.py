# -*- encoding: utf-8 -*-
# @ModuleName: learn_selenium_chrome_debug
# @Author: SZQ
# @Time: 2023/4/20 16:35
# -*- encoding: utf-8 -*-
# @ModuleName: learn_selenium_bd_login_register
# @Author: SZQ
# @Time: 2023/4/18 12:52

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestBdLoginRegister:
    def setup(self):
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_login_register(self):
        self.driver.get('https://www.baidu.com/')
        print('打开百度了')
        self.driver.find_element(By.LINK_TEXT, '登录').click()
        self.driver.find_element(By.LINK_TEXT, '立即注册').click()

    def test_qi_ye_wx(self):
        self.driver.get('https://work.weixin.qq.com/')
        # print(self.driver.get_cookies())
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'a9767609'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'skey', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '@HgFobYxAu'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'uin', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'o819418372'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'true'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1688856518465958'}, {'domain': '.qq.com', 'expiry': 1715755886, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '2661177800'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1970325154991966'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '3302230640912556'}, {'domain': '.work.weixin.qq.com', 'expiry': 1713503712, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'tW3rMsHMFfY7H83TpKfj1X90u9snGNzgyhyimJLLGdDkQvuRHpaMpsHTrUU7BRb340NKnBItIcBZBupweHWzIw1wa6nYFoWi9rqoJ-WumUatMP_UZYA7Z5yQr8Fvtz06LX1yFifh8VTN0lTjECk4_1yXlOLSu6mVblftf84gKEH7Gjeg30I8X8EO2HCmV0GV-dURE8ObBxIYvd7mDnlaz7rod-xCmHHyPcKfeTRTh1XfPcF_vk0-7-C9q5Qhs530FAyBiUhI_pbJFUS2aBTH2g'}, {'domain': '.qq.com', 'httpOnly': False, 'name': '_qpsvr_localtk', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '0.3470466878250167'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'midas_openkey', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '@LvOynU4Es'}, {'domain': '.qq.com', 'expiry': 1711424085, 'httpOnly': False, 'name': '_clck', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'l19tp8|1|fa9|0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'midas_openid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '819418372'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'mN3TIRWCX2qFZZQ0QSqYgqlkGwmGKQ3rhfOEx4UxTBMk_K3xN2ZxctG0e5nijt4W'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'ssid=s9455660899'}, {'domain': '.work.weixin.qq.com', 'expiry': 1684646997, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1688856518465958'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'utm_platform', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'webv2_plat_PC'}, {'domain': '.qq.com', 'expiry': 1716562575, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1fe62a380c6627e0ba087debff2fd4fab9655eb32012db2c9dd6d78a4b6185da'}, {'domain': '.qq.com', 'expiry': 1713407699, 'httpOnly': False, 'name': 'RK', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'DfeAs4noXr'}]
        for cookie in cookies:
            # if 'expiry' in cookie.keys():
            #     cookie.pop('expiry')

            self.driver.add_cookie(cookie)

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')


