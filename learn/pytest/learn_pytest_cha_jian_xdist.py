# -*- encoding: utf-8 -*-
# @ModuleName: learn_pytest_cha_jian_xdist 多线程并行与分布式执行
# @Author: SZQ
# @Time: 2023/4/10 19:12
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