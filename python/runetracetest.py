import sys
import tkinter as tk

from runes import *
from helpers import *

CANVASWIDTH = 800
CANVASHEIGHT = 400
RESOLUTION = 100
WIGGLE = 20

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rune Trace Test")
        self.canvas = tk.Canvas(self, width=CANVASWIDTH, height=CANVASHEIGHT)
        self.canvas.pack()
        self.scale = 45
        self.status = tk.StringVar()
        self.status.set("None")
        self.statusLabel = tk.Label(self.canvas, textvariable=self.status)

        self.canvas.bind('<Motion>', self.checkCursor)

    def update(self):
        self.canvas.delete("all")
        self.drawCoordPlane()
        self.drawFireRune()
        self.statusLabel.place(x=1,y=1)
        self.canvas.pack()
        self.canvas.after(1000, self.update)

    def drawCoordPlane(self):
        self.canvas.create_line(CANVASWIDTH/2,0,CANVASWIDTH/2,CANVASHEIGHT)
        self.canvas.create_line(0,CANVASHEIGHT/2,CANVASWIDTH,CANVASHEIGHT/2)

    def checkCursor(self, e):
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
                    self.status.set("None")
                    return
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
        if(abs(x) > CANVASWIDTH/2 or abs(y) > CANVASHEIGHT/2):
            print("Error: coordinate out of bounds")
        return (CANVASWIDTH/2+x,CANVASHEIGHT-(CANVASHEIGHT/2+y))

    def trueToZeroCoord(self, x, y):
        if(x < 0 or x > CANVASWIDTH or y < 0 or y > CANVASHEIGHT):
            print("Error: coordinate out of bounds")
        return (x-CANVASWIDTH/2,(-1*y)+(CANVASHEIGHT/2))

def main():
    app = App()
    app.update()
    app.canvas.mainloop()

if __name__ == "__main__":
    sys.exit(main())
