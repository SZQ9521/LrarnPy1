# -*- encoding: utf-8 -*-
# @ModuleName: test_requests
# @Author: SZQ
# @Time: 2023/4/25 15:30
import csv
import json
import random

import pytest
import requests
import jsonpath
from hamcrest import *


def test_make_data():
    data = [(('nibaba' + str(x)), '你爸爸', ('188%08d' % x)) for x in range(10)]
    return data


class TestWeWork:
    corp_id = 'ww3de68e188a4b0eba'
    secret_tong_xun_lu = '3VUohJVzTI7NoNGirux0oo9pDlFBrvsuRtThvaVcFJ8'

    @pytest.fixture()
    def get_access_token(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corp_id}&corpsecret={self.secret_tong_xun_lu}'
        r = requests.get(url)
        assert_that(r.status_code, equal_to(200))
        print(f'--------------------{r.json()}')
        return r.json()['access_token']

    def test_add_member(self, get_access_token, userid, name, mobile):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_access_token}'
        # print(f'这是URL{url}')
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": 1
        }
        r = requests.post(url, json=data)
        print(r.json())
        # errmsg = r.json()['errmsg']
        # assert_that(errmsg, equal_to('created'))

    def test_read_member(self, get_access_token, userid):

        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/list_id?access_token={get_access_token}'
        r = requests.get(url)
        print(r.content)
        user_list = r.json()['dept_user']

        # 查找用户列表里有没有王五
        for user in user_list:
            if user['userid'] == userid:
                print('---这个人存在---')
                return True

        print('---这个人不存在---')
        return False

    def test_update_member(self, get_access_token):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_access_token}'

        request_body = {
            "userid": "chengyaojib",
            "name": "半路杀出来一个程咬金",
            "mobile": "16600000006",
            "department": 1
        }

        r = requests.post(url, json=request_body)
        print(r.json())

    def test_delete_member(self, get_access_token, userid):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_access_token}&userid={userid}'
        r = requests.get(url)
        print(r.json())

    @pytest.mark.parametrize('userid, name, mobile', test_make_data())
    def test_all(self, get_access_token, userid, name, mobile):
        # 0、准备添加，设置一下准备添加的用户信息
        # userid = 'woshinibaba'
        # name = '我是你爸爸啊'
        # mobile = '18888886666'

        # 1、添加用户之前查一下有没有这个用户，如果有，删了
        if self.test_read_member(get_access_token, userid):
            self.test_delete_member(get_access_token, userid)

        # 2、添加用户
        self.test_add_member(get_access_token, userid, name, mobile)
        # 3、添加完查一下用户列表里有没有新添加的用户，如果有，才说明添加成果了
        self.test_read_member(get_access_token, userid)

        # 4、把刚才添加的用户删了
        self.test_delete_member(get_access_token, userid)


class TestRequests:
    def test_requests(self):
        headers = {
            'Cookie': 'JSESSIONID=ECA6A5A674A0DF233728D484774082EC'
        }

        param = {'start': '0', 'length': '10', 'mobile': '16600000000', 'moduleId': '798731860393201664',
                 'registerStartTime': '', 'registerEndTime': '', 'userId': '', 'status': '', 'osType': '',
                 'channel': '', 'sex': ''}
        r = requests.post('http://test.admin.dtgas.my-dt.com/dtadmin/user/getUserPage.do', data=param, headers=headers)
        # print(r.status_code)
        # print(r.request.headers)

        # json.dumps把r.json()的内容转换成json格式
        # ensure_ascii=False解决了打印出来中文乱码的问题
        response = json.dumps(r.json(), ensure_ascii=False)
        response1 = r.content
        print(response)
        print(response1)


def read_csv_file(file_path):
    data = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)  # 读取CSV文件的列标题
        for row in reader:
            data.append(row)  # 将每一行数据添加到列表中
    return headers, data


def test_1():
    file_path = 'test_data.txt'
    headers, data = read_csv_file(file_path)

    print("Headers:", headers)
    print("Data:")
    for row in data:
        print(row)
