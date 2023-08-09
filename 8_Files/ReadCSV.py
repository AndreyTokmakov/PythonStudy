import csv
from csv import DictReader

TEST_FILE_PATH: str = '../data/csv_file_example.csv'


def ReadFileSimple():
    with open(TEST_FILE_PATH, newline='', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(' | '.join(row))


def ReadWithoutHeader():
    # skip first line i.e. read header first and then iterate over each row od csv as a list
    with open(TEST_FILE_PATH, 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        header = next(csv_reader)
        if header:  # Check file as empty
            # Iterate over each row after the header in the csv
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                print(row)


def Read_Specific_Columns():
    # iterate over each line as a ordered dictionary and print only few column by column name
    with open(TEST_FILE_PATH, 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:
            print(row['Last name'], row['SSN'])


if __name__ == '__main__':
    # ReadFileSimple()
    ReadWithoutHeader()
    #  Read_Specific_Columns()
