# -*- encoding: utf-8 -*-
# @ModuleName: wework
# @Author: SZQ
# @Time: 2023/4/26 18:06
import requests

from testcode.request.testcase.base_api import BaseApi
from testcode.request.testcase.utils import Utils


class WeWork(BaseApi):
    def __init__(self):
        # utils = Utils()
        self.access_token = Utils().get_access_token()
        print(f'----aaa------{self.access_token}')


    def add_member(self, userid, name, mobile):
        # print(f'这是token{self.access_token}')
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.access_token}'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": 1
        }
        # r = requests.post(url, json=data)
        # print(r.json())
        # errmsg = r.json()['errmsg']
        # assert_that(errmsg, equal_to('created'))
        send_data = {
            'method': 'post',
            'url': url,
            'json': data
        }

        return self.send(send_data)

    def read_member(self):

        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/list_id?access_token={self.access_token}'

        send_data = {
            'method': 'get',
            'url': url
        }

        r = self.send(send_data)
        # r = requests.get(url)
        print(type(r))
        return r

        # 查找用户列表里有没有王五
        # for user in user_list:
        #     if user['userid'] == userid:
        #         print('---这个人存在---')
        #         return True
        #
        # print('---这个人不存在---')
        # return False

    def update_member(self, userid, name, mobile):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.access_token}'

        body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": 1
        }
        send_data = {
            'method': 'post',
            'url': url,
            'json': body
        }
        return self.send(send_data)


    def delete_member(self, userid):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.access_token}&userid={userid}'
        r = requests.get(url)
        print(r.json())
