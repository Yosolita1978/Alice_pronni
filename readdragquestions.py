import os
import csv
import json



#Return the path of the file
def pathFile(Path, filename):
    input = os.path.join(Path, filename)
    return input

#Return an object with all the activities that will be convert to json
def processDataframe(pathfile):
    activities = []
    with open(pathfile, encoding="utf8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:

            if row["Instruccion"]:
                activities.append({"Nomenclatura": row["Archivo JSON"],
                                   "kind": "draganddrop",
                                   "Instruccion": row["Instruccion"],
                                   "questions": []})

            else:
                question = {"question": row["opciones"],
                            "answer": row["respuestas"]}

                activities[-1]["questions"].append(question)

    root = {"kind": "dragndrop",
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
    filename = "DragandDropTodosS1.csv"
    filenameJson = "DragandDropTodosS1.json"
    pathfile = pathFile(path, filename)
    root = processDataframe(pathfile)
    writeToJson(root, filenameJson)
