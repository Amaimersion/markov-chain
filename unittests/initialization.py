# !/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
from common import test


class SimpleTest(test.InitializationTest, unittest.TestCase):

    text_name = "simple_text"


class ExtraTest(test.InitializationTest, unittest.TestCase):

    text_name = "extra_text"


if __name__ == "__main__":
    unittest.main()
