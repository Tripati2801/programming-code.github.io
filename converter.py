import csv, json
csvfilepath='raina.csv'
jsonfilepath='suresh.json'
data={}
with open(csvfilepath) as csvfile:
    csvReader=csv.DictReader(csvfile)
    for rows in csvReader:
        id = rows['name']
        data[id] = rows

with open(jsonfilepath,'w')as jsonfile:
    jsonfile.write(json.dumps(data,indent=4))