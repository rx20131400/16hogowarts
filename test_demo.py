#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
class Test_demo():

    def test_one(self):
        a = 5
        b = 1

        assert a != b

        print("这是我第一个测试用例")


    def add_function(a,b):
        return a + b

@pytest.mark.parametrize("a",[0,1])
@pytest.mark.parametrize("b",[2,4])

def test_add(a,b):
        print("测试数据组合： a > %s, b > %s"%(a,b))


