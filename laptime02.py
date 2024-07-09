import math
from pprint import pprint

class colors:
    class fg:
        white = '\033[0m'
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

gravity = 9.81
ggCoef = 2
nextDistanceStep = [0,50,50,50,50,50,50,34,0,50,50,50,50,50,50,50,50,50,50,0,50,50,47,0,50,50,50,50,50,0,50,50,50,50,50]
trackRadius = [0,100,100,100,100,100,100,100,100,0,0,0,0,0,0,0,0,0,0,0,50,50,50,50,0,0,0,0,0,0,0,0,0,0,0]
#nextDistanceStep = [0,50,50,50,50,50,50,50,50,50,50,0,50,50,47,0,50,50,50,50,50,0,50,50,50,50,50,0,50,50,50,50,50,50,34]
#trackRadius = [0,0,0,0,0,0,0,0,0,0,0,50,50,50,50,0,0,0,0,0,0,0,0,0,0,0,0,100,100,100,100,100,100,100,100]
accelerationTable = []
decelerationTable = []
firstTurnRadius = 100
secondTurnRadius = 50

#calculate apex velocity using the turns radius
def apexVelocity(radius,table):
    V = math.sqrt(radius*gravity*ggCoef)
    table.append(V)
    #print(colors.fg.white,table[-1])

#calculate velocity of vehicle for next distance step using previous velocity    
def raceAccel(distance,accTable):
    currentAccel = math.sqrt(accTable[-1]**2+2*ggCoef*gravity*distance)
    #speedCheck(currentAccel,accTable)
    accTable.append(currentAccel)

#main lap acceleration calculation only does acceleration right now need to do deaceelerartion and compare and take lowest value
def lapAcceleration(turnRadius,celerationTable):
    counter = False
    for distance,radius in zip(nextDistanceStep,trackRadius):
        #first leg uses the exit V of the first turn so need to calculate what it is before using it to calculate the next one
        #checks if it needs the first calculation yet
        if counter == False:
            #do first calculation
            apexVelocity(turnRadius,celerationTable)
            #changes counter to do rest of the math using the results of this
            counter = True
        else:
            #if radius is greater than 0, so a turn, give the highest possible value
            if radius > 0:
                apexVelocity(radius,celerationTable)
                #else using the last velocity on the table calculate acceleration
            else:
                raceAccel(distance,celerationTable)



def speedCheck(x,y):
    if x > y[-1]:
        print(colors.fg.green,x)
    elif x == y[-1]:
        print(colors.fg.yellow,x)
    else:
        print(colors.fg.red,x)

def getLapTimeTotal():
    print(colors.fg.pink,sum(accelerationTable))
    print(colors.fg.lightgreen,sum(decelerationTable))

# getLapTimeTotal()
lapAcceleration(firstTurnRadius,accelerationTable)
# def printtable(x):
#     for i in x:
#         print(i)
# printtable(accelerationTable)
pprint(accelerationTable)
getLapTimeTotal()
print('\n')
lapAcceleration(secondTurnRadius,decelerationTable)
# getLapTimeTotal()

finalTable = [min(*item) for item in zip(accelerationTable,decelerationTable)]
for x,y,z in zip(finalTable,accelerationTable,decelerationTable):
    print(colors.fg.green,x,colors.fg.red,y,colors.fg.orange,z)
