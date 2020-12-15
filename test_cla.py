#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from pythoncode.calculator import Calculator


class TestCalc():
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 8), (-1, -2, -3), (100, 300, 400)
    ], ids=["int", "minus", "bigint"])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)




    @pytest.mark.parametrize("a,b,expect", [
        (5, 3, 2), (-5, -2, -3), (300, 200, 100)], ids=["int", "minus", "bigint"])

    def test_sub(self,a,b,expect):
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (2, 5, 10),(2.5, 4, 10),(100, 200, 20000)],
                             ids=["int","minus","bigint"])
    def test_mul(self,a,b,expect):
        assert expect == self.calc.mul(a,b)


    @pytest.mark.parametrize("a,b,expect", [(10, 2, 5), (6.2, 2, 3.1), (2000, 20, 100)],
                             ids=['int', 'float', 'bigint'])

    def test_div(self,a,b,expect):
        assert  expect == self.calc.div(a,b)