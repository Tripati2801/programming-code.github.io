import json 
import csv
with open('input.json')as f:
    data=json.load(f)

fname="output.csv"  

with open(fname,"w")as f:
    csv_file=csv.writer(f)
    csv_file.writerow(["name","age","birthplace"])
    for item in data ["sanu"] :   
        csv_file.writerow((item['name'],item['age'],item["birthplace"]))