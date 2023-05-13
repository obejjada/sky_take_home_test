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
            return response.status
        except error.HTTPError as e:
            return e.status
