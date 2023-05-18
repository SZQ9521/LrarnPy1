# -*- encoding: utf-8 -*-
# @ModuleName: learn_yield
# @Author: SZQ
# @Time: 2023/4/10 11:46

def fun():
    for i in range(3):
        print(f'i = {i}')
        yield
        print('end')


f = fun()
next(f)
next(f)
# next(f)
