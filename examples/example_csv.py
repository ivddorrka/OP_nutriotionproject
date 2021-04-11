'''
This module demonstrates how to use some functionality of python built-in csv module
'''
import csv

def csv_usage():
    '''
    This function demonstrates how to use csv module to read and write csv files
    '''
    with open('example.csv', 'r', newline='') as csvfile:
        reader_c = csv.reader(csvfile, delimiter=';')
        for row in reader_c:
            print(', '.join(row))

    with open('new-2.csv', 'w', newline='') as csvfile:
        writer_c = csv.writer(csvfile, delimiter=',')
        writer_c.writerow(['Name', 'Age', 'City'])
        writer_c.writerow(['Joe', '25', 'Miami'])
        writer_c.writerow(['Nick', '21', 'Mexico'])

if __name__ == '__main__':
    csv_usage()
