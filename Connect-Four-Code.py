from graphics import *

#Defines how a turn will process
def turn(a, b, c, d, e, f, g, k, columns, i, win):
    turnend = False
    #While loop in case a column is full
    while(turnend == False):
        #Decides which player's turn it is
        if(i == "yellow"):
            print("Yellow player's turn.")
        if(i == "red"):
            print("Red player's turn.")
        #Obtains player's input
        p = win.getMouse()
        x = p.getX()
        y = p.getY()
        #First column
        if (x >= 0 and x < 120):
            if (a >= 6):
                print("The column is full, try again.")
            else:   
                check = 660 - (120 * a)
                chip = Circle(Point(60, check), 37.5)
                chip.setFill(i)
                chip.setOutline(i)
                chip.draw(win)
                columns[0][a] = i
                a = a + 1
                turnend = True
        #Second column
        if (x >= 120 and x < 240):
            if (b >= 6):
                print("The column is full, try again.")
            else:    
                check = 660 - (120 * b)
                chip = Circle(Point(180, check), 37.5)
                chip.setFill(i)
                chip.setOutline(i)
                columns[1][b] = i
                b = b + 1
                chip.draw(win)
                turnend = True
        #Third column
        if (x >= 240 and x < 360):
            if (c >= 6):
                print("The column is full, try again.")
            else:    
                check = 660 - (120 * c)
                chip = Circle(Point(300, check), 37.5)
                chip.setFill(i)
                chip.setOutline(i)
                columns[2][c] = i
                c = c + 1
                chip.draw(win)
                turnend = True
        #Fourth column
        if (x >= 360 and x < 480):
            if (d >= 6):
                print("The column is full, try again.")
            else:    
                check = 660 - (120 * d)
                chip = Circle(Point(420, check), 37.5)
                chip.setFill(i)
                chip.setOutline(i)
                columns[3][d] = i
                d = d + 1
                chip.draw(win)
                turnend = True
        #Fifth column
        if (x >= 480 and x < 600):
            if (e >= 6):
                print("The column is full, try again.")
            else:    
                check = 660 - (120 * e)
                chip = Circle(Point(540, check), 37.5)
                chip.setFill(i)
                chip.setOutline(i)
                columns[4][e] = i
                e = e + 1
                chip.draw(win)
                turnend = True
        #Sixth column
        if (x >= 600 and x < 720):
            if (f >= 6):
                print("The column is full, try again.")
            else:    
                check = 660 - (120 * f)
                chip = Circle(Point(660, check), 37.5)
                chip.setFill(i)
                chip.setOutline(i)
                columns[5][f] = i
                f = f + 1
                chip.draw(win)
                turnend = True
        #Seventh column
        if (x >= 720 and x <= 840):
            if (g >= 6):
                print("The column is full, try again.")
            else:    
                check = 660 - (120 * g)
                chip = Circle(Point(780, check), 37.5)
                chip.setFill(i)
                chip.setOutline(i)
                columns[6][g] = i
                g = g + 1
                chip.draw(win)
                turnend = True
    #Returns updated variables and list
    return a, b, c, d, e, f, g, k, columns

#Defines how the program checks for a win
def check_win(columns, k):
    #Initializes values in case they aren't initialized within the function
    winner = "nobody"
    k = 2
    m = 0
    #Checks for a diagonal win
    for j in range(3, 9):
        previous = "nothing"
        t = j
        p = j
        q = 0
        u = 0
        if(t > 5):
            q = t - 5
            t = t - q
        if(p > 6):
            p = p - (p - 6) - (1 * m)
            m += 1
        for s in range(p + 1):
            w = s + q
            if(w <= p + 1 and w <= 6):
                if(previous == "nothing"):
                    previous = columns[w][t]
                    u += 1
                else:
                    if(previous == columns[w][t]):
                        u += 1
                    else:
                        previous = columns[w][t]
                        u = 1
                if(u >= 4 and previous != None):
                    k = 42
                    winner = previous
            t -= 1
    m = 0
    #Checks for a diagonal win(other side)
    for j in range(3, 9):
        previous = "nothing"
        t = -j - 1
        p = j
        q = 0
        u = 0
        if(t < -6):
            q = t + 6
            t = -6
        if(p > 6):
            p = p - (p - 6) - (1 * m)
            m += 1
        for s in range(p + 1):
            w = s - q
            if(w <= p + 1 and w <= 6):
                if(previous == "nothing"):
                    previous = columns[w][t]
                    u += 1
                else:
                    if(previous == columns[w][t]):
                        u += 1
                    else:
                        previous = columns[w][t]
                        u = 1
                if(u >= 4 and previous != None):
                    k = 42
                    winner = previous
            t += 1
    #Checks for a horizontal win
    for j in range(7):
        u = 0
        previous = "nothing"
        for s in range(6):
            if(previous == "nothing"):
                previous = columns[j][s]
                u += 1
            else:
                if(previous == columns[j][s]):
                    u += 1
                else:
                    previous = columns[j][s]
                    u = 1
            if(u >= 4 and previous != None):
                k = 42
                winner = previous
    #Checks for a vertical win
    for s in range(6):
        u = 0
        previous = "nothing"
        for j in range(7):
            if(previous == "nothing"):
                previous = columns[j][s]
                u += 1
            else:
                if(previous == columns[j][s]):
                    u += 1
                else:
                    previous = columns[j][s]
                    u = 1
            if(u >= 4 and previous != None):
                k = 42
                winner = previous
    if(winner == "red"):
        k = 1
    if(winner == "yellow"):
        k = 0
    return k

#Defines how a winner is decided
def check_winner(k, winner):
    if(winner == 1):
        print("Red player wins!")
        k = 42
    if(winner == 0):
        print("Yellow player wins!")
        k = 42
    if(winner == 2 and k >= 42):
        print("Draw! Nobody wins!")
        k = 42
    return k

#Main program
def main():
    #Creates the connect four board
    win = GraphWin("Connect 4!", 840, 720)
    win.setBackground("dodgerblue")
    for i in range(120, 840, 120):
        line = Line(Point(i, 0), Point(i, 720))
        line.draw(win)
    for i in range(60, 840, 120):
        for j in range(60, 720, 120):
            hole = Circle (Point(i, j), 37.5)
            hole.setFill("white")
            hole.setOutline("white")
            hole.draw(win)
            
    #Initializes default values
    a, b, c, d, e, f, g, k = 0, 0, 0, 0, 0, 0, 0, 0
    columns = [[None] * 6, [None] * 6, [None] * 6, [None] * 6, [None] * 6, [None] * 6, [None] * 6]
    colors = ["yellow", "red"]
    winner = 2
    
    #Connect four game starts here
    #While loop for turn count(max turns = how many holes there are on the board)
    while (k < 42):
        for i in colors:
            #If a winner is decided, stops the while loop
            if(winner == 2):
                #Waits for and stores a player's input
                a, b, c, d, e, f, g, k, columns = turn(a, b, c, d, e, f, g, k, columns, i, win)
                #Check if a win happened
                winner = check_win(columns, k)
                #Increase turn count
                k = k + 1
                #Check for winner, if a winn happened
                k = check_winner(k, winner)       
    #Final click to close the program
    win.getMouse()
    win.close()
    
main()
