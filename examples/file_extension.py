# !/usr/bin/python
# -*- coding: utf-8 -*-


import sys

# relative import.
sys.path.insert(0, "..")
from chain._main import MarkovChain
from extensions import file

from common import functions


def main():
    """Execute examples."""
    text = functions.read_json("./common/text.json")

    markov_chain = MarkovChain()
    markov_chain.init(text["text"]["simple"])
    markov_chain.create()

    file.json.save(markov_chain.chain, "./common/simple_example.json")
    file.pickle.save(markov_chain.chain, "./common/simple_example.pickle")
    file.sqlite.save(markov_chain.chain, "./common/simple_example.sqlite")

    markov_chain.chain = file.json.read("./common/simple_example.json")
    markov_chain.chain = file.pickle.read("./common/simple_example.pickle")
    # markov_chain.generate()
    markov_chain_sqlite = file.SQLiteFile(path=".common/simple_example.sqlite")
    # markov_chain_sqlite.generate()


if __name__ == "__main__":
    main()
