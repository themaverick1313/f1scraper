import math

class colors:
    class fg:
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
distanceStep = [0,50,50,50,50,50,50,34,0,50,50,50,50,50,50,50,50,50,50,0,50,50,47,0,50,50,50,50,50,0,50,50,50,50,50]
trackRadius = [0,100,100,100,100,100,100,100,100,0,0,0,0,0,0,0,0,0,0,0,50,50,50,50,0,0,0,0,0,0,0,0,0,0,0]
firstTurnRadius = 100

def apexVelocity(radius):
    V = math.sqrt(radius*gravity*ggCoef)
    return V

def raceAccel(distance,radius):
    V = apexVelocity(radius)
    currentAccel = math.sqrt((V**2)+(2*ggCoef*gravity*distance))
    print(colors.fg.green,'currentAccel: ',currentAccel,'\ndistance: ',distance,' radius: ',radius)    



for distance,radius in zip(distanceStep,trackRadius):
    if radius > 0:
        apexVelocity(radius)
        print(colors.fg.red,'distance: ', distance,' radius:',radius)
    else:
        raceAccel(distance,radius)
