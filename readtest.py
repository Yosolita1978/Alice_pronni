import os
import csv
import json

#csvFilepath = 'Test_EPgrade1WBFill.csv'



#Path files
PATH = '/Users/cristina/src/Alice_proni/Excel_files'

#Return a list with all the csv files as objects
def get_files(PATH):
    files = []
    for file in os.listdir(PATH):
        files.append(file)
    return(files)

csvFileList = get_files(PATH)
csvFilePath = os.path.join(PATH, csvFileList[0])


#read the csv file and add to dict dat
data = {}
jsonFilePath = 'Test_EPgrade1WBFill.json'


with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['Module']
        data[id] = rows

#Write the Json file
with open(jsonFilePath, 'w') as JsonFile:
    JsonFile.write(json.dumps(data, indent=4))
