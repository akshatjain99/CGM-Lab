from graphics import *
from math import *
win = GraphWin("", 200, 200)

def midPointCircleDraw(xc,  
                       yc, r): 
  
    x = r 
    y = 0

    Point(x+xc,y+yc).draw(win)

    if (r > 0) : 
      
        Point(x+xc,-y+yc).draw(win)
        Point(y+xc,x+yc).draw(win)
        Point(-y+xc,x+yc).draw(win)
      
    P = 1 - r  
    while (x > y) : 
      
        y += 1
        if (P <= 0):  
            P = P + 2 * y + 1

        else:          
            x -= 1
            P = P + 2 * y - 2 * x + 1

        if (x < y): 
            break


        Point(x+xc,y+yc).draw(win)
        Point(-x+xc,y+yc).draw(win)
        Point(x+xc,-y+yc).draw(win)
        Point(-x+xc,-y+yc).draw(win)

        if (x != y) : 
            
            Point(y+xc,x+yc).draw(win)
            Point(-y+xc,x+yc).draw(win)
            Point(y+xc,-x+yc).draw(win)
            Point(-y+xc,-x+yc).draw(win)

midPointCircleDraw(100,100,50)