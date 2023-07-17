import math

gravity = 9.81
ggCoef = 2
radius_turn01 = 100
radius_turn02 = 50
distanceStep = 50


def apexVelocity(x):
    V = math.sqrt(x*gravity*ggCoef)
    return V
print(apexVelocity(radius_turn01))


def raceAccel():
    V = apexVelocity(radius_turn01)
    currentAccel = math.sqrt((V**2)+(2*ggCoef*gravity*distanceStep))
    print('currentAccel:',currentAccel)
raceAccel()