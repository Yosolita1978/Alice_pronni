import os
import csv
import json

#csvFilepath = 'Test_EPgrade1WBFill.csv'



#Path files
PATH = '/Users/cristina/src/Alice_proni/Excel_files/'
file = 'EPgrade1WBFill.csv'
csv_file_path = os.path.join(PATH, file)


#read the csv file and add to dict data using "Instruccion" as key
data = {}
with open(csv_file_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for csv_row in csv_reader:
        key = csv_row["Instruccion"]
        data[key] = csv_row

#Adding the data to the root mode "fillblanks"
root = {}
root["fillblanks"] = data

#Write the data in a json files
json_file_path = "EPgrade1WBFill.json"
with open(json_file_path, "w") as json_file:
    json_file.write(json.dumps(root,indent=4))
