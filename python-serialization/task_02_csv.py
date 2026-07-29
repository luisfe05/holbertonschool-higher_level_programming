#!/usr/bin/python3
"""
Module to convert CSV data to JSON format using serialization.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to JSON format and writes to data.json.

    Args:
        csv_filename (str): Name of the CSV file to read.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_f:
            reader = csv.DictReader(csv_f)
            data = list(reader)

        with open('data.json', 'w', encoding='utf-8') as json_f:
            json.dump(data, json_f, indent=4)

        return True
    except Exception:
        return False
