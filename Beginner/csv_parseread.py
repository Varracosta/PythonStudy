import csv
import os

os.chdir('C:/Study/IT projects/Practice files for tasks')
with open('environment.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)
