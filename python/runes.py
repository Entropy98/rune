import math

def calcStageOneOffset(s, fibCalc, x=1, y=0, i=1):
    if(i > s):
        return (x,y)
    return calcStageOneOffset(s,fibCalc,fibCalc(i),fibCalc(i)-1,i+1)

def calcStageTwoOffset(s, fibCalc, x=1, y=1, i=1):
    if(i > s):
        return (x,y)
    return calcStageTwoOffset(s,fibCalc,fibCalc(i),y+fibCalc(i-1),i+1)

def calcStageThreeOffset(s,fibCalc,y=1,i=1):
    if(i > s):
        return y
    return calcStageThreeOffset(s,fibCalc,y+fibCalc(i-1),i+1)

def calcStageSixOffset(s,fibCalc,y=7,i=1):
    if(i > s):
        return y
    return calcStageSixOffset(s,fibCalc,y+2*fibCalc(i),i+1)

class Fire():
    def stageOneY(x,fib,s,fibCalc):
        offset = calcStageOneOffset(s, fibCalc)
        return math.sqrt(abs(fib)**2-(abs(x)-offset[0])**2)-offset[1]

    def stageOneX(y,fib,s,fibCalc):
        offset = calcStageOneOffset(s, fibCalc)
        return math.sqrt(abs(fib)**2-(abs(y)-offset[1])**2)-offset[0]

    def stageTwoY(x,fib,s,fibCalc):
        offset = calcStageTwoOffset(s, fibCalc)
        return math.sqrt(abs(fib)**2-(abs(x)-offset[0])**2)-offset[1]

    def stageTwoX(y,fib,s,fibCalc):
        offset = calcStageTwoOffset(s, fibCalc)
        return math.sqrt(abs(fib)**2-(abs(y)-offset[1])**2)-offset[0]

    def stageThreeY(x,fib,s,fibCalc):
        return -1*math.sqrt(abs(fib)**2-abs(x)**2)-calcStageThreeOffset(s,fibCalc)

    def stageFourY(x,fib):
        return -1*math.sqrt(abs(fib)**2-abs(x)**2)+1

    def stageFiveY(x,fib):
        return math.sqrt(abs(fib)**2-abs(x)**2)+1

    def stageSixY(x,fib,s,fibCalc):
        return -1*math.sqrt(abs(fib)**2-abs(x)**2)+calcStageSixOffset(s,fibCalc)

