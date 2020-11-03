import os
import csv
import json


#Return the path of the file
def pathFile(Path, filename):
    input = os.path.join(Path, filename)
    return input




#Dropdown
#Return an object with all the activities that will be convert to json
def processDataframe(pathfile):
    activities = []
    with open(pathfile) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row["Instruccion"]:
                activities.append({"title": row["Instruccion"],
                               "questions": []})

            else:
                #The list of options goes in evry case
                options = [row["Opcion 1"], row["Opcion 2"], row["Opcion 3"], row["Opcion 4"], row["Opcion 5"]]

                #if the question is typo dropdown the correct answer will be always a index interger
                if row["Tipo"] == "dropdown":
                    try:
                        correct = int(row["Opcion Correcta"])

                    except ValueError:
                        correct = options.index(row["Opcion Correcta"])
                        
                #if the question is text the correct answer will be a string
                else:
                    correct = row["Opcion Correcta"]


                question = {"question": row["Pregunta"],
                            "options": options,
                            "correct": correct,
                            "type": row["Tipo"]}


                activities[-1]["questions"].append(question)

        root = {"kind": "Dropdown",
                "questions": activities}

        return root

#Return a Json object, the parameter is an object
def writeToJson(root, filename):
    with open(filename, "w", encoding='utf8') as json_file:
        json_file.write(json.dumps(root,indent=4, ensure_ascii=False))

    return json_file


#Main
if __name__ == '__main__':

    path = "/Users/cristina/src/Alice_proni/Excel_files/"
    filename = "DropdowntodosTestCases.csv"
    filenameJson = "DropdowntodosTestCases.json"
    pathfile = pathFile(path, filename)
    root = processDataframe(pathfile)
    writeToJson(root, filenameJson)
