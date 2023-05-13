import csv_parser
import interface
import sys, os
sys.path.append("C:\\Users\\omarb\\vscode-workspace\\sky_take_home_test")


class SkyTakeHome():
    """Main class for the Sky take home test"""
    interface = interface.user_interface()
    csv_parser = csv_parser.CSVParser()

    def main(self):
        """"Method that is called from the command line"""
        self.interface.welcome_message()
        csv_url = input('Please enter URL of .csv file\n')
        try:
            self.csv_parser.valid_csv(csv_url)            
        except Exception as e:
            print(e)

        try:
            data_object = self.csv_parser.parse_csv(self.csv_parser.open_url(csv_url))
            self.csv_parser.import_data_to_sql(data_object)
        except Exception as e:
            print(e)
        output_file_loc = input('Please enter path of where to save output files\n')
        try:
            self.interface.write_q_one_a_file(self.csv_parser.average_time_hottest_temp(str(os.getcwd()) + r'\weather_data.db'), output_file_loc)
        except Exception as e:
            print(e)
        try:
            print(self.csv_parser.common_time_hotest(str(os.getcwd()) + r'\weather_data.db'))
        except Exception as e:
            print(e)
        try:
            print(self.csv_parser.top_ten_temps(str(os.getcwd()) + r'\weather_data.db'))
        except Exception as e:
            print(e)
        try:
            print(self.csv_parser.hi_low_temps(str(os.getcwd()) + r'\weather_data.db'))
        except Exception as e:
            print(e)

if __name__ == "__main__":
    SkyTakeHome().main()
