import json
import pandas as pd


#Script to convert a json to a xlsx file with the key on questions
#This uses Pandas
with open('somejson.json') as json_file:
    data = json.load(json_file)

csv_data = pd.json_normalize(data["questions"])

csv_data.to_excel('TestJsonToCsvSomeJson.xlsx', sheet_name='Questions', index=False)
