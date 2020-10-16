import json
import csv

with open('somejson.json') as json_file:
    data = json.loads(json_file)

csv_data = data["questions"]

csv_file = open('csvtestfromjson.csv', 'w')
csv_writer = csv.writer(csv_file)

count = 0
for question in csv_data:
    if count == 0:

        header = question.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(question.values())

csv_file.close()
