"""@package docstring
helpers.py
@date Jan 8, 2022
@author Harper Weigle
@brief miscellaneous functions that are heavily repeated to clean up main code base. Mostly common equations
"""
import math

def distance(x1, y1, x2, y2):
    '''
    @brief      calculates the distance between two points. d=sqrt((x2-x1)^2+(y2-y1)^2)
    @param      x1 - x coordinate of point 1; Type: float
                y1 - y coordinate of point 1; Type: float
                x2 - x coordinate of point 2; Type: float
                y2 - y coordinate of point 2; Type: float
    @returns    result of the distance equation
    '''
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def midpoint(x1, y1, x2, y2):
    '''
    @brief      calculates the midpoint between two points. (xm,ym)=((x1+x2)/2,(y1+y2)/2)
    @param      x1 - x coordinate of point 1; Type: float
                y1 - y coordinate of point 1; Type: float
                x2 - x coordinate of point 2; Type: float
                y2 - y coordinate of point 2; Type: float
    @returns    result of the midpoint equation
    '''
    return ((x1+x2)/2,(y1+y2)/2)
