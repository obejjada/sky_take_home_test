
class user_interface():
    """Class Method to define user interface and error messages which are called from the command line"""
    def welcome_message(self):
        """Method to display to the user a welcome message and for them to enter the URL to the CSV"""
        print('Welcome to the Take Home Test')

    def write_q_one_a_file(self, answers, location):
        """Method to write the answers for question 1 part a to .txt file"""
        file_name = str(location) + r'/Question_1_answer.txt'
        f = open(file_name, "a")
        f.write('Question 1)\n')
        f.write('a) ')
        f.write(answers + '\n')
        f.close()

    def write_q_one_b_file(self, answers, location):
        """Method to write the answers for question 1 part b to .txt file"""
        file_name = str(location) + r'/Question_1_answer.txt'
        f = open(file_name, "a")
        f.write('Question 1)\n')
        f.write('b) ')
        f.write(answers + '\n')
        f.close()

    def write_q_one_c_file(self, answers, location):
        """Method to write the answers for question 1 part c to .txt file"""
        file_name = str(location) + r'/Question_1_answer.txt'
        f = open(file_name, "a")
        f.write('Question 1)\n')
        f.write('c)\n')
        for i in answers:
            f.write(str(i) + '\n')
        f.close()

    def write_q_two_file(self, answers, location):
        """Method to write the answers for question 2 to .txt file"""
        file_name = str(location) + r'/Question_2_answer.txt'
        f = open(file_name, "a")
        f.write('Question 2)\n')
        f.write('Hi Temperature that are +- 1 degree from 22.3)\n')
        for i in answers[0]:
            f.write(str(i) + '\n')
        f.write('Low Temperature that are +- 0.2 degrees from 10.3 in the first 9 days of June)\n')
        for i in answers[1]:
            f.write(str(i) + '\n')
        f.close()

    def write_q_three_file(self, answers, location):
        """Method to write the asnwers for question 3 to .txt file"""
        file_name = str(location) + r'/Question_3_answer.txt'
        f = open(file_name, "a")
        f.write('Question 3)\n')
        f.write('Forecast July temperatures\n')
        for i in answers:
            f.write(str(i) + '\n')
        f.close()

    def closing_message(self, location):
        """Method to write a final message to the user signalling the end of the program"""
        print("Output files written to %s\n" % location)
        print('Thanks for using Take Home Test program :)\n')
