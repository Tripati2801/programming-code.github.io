import requests
import csv
from bs4 import BeautifulSoup as f
sanu=requests.get("https://www.infoplease.com/culture-entertainment/film/top-50-greatest-heroes-and-villains")
soup=f(sanu.content,"html.parser")
filename="website.csv"
csv_writer=csv.writer(open(filename,"w"))
for tr in soup.find_all('tr'):
    data=[]
    for th in tr.find_all('th'):  
        data.append(th.text)
    if data:
        print('inertion header:{}'.format(','.join(data)))
        csv_writer.writerow(data)
        continue
    for td in tr.find_all('td'):
        data.append(td.text.strip())
    if data:
        print('insertion order:{}'.format(','.join(data)))
        csv_writer.writerow(data)    






