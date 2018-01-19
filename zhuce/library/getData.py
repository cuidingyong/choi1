#coding=utf-8
import csv
from library.getPath import get_path

def get_csv_data(filename):
    rows = []
    csv_data = open(get_path(filename))
    content = csv.reader(csv_data)
    next(content,None)

    for row in content:
        # print(row)
        rows.append(row)
    return rows

# print(get_csv_data('canshu.csv'))