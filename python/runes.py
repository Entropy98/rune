import math

class Fire():
    def stageOneY(x,s1):
        if(x > s1 or x < 0):
            return None
        return math.sqrt(abs(s1)**2-(abs(x-s1))**2)-(s1-1)

    def stageOneX(y,s1):
        if(y > 1 or y < -1*(s1-1)):
            return None
        return -1*(math.sqrt(abs(s1)**2-abs(y+(s1-1))**2)-s1)

    def stageTwoY(x,s1,s2,s3):
        if(x < s1 or x > s3):
            return None
        return math.sqrt(abs(s2)**2-(abs(x-s1))**2)-s1

    def stageTwoX(y,s1,s2):
        if(y > 1 or y < -1*s1):
            return None
        return math.sqrt(abs(s2)**2-(abs(y+s1))**2)+s1

    def stageThreeY(x,s1,s3):
        if(x < 0 or x > s3):
            return None
        return -1*math.sqrt(abs(s3)**2-abs(x)**2)-s1

    def stageThreeX(y,s1,s3,s4):
        if(y > -1*s1 or y < -1*(s4-1)):
            return None
        return math.sqrt(abs(s3)**2-abs(y+s1)**2)

    def stageFourY(x,s4):
        if(x > 0 or x < -1*s4):
            return None
        return -1*math.sqrt(abs(s4)**2-abs(x)**2)+1

    def stageFourX(y,s4):
        if(y < -1*(s4-1) or y > 0):
            return None
        return -1*math.sqrt(abs(s4)**2-abs(y-1)**2)

    def stageFiveY(x,s4):
        if(x > 0 or x < -1*s4):
            return None
        return math.sqrt(abs(s4)**2-abs(x)**2)+1

    def stageFiveX(y,s4):
        if(y < 0 or y > s4+1):
            return None
        return -1*math.sqrt(abs(s4)**2-abs(y-1)**2)

    def stageSixY(x,s1):
        if(x < 0 or x > s1):
            return None
        return -1*math.sqrt(abs(s1)**2-abs(x)**2)+(7+4*(s1-1))

    def stageSixX(y,s1,s4):
        if(y > 7+4*(s1-1) or y < s4):
            return None
        return math.sqrt(abs(s1)**2-abs(y-(7+4*(s1-1)))**2)
