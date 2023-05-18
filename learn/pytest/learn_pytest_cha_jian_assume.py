# -*- encoding: utf-8 -*-
# @ModuleName: learn_pytest_cha_jian_assume 多条断言 有失败的也继续执行
# @Author: SZQ
# @Time: 2023/4/10 15:56

import pytest
import pytest_assume


def test_assume():
    pytest.assume(1 == 2)
    pytest.assume(1 == 1)
    pytest.assume(1 == 5)
