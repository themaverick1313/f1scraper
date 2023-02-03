import csv
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
import re

# #made variable because I can probably figure out how to loop it with a dictionary or whatever
websiteSource = 'https://www.formula1.com/en/results.html/2022/races/1124/bahrain/race-result.html'

#1100-1140
soupData = requests.get(websiteSource).text
doc = BeautifulSoup(soupData, "html.parser")
regice = r"\d{1}:\d{2}:\d{2}.\d{3}"
regirock = r"(?<=\+).*(?=<sp)"
#registeel = r"\+\d{1}.\d{3}"
regileci = r"(?<=>)DNF(?=<)"
regigigas = r"(?<=mobile\">).*(?=<\/td>\n<td class=\"dark bold\">\n<span class=\"hide-for-tablet\">)"

#finding driver number values
#this searches for class and subclass to allow easier regex 

pageTextArchiveTable = doc.find(class_="inner-wrap ResultArchiveWrapper").find(class_="resultsarchive-table")
stringTable = str(pageTextArchiveTable)

print('\n')
print(Fore.CYAN + '---start of app---')

#finding driver number
matches = re.finditer(regigigas, stringTable, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
    print ("{match}".format(matches, start = match.start(), end = match.end(), match = match.group()))
    
#find race winner using regice for full time write out 1:23:45.678
print('\n')
print(Fore.RED + '---winner---')
matches = re.finditer(regice, stringTable, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    print ("{match}".format(matchNum, start = match.start(), end = match.end(), match = match.group()))

#find midfield using regirock for +1.234
print('\n')
print(Fore.GREEN +'---midfield---')
matches = re.finditer(regirock, stringTable, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
    print ("{match}".format(matchNum, start = match.start(), end = match.end(), match = match.group()))
print('\n')
print(Fore.MAGENTA + '---backfield---')

# #find backfield using registeel for +12.345
# matches = re.finditer(registeel, stringTable, re.MULTILINE)
# for matchNum, match in enumerate(matches, start=1):
#     print ("{match}".format(matchNum, start = match.start(), end = match.end(), match = match.group()))

#find DNF
matches = re.finditer(regileci, stringTable, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
    print ("{match}".format(matchNum, start = match.start(), end = match.end(), match = match.group()))

#print(pageTextArchiveTable)


