x=int (input ("enter a number"))
for i in range (x):
    print((" ") * ((x+1) - i), end="")
    for j in range(i+1):
        print( '*' + (" ") ,end="")

    print()



for i in range(x-1):
    print((" ") * (i + 3), end="")
    for j in range(x-1 - i):
        print( '*' + (" ") ,end="")

    print()


# ANOTHER METHOD

