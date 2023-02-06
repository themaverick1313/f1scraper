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
# regex = r"(?<=^)\s*\w*\W\d.*"
firstPlaceRegex = re.compile("\w*\d:\d*:\d*.\d*")
otherPlaceRegex = re.compile(r"\w*\+\d*.\d*s\d*")
#debug tools
def debugBlue(x): print(Fore.CYAN + x)
def debugRed(x): print(Fore.RED + x)
def debugGreen(x): print(Fore.GREEN + x)
   
#grabbing html from webstie
soupData = requests.get(websiteSource2).text
doc = BeautifulSoup(soupData, "html.parser")
tables = doc.find_all("table")

# use for filtering data
# x is the place regex search
def pullTableLapDataText(x):
    dataForDataFrame = x.findall(filterData)
    dataToString = pd.DataFrame(dataForDataFrame)
    stringForExport = dataToString.to_string(index=False)
    print(stringForExport)

#storage arrays
lapTime = []

for my_table in tables:
    rows = my_table.findChildren('td')
    for row in rows:
        cells = row.get_text()
        value = cells.strip
        lapTime.append(cells)
        whiteSpaceRemove = ''.join(lapTime).split()
        df = pd.DataFrame(whiteSpaceRemove)
        filterData = df.to_string(index=False)  
    pullTableLapDataText(firstPlaceRegex)
    pullTableLapDataText(otherPlaceRegex)  







     



