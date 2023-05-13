import csv_parser
import interface
import sys
import os
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
        output_file_loc = input('Please enter path of where to save output files\n')
        try:
            if os.path.exists(output_file_loc + r"\weather_data.db"):
                os.remove(output_file_loc + r"\weather_data.db")
        except Exception as e:
            print(e)
        try:
            if os.path.exists(output_file_loc + r"\Question_1_answer.txt"):
                os.remove(output_file_loc + r"\Question_1_answer.txt")
        except Exception as e:
            print(e)
        try:
            if os.path.exists(output_file_loc + r"\Question_2_answer.txt"):
                os.remove(output_file_loc + r"\Question_2_answer.txt")
        except Exception as e:
            print(e)
        try:
            if os.path.exists(output_file_loc + r"\Question_3_answer.txt"):
                os.remove(output_file_loc + r"\Question_3_answer.txt")
        except Exception as e:
            print(e)
        try:
            data_object = self.csv_parser.parse_csv(self.csv_parser.open_url(csv_url))
            self.csv_parser.import_data_to_sql(data_object)
        except Exception as e:
            print(e)
        try:
            self.interface.write_q_one_a_file(self.csv_parser.average_time_hottest_temp(str(os.getcwd()) + r'\weather_data.db'), output_file_loc)
        except Exception as e:
            print(e)
        try:
            self.interface.write_q_one_b_file(self.csv_parser.common_time_hotest(str(os.getcwd()) + r'\weather_data.db'), output_file_loc)
        except Exception as e:
            print(e)
        try:
            self.interface.write_q_one_c_file(self.csv_parser.top_ten_temps(str(os.getcwd()) + r'\weather_data.db'), output_file_loc)
        except Exception as e:
            print(e)
        try:
            self.interface.write_q_two_file(self.csv_parser.hi_low_temps(str(os.getcwd()) + r'\weather_data.db'), output_file_loc)
        except Exception as e:
            print(e)
        try:
            self.interface.write_q_three_file(self.csv_parser.forecast_july(str(os.getcwd()) + r'\weather_data.db'), output_file_loc)
        except Exception as e:
            print(e)
        self.interface.closing_message(output_file_loc)
if __name__ == "__main__":
    SkyTakeHome().main()
