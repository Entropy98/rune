import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def midpoint(x1, y1, x2, y2):
    return ((x1+x2)/2,(y1+y2)/2)
