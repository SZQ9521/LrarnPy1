# -*- encoding: utf-8 -*-
# @ModuleName: test_wework
# @Author: SZQ
# @Time: 2023/4/26 18:10
import json

import requests

from testcode.request.api.wework import WeWork
from testcode.request.testcase.utils import Utils


class TestWeWork:
    # we_work = WeWork()

    def test_add_member(self):
        print(WeWork().add_member(userid='lisilisi', name='又一个李四', mobile='16600000055'))

    def test_delete_member(self):
        print(WeWork().delete_member(userid='lisilisi'))

    def test_read_member(self):
        response = WeWork().read_member()
        print(json.dumps(response))

    def test_update_member(self):
        print(WeWork().update_member('37872', '你大爷（改）', '16600000011'))

    def test_session(self):
        """
        把access_token放到session里，请求的时候自动传
        :return:
        """
        s = requests.session()
        s.params = {'access_token': Utils().get_access_token()}
        r = s.get('https://qyapi.weixin.qq.com/cgi-bin/user/list_id')
        print(r.json())
