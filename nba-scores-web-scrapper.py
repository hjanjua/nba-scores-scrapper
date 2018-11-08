#!/usr/bin/python
import requests
import smtplib, re
import datetime
from bs4 import BeautifulSoup
from time import strftime, gmtime

url = 'https://www.cbssports.com/nba/scoreboard/20181106/'

teams=[]
scores=[]

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
tables=soup.findAll("div", {"class": "in-progress-table section "})
#print(table_)
#table = soup.find('div', attrs={'class': 'in-progress-table section '})
for table in tables:
    rows = table.findAll('tr')
    #print(rows)
    for tr in rows:
        cols = tr.findAll('td')
       
        for td in cols:          
            #print(td)
            for a in td.find_all('a'):
                atext=a.string
                teams.append(atext) 

            #link1 = td.find_all('a',text=True)
            #link = td.find('a', href=True)
            
            text = td.find(text=True) + ''
            scores.append(text)
            #print(text) 

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

#get rid of none
teams=[x for x in teams if x is not None]
#get rid of \n - nice function!!
scores=remove_values_from_list(scores,'\n')
#convert string list to int list
scores=list(map(int, scores))
#only keep the scores > 70 (what if its low scoring game)
scores=list(filter(lambda a: a >70, scores))

print(teams)
print(scores)  