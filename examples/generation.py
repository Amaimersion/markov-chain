# !/usr/bin/python
# -*- coding: utf-8 -*-


import sys

# relative import.
sys.path.insert(0, "..")
from chain._main import MarkovChain

from common import functions


def main():
    """Execute examples."""
    text = functions.read_json("./common/text.json")

    start_example("correct parameters", "correct_parameters", text)
    start_example("incorrect parameters", "incorrect_parameters", text)


def start_example(parameters_name, parameters_json, text):
    """Execute all parameters examples."""
    if parameters_json in text:
        print("The following examples show a %s." % parameters_name, '\n')

        for parameters_instance in text[parameters_json]:
            text_name = parameters_instance["text"]
            text_instance = text["text"][text_name]
            start_generation(text_instance, parameters_instance)


def start_generation(text_instance, parameters_instance):
    """Start generation of one parameter example."""
    markov_chain = MarkovChain(
        **parameters_instance.get("parameters", {}).get("init", {})
    )

    functions.start(
        chain=markov_chain, 
        text=text_instance, 
        parameters=parameters_instance.get("parameters", {})
    )
    print('\n')


if __name__ == "__main__":
    main()
