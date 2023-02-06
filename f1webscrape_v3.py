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
teamNameRegex = re.compile(r"^\s*[a-zA-Z]*")
fastestTimeRegex = re.compile(r"(?<=\w\d{2})\d{1}:\d{2}:\d{2}.\d*$")

#debug tools
def debugBlue(x): print(Fore.CYAN + x)
def debugRed(x): print(Fore.RED + x)
def debugGreen(x): print(Fore.GREEN + x)
   
#grabbing html from webstie
soupData = requests.get(websiteSource2).text
doc = BeautifulSoup(soupData, "html.parser")
tables = doc.find_all("table")

# =============Functions=============

# x is the place regex search
# use for filtering data
def pullTableLapDataText(x):
    dataForDataFrame1 = x.findall(filterData)
    dataToString2 = pd.DataFrame(dataForDataFrame1)
    breakIntoColumns3 = dataToString2.to_string(index=False, header=False)
    debugGreen('break')
    print(breakIntoColumns3)
    teamName4 = teamNameRegex.findall(breakIntoColumns3)
    teamdf5 = pd.DataFrame(teamName4)
    debugRed('teamname')
    print(teamdf5.to_string(index=False, header=False))


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
        filterData = df.to_string(index=False, header=False)  

    pullTableLapDataText(firstPlaceRegex)
    debugBlue('other place')
    pullTableLapDataText(otherPlaceRegex)  