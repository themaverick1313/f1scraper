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

firstPlaceRegex = re.compile("\w*\d:\d*:\d*.\d*")
otherPlaceRegex = re.compile(r"\w*\+\d*.\d*s\d*")
teamNameRegex = re.compile(r"^\s*[a-zA-Z]*")
fastestTimeRegex = re.compile(r"(?<=\w\d{2})\d{1}:\d{2}:\d{2}.\d*$")
otherTimeRegex = re.compile(r"(?<=\+)\d*.\d*s\d*")
(?<=\+)\d*.\d*s\d{3}
#storage arrays
lapTime = []
teamNames = []

#debug tools
def debugBlue(x): print(Fore.CYAN + x)
def debugRed(x): print(Fore.RED + x)
def debugGreen(x): print(Fore.GREEN + x)
   
#grabbing html from webstie
soupData = requests.get(websiteSource).text
doc = BeautifulSoup(soupData, "html.parser")
tables = doc.find_all("table")
#creates filterData to be used
for my_table in tables:
    rows = my_table.findChildren('td')
    for row in rows:
        cells = row.get_text()
        value = cells.strip
        lapTime.append(cells)
        whiteSpaceRemove = ''.join(lapTime).split()
        df = pd.DataFrame(whiteSpaceRemove)
        filterData = df.to_string(index=False, header=False)

# =============Functions=============

# x,y is the place regex search
# use for filtering data
#this runs withing the for loop, filterData needs to be created from the for loop before this can be used
def pullTableLapDataText(x,y):
    #this function pulls out the raw sting for parsing ex. "Mercedes50+91.742s01318" to then be broken into team name and time and number
    # dataForDataFrame1 = regex is determined by x in the function, use regex from above, and pull the filterData based on that
    dataForDataFrame1 = x.findall(filterData)
    print(filterData)
    #this takes the results from above and puts them into a df for pandas and then uses these results to put to a string
    dataToString1 = pd.DataFrame(dataForDataFrame1)
    #puts it into a string, without the 0,0 for index and header so it doesn't end up in the final array
    breakIntoColumns1 = dataToString1.to_string(index=False, header=False)
    #uses results in breakIntoColumns1 to find all the matches based on y from pullTableLapDataText
    names = y.findall(breakIntoColumns1)
    teamNames.append(names)
    teamdNamesdf = pd.DataFrame(teamNames)
    teamNamesString = teamdNamesdf.to_string(index=False, header=False)
    #use breakintocolumns1 to do the regex because it is pushed to string and can be iterated
    dataforDataFrame2 = otherTimeRegex.findall(breakIntoColumns1)

pullTableLapDataText(otherPlaceRegex,teamNameRegex)
debugGreen('fasttime')
pullTableLapDataText(firstPlaceRegex,fastestTimeRegex)