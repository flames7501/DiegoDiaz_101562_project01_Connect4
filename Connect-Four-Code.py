from graphics import *

def main():
    #Create the connect four board
    win = GraphWin("Connect 4!", 840, 720)
    background = Rectangle(Point(0,0), Point(840,720))
    background.setFill("dodgerblue")
    background.setOutline("dodgerblue")
    background.draw(win)
    for i in range(120, 840, 120):
        line = Line(Point(i, 0), Point(i, 720))
        line.draw(win)
    for i in range(60, 840, 120):
        for j in range(60, 720, 120):
            hole = Circle (Point(i, j), 37.5)
            hole.setFill("white")
            hole.setOutline("white")
            hole.draw(win)
            
    #Setting up default values
    a, b, c, d, e, f, g, k = 0, 0, 0, 0, 0, 0, 0, 0

    #Connect four!
    while (k < 42):
        #Yellow's turn
        turnend = False
        while(turnend is False):
            p = win.getMouse()
            x = p.getX()
            y = p.getY()
            if (x >= 0 and x < 120):
                if (a >= 6):
                    turnend = False
                else:    
                    check = 660 - (120 * a)
                    chip = Circle(Point(60, check), 37.5)
                    chip.setFill("yellow")
                    chip.setOutline("yellow")
                    a = a + 1
                    chip.draw(win)
                    turnend = True
            if (x >= 120 and x < 240):
                if (b >= 6):
                    pass
                else:    
                    check = 660 - (120 * b)
                    chip = Circle(Point(180, check), 37.5)
                    chip.setFill("yellow")
                    chip.setOutline("yellow")
                    b = b + 1
                    chip.draw(win)
                    turnend = True
            if (x >= 240 and x < 360):
                if (c >= 6):
                    pass
                else:    
                    check = 660 - (120 * c)
                    chip = Circle(Point(300, check), 37.5)
                    chip.setFill("yellow")
                    chip.setOutline("yellow")
                    c = c + 1
                    chip.draw(win)
                    turnend = True
            if (x >= 360 and x < 480):
                if (d >= 6):
                    pass
                else:    
                    check = 660 - (120 * d)
                    chip = Circle(Point(420, check), 37.5)
                    chip.setFill("yellow")
                    chip.setOutline("yellow")
                    d = d + 1
                    chip.draw(win)
                    turnend = True
            if (x >= 480 and x < 600):
                if (e >= 6):
                    pass
                else:    
                    check = 660 - (120 * e)
                    chip = Circle(Point(540, check), 37.5)
                    chip.setFill("yellow")
                    chip.setOutline("yellow")
                    e = e + 1
                    chip.draw(win)
                    turnend = True
            if (x >= 600 and x < 720):
                if (f >= 6):
                    pass
                else:    
                    check = 660 - (120 * f)
                    chip = Circle(Point(660, check), 37.5)
                    chip.setFill("yellow")
                    chip.setOutline("yellow")
                    f = f + 1
                    chip.draw(win)
                    turnend = True
            if (x >= 720 and x <= 840):
                if (g >= 6):
                    pass
                else:    
                    check = 660 - (120 * g)
                    chip = Circle(Point(780, check), 37.5)
                    chip.setFill("yellow")
                    chip.setOutline("yellow")
                    g = g + 1
                    chip.draw(win)
                    turnend = True
        k = k + 1
        #Red's turn
        turnend = False
        while(turnend is False):
            p = win.getMouse()
            x = p.getX()
            y = p.getY()
            if (x >= 0 and x < 120):
                if (a >= 6):
                    turnend = False
                else:    
                    check = 660 - (120 * a)
                    chip = Circle(Point(60, check), 37.5)
                    chip.setFill("red")
                    chip.setOutline("red")
                    a = a + 1
                    chip.draw(win)
                    turnend = True
            if (x >= 120 and x < 240):
                if (b >= 6):
                    pass
                else:    
                    check = 660 - (120 * b)
                    chip = Circle(Point(180, check), 37.5)
                    chip.setFill("red")
                    chip.setOutline("red")
                    b = b + 1
                    chip.draw(win)
                    turnend = True
            if (x >= 240 and x < 360):
                if (c >= 6):
                    pass
                else:    
                    check = 660 - (120 * c)
                    chip = Circle(Point(300, check), 37.5)
                    chip.setFill("red")
                    chip.setOutline("red")
                    c = c + 1
                    chip.draw(win)
                    turnend = True
            if (x >= 360 and x < 480):
                if (d >= 6):
                    pass
                else:    
                    check = 660 - (120 * d)
                    chip = Circle(Point(420, check), 37.5)
                    chip.setFill("red")
                    chip.setOutline("red")
                    d = d + 1
                    chip.draw(win)
                    turnend = True
            if (x >= 480 and x < 600):
                if (e >= 6):
                    pass
                else:    
                    check = 660 - (120 * e)
                    chip = Circle(Point(540, check), 37.5)
                    chip.setFill("red")
                    chip.setOutline("red")
                    e = e + 1
                    chip.draw(win)
                    turnend = True
            if (x >= 600 and x < 720):
                if (f >= 6):
                    pass
                else:    
                    check = 660 - (120 * f)
                    chip = Circle(Point(660, check), 37.5)
                    chip.setFill("red")
                    chip.setOutline("red")
                    f = f + 1
                    chip.draw(win)
                    turnend = True
            if (x >= 720 and x <= 840):
                if (g >= 6):
                    pass
                else:    
                    check = 660 - (120 * g)
                    chip = Circle(Point(780, check), 37.5)
                    chip.setFill("red")
                    chip.setOutline("red")
                    g = g + 1
                    chip.draw(win)
                    turnend = True
        k = k + 1
    #Final click to close the program
    win.getMouse()
    win.close()
    
main()
