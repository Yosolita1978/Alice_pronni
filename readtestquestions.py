import os
import csv
import json
import pandas as pd

PATH = '/Users/cristina/src/Alice_proni/Excel_files/'
file = 'DropdownTestCases.csv'
input = os.path.join(PATH, file)
activities = []

with open(input) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    fields = csv_reader.fieldnames
    print(fields)
