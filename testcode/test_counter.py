# -*- encoding: utf-8 -*-
# @ModuleName: test_counter 计算器的测试代码
# @Author: SZQ
# @Time: 2023/4/7 15:29
# 测试文件# 为了优化这个文件，可以考虑以下几点：

# 1. 将重复的代码封装成函数，减少代码冗余，提高代码复用性。
# 2. 将测试数据和测试步骤封装到一个文件中，方便管理和维护。
# 3. 使用 fixture 来管理测试数据，避免重复读取文件。
# 4. 使用参数化来简化测试用例的编写，提高代码可读性。

# 下面是优化后的代码：

import pytest
import yaml

from pycode.counter import Counter


class TestCounter:
    counter = Counter()

    '''
    这是Cursor生成的优化后的代码 目前报错 解决不了 学会了再看看因为啥
    # 获取测试步骤
    # 使用 fixture 来管理测试数据
    @pytest.fixture(params=['data_counter_add.yml', 'data_counter_subtract.yml', 'data_counter_multiply.yml', 'data_counter_divide.yml'])
    def get_data(self, request):
        with open(f'datas/{request.param}') as f:
            data = yaml.safe_load(f)
            print(data)
        return data['data']

    # 获取测试步骤
    def get_steps(self, filename):
        with open(f'steps/{filename}') as f:
            steps = yaml.safe_load(f)
        return steps

    # 执行测试步骤
    def use_steps(self, steps, one, two, result):
        for step in steps:
            assert result == getattr(self.counter, step)(one, two)

    # 测试加法、减法、乘法、除法
    @pytest.mark.parametrize('one, two, result', get_data, ids=['add', 'subtract', 'multiply', 'divide'])
    def test_counter(self, one, two, result, get_data):
        print(self.get_steps(f'step_counter_{get_data["operation"]}.yml'))
        steps = self.get_steps(f'step_counter_{get_data["operation"]}.yml')
        self.use_steps(steps, one, two, result)
    '''


class TestCounter:
    counter = Counter()

    # 获取测试加法的测试步骤
    def get_add_steps(self):
        with open('steps/step_counter_add.yml') as file_step_add:
            step_add = yaml.safe_load(file_step_add)
            # print(step_add)
        return step_add

    # 执行测试加法的测试步骤
    def use_add_steps(self, one, two, result):
        add_steps = self.get_add_steps()
        # print(f'-------------{add_steps}-----------')
        for step in add_steps:
            if step == 'add':
                assert result == self.counter.add(one, two)
            elif step == 'add2':
                assert result == self.counter.add2(one, two)
            elif step == 'add3':
                assert result == self.counter.add3(one, two)
            elif step == 'add4':
                assert result == self.counter.add4(one, two)

    # 获取测试减法的测试步骤
    def get_subtract_steps(self):
        with open('steps/step_counter_subtract.yml') as file_step_counter_subtract:
            step_counter_subtract = yaml.safe_load(file_step_counter_subtract)
            return step_counter_subtract

    # 使用测试减法的测试步骤
    def use_subtract_steps(self, one, two, result):
        subtract_steps = self.get_subtract_steps()
        for step in subtract_steps:
            if step == 'subtract':
                assert result == self.counter.subtract(one, two)

    # 获取测试乘法的测试步骤
    def get_multiply_steps(self):
        with open('steps/step_counter_multiply.yml') as file_step_counter_multiply:
            step_counter_multiply = yaml.safe_load(file_step_counter_multiply)
            return step_counter_multiply

    # 使用测试乘法的测试步骤
    def use_multiply_steps(self, one, two, result):
        multiply_steps = self.get_multiply_steps()
        for step in multiply_steps:
            if step == 'multiply':
                assert result == self.counter.multiply(one, two)

    # 获取测试除法的测试步骤
    def get_divide_steps(self):
        with open('steps/step_counter_divide.yml') as file_step_counter_divide:
            step_counter_divide = yaml.safe_load(file_step_counter_divide)
            return step_counter_divide

    # 使用测试除法的测试步骤
    def use_divide_steps(self, one, two, result):
        divide_steps = self.get_divide_steps()
        for step in divide_steps:
            if step == 'divide':
                assert result == self.counter.divide(one, two)

    # def setup(self):
    #     print('开始计算')
    #
    # def teardown(self):
    #     print('计算结束')
    # 获取测试加法的测试数据
    with open('datas/data_counter_add.yml') as file_data_counter_add:
        data_counter_add = yaml.safe_load(file_data_counter_add)

    # 获取测试减法的测试数据
    with open('datas/data_counter_subtract.yml') as file_data_counter_subtract:
        data_counter_subtract = yaml.safe_load(file_data_counter_subtract)

    # 获取测试乘法的测试数据
    with open('datas/data_counter_multiply.yml') as file_data_counter_multiply:
        data_counter_multiply = yaml.safe_load(file_data_counter_multiply)

    # 获取测试除法的测试数据
    with open('datas/data_counter_divide.yml') as file_data_counter_divide:
        data_counter_divide = yaml.safe_load(file_data_counter_divide)

    @pytest.mark.parametrize('one, two, result', data_counter_add)
    def test_add(self, one, two, result):
        self.use_add_steps(one, two, result)
        # assert result == self.counter.add(one, two)
        # assert result == self.counter.add2(one, two)
        # assert result == self.counter.add3(one, two)
        # assert result == self.counter.add4(one, two)

    @pytest.mark.parametrize('one, two, result', data_counter_subtract)
    def test_subtract(self, one, two, result):
        self.use_subtract_steps(one, two, result)

    @pytest.mark.parametrize(', one, two, result', data_counter_multiply, ids=['第一组', '第二组', '第三组'])
    def test_multiply(self, one, two, result):
        self.use_multiply_steps(one, two, result)

    @pytest.mark.parametrize('one, two, result', data_counter_divide)
    def test_divide(self, one, two, result):
        self.use_divide_steps(one, two, result)
