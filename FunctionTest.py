"""
@Project ：TrigonometricFunctions-main
@File ：Operation_test.py
@Author ：ZouXuan
@Date ：2021/6/30 14:14
"""

import unittest
from TriFunctions.arcsin import asin
from TriFunctions.arctan import atan
from TriFunctions.cos import cos
from TriFunctions.sin import sin


class TestFunc(unittest.TestCase):  # 测试类

    def __init__(self):
        # 标准值数据库
        arcsin_standard_values = {0: 0, 0.5: 30, 0.707: 45, 0.866: 60, 1: 90, -0.5: -30, -0.707: -45, -1: -90,
                                  -0.866: -60}
        arctan_standard_values = {0: 0, 0.577: 30, 1: 45, 1.732: 60, 0: 0, -0.577: -30, -1: -45, -1.732: -60}
        sin_standard_values = {0: 0, 30: 0.5, 60: 0.866, 90: 1, 120: 0.866, 180: 0, 270: -1, 360: 0,
                               -30: -0.5, -60: -0.866, -90: -1, -120: -0.866, -180: 0, -270: 1, -360: 0}
        cos_standard_values = {0: 1, 30: 0.866, 60: 0.5, 90: 0, 120: -0.5, 180: -1, 270: 0, 360: 1,
                               -30: 0.866, -60: 0.5, -90: 0, -120: -0.5, -180: -1, -270: 0, -360: 1}
        self.task_functions = {
            "sin": sin,
            "arcsin": asin,
            "cos": cos,
            "arctan": atan,
        }
        self.task_datas = {
            "sin": sin_standard_values,
            "cos": cos_standard_values,
            "arcsin": arcsin_standard_values,
            "arctan": arctan_standard_values
        }

    def test_value(self, task, value):
        try:
            standard_value = float(self.task_datas[task][value])  # 获取输入值的标准结果
            compute_value = self.task_functions[task](value)  # 获取输入值的函数计算结果
            return standard_value == compute_value
        except Exception as e:
            print(e)
            return "该输入值不进行测试"

    def test_arcsin(self):  # 测试arcsin函数
        self.assertEqual(0, asin(0))
        self.assertEqual(30, asin(0.5))
        self.assertEqual(45, asin(0.7071))
        self.assertEqual(60, asin(0.8660))
        self.assertEqual(90, asin(1))
        self.assertEqual(-30, asin(-0.5))
        self.assertEqual(-45, asin(-0.7071))
        self.assertEqual(-90, asin(-1))
        self.assertEqual(-60, asin(-0.8660))

    def test_arctan(self):  # 测试arctan函数
        self.assertEqual(0, atan(0))
        self.assertEqual(30, atan(0.5773))
        self.assertEqual(45, atan(1))
        self.assertEqual(60, atan(1.732))
        self.assertEqual(0, atan(0))
        self.assertEqual(-30, atan(-0.5773))
        self.assertEqual(-45, atan(-1))
        self.assertEqual(-60, atan(-1.732))

    def test_cos(self):  # 测试cos函数
        self.assertEqual(1, cos(0))
        self.assertEqual(0.866, cos(30))
        self.assertEqual(0.5, cos(60))
        self.assertEqual(0, cos(90))
        self.assertEqual(-0.5, cos(120))
        self.assertEqual(-1, cos(180))
        self.assertEqual(0, cos(270))
        self.assertEqual(1, cos(360))
        self.assertEqual(0.866, cos(-30))
        self.assertEqual(0.5, cos(-60))
        self.assertEqual(0, cos(-90))
        self.assertEqual(-0.5, cos(-120))
        self.assertEqual(-1, cos(-180))
        self.assertEqual(0, cos(-270))
        self.assertEqual(1, cos(-360))

    def test_sin(self):  # 测试sin函数
        self.assertEqual(0, sin(0))
        self.assertEqual(0.5, sin(30))
        self.assertEqual(0.866, sin(60))
        self.assertEqual(1, sin(90))
        self.assertEqual(0.866, sin(120))
        self.assertEqual(0, sin(180))
        self.assertEqual(-1, sin(270))
        self.assertEqual(0, sin(360))
        self.assertEqual(-0.5, sin(-30))
        self.assertEqual(-0.866, sin(-60))
        self.assertEqual(-1, sin(-90))
        self.assertEqual(-0.866, sin(-120))
        self.assertEqual(0, sin(-180))
        self.assertEqual(1, sin(-270))
        self.assertEqual(0, sin(-360))


if __name__ == '__main__':
    unittest.main()
