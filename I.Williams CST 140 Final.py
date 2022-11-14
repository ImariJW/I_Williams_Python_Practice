# Import the random and turtle modules
import random
import turtle
# Adjust the screen size for turtle
screen = turtle.Screen()
screen.setup(1200, 1200)

# Create a list for the user's input
us = []

# Create a list for the runs, wins, and losses
results = []

# Create a tuple for your range of user options to go through the game
options = ('0', '1', '2')

# Personalization***
turtle.screensize(canvwidth=1000, canvheight=100, bg="purple")

turtle.shape('turtle')

# Establish the main function
# Greet the user
# Explain how the game is played
def main():
    turtle.reset()
    turtle.screensize(1000, 1000)
    turtle.shape('turtle')
    turtle.delay(4)
    turt_move(-310, 0)
    turtle.write("Welcome to the Lo Shu Magic Square!", font=("Arial", 35, "bold"))
    turt_move(-375, -280)
    turtle.write("\tIn this game you need to identify"
                 " the correct sequence of numbers\n\n\t from 1-9 that makes each row, each column, and the diagonals"
                 "\n\n\t"
                 " of a 3x3 square equal to '15'. You can choose to enter the"
                 "\n\n\t numbers individually or have a random set of numbers chosen\n\n\t for you."
                 " \n\n\tAre you ready?", font=("Arial", 20, "normal"))
    choice()
    turtle.done()

# Create functions for commonly used code

