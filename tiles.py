def findOutWhereHeIsGoing(x, y, letter):
    if (checkIfValidDirection(x, y, letter) == True):
        if (letter == 'n'):
            y += 1
        elif (letter == 's'):
            y -= 1
        elif (letter == 'w'):
            x -= 1
        elif (letter == 'e'):
            x += 1
    return x,y

def checkIfValidDirection(x, y, letter):
    printString = 'Direction: '
    if (x == 1 and y == 1):
        # do stuff, f.x. call tile function for 1 and 1
    elif (x == 1 and y == 2):


    return True

def checkIfValidInput(letter):
    letter = letter.toLower()
    if (letter == "n" or ...):
        return True
    else:
        return False

# Playing the Tile game
n = "(N)orth"
e = "(E)ast"
s = "(S)outh"
w = "(W)est"

x = 1
y = 1
while True:
    if (x == 3 and y == 3):
        print('Victory')
        break  

    user_input = input("Direction: ")
    user_input = user_input.toLower()
    if (checkIfValidInput(user_input) == True):
        x, y = findOutWhereHeIsGoing(x, y, user_input)
    else:
        print('Not a valid direction')
