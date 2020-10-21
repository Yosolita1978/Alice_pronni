import os
import csv
import json
import pandas as pd

PATH = '/Users/cristina/src/Alice_proni/Excel_files/'
file = 'EPgrade1WBFill.csv'
input_csv_file_path = os.path.join(PATH, file)
activities = []


#Fill the blanks
with open(input_csv_file_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)


    for csv_row in csv_reader:
        #print(csv_row)
        if csv_row["Instruccion"]:
                activities.append({"title": csv_row["Instruccion"],
                                    "questions": []
                })

        else:
            question = {"content": csv_row["Pregunta 1"],
                        "answer": csv_row["Respuesta 1"]}

            activities[-1]["questions"].append(question)


#Write the data in a json files
root = {"kind": "fillblanks",
        "title": file,
        "questions": activities
}

json_file_path = "EPgrade1WBFill.json"
with open(json_file_path, "w") as json_file:
    json_file.write(json.dumps(root,indent=4))
