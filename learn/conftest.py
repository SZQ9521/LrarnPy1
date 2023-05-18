# -*- encoding: utf-8 -*-
# @ModuleName: conftest
# @Author: SZQ
# @Time: 2023/4/10 12:21

import pytest


@pytest.fixture()
def login(request):
    print('登录了')
    print(request.param)
