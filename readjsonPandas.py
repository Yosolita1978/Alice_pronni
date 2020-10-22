import json
import pandas as pd


#Script to convert a json to a xlsx file with the key on questions
#This uses Pandas
with open('workbook3.json') as json_file:
    data = json.load(json_file)

csv_data = pd.json_normalize(data["questions"])

csv_data.to_excel('Testworkbook3.xlsx', sheet_name='Questions', index=False)
