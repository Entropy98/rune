import math

class Fire():
    def stageOne(x,s):
        return math.sqrt(s**2-(x-1)**2)

    def stageTwo(x,s):
        return math.sqrt(s**2-(x-1)**2)-1

    def stageThree(x,s):
        return -1*math.sqrt(s**2-x^2)-1

    def stageFour(x,s):
        return -1*math.sqrt(s**2-x^2)+1

    def stageFive(x,s):
        return math.sqrt(s**2-x^2)+1

    def stageSix(x,s):
        return -1*math.sqrt(s**2-x^2)+7
