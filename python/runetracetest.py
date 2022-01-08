"""@package docstring
runetracetest.py
@date Jan 8, 2022
@author Harper Weigle
@brief main app for rune trace test. Handles main loop and core app functions
"""

import sys
import tkinter as tk

from runes import *
from helpers import *

CANVASWIDTH = 800
CANVASHEIGHT = 400
RESOLUTION = 100
WIGGLE = 20

class App(tk.Tk):
    '''
    @brief  core app class handles tkinter root functions as well as core app functions. Must be initialized before functional
            Child of tk.Tk
    '''
    def __init__(self):
        '''
        @brief      Initializes:
                    super()
                    title - tk app title; Type: tk.title
                    canvas - app window; Type: tk.canvas
                    scale - starting value of relative fib sequence; Type: int
                    scale_mod - 0 = Null, >0 = Grow, <0 = Shrink; Type: int
                    status - stage of rune user is in; Type: tk.StringVar
                    statusLabel - status displayed on canvas; Type: tk.Label

                    binds mouse motion to checkCursor()
        @param      None
        @returns    None
        '''
        super().__init__()
        self.title("Rune Trace Test")
        self.canvas = tk.Canvas(self, width=CANVASWIDTH, height=CANVASHEIGHT)
        self.canvas.pack()
        self.scale = 10
        self.scale_mod = 0
        self.status = tk.StringVar()
        self.status.set("None")
        self.statusLabel = tk.Label(self.canvas, textvariable=self.status)

        self.canvas.bind('<Motion>', self.checkCursor)

    def update(self):
        '''
        @brief      clears canvas, redraws canvas items, and reschedules self
        @param     None
        @returns    None
        '''
        self.canvas.delete("all")
        self.drawCoordPlane()
        self.drawFireRune()
        self.statusLabel.place(x=1,y=1)
        self.canvas.pack()
        self.canvas.after(1000, self.update)

    def drawCoordPlane(self):
        '''
        @brief      Draws cartesian plane
        @param     None
        @returns    None
        '''
        self.canvas.create_line(CANVASWIDTH/2,0,CANVASWIDTH/2,CANVASHEIGHT)
        self.canvas.create_line(0,CANVASHEIGHT/2,CANVASWIDTH,CANVASHEIGHT/2)

    def checkCursor(self, e):
        '''
        @brief      Checks cursor location relative to rune. Updates status, scale_mod, and scale
        @param     e - trigger event; Type: tk.Event
        @returns    None
        '''
        fib1 = self.scale
        fib2 = fib1+1
        fib3 = fib1+fib2
        fib4 = fib2+fib3
        rune_start = self.zeroToTrueCoord(0, Fire.stageOneY(0,fib1))
        if(distance(e.x,e.y,rune_start[0],rune_start[1]) < WIGGLE):
            self.status.set("Stage One")
        else:
            zeroed_cursor = self.trueToZeroCoord(e.x,e.y)
            if(self.status.get() == "Stage One"):
                rune_y = Fire.stageOneY(zeroed_cursor[0],fib1)
                rune_x = Fire.stageOneX(zeroed_cursor[1],fib1)
                #TODO out of bounds does not find nearest point. Instead it just uses valid coordinate
                if(rune_y is not None and rune_x is not None):
                    rune_mp = midpoint(rune_x,zeroed_cursor[1],zeroed_cursor[0],
                            rune_y)
                elif(rune_y is None and rune_x is not None):
                    new_y = Fire.stageOneY(rune_x, fib1)
                    rune_mp = (rune_x, new_y)
                elif(rune_x is None and rune_y is not None):
                    new_x = Fire.stageOneX(rune_y, fib1)
                    rune_mp = (new_x, rune_y)
                else:
                    self.status.set("None")
                    return
                d = distance(rune_mp[0],rune_mp[1],zeroed_cursor[0],zeroed_cursor[1])
                if(d > WIGGLE):
                    if(self.scale_mod == 0):
                        if(zeroed_cursor[0] > rune_mp[0]):
                            self.scale_mod = -1
                            self.scale -= 1
                        elif(zeroed_cursor[0] < rune_mp[0]):
                            self.scale_mod = 1
                            self.scale += 1
                        else:
                            print("Should never get here. Cursor to MP distance > {0} but Cursor x: {1} == MP x {2}".format(WIGGLE,zeroed_cursor[0],rune_mp[0]))
                    elif(self.scale_mod < 0):
                        if(zeroed_cursor[0] > rune_mp[0]):
                            self.scale -= 1
                        elif(zeroed_cursor[0] < rune_mp[0]):
                            self.scale_mod = 0
                            self.status.set("None")
                            return
                        else:
                            print("Should never get here. Cursor to MP distance > {} but Cursor x == MP x".format(WIGGLE))
                    else:
                        if(zeroed_cursor[0] > rune_mp[0]):
                            self.scale_mod = 0
                            self.status.set("None")
                            return
                        elif(zeroed_cursor[0] < rune_mp[0]):
                            self.scale += 1
                        else:
                            print("Should never get here. Cursor to MP distance > {} but Cursor x == MP x".format(WIGGLE))
                stage2_start_y = Fire.stageTwoY(fib1,fib1,fib2,fib3)
                stage2_start_x = Fire.stageTwoX(stage2_start_y,fib1,fib2)
                d = distance(zeroed_cursor[0],zeroed_cursor[1], stage2_start_x,
                    stage2_start_y)
                if(d < WIGGLE):
                    self.status.set("Stage Two")
            elif(self.status.get() == "Stage Two"):
                stage2_start_y = Fire.stageTwoY(fib1,fib1,fib2,fib3)
                stage2_start_x = Fire.stageTwoX(stage2_start_y,fib1,fib2)
                d = distance(zeroed_cursor[0],zeroed_cursor[1], stage2_start_x,
                    stage2_start_y)
                if(d < WIGGLE):
                    self.status.set("Stage Two")
                else:
                    rune_y = Fire.stageTwoY(zeroed_cursor[0],fib1,fib2,fib3)
                    rune_x = Fire.stageTwoX(zeroed_cursor[1],fib1,fib2)
                    #TODO out of bounds does not find nearest point. Instead it just uses valid coordinate
                    if(rune_y is not None and rune_x is not None):
                        rune_mp = midpoint(rune_x,zeroed_cursor[1],zeroed_cursor[0],
                                rune_y)
                    elif(rune_y is None and rune_x is not None):
                        new_y = Fire.stageTwoY(rune_x, fib1, fib2, fib3)
                        rune_mp = (rune_x, new_y)
                    elif(rune_x is None and rune_y is not None):
                        new_x = Fire.stageTwoX(rune_y, fib1, fib2)
                        rune_mp = (new_x, rune_y)
                    else:
                        self.status.set("None")
                        return
                    d = distance(rune_mp[0],rune_mp[1],zeroed_cursor[0],zeroed_cursor[1])
                    if(d > WIGGLE):
                        self.status.set("None")
                        return
                    stage3_start_y = Fire.stageThreeY(fib3,fib1,fib3)
                    stage3_start_x = Fire.stageThreeX(stage3_start_y,fib1,fib3,fib4)
                    d = distance(zeroed_cursor[0],zeroed_cursor[1], stage3_start_x,
                        stage3_start_y)
                    if(d < WIGGLE):
                        self.status.set("Stage Three")
            elif(self.status.get() == "Stage Three"):
                stage3_start_y = Fire.stageThreeY(fib3,fib1,fib3)
                stage3_start_x = Fire.stageThreeX(stage3_start_y,fib1,fib3,fib4)
                d = distance(zeroed_cursor[0],zeroed_cursor[1], stage3_start_x, stage3_start_y)
                if(d < WIGGLE):
                    self.status.set("Stage Three")
                else:
                    rune_y = Fire.stageThreeY(zeroed_cursor[0],fib1,fib3)
                    rune_x = Fire.stageThreeX(zeroed_cursor[1],fib1,fib3,fib4)
                    #TODO out of bounds does not find nearest point. Instead it just uses valid coordinate
                    if(rune_y is not None and rune_x is not None):
                        rune_mp = midpoint(rune_x,zeroed_cursor[1],zeroed_cursor[0],
                                rune_y)
                    elif(rune_y is None and rune_x is not None):
                        new_y = Fire.stageThreeY(rune_x, fib1, fib3)
                        rune_mp = (rune_x, new_y)
                    elif(rune_x is None and rune_y is not None):
                        new_x = Fire.stageThreeX(rune_y, fib1, fib3, fib4)
                        rune_mp = (new_x, rune_y)
                    else:
                        self.status.set("None")
                        return
                    d = distance(rune_mp[0],rune_mp[1],zeroed_cursor[0],zeroed_cursor[1])
                    if(d > WIGGLE):
                        self.status.set("None")
                        return
                    stage4_start_y = Fire.stageFourY(0,fib4)
                    stage4_start_x = Fire.stageFourX(stage4_start_y,fib4)
                    d = distance(zeroed_cursor[0],zeroed_cursor[1], stage4_start_x,
                        stage4_start_y)
                    if(d < WIGGLE):
                        self.status.set("Stage Four")
            elif(self.status.get() == "Stage Four"):
                stage4_start_y = Fire.stageFourY(0,fib4)
                stage4_start_x = Fire.stageFourX(stage4_start_y,fib4)
                d = distance(zeroed_cursor[0],zeroed_cursor[1], stage4_start_x, stage4_start_y)
                if(d < WIGGLE):
                    self.status.set("Stage Four")
                else:
                    rune_y = Fire.stageFourY(zeroed_cursor[0],fib4)
                    rune_x = Fire.stageFourX(zeroed_cursor[1],fib4)
                    #TODO out of bounds does not find nearest point. Instead it just uses valid coordinate
                    if(rune_y is not None and rune_x is not None):
                        rune_mp = midpoint(rune_x,zeroed_cursor[1],zeroed_cursor[0],
                                rune_y)
                    elif(rune_y is None and rune_x is not None):
                        new_y = Fire.stageFourY(rune_x,fib4)
                        rune_mp = (rune_x, new_y)
                    elif(rune_x is None and rune_y is not None):
                        new_x = Fire.stageFourX(rune_y,fib4)
                        rune_mp = (new_x, rune_y)
                    else:
                        self.status.set("None")
                        return
                    d = distance(rune_mp[0],rune_mp[1],zeroed_cursor[0],zeroed_cursor[1])
                    if(d > WIGGLE):
                        self.status.set("None")
                        return
                    stage5_start_y = Fire.stageFiveY(-1*fib4,fib4)
                    stage5_start_x = Fire.stageFiveX(stage5_start_y,fib4)
                    d = distance(zeroed_cursor[0],zeroed_cursor[1], stage5_start_x,
                        stage5_start_y)
                    if(d < WIGGLE):
                        self.status.set("Stage Five")
            elif(self.status.get() == "Stage Five"):
                stage5_start_y = Fire.stageFiveY(-1*fib4,fib4)
                stage5_start_x = Fire.stageFiveX(stage5_start_y,fib4)
                d = distance(zeroed_cursor[0],zeroed_cursor[1], stage5_start_x, stage5_start_y)
                if(d < WIGGLE):
                    self.status.set("Stage Five")
                else:
                    rune_y = Fire.stageFiveY(zeroed_cursor[0],fib4)
                    rune_x = Fire.stageFiveX(zeroed_cursor[1],fib4)
                    #TODO out of bounds does not find nearest point. Instead it just uses valid coordinate
                    if(rune_y is not None and rune_x is not None):
                        rune_mp = midpoint(rune_x,zeroed_cursor[1],zeroed_cursor[0],
                                rune_y)
                    elif(rune_y is None and rune_x is not None):
                        new_y = Fire.stageFiveY(rune_x,fib4)
                        rune_mp = (rune_x, new_y)
                    elif(rune_x is None and rune_y is not None):
                        new_x = Fire.stageFiveX(rune_y,fib4)
                        rune_mp = (new_x, rune_y)
                    else:
                        self.status.set("None")
                        return
                    d = distance(rune_mp[0],rune_mp[1],zeroed_cursor[0],zeroed_cursor[1])
                    if(d > WIGGLE):
                        self.status.set("None")
                        return
                    stage6_start_y = Fire.stageSixY(0,fib1)
                    stage6_start_x = Fire.stageSixX(stage6_start_y,fib1,fib4)
                    d = distance(zeroed_cursor[0],zeroed_cursor[1], stage6_start_x,
                        stage6_start_y)
                    if(d < WIGGLE):
                        self.status.set("Stage Six")
            elif(self.status.get() == "Stage Six"):
                stage6_start_y = Fire.stageSixY(0,fib1)
                stage6_start_x = Fire.stageSixX(stage6_start_y,fib1,fib4)
                d = distance(zeroed_cursor[0],zeroed_cursor[1], stage6_start_x, stage6_start_y)
                if(d < WIGGLE):
                    self.status.set("Stage Six")
                else:
                    rune_y = Fire.stageSixY(zeroed_cursor[0],fib1)
                    rune_x = Fire.stageSixX(zeroed_cursor[1],fib1,fib4)
                    #TODO out of bounds does not find nearest point. Instead it just uses valid coordinate
                    if(rune_y is not None and rune_x is not None):
                        rune_mp = midpoint(rune_x,zeroed_cursor[1],zeroed_cursor[0],
                                rune_y)
                    elif(rune_y is None and rune_x is not None):
                        new_y = Fire.stageSixY(rune_x,fib1)
                        rune_mp = (rune_x, new_y)
                    elif(rune_x is None and rune_y is not None):
                        new_x = Fire.stageSixX(rune_y,fib1,fib4)
                        rune_mp = (new_x, rune_y)
                    else:
                        self.status.set("None")
                        return
                    d = distance(rune_mp[0],rune_mp[1],zeroed_cursor[0],zeroed_cursor[1])
                    if(d > WIGGLE):
                        self.status.set("None")
                        return
                    stage6_end_y = Fire.stageSixY(fib1,fib1)
                    stage6_end_x = Fire.stageSixX(stage6_end_y,fib1,fib4)
                    d = distance(zeroed_cursor[0],zeroed_cursor[1], stage6_end_x,
                        stage6_end_y)
                    if(d < WIGGLE):
                        self.status.set("None")
                        print("Fire Rune Complete")

    def drawFireRune(self):
        '''
        @brief      draws fire rune based on stages defined in rune.py
        @param     None
        @returns    None
        '''
        y=0
        fib1 = self.scale
        fib2 = fib1+1
        fib3 = fib1+fib2
        fib4 = fib2+fib3
        for x in range(0,fib1*RESOLUTION,1):
            y=Fire.stageOneY(x/RESOLUTION,fib1)
            coords=self.zeroToTrueCoord(x/RESOLUTION,y)
            self.canvas.create_oval(coords[0],coords[1],coords[0],coords[1],
                    outline="blue",width=2)
        for x in range(fib1*RESOLUTION,fib3*RESOLUTION,1):
            y=Fire.stageTwoY(x/RESOLUTION,fib1,fib2,fib3)
            coords=self.zeroToTrueCoord(x/RESOLUTION,y)
            self.canvas.create_oval(coords[0],coords[1],coords[0],coords[1],
                    outline="red",width=2)
        for x in range(0,fib3*RESOLUTION,1):
            y=Fire.stageThreeY(x/RESOLUTION,fib1,fib3)
            coords=self.zeroToTrueCoord(x/RESOLUTION,y)
            self.canvas.create_oval(coords[0],coords[1],coords[0],coords[1],
                    outline="blue",width=2)
        for x in range(-1*fib4*RESOLUTION,0,1):
            y=Fire.stageFourY(x/RESOLUTION,fib4)
            coords=self.zeroToTrueCoord(x/RESOLUTION,y)
            self.canvas.create_oval(coords[0],coords[1],coords[0],coords[1],
                    outline="red",width=2)
        for x in range(-1*fib4*RESOLUTION,0,1):
            y=Fire.stageFiveY(x/RESOLUTION,fib4)
            coords=self.zeroToTrueCoord(x/RESOLUTION,y)
            self.canvas.create_oval(coords[0],coords[1],coords[0],coords[1],
                    outline="blue",width=2)
        for x in range(0,fib1*RESOLUTION,1):
            y=Fire.stageSixY(x/RESOLUTION,fib1)
            coords=self.zeroToTrueCoord(x/RESOLUTION,y)
            self.canvas.create_oval(coords[0],coords[1],coords[0],coords[1],
                    outline="red",width=2)

    def zeroToTrueCoord(self, x, y):
        '''
        @brief      Converts coordinates relative to the cartesian plane to coordinates relative to the canvas
        @param     x - x coordinate; Type: float
                    y - y coordinate; Type: float
        @returns    Converted coordinates; Type: tuple(float,float)
        '''
        if(abs(x) > CANVASWIDTH/2 or abs(y) > CANVASHEIGHT/2):
            print("Error: coordinate out of bounds")
        return (CANVASWIDTH/2+x,CANVASHEIGHT-(CANVASHEIGHT/2+y))

    def trueToZeroCoord(self, x, y):
        '''
        @brief      Converts coordinates relative to the canvas to coordinates relative to the cartesian plane
        @param     x - x coordinate; Type: float
                    y - y coordinate; Type: float
        @returns    Converted coordinates; Type: tuple(float,float)
        '''
        if(x < 0 or x > CANVASWIDTH or y < 0 or y > CANVASHEIGHT):
            print("Error: coordinate out of bounds")
        return (x-CANVASWIDTH/2,(-1*y)+(CANVASHEIGHT/2))

def main():
    '''
    @brief      initializes app, starts app.update recursive cycle, executes mainloop
    @param     None
    @returns    None
    '''
    app = App()
    app.update()
    app.canvas.mainloop()

if __name__ == "__main__":
    sys.exit(main())
