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
        """Test method to validate the valid_csv method executes as expected"""
        valid_csv_path = str(resouce_path) + r'\valid.csv'
        fail_msg = '%s does not exist', valid_csv_path
        self.assertTrue(self.csv_parser.valid_csv(valid_csv_path), fail_msg)


if __name__ == "__main__":
    unittest.main()
