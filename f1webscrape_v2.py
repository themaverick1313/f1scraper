import csv
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
import re

# #made variable because I can probably figure out how to loop it with a dictionary or whatever
websiteSource = 'https://www.formula1.com/en/results.html/2022/races/1125/saudi-arabia/race-result.html'
websiteSource2 = 'https://www.formula1.com/en/results.html/2022/races/1124/bahrain/race-result.html'

#/races/(pagenumber)1100-1140/(trackname)/race-result.html
regex = r"(?<=^)\s*\w*\W\d.*"
#debug tools
def debugBlue(x): print(Fore.CYAN + x)
def debugRed(x): print(Fore.RED + x)
def debugGreen(x): print(Fore.GREEN + x)
   
#grabbing html from webstie
soupData = requests.get(websiteSource2).text
doc = BeautifulSoup(soupData, "html.parser")
tables = doc.find_all("table")

#storage arrays
lapTime = []
driverNum = []
pullInfo = []
sortedInfo =[]

for my_table in tables:
    rows = my_table.findChildren('td')
    for row in rows:
        cells = row.get_text()
        value = cells.strip
        lapTime.append(cells)
        whiteSpaceRemove = ''.join(lapTime).split()
        df = pd.DataFrame(whiteSpaceRemove)
        
        filteredData = df.to_string(index=False)
        
        regFilteredData = re.finditer(regex, filteredData, re.MULTILINE)
        for matchNum, match in enumerate(regFilteredData):
            nameDict = {("{match}".format(regFilteredData, match = match.group()))}
            sortedInfo.append(nameDict)
    debugBlue
    print(filteredData)        
    # debugGreen('___regex___')
    # print(sortedInfo)
        
#     debugBlue('-------data--------')
#     print(df.to_string(index=False))
# debugRed('---whitespace---')    
# print(whiteSpaceRemove)

     



