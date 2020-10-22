import os
import csv
import json
import pandas as pd

#csvFilepath = 'Test_EPgrade1WBFill.csv'



#Path files
PATH = '/Users/cristina/src/Alice_proni/Excel_files/'
file = 'EPgrade1WBDrag.csv'
input_csv_file_path = os.path.join(PATH, file)

#Drop the columns "Module", "Lesson", "Page", "Orden"
input_data = pd.read_csv(input_csv_file_path)
df = input_data.drop(["Module", "Lesson", "Page", "Orden"], axis=1)
df.to_csv("EPgrade1WBDrag_output.csv", index=False, header=True)



#read the csv file and add to dict data using "Instruccion" as key
data = {}
with open('EPgrade1WBDrag_output.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for csv_row in csv_reader:
        key = csv_row["Instruccion"]
        data[key] = csv_row

#Adding the data to the root mode "fillblanks"
root = {}
root["dragndrop"] = data

#Write the data in a json files
json_file_path = "EPgrade1WBDrag.json"
with open(json_file_path, "w") as json_file:
    json_file.write(json.dumps(root,indent=4))
