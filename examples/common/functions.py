# !/usr/bin/python
# -*- coding: utf-8 -*-


import json


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
    generation(chain, text, **generation_parameters)
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


def read_json(path):
    """Read a json file."""
    with open(path, 'r', encoding="utf-8") as file:
        return json.load(file)
