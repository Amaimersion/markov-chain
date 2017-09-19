# !/usr/bin/python
# -*- coding: utf-8 -*-


import json


def read_json(path):
    """Read a json file."""
    with open(path, 'r', encoding="utf-8") as file:
        return json.load(file)
