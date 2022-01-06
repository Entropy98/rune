import sys
import tkinter as tk

from runes import *

CANVASWIDTH = 800
CANVASHEIGHT = 400
RESOLUTION = 100

def App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rune Trace Test")
        self.canvas = tk.Canvas(self, width=CANVASWIDTH, height=CANVASHEIGHT)
        self.scale = 1

    def update(self):
        self.canvas.delete("all")
        self.canvas.after(1000, self.update)

    def drawFireRune(self):
        y=0
        fib1 = self.scale
        fib2 = fib1+self.scale
        fib3 = fib1+fib2
        for x in range(0,1,1/RESOLUTION):
            y=Fire.stageOne(x,fib1)
            coords=self.zeroCoord(x,y)
            self.canvas.create_oval(coords[0].coords[1].coords[0],coords[1],
                    fill="black",width=2)
        for x in range(1,3,1/RESOLUTION):
            y=Fire.stageTwo(x,fib2)
            coords=self.zeroCoord(x,y)
            self.canvas.create_oval(coords[0].coords[1].coords[0],coords[1],
                    fill="black",width=2)
        for x in range(0,3,1/RESOLUTION):
            y=Fire.stageTwo(x,fib3)
            coords=self.zeroCoord(x,y)
            self.canvas.create_oval(coords[0].coords[1].coords[0],coords[1],
                    fill="black",width=2)

    def zeroCoord(x,y):
        if(abs(x) > CANVASWIDTH/2 or abs(y)>CANVASHEIGHT/2):
            print("Error: coordinate out of bounds")
            return
        return (CANVASWIDTH/2+x,-1*(CANVASHEIGHT/2+y))

    def nthFib(n, fib1=1, fib2=1, i=0):
        if(i >= n):
            return fib2
        self.nthFib(n, fib2, fib1+fib2, i+1)

def main():
    app = App()
    app.update()
    app.canvas.mainloop()

if __name__ == "__main__":
    sys.exit(main())
