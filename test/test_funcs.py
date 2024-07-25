"""Test Random Funcs"""


import unittest

from funcs import fibonnacci


class TestFuncs(unittest.TestCase):

    def test_fibonnaci_with_number(self):
        self.assertEqual(fibonnacci(5), 15)
        self.assertEqual(fibonnacci(6), 21)

    def test_fibonnacci_with_things(self):
        # self.assertRaises(ValueError, fibonnacci(0))
        # self.assertRaises(TypeError, fibonnacci('a23'))
        # self.assertRaises(ValueError, fibonnacci(-1))
        # self.assertRaises(OverflowError, fibonnacci(3e23))
        pass
