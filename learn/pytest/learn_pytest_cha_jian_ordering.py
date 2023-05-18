# -*- encoding: utf-8 -*-
# @ModuleName: learn_pytest_cha_jian_ordering
# @Author: SZQ
# @Time: 2023/4/10 16:09
import pytest


@pytest.mark.run(order=3)
def test_case1():
    print('第三条执行')


@pytest.mark.run(order=3)
def test_case2():
    print('第一条执行')


@pytest.mark.run(order=3)
def test_case3():
    print('第二条执行')
