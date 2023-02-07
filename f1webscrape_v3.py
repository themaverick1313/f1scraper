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
teamNameRegex = re.compile(r"^\s*[a-zA-Z]*")

firstPlaceRegex = re.compile("\w*\d:\d*:\d*.\d*")
fastestTimeRegex = re.compile(r"(?<=\w\d{2})\d{1}:\d{2}:\d{2}.\d*$")

otherPlaceRegex = re.compile(r"\w*\+\d*.\d*s\d*")
otherTimeRegex = re.compile(r"(?<=\+)\d*.\d*s\d*")
# (?<=\+)\d*.\d*s\d{3}
#storage arrays
lapTime = []
teamNames = []
otherTeamNames = []
fastestTime = []
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
def function(returnedValue,regex1,regex2):
    debugBlue('running test function')
    variable1 = regex1.findall(regex2)
    variable1todataframe = pd.DataFrame(variable1)
    returnedValue = variable1todataframe.to_string(index=False, header=False)
    debugGreen('inside print')
    print(returnedValue)
    return returnedValue

def pullTableLapDataText(regex1,regex2):
    #this function pulls out the raw sting for parsing ex. "Mercedes50+91.742s01318" to then be broken into team name and time and number
    # dataForDataFrame1 = regex is determined by x in the function, use regex from above, and pull the filterData based on that
    #this takes the results from above and puts them into a df for pandas and then uses these results to put to a string
    #puts it into a string, without the 0,0 for index and header so it doesn't end up in the final array
    #uses results in breakIntoColumns1 to find all the matches based on y from pullTableLapDataText
    #use breakintocolumns1 to do the regex because it is pushed to string and can be iterated
    
    #get first place
    dataForDataFrame1 = regex1.findall(filterData)
    dataToString1 = pd.DataFrame(dataForDataFrame1)
    breakIntoColumns1 = dataToString1.to_string(index=False, header=False)
    #use breakIntoColums1 as the master findall(x)
    #you completed finding what you were looking for now break it apart

 #new functinon?
 # get team from firstplaceregex breakintoclolumns1   
    names = regex2.findall(breakIntoColumns1)
    teamNames.append(names)
    teamdNamesdf = pd.DataFrame(teamNames)
    teamNamesString = teamdNamesdf.to_string(index=False, header=False)
    print('firstNamestring')
    print(teamNamesString)
    #you found what you are looking for
    function(df,fastestTimeRegex,breakIntoColumns1)
    debugRed('outside print')

    # fastestRace = regex3.findall(breakIntoColumns1)
    # fastestTime.append(fastestRace)
    # fastestTime

    # otherNames = otherPlaceRegex.findall(breakIntoColumns1)
    # print(otherNames)
    # otherTeamNames.append(otherNames)
    # otherTeamNamesdf = pd.DataFrame(otherTeamNames)
    # print(otherTeamNamesdf)
    # otherTeamNamesString = otherTeamNamesdf.to_string(index=False, header=False)
    # debugBlue('otherteamnamestring')
    # print(otherTeamNamesString)



pullTableLapDataText(firstPlaceRegex,teamNameRegex)


# turn this into a function?

