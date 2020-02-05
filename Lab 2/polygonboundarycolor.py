from graphics import *

win = GraphWin("", 500, 500)

line1 = Line(Point(250,100),Point(250+100,100+100))
line1.setFill("red")
line1.draw(win)

line2 = Line(Point(250+100,100+100),Point(250+100,100+100+100))
line2.setFill("green")
line2.draw(win)

line3 = Line(Point(250+100,100+100+100),Point(250-100,100+100+100))
line3.setFill("blue")
line3.draw(win)

line4 = Line(Point(250-100,100+100+100),Point(250-100,100+100))
line4.setFill("red")
line4.draw(win)

line5 = Line(Point(250-100,100+100),Point(250,100))
line5.setFill("green")
line5.draw(win)

win.getMouse() 
win.close()