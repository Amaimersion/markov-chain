# !/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import json

# relative import.
sys.path.insert(0, "..")
from chain._main import MarkovChain


class InitializationTest(object):
    """Test for init() method."""

    @classmethod
    def setUpClass(self):
        with open("./common/_data.json", 'r', encoding="utf-8") as file:
            self._DATA = json.load(file)

        # get a data from the json file.
        self._text = self._DATA[self.text_name]["text"]
        self._correct_data = self._DATA[self.text_name]["data"]

        # create a MarkovChain instance for testing.
        self.chain = MarkovChain()
        self.chain.init(self._text)

    def test_init_method(self):
        self.assertEqual(list(self.chain._data), self._correct_data, "_data is not correct")


class CreationTest(object):
    """Test for create() method."""

    @classmethod
    def setUpClass(self):
        with open("./common/_data.json", 'r', encoding="utf-8") as file:
            self._DATA = json.load(file)

        # get a data from the json file.
        self._text = self._DATA[self.text_name]["text"]
        self._correct_chain = self._DATA[self.text_name]["chain"][self.chain_window]

        # create a MarkovChain instance for testing.
        self.chain = MarkovChain(window=self.window)
        self.chain.init(self._text)
        self.chain.create()

    def test_create_method(self):
        self.assertEqual(self.chain._chain, self._correct_chain, "_chain is not correct")


class GenerationTest(object):
    """Test for generate() method."""

    @classmethod
    def setUpClass(self):
        with open("./common/_data.json", 'r', encoding="utf-8") as file:
            self._DATA = json.load(file)

        # create a MarkovChain instance for testing.
        self.chain = MarkovChain()
        self.chain._chain = self._DATA[self.text_name]["chain"][self.chain_window]

        # create a generate() parameters.
        self.max_words = 20 # default.
        self.max_length = self.max_words * 10 # default.

        # create a test parameters.
        self.number_of_tests = 50

    def test_empty_text(self):
        generated_text = self.chain.generate(max_words=self.max_words, max_length=self.max_length)
        self.assertNotEqual(generated_text, '', "The text with the default data cannot be an empty")

    def test_type_text(self):
        generated_text = self.chain.generate(max_words=self.max_words, max_length=self.max_length)
        self.assertIsInstance(generated_text, str, "The text should have a str type")

    def test_words_length(self):
        # self.subTest not needed here.
        # if first failure, then a chain already incorrect.
        for i in range(self.number_of_tests):
            generated_text = self.chain.generate(max_words=self.max_words, max_length=self.max_length)
            self.assertTrue(len(generated_text.split()) <= self.max_words, "A count of words in the text cannot be > max_words")

    def test_length_text(self):
        # self.subTest not needed here.
        # if first failure, then a chain already incorrect.
        for i in range(self.number_of_tests):
            generated_text = self.chain.generate(max_words=self.max_words, max_length=self.max_length)
            self.assertTrue(len(generated_text) <= self.max_length, "A length of the text cannot be > max_length")
