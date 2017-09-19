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

    start(
        chain=markov_chain, 
        text=text_instance, 
        parameters=parameters_instance.get("parameters", {})
    )
    print('\n')


def start(**kwargs):
    """Start of generation.
    
    Args:
        **chain (MarkovChain instance)

        **text (list):
            text for MarkovChain init.

        **parameters (dict):
            parameters for generation.
    """
    chain = kwargs.get("chain", None)
    text = kwargs.get("text", None)
    parameters = kwargs.get("parameters", {})

    if not chain:
        raise ValueError("MarkovChain instance is required")

    if not text:
        raise ValueError("text is required")

    symbol_parameters = parameters.get("symbol", {})
    start_parameters = {
        "name": parameters.get("name", "undefined"),
        "parameters": (
            '\n'
            + "__init__: "+ str(parameters.get("init", "default"))
            + '\n'
            + "generate(): " + str(parameters.get("generation", "default"))
        )
    }
    generation_parameters = parameters.get("generation", {})

    print(
        symbol_text(**symbol_parameters)
        + '\n'
        + start_text(**start_parameters)
        + '\n'
    )
    generation(chain, text=text, **generation_parameters)
    print(
        symbol_text(**symbol_parameters)
    )


def symbol_text(**kwargs):
    """Return a string of symbols."""
    symbol = kwargs.get("symbol", '=')
    symbol_count = kwargs.get("symbol_count", 50)

    return symbol * symbol_count


def start_text(**kwargs):
    """Return a start text."""
    name = kwargs.get("name", "undefined")
    parameters = kwargs.get("parameters", "undefined")

    message = (
        "Start of generation: {name}"
        + '\n'
        + "Parameters: {parameters}"
    ).format(
        name=name,
        parameters=parameters
    )

    return message


def generation(chain, init=True, **kwargs):
    """Generation."""

    if init:
        chain.init(kwargs.get("text", []))
        chain.create()

    while True:
        answer = input("Generate? (y/n): ").lower()

        if answer == 'y':
            print(chain.generate(**kwargs), '\n')
        else:
            break


if __name__ == "__main__":
    main()
