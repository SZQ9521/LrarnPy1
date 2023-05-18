# -*- encoding: utf-8 -*-
# @ModuleName: learn_pytest_cha_jian_dependency 用例b依赖于用例a
# @Author: SZQ
# @Time: 2023/4/10 17:11
import pytest


@pytest.mark.dependency()
@pytest.mark.xfail(reason='fail_fail')
def test_a():
    print('case_a')
    assert False


@pytest.mark.dependency(depends=['test_a'])
def test_b():
    print('case_b')
    pass


# def test_c():
#     print('case_c')
#
#
# def test_d():
#     print('case_d')
