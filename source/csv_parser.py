import csv
from urllib import request, error
from pathlib import Path
import logging


class CSVParser():
    """Class that parses the inputed CSV file and calculates the necessary data"""

    def valid_csv(self, file_path):
        """Method to validate whether the input file is a CSV file or not"""
        if Path(file_path).suffix == '.csv':
            return True
        else:
            return False

    def open_url(self, url_path):
        """Method to open the remote URL path given"""
        try:
            response = request.urlopen(url_path)
            return response
        except error.HTTPError as e:
            return e

    def parse_csv(self, csv_object):
        """Method to parse the csv file and return the contents in a list"""
        lines = [l.decode('utf-8') for l in csv_object]
        data = list(csv.DictReader(lines))
        return data
