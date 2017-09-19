# !/usr/bin/python
# -*- coding: utf-8 -*-


import sys

# relative import.
sys.path.insert(0, "..")
from chain._main import MarkovChain

from common import functions


def basic_usage(text):
    """Basic usage example."""
    chain = MarkovChain("Simple test MarkovChain instance")
    chain.init(text)
    chain.create()
    print(chain.generate())


def instance_arguments(text):
    """Instance arguments example."""
    chain = MarkovChain("Hard test MarkovChain instance", window=2)
    chain.init(text)
    chain.create()
    print(chain.generate())


def generation_arguments(text):
    """Generation arguments example."""
    chain = MarkovChain("Insane test MarkovChain instance")
    chain.init(text)
    chain.create()
    print(chain.generate(start="You", max_words=10))


if __name__ == "__main__":
    text = functions.read_json("./common/text.json")

    basic_usage(text["text"]["simple"])
    instance_arguments(text["text"]["hard"])
    generation_arguments(text["text"]["insane"])