# To move turtle
def turt_move(x,y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

# The square formation
def turt_square():
    turtle.speed(4)
    turtle.width(3)
    turt_move(-225, 50)

    for x in range(1, 5):
        turtle.forward(450)
        turtle.right(90)

    turtle.width(2)

    turt_move(-75, 50)
    turtle.right(90)
    turtle.forward(450)
    turt_move(75, -400)
    turtle.left(180)
    turtle.forward(450)
    turt_move(-225, -250)
    turtle.right(90)
    turtle.forward(450)
    turt_move(225, -100)
    turtle.left(180)
    turtle.forward(450)

# To go to the next part of the game
# Make sure the user presses the right button.
def next(x, q, f):
    try:
        index = options.index(f)
        if index == 1:
            x()
        elif index == 0:
            results.clear()
            main()
        elif index == 2:
            q()
    except Exception as err:
        print(err)
        turtle.reset()
        turt_move(-400, -50)
        turtle.write("You must enter a number from 0-2.\n1:Redo\n2:Try it differently\n0:Home.",
                     font=("Arial", 35, "bold"))
        screen.onkey(main, "0")
        screen.onkey(x, "1")
        screen.onkey(q, "2")
        turtle.listen()


# Give the user an option to enter the numbers manually,have them randomly generated, or to quit the game.
def choice():
    x = turtle.textinput("Manual, Random, or Reset", 'Type "1" for Manual\nType "2" for Random\nType "0" to Exit:')
    try:
        index = options.index(x)
        if index == 1:
            scoreboard()
            manual()
        elif index == 2:
            scoreboard()
            generate()
        elif index == 0:
            turtle.reset()
            turtle.write('Thank You! Bye Bye!', font=("Arial", 35, "bold"))
    except Exception as err:
        print(err)
        turtle.clear()
        turt_move(-310, -50)
        turtle.write("You must enter a number from 0-2. Press 'space' to continue.", font=("Arial", 35, "bold"))
        screen.onkey(main, "space")
        turtle.listen()

# Establish the scoreboard at '0' for all values.
def scoreboard():
    wins = 0
    losses = 0
    runs = 0
    results.append(runs)
    results.append(wins)
    results.append(losses)
    return runs, wins, losses

# FOR MANUAL INPUT
# Clear turtle
# Append 3 list to the user entry list
# # Make the square
# Call necessary functions
# Display the amount of runs, wins, and losses the user has accumulated.
# Offer to try again, reset the score, or do a random input.
def manual():
    us.clear()
    turtle.reset()
    us.append([])
    us.append([])
    us.append([])
    turt_square()
    in_us(1, 0)
    in_us(2, 1)
    in_us(3, 2)
    add_man()
    turt_move(-350, 100)
    turtle.write("Runs: " + str(results[0]), font=("Arial", 35, "bold"))
    turt_move(0, 100)
    turtle.write("Wins: " + str(results[1]), font=("Arial", 35, "bold"))
    turt_move(350, 100)
    turtle.write("Loses: " + str(results[2]), font=("Arial", 35, "bold"))
    f = turtle.textinput('Try Manual Again?', '(1: yes)\n(0: no & reset)\n(2: Try Random): ')
    next(manual, generate, f)

# Prompt the user to enter 9 numbers from 1-9 without repeating.
''' 
    If they repeat a number, input a number that's out of range,
    or has an invalid input all-together, instruct them to input 
    a number within the range allotted. Offer them to start over.
'''
def in_us(a, b):
    try:
        counter = 0
        while counter < 3:
            x = turtle.textinput('Row ' + str(a), 'Enter a number for row ' + str(a) +
                                 ':\n(Make sure to not repeat a number)')
            if int(x) < 1 or int(x) > 9:
                turtle.reset()
                counter += 3
                turt_move(-300, -25)
                turtle.write('Your number must be between 1 and 9.', font=("Arial", 30, "bold"))
                turt_move(-300, -75)
                f = turtle.textinput('Try Again?', '(1: yes)\n(0: no & reset)\n(2: Try Random): ')
                next(manual, generate, f)
            else:
                counter += 1
                us[b].append(x)
        if us[b][0] == us[b][1] or us[b][0] == us[b][2] or us[b][2] == us[b][1]:
            turtle.clear()
            turtle.write('You can\'t repeat a number in a row', font=("Arial", 30, "bold"))
            f = turtle.textinput('Try Manual Again?', '(1: yes)\n(0: no & reset)\n(2: Try Random): ')
            next(manual, generate, f)
    except Exception as err:
        print(err, "in in_us")
        turtle.reset()
        turt_move(-300, -25)
        turtle.write('You must enter a NUMBER between 1 and 9.', font=("Arial", 30, "bold"))
        turt_move(-300, -75)
        f = turtle.textinput('Try Row Again?', '(1: yes)\n(0: no & reset)\n(2: Try Random): ')
        next(manual, generate, f)

# Compare each number in the square to make sure that there are no repeated values.
# Display the numbers in the square.
# Check if they made the Lo Shu Magic Square.
# Add 1 to runs and 1 to wins if they won or to losses if they lost.
def add_man():
    try:
        turt_move(-310, -175)
        t = 0
        i = 0
        px = -150
        py = -25
        while t < 8 and i < 3:
            f = 0
            k = 3
            while f < k:
                turt_move(px, py)
                turtle.write(us[i][f], font=("Arial", 50, "bold"))
                px += 150
                f += 1
                t += 1
            i += 1
            px = -150
            py -= 150
            k += 3
        a = int(us[0][0])
        b = int(us[0][1])
        c = int(us[0][2])
        d = int(us[1][0])
        e = int(us[1][1])
        f = int(us[1][2])
        g = int(us[2][0])
        h = int(us[2][1])
        i = int(us[2][2])
        if a == d or a == e or a == f or a == g or a == h or a == i:
            try_again()
            us.clear()
        elif b == d or b == e or b == f or b == g or b == h or b == i:
            try_again()
            us.clear()
        elif c == d or c == e or c == f or c == g or c == h or c == i:
            try_again()
            us.clear()
        elif d == g or d == h or d == i:
            try_again()
            us.clear()
        elif e == g or e == h or e == i:
            try_again()
            us.clear()
        elif f == g or f == h or f == i:
            try_again()
            us.clear()
        else:
            rowA = a + b + c
            rowB = d + e + f
            rowC = g + h + i
            colA = a + d + g
            colB = b + e + h
            colC = g + h + i
            diagA = a + e + i
            diagB = c + e + g
            if rowA == 15 and rowB == 15 and rowC == 15 and colA == 15 and colB == 15 and colC == 15 and diagA == 15\
                    and diagB == 15:
                turt_move(-300, -450)
                turtle.write('You did it!', font=("Arial", 30, "bold"))
                results[1] += 1
            else:
                turt_move(-300, -450)
                turtle.write('You did not win.', font=("Arial", 30, "bold"))
                results[2] += 1
            results[0] += 1
    except Exception as err:
        print(err, "in add_man")

# Try again if a value has been repeated.
def try_again():
    turt_move(-300, -450)
    turtle.write('You can\'t repeat a number in the square', font=("Arial", 30, "bold"))
    f = turtle.textinput('Try Manual Again?', '(1: yes)\n(0: no & reset)\n(2: Try Random): ')
    next(manual, generate, f)

# FOR RANDOM INPUT.
# Clear turtle
# Clear the user list whenever the function is called.
# # Make the square
# Call necessary functions
# Display the amount of runs, wins, and losses the user has accumulated.
# Offer to try again, reset the score, or do a manual input.
def generate():
    us.clear()
    turtle.reset()
    ran()
    turt_square()
    add_ran()
    turt_move(-350, 100)
    turtle.write("Runs: " + str(results[0]), font=("Arial", 35, "bold"))
    turt_move(0, 100)
    turtle.write("Wins: " + str(results[1]), font=("Arial", 35, "bold"))
    turt_move(350, 100)
    turtle.write("Loses: " + str(results[2]), font=("Arial", 35, "bold"))
    f = turtle.textinput('Try Random Again?', '(1: yes)\n(0: no & reset)\n(2: Try Manual): ')
    next(generate, manual, f)

# Randomly generate 9 numbers from 1-9.
def ran():
    x = random.sample(range(1, 10), 9)
    us.append(x)

# Display numbers in the square.
# Check if it made the Lo Shu Magic Square.
# Add 1 to runs and 1 to wins if they won or to losses if they lost.
def add_ran():
    t = 0
    px = -150
    py = -25
    while t < 8:
        f = 0
        k = 3
        while f < k:
            turt_move(px, py)
            turtle.write(us[0][t], font=("Arial", 50, "bold"))
            px += 150
            f += 1
            t += 1
        px = -150
        py -= 150
        k += 3
    a = us[0][0]
    b = us[0][1]
    c = us[0][2]
    d = us[0][3]
    e = us[0][4]
    f = us[0][5]
    g = us[0][6]
    h = us[0][7]
    i = us[0][8]
    rowA = a + b + c
    rowB = d + e + f
    rowC = g + h + i
    colA = a + d + g
    colB = b + e + h
    colC = g + h + i
    diagA = a + e + i
    diagB = c + e + g
    if rowA == 15 and rowB == 15 and rowC == 15 and colA == 15 and colB == 15 and colC == 15 and diagA == 15\
            and diagB == 15:
        turt_move(-300, -450)
        turtle.write('You did it!', font=("Arial", 30, "bold"))
        results[1] += 1
    else:
        turt_move(-300, -450)
        turtle.write('You did not win.', font=("Arial", 30, "bold"))
        results[2] += 1
    results[0] += 1


# Call the main function.
main()
