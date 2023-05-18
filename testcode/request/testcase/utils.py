# -*- encoding: utf-8 -*-
# @ModuleName: utils
# @Author: SZQ
# @Time: 2023/4/26 18:25
import requests


class Utils:
    def get_access_token(self):
        corp_id = 'ww3de68e188a4b0eba'
        secret_tong_xun_lu = '3VUohJVzTI7NoNGirux0oo9pDlFBrvsuRtThvaVcFJ8'

        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={secret_tong_xun_lu}'
        r = requests.get(url)
        print(f'--------------------{r.json()}')
        return r.json()['access_token']
