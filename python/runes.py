"""@package docstring
runes.py
@date Jan 8, 2022
@author Harper Weigle
@brief file to contain rune specific equations
"""

import math

class Fire():
    '''
    @brief class has no initialization because it does not store member variables. It simply organizes stages of the rune by rune
    '''
    def stageOneY(x,s1):
        '''
        @brief      calculates stage one given x: y=sqrt(s1^2-(x-s1)^2)-(s1-1)
        @param      x - x coordinate of rune stage; Type: float
                    s1 - first value in relative fib sequence; Type: float
        @returns    None if x > s1 or if x < 0. Result of equation otherwise
        '''
        if(x > s1 or x < 0):
            return None
        return math.sqrt(abs(s1)**2-(abs(x-s1))**2)-(s1-1)

    def stageOneX(y,s1):
        '''
        @brief      calculates stage one given y: x=-sqrt(s1^2-(y+(s1-1)^2)-s1)
        @param      y - y coordinate of rune stage; Type: float
                    s1 - first value in relative fib sequence; Type: float
        @returns    None if y > 1 or if y < -(s1-1). Result of equation otherwise
        '''
        if(y > 1 or y < -1*(s1-1)):
            return None
        return -1*(math.sqrt(abs(s1)**2-abs(y+(s1-1))**2)-s1)

    def stageTwoY(x,s1,s2,s3):
        '''
        @brief      calculates stage two given x: y=sqrt(s2^2-(x-s1)^2)-s1
        @param      x - x coordinate of rune stage; Type: float
                    s1 - first value in relative fib sequence; Type: float
                    s2 - second value in relative fib sequence; Type: float
                    s3 - third value in relative fib sequence; Type: float
        @returns    None if x > s3 or if x < s1. Result of equation otherwise
        '''
        if(x < s1 or x > s3):
            return None
        return math.sqrt(abs(s2)**2-(abs(x-s1))**2)-s1

    def stageTwoX(y,s1,s2):
        '''
        @brief      calculates stage two given y: x=sqrt(s2^2-(y+s1)^2)+s1
        @param      y - y coordinate of rune stage; Type: float
                    s1 - first value in relative fib sequence; Type: float
                    s2 - second value in relative fib sequence; Type: float
        @returns    None if y > 1 or if y < -(s1-1). Result of equation otherwise
        '''
        if(y > 1 or y < -1*s1):
            return None
        return math.sqrt(abs(s2)**2-(abs(y+s1))**2)+s1

    def stageThreeY(x,s1,s3):
        '''
        @brief      calculates stage three given x: y=-sqrt(s3^2-x^2)-s1
        @param      x - x coordinate of rune stage; Type: float
                    s1 - first value in relative fib sequence; Type: float
                    s3 - third value in relative fib sequence; Type: float
        @returns    None if x > s3 or if x < 0. Result of equation otherwise
        '''
        if(x < 0 or x > s3):
            return None
        return -1*math.sqrt(abs(s3)**2-abs(x)**2)-s1

    def stageThreeX(y,s1,s3,s4):
        '''
        @brief      calculates stage three given y: x=sqrt(s3^2-(y+s1)^2)
        @param      y - y coordinate of rune stage; Type: float
                    s1 - first value in relative fib sequence; Type: float
                    s3 - third value in relative fib sequence; Type: float
                    s4 - fourth value in relative fib sequence; Type: float
        @returns    None if y > -s1 or if y < -(s4-1). Result of equation otherwise
        '''
        if(y > -1*s1 or y < -1*(s4-1)):
            return None
        return math.sqrt(abs(s3)**2-abs(y+s1)**2)

    def stageFourY(x,s4):
        '''
        @brief      calculates stage four given x: y=-sqrt(s4^2-x^2)+1
        @param      x - x coordinate of rune stage; Type: float
                    s4 - fourth value in relative fib sequence; Type: float
        @returns    None if x > 0 or if x < -s4. Result of equation otherwise
        '''
        if(x > 0 or x < -1*s4):
            return None
        return -1*math.sqrt(abs(s4)**2-abs(x)**2)+1

    def stageFourX(y,s4):
        '''
        @brief      calculates stage four given y: x=-sqrt(s4^2-(y-1)^2)
        @param      y - y coordinate of rune stage; Type: float
                    s4 - fourth value in relative fib sequence; Type: float
        @returns    None if y > 0 or if y < -(s4-1). Result of equation otherwise
        '''
        if(y < -1*(s4-1) or y > 0):
            return None
        return -1*math.sqrt(abs(s4)**2-abs(y-1)**2)

    def stageFiveY(x,s4):
        '''
        @brief      calculates stage five given x: y=sqrt(s4^2-x^2)+1
        @param      x - x coordinate of rune stage; Type: float
                    s4 - fourth value in relative fib sequence; Type: float
        @returns    None if x > 0 or if x < -s4. Result of equation otherwise
        '''
        if(x > 0 or x < -1*s4):
            return None
        return math.sqrt(abs(s4)**2-abs(x)**2)+1

    def stageFiveX(y,s4):
        '''
        @brief      calculates stage five given y: x=-sqrt(s4^2-(y-1)^2)
        @param      y - y coordinate of rune stage; Type: float
                    s4 - fourth value in relative fib sequence; Type: float
        @returns    None if y > s4+1 or if y < 0. Result of equation otherwise
        '''
        if(y < 0 or y > s4+1):
            return None
        return -1*math.sqrt(abs(s4)**2-abs(y-1)**2)

    def stageSixY(x,s1):
        '''
        @brief      calculates stage six given x: y=-sqrt(s1^2-x^2)+7+4(s1-1)
        @param      x - x coordinate of rune stage; Type: float
                    s1 - first value in relative fib sequence; Type: float
        @returns    None if x > s1 or if x < 0. Result of equation otherwise
        '''
        if(x < 0 or x > s1):
            return None
        return -1*math.sqrt(abs(s1)**2-abs(x)**2)+(7+4*(s1-1))

    def stageSixX(y,s1,s4):
        '''
        @brief      calculates stage five given y: \f\x=sqrt{(s_1^2-(y-(7+4(s_1)))^2)}\fmath.sqrt(s1^2-y-(7+4(s1-1))^2)
        @param      y - y coordinate of rune stage; Type: float
                    s1 - first value in relative fib sequence; Type: float
                    s4 - fourth value in relative fib sequence; Type: float
        @returns    None if y > 7+4(s_1-1) or if y < s4. Result of equation otherwise
        '''
        if(y > 7+4*(s1-1) or y < s4):
            return None
        return math.sqrt(abs(s1)**2-abs(y-(7+4*(s1-1)))**2)
