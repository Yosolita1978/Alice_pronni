import os
import csv
import json
import pandas as pd

PATH = '/Users/cristina/src/Alice_proni/Excel_files/'
file = 'DropdownTestCases.csv'
input = os.path.join(PATH, file)
activities = []




#Dropdown
with open(input) as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for csv_row in csv_reader:
        #print(csv_row)
        if csv_row["Instruccion"]:
            #print(csv_row)
            activities.append({"title": csv_row["Instruccion"],
                               "questions": []
            })

        else:
            if csv_row["Tipo"] == "text":
                question = {"question": csv_row["Pregunta"],
                            "options": [csv_row["Opcion 1"], csv_row["Opcion 2"], csv_row["Opcion 3"], csv_row["Opcion 4"], csv_row["Opcion 5"]],
                            "correct": csv_row["Opcion Correcta"],
                            "type": csv_row["Tipo"]}
            else:
                question = {"question": csv_row["Pregunta"],
                            "options": [csv_row["Opcion 1"], csv_row["Opcion 2"], csv_row["Opcion 3"], csv_row["Opcion 4"], csv_row["Opcion 5"]],
                            "correct": int(csv_row["Opcion Correcta"]),
                            "type": csv_row["Tipo"]}

            activities[-1]["questions"].append(question)

#Write the data in a json files
root = {"kind": "dropdown",
        "title": file,
        "questions": activities
}

json_file_path = "DropdownTestCases.json"
with open(json_file_path, "w") as json_file:
    json_file.write(json.dumps(root,indent=4))
