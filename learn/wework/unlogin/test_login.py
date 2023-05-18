# -*- encoding: utf-8 -*-
# @ModuleName: test_login
# @Author: SZQ
# @Time: 2023/4/21 17:42
from learn.wework.unlogin.index import Index


class TestLogin:

    def test_register(self):
        index = Index()
        result = index.go_to_register().register()
        assert result
