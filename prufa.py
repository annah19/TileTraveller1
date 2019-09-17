x = 1
y = 1

n = str("(N)orth")
e = str("(E)ast")
s = str("(S)outh")
w = str("(W)est")

def canTravel():
        
    if(x == 1):
        if(y == 1):
            return n
        if(y == 2):
            return n,s,e
        if(y == 3):
            return s,e
        
    if(x == 2):
        if(y == 1):
            return n
        if(y == 2):
            return s,w
        if(y == 3):
            return e,w
        
    if(x == 3):
        if(y == 1):
            return n
        if(y == 2):
            return n,s
        if(y == 3):
            return s,w

    return "Not a valid direction"


def travel(direction):
    global y
    global x
    if(direction == "n"):
        y = y + 1
    if(direction == "s"):
        y = y - 1
    if(direction == "e"):
        x = x + 1
    if(direction == "w"):
        x = x - 1

while True:
    print("You can travel:", canTravel())
    user_input = input("Direction:")
    travel(user_input)