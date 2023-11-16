#!/usr/bin/python3
"""
Formats response object in json form
"""

import json


def format():
    """
    Format json string
    """
    filename = '0-index.html'
    with open(filename, 'r') as f:
        data_json = json.load(f)
    with open(filename, 'w') as f:
        json.dump(data_json, f, indent=4)

if __name__ == "__main__":
    format()