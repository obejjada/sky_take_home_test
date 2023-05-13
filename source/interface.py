import os


class user_interface():
    """Class Method to define user interface and error messages which are called from the command line"""
    def welcome_message(self):
        """Method to display to the user a welcome message and for them to enter the URL to the CSV"""
        print('Welcome to the Sky Take Home Test')

    def write_q_one_a_file(self, answers, location):
        """Method to write the answers for question 1 part a"""
        file_name = str(location) + r'\Question_1_answer.txt'
        f = open(file_name, "a")
        f.write('Quenstion 1)\n')
        f.write('a) ')
        f.write(answers + '\n')
        f.close()

    def write_q_one_b_file(self, answers, location):
        """Method to write the answers for question 1"""
        file_name = str(location) + r'\Question_1_answer.txt'
        f = open(file_name, "a")
        f.write('Quenstion 1)\n')
        f.write('b) ')
        f.write(answers + '\n')
        f.close()
