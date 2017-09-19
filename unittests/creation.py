# !/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
from common import test


class SimpleOneWindowTest(test.CreationTest, unittest.TestCase):

    window = 1
    text_name = "simple_text"
    chain_window = '1'


class SimpleTwoWindowTest(test.CreationTest, unittest.TestCase):

    window = 2
    text_name = "simple_text"
    chain_window = '2'


class SimpleThreeWindowTest(test.CreationTest, unittest.TestCase):

    window = 3
    text_name = "simple_text"
    chain_window = '3'


class ExtraOneWindowTest(test.CreationTest, unittest.TestCase):

    window = 1
    text_name = "extra_text"
    chain_window = '1'


class ExtraTwoWindowTest(test.CreationTest, unittest.TestCase):

    window = 1
    text_name = "extra_text"
    chain_window = '1'


class ExtraThreeWindowTest(test.CreationTest, unittest.TestCase):

    window = 1
    text_name = "extra_text"
    chain_window = '1'


if __name__ == "__main__":
    unittest.main()
