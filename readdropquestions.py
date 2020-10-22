import os
import csv
import json
import pandas as pd

PATH = '/Users/cristina/src/Alice_proni/Excel_files/'
file = 'EPgrade1WBDropdown.csv'
input_csv_file_path = os.path.join(PATH, file)
activities = []


#Dropdown
with open(input_csv_file_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)


    for csv_row in csv_reader:
        #print(csv_row)
        if csv_row["Instruccion"]:
            #print(csv_row)
            activities.append({"title": csv_row["Instruccion"],
                               "activity": []
            })

        else:
            question = {"question": csv_row["Pregunta"],
                        "options": [csv_row["Opcion 1"], csv_row["Opcion 2"]],
                        "correct": csv_row["Opcion Correcta"],
                        "type": "text"}
            activities[-1]["activity"].append(question)


#Write the data in a json files
root = {"kind": "dropdown",
        "title": file,
        "questions": activities
}

json_file_path = "EPgrade1WBDropdow.json"
with open(json_file_path, "w") as json_file:
    json_file.write(json.dumps(root,indent=2))
