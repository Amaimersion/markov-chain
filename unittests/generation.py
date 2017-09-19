# !/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
from common import test


class SimpleOneWindowTest(test.GenerationTest, unittest.TestCase):

    text_name = "simple_text"
    chain_window = '1'


class SimpleTwoWindowTest(test.GenerationTest, unittest.TestCase):

    text_name = "simple_text"
    chain_window = '2'


class SimpleThreeWindowTest(test.GenerationTest, unittest.TestCase):

    text_name = "simple_text"
    chain_window = '3'


class ExtraOneWindowTest(test.GenerationTest, unittest.TestCase):

    text_name = "extra_text"
    chain_window = '1'


class ExtraTwoWindowTest(test.GenerationTest, unittest.TestCase):

    text_name = "extra_text"
    chain_window = '2'


class ExtraThreeWindowTest(test.GenerationTest, unittest.TestCase):

    text_name = "extra_text"
    chain_window = '3'


if __name__ == "__main__":
    unittest.main()
