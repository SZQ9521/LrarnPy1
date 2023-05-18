# -*- encoding: utf-8 -*-
# @ModuleName: base_api
# @Author: SZQ
# @Time: 2023/4/26 19:40
import requests


class BaseApi:
    def send(self, data):
        return requests.request(**data).json()
