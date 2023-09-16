import requests
import sqlite3
from bs4 import BeautifulSoup

response=requests.get("https://www.bbc.com/ukrainian/features-66330880")
if response.status_code==200:
    bs4=BeautifulSoup(response.text, features="html.parser")
    list=bs4.find_all("h2", {"class":"bbc-1aaitma eglt09e0"})
    conection = sqlite3.connect("o.sl3", 5)
    cur = conection.cursor()
    cur.execute("DROP TABLE first_table")
    cur.execute(f'CREATE TABLE first_table (place TEXT, name Text);')
    for i in range(10):
        cur.execute("INSERT INTO first_table (place, name) VALUES(?, ?)", (i+1, list[i].text))
conection.commit()
conection.close()