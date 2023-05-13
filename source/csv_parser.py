import csv
import sqlite3
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
        data = list(csv.reader(lines))
        return data

    def import_data_to_sql(self, data):
        """This method imports the data from the CSV into a SQLite3 databse which will be used for data calculations"""
        connection = sqlite3.connect('weather_data.db')
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS weather_data(
            Date text,
            Time text,
            Temp_Humidity_Index text,
            Outside_Temperature text,
            WindChill text,
            Hi_Temperature text,
            Low_Temperature text,
            Outside_Humidity text,
            DewPoint text,
            WindSpeed text,
            Hi text,
            Wind_Direction text,
            Rain text,
            Barometer text,
            Inside_Temperature text,
            Inside_Humidity text,
            ArchivePeriod text)""")
        connection.commit()

        for row in data:
            cursor.execute("insert into weather_data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            (row[0], row[1], row[1], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                row[10], row[11], row[12], row[13], row[14], row[15], row[16]))
        connection.commit()
        connection.close()
