import sys
import os
import csv
from tabulate import tabulate

document_name = sys.argv[1]


data = csv.reader(open(document_name), delimiter=';')

header = next(data)

frequency_index = header.index('Frequency (Hz)')
real_z_index = header.index("Z' (Î©)")
imaginary_z_index = header.index("-Z'' (Î©)")

frequency_list = []
real_z_list = []
imaginary_z_list = []
number_of_rows = 0

for row in data:
    number_of_rows = number_of_rows + 1
    frequency_list.append(row[frequency_index])
    real_z_list.append(row[real_z_index])
    imaginary_z_list.append(row[imaginary_z_index])


new_file_path, new_file_name = os.path.split(document_name)
new_file_full_path = os.path.join(new_file_path, '[CONVERTED] ' + new_file_name)

f = open(new_file_full_path, "w")

f.write(str(number_of_rows) + '\n')

table = []

for index, row in enumerate(real_z_list):
    table.append([real_z_list[index], imaginary_z_list[index], frequency_list[index]])

f.write(tabulate(table, tablefmt='plain'))