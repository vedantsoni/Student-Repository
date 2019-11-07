import os
from prettytable import PrettyTable
from datetime import datetime, timedelta

def date_arithmetic():
    """ Function to check the functionality of date arithematic """

    three_days_after_02272000 = datetime.strptime('Feb 27 2000', '%b %d %Y') + timedelta(days=3)
    dt1 = three_days_after_02272000.strftime('%b %d %Y')

    three_days_after_02272017 = datetime.strptime('Feb 27 2017', '%b %d %Y') + timedelta(days=3)
    dt2 = three_days_after_02272017.strftime('%b %d %Y')

    days_passed_01012017_10312017 = datetime.strptime('Oct 31 2017', '%b %d %Y') - datetime.strptime('Jan 1 2017', '%b %d %Y')

    return dt1, dt2, days_passed_01012017_10312017


def file_reading_gen(path, fields, sep='|', header=False):
    """ Function to check the functionality of the File Reader """

    try:
        fp = open(path, encoding='UTF-8')
    except FileNotFoundError:
        raise FileNotFoundError()
    else:
        with fp:
            data = fp.readlines()
            for offset, line in enumerate(data, 1):
                striped_line = line.rstrip()
                sep_line = striped_line.split(sep)
                if len(sep_line) == fields:
                    if header is True and offset == 1:
                        continue

                    yield tuple(sep_line)
                else:
                    raise ValueError()

class FileAnalyzer:
    """ Class that incorporates the functionality of Analyzing the files """

    def __init__(self, directory):
        """ Dunder Function that incorporates the directory """

        self.directory = directory
        self.files_summary = dict() 
        self.analyze_files()

        try:
            os.path.exists(self.directory)
        except OSError:
            raise OSError()


    def analyze_files(self):
        """ Function to check the functionality of analyzing the file """

        files = os.listdir(self.directory)

        for file in files:
            if file.endswith('.py'):
                self.files_summary[file] = {}
                try:
                    fp = open(file, 'r')
                except:
                    FileNotFoundError()
                else:
                    with fp:
                        lines = 0
                        functions = 0
                        classes = 0
                        character = 0
                        for line in fp:
                            lines = lines + 1
                            for char in line:
                                character = character + 1
                            file_line = line.lstrip()
                            if file_line.startswith('class '):
                                classes += 1
                            elif file_line.startswith('def '):
                                functions += 1

                    self.files_summary[file] = {

                        'class': classes,
                        'function': functions,
                        'line': lines,
                        'chars': character
                    }
                    
                    

    
    def pretty_print(self):
        """ Function to print a pretty tale for the same """

        pt = PrettyTable(field_names=['File Name', 'Class', 'Functions', 'Line', 'Chars'])
        for file_name in self.files_summary:
            pt.add_row([file_name, self.files_summary[file_name]["class"], self.files_summary[file_name]["function"], self.files_summary[file_name]["line"], self.files_summary[file_name]["chars"]])

        return pt
            

# fa = FileAnalyzer("C://Users//VedantS//Desktop//810//HW08")
# fa.pretty_print()
# print(fa.files_summary)
# print(fa.pretty_print())



