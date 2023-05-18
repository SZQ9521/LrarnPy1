# -*- encoding: utf-8 -*-
# @ModuleName: test_add_member
# @Author: SZQ
# @Time: 2023/4/21 18:29
from learn.wework.logined.index import Index


class TestAddMember:

    def test_add_member(self):
        self.index = Index()
        result = self.index.go_to_add_member().add_member()
        assert result
