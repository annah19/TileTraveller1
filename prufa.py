VERTICAL = 1
HORIZONTAL = 1

while True:

	print("You can travel: ", end="")

if VERTICAL > 1:
    print("(N)orth", end="")
    if VERTICAL < 3:
        print("(S)outh", end="")
    if HORIZONTAL > 1: 
        print("(R)ight", end="")
    if HORIZONTAL < 3:
        print("(L)eft", end="")

direction = input("Direction: ")