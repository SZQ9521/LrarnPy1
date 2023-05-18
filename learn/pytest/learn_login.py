# -*- encoding: utf-8 -*-
# @ModuleName: learn_login
# @Author: SZQ
# @Time: 2023/4/10 12:18
import pytest


# def test_case1(login):
#     print('case1')
#
#
# def test_case2():
#     print('case2')

#


@pytest.mark.parametrize('login', [
    ('username', 'password'),
    ('username1', 'password1')
], indirect=True)
def test_case3(login):
    print('case3')


def learn_a():
    print('learn')
