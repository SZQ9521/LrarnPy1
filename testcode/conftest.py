# -*- encoding: utf-8 -*-
# @ModuleName: conftest
# @Author: SZQ
# @Time: 2023/4/10 11:31
from typing import List
import pytest


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

# @pytest.fixture(scope='function', autouse=True)
# def open_close():
#     print('计算开始')
#     yield
#     print('计算结束')
