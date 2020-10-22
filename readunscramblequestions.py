import os
import csv
import json
import pandas as pd

PATH = '/Users/cristina/src/Alice_proni/Excel_files/'
file = 'EPgrade1WBUnscramble.csv'
input_csv_file_path = os.path.join(PATH, file)
activities = []
Nomenclatura = None


#Unscramble
with open(input_csv_file_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)


    for csv_row in csv_reader:
        #print(csv_row)
        if csv_row["Intruccion"]:
            #print(type(csv_row["Module"]))
            Nomenclatura = "Module" + csv_row["Module"] + " Lesson" + csv_row["Lesson"] + " Page" + csv_row["Page"] + " Orden" + csv_row["Orden"]
            activities.append({"title": csv_row["Intruccion"],
                               "Nomenclatura": Nomenclatura,
                               "questions": []
            })

        else:
            question = {"content": csv_row["Pregunta "],
                        "answer": csv_row["Respuesta"]}
            activities[-1]["questions"].append(question)


#Write the data in a json files
root = {"kind": "Unscramble",
        "title": file,
        "questions": activities
}

json_file_path = "EPgrade1WBUnscramble.json"
with open(json_file_path, "w") as json_file:
    json_file.write(json.dumps(root,indent=2))
