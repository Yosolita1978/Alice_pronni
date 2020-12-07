import os
import csv
import json
import pandas as pd

PATH = '/Users/cristina/src/Alice_proni/Excel_files/'
file = 'FillTodosWBP2.csv'
input_csv_file_path = os.path.join(PATH, file)
activities = []
Nomenclatura = None


#Fill the blanks
with open(input_csv_file_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)


    for csv_row in csv_reader:
        #print(csv_row)
        if csv_row["Instruccion"]:
                Orden = csv_row["Orden"]
                activities.append({"title": csv_row["Instruccion"],
                                   "Nomenclatura": Orden,
                                   "questions": []
                })

        else:
            question = {"orden": csv_row["Orden"],
                        "content": csv_row["Pregunta"],
                        "answer": csv_row["Respuesta"]}

            activities[-1]["questions"].append(question)


#Write the data in a json files
root = {"kind": "fillblanks",
        "title": file,
        "questions": activities
}

json_file_path = "FillTodosWBP2.json"
with open(json_file_path, "w") as json_file:
    json_file.write(json.dumps(root,indent=4))
