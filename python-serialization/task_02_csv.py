#!/usr/bin/python3
"""Module reads data from CSV format and covnerts to JSON format
using serialization techniques."""


import json
import csv


def convert_csv_to_json(csv_filename):
    """Method converts csv file to JSON format."""

    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_list = list(csv_reader)

        with open('data.json', "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file)

        return True
    except Exception:
        return False
