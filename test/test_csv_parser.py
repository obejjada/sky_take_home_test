import unittest
import sys
sys.path.append("C:\\Users\\omarb\\vscode-workspace\\sky_take_home_test")
from source.csv_parser import CSVParser
from pathlib import Path


resouce_path = Path.cwd()


class TestCSVParser(unittest.TestCase):
    """Unit test class that will verfiy the CSV parsing functions of the sky-take-home projects"""
    csv_parser = CSVParser()

    def setUp(self):
        """Method thar runs before each test method is run"""
        pass

    def tearDown(self):
        """Method that runs after each method has finished running"""
        pass

    def test_valid_csv(self):
        """Test method to validate the valid_csv method returns True when a CSV file path is given"""
        valid_csv_path = str(resouce_path) + r'\valid.csv'
        fail_msg = '%s is not a csv file', valid_csv_path
        self.assertTrue(self.csv_parser.valid_csv(valid_csv_path), fail_msg)

    def test_invalid_csv(self):
        """Test method to validate the valid_csv method returns False when a none CSV file path is given"""
        invalid_csv_path = str(resouce_path) + r'\invalid.txt'
        fail_msg = '%s is not a csv file', invalid_csv_path
        self.assertFalse(self.csv_parser.valid_csv(invalid_csv_path), fail_msg)

    def test_open_url(self):
        """Test method to validate the open_url method returns an HTTP status of 200 for a valid URL"""
        remote_url = 'http://www.fifeweather.co.uk/cowdenbeath/200606.csv'
        fail_msg = '%s has not opened', remote_url
        self.assertTrue(self.csv_parser.open_url(remote_url) == 200, fail_msg)

    def test_open_bad_url(self):
        """Test method to validate the open_url method returns an HTTP status of 404 for an invalid URL"""
        remote_url = 'http://www.fifeweather.co.uk/cowdenbeath/1.csv'
        fail_msg = '%s can not be found', remote_url
        self.assertTrue(self.csv_parser.open_url(remote_url) == 404, fail_msg)

if __name__ == "__main__":
    unittest.main()
