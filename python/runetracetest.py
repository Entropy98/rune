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
        self.scale = 7
        self.status = tk.StringVar()
        self.status.set("None")
        self.statusLabel = tk.Label(self.canvas, textvariable=self.status)

        self.canvas.bind('<Motion>', self.checkCursor)

    def update(self):
        self.canvas.delete("all")
        self.drawFireRune()
        self.statusLabel.place(x=1,y=1)
        self.canvas.pack()
        self.canvas.after(1000, self.update)

    def checkCursor(self, e):
        rune_start = self.zeroToTrueCoord(0,
                Fire.stageOneY(0,self.nthFib(self.scale),self.scale, self.nthFib))
        if(distance(e.x,e.y,rune_start[0],rune_start[1]) < WIGGLE):
            self.status.set("Stage One")
        else:
            if(self.status.get() == "Stage One"):
                zeroedCursor = self.trueToZeroCoord(e.x,e.y)
                runeY = Fire.stageOneY(zeroedCursor[0],self.nthFib(self.scale),
                        self.scale, self.nthFib)
                runeX = Fire.stageOneX(zeroedCursor[1],self.nthFib(self.scale),
                        self.scale, self.nthFib)
                runeMP = midpoint(runeX, e.y, e.x, runeY)
                if(distance(runeMP[0],runeMP[1],e.x,e.y) > WIGGLE):
                    self.status.set("None")

    def drawFireRune(self):
        y=0
        fib1 = self.nthFib(self.scale)
        fib2 = self.nthFib(self.scale+1)
        fib3 = fib1+fib2
        for x in range(0,fib1*RESOLUTION,1):
            y=Fire.stageOneY(x/RESOLUTION,fib1,self.scale,self.nthFib)
            coords=self.zeroToTrueCoord(x/RESOLUTION,y)
            self.canvas.create_oval(coords[0],coords[1],coords[0],coords[1],
                    outline="blue",width=2)
        for x in range(fib1*RESOLUTION,fib3*RESOLUTION,1):
            y=Fire.stageTwoY(x/RESOLUTION,fib2,self.scale,self.nthFib)
            coords=self.zeroToTrueCoord(x/RESOLUTION,y)
            self.canvas.create_oval(coords[0],coords[1],coords[0],coords[1],
                    outline="red",width=2)
        for x in range(0,fib3*RESOLUTION,1):
            y=Fire.stageThreeY(x/RESOLUTION,fib3,self.scale,self.nthFib)
            coords=self.zeroToTrueCoord(x/RESOLUTION,y)
            self.canvas.create_oval(coords[0],coords[1],coords[0],coords[1],
                    outline="blue",width=2)
        fib4 = fib2+fib3
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
            y=Fire.stageSixY(x/RESOLUTION,fib1,self.scale, self.nthFib)
            coords=self.zeroToTrueCoord(x/RESOLUTION,y)
            self.canvas.create_oval(coords[0],coords[1],coords[0],coords[1],
                    outline="red",width=2)

    def zeroToTrueCoord(self, x, y):
        if(abs(x) > CANVASWIDTH/2 or abs(y)>CANVASHEIGHT/2):
            print("Error: coordinate out of bounds")
        return (CANVASWIDTH/2+x,CANVASHEIGHT-(CANVASHEIGHT/2+y))

    def trueToZeroCoord(self, x, y):
        if(x < 0 or x > CANVASWIDTH or y < 0 or y > CANVASHEIGHT):
            print("Error: coordinate out of bounds")
        return (x-CANVASWIDTH/2,y-(CANVASHEIGHT-CANVASHEIGHT/2))

    def nthFib(self, n, fib1=1, fib2=1, i=0):
        if(i >= n):
            return fib2
        return self.nthFib(n, fib2, fib1+fib2, i+1)

def main():
    app = App()
    app.update()
    app.canvas.mainloop()

if __name__ == "__main__":
    sys.exit(main())
