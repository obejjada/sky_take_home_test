import csv
import sqlite3
import datetime
from urllib import request, error
from pathlib import Path
import logging


class CSVParser():
    """Class that parses the inputed CSV file and calculates the necessary data"""

    def valid_csv(self, file_path):
        """Method to validate whether the input file is a CSV file or not"""
        if Path(file_path).suffix == '.csv':
            #  return true if the extension is valid .csv
            return True
        else:
            # return can be used to flag to user that the file they have inputed does not have a .csv extension 
            return False

    def open_url(self, url_path):
        """Method to open the remote URL path given"""
        try:
            response = request.urlopen(url_path)
            #  response return allows this function to be used for more than returning
            #  http status
            return response
        except error.HTTPError as e:
            #  If unable to open the given url, return the http error staus
            return e

    def parse_csv(self, csv_object):
        """Method to parse the csv file and return the contents in a list"""
        #  Decode the url and make a list which will be used to parse the data into a database
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
            Outside_Temperature real,
            WindChill text,
            Hi_Temperature real,
            Low_Temperature real,
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

        for row in data[1:(len(data)-1)]:
            cursor.execute("insert into weather_data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                           (row[0], row[1], row[1], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                            row[10], row[11], row[12], row[13], row[14], row[15], row[16]))
        connection.commit()
        connection.close()

    def average_time_hottest_temp(self, database_path):
        """Method to calculate the average time of the hotest daily temperature over the month"""

        connection = sqlite3.connect('weather_data.db')
        cursor = connection.cursor()
        # SQL query returns the Date and Time of the Max outside temperature,for each unique date
        cursor.execute("SELECT Date,Time, MAX(Outside_Temperature) FROM weather_data GROUP BY Date")
        rows = cursor.fetchall()
        connection.close()
        # Iterate through each Date for the Time the Max outside temperature occured
        total_time = 0
        for row in rows:
            temp_time = row[1].split(':')  # Split string format of time in a new varable to allow multiplication
            time_to_seconds = (int(temp_time[0]) * 3600) + (int(temp_time[1]) * 60)  # Multiple by 3600 for hours to seconds and Multiple by 60 for mins to seconds
            total_time += time_to_seconds
        # Average time is calculated by summing how many hours from 00:00 have elapased before dividing by the number of days and re-convert back into a 24Hr format
        average_time = str(datetime.timedelta(seconds=total_time/len(rows)))
        return average_time

    def common_time_hotest(self, database_path):
        """Method to calculate the most common time the hottest time of the day occurs"""
        connection = sqlite3.connect('weather_data.db')
        cursor = connection.cursor()
        # SQL query returns the time the maximum temperature occured for the month
        cursor.execute("SELECT Time, MAX(Outside_Temperature) FROM weather_data GROUP BY Date")
        rows = cursor.fetchall()
        connection.close()

        remove_duplicates_time = set()
        time_list = []
        max_count = 0
        for row in rows:
            remove_duplicates_time.add(row[0])  # Creating set will remove duplicates which can be looped through rows to count the time with the most matches
            time_list.append(row[0])  # This list will allow looping through the times and not the temperatures
        for i in remove_duplicates_time:
            if time_list.count(i) > max_count:  # If the number of occurances of i is greater than the last max count, then update the max
                max_time = i
                max_count = time_list.count(i)

        return max_time

    def top_ten_temps(self, database_path):
        """Method to calculate the top ten hottest times on distinct days"""
        connection = sqlite3.connect('weather_data.db')
        cursor = connection.cursor()
        # SQL query returns a list of Date, Time and outside temperatures sorted descending order of outside temperatures 
        cursor.execute("""SELECT Date,Time, MAX(Outside_Temperature)
                        FROM weather_data
                        GROUP BY Date
                        ORDER BY
                        Outside_temperature DESC""")
        rows = cursor.fetchall()
        connection.close()
        top_ten_temps = []
        for row in rows[0:10]:
            top_ten_temps.append(row)
        return top_ten_temps

    def hi_low_temps(self, database_path):
        """Method to calculate the outside where the Hi Temperature is +- 1 degree of 22.3 or
        the Low Temperature is +- 0.2 degrees of 10.3 for the first 9 days of June"""

        connection = sqlite3.connect('weather_data.db')
        cursor = connection.cursor()
        # SQL query returns Date, Time and and Hi temperature where the Hi Temperature is +- 1 degree of 22.3
        cursor.execute("""SELECT Date,Time, Hi_Temperature
                        FROM weather_data
                        WHERE Hi_Temperature BETWEEN 21.3 AND 23.3
                        """)
        results_1_degree = cursor.fetchall()
        connection.close()

        connection = sqlite3.connect('weather_data.db')
        cursor = connection.cursor()
        # SQL query returns Date, Time and and Lo temperature where the Low Temperature is +- 0.2 degrees from 10.3 in the first 9 days of June
        cursor.execute("""SELECT Date,Time, Low_Temperature
                        FROM weather_data
                        WHERE Low_Temperature BETWEEN 10.1 AND 10.5""")
        nine_june = cursor.fetchall()
        connection.close()
        one_to_nine_june = ['01/06/2006', '02/06/2006', '03/06/2006',
                            '04/06/2006', '05/06/2006', '06/06/2006',
                            '07/06/2006', '08/06/2006', '09/06/2006']
        results_nine_june = []
        for row in nine_june:
            if row[0] in one_to_nine_june:
                results_nine_june.append(row)
        return results_1_degree, results_nine_june

    def forecast_july(self, database_path):
        """Method to forecast the weather for July"""
        connection = sqlite3.connect('weather_data.db')
        cursor = connection.cursor()
        average_list = []
        july_average = float(25)
        july_forecast = []
        for i in range(10):
            # SQL query returns
            sql_query = ("""SELECT Date,Time, Outside_Temperature FROM weather_data WHERE Date = '0%s/06/2006'""" % i)
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            total = 0
            for i in rows:
                total += float(i[2])
            if len(rows) > 0:
                average = total / len(rows)
                average_list.append(average)
            for i in rows:
                perctage_change = ((float(i[2]) - average)/average)
                month = str(i[0])
                before = month[0:4]
                after = month[5:10]
                merge = str(before) + '7' + str(after)
                if perctage_change > 0:
                    july_new_value = july_average * (1 + abs(perctage_change))
                    print_tup = (str(merge), str(i[1]), str(july_new_value))
                    july_forecast.append(print_tup)
                if perctage_change < 0:
                    july_new_value = july_average * (1 - abs(perctage_change))
                    print_tup = (str(merge), str(i[1]), str(july_new_value))
                    july_forecast.append(print_tup)

        connection.close()
        return july_forecast
