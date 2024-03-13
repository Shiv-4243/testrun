# for else loop

for i in range(5):
    print(i)
else:                            # executes after all iterations are COMPLETED
    print('i am out of loop')    # if loop BREAKS then it does not executes

print()
print()
print()
print()

# for loop no need to initiate before hand

x = ['shiv', 'Sush', 4243, 4227]

for i in x:
    print(i, end="")

for j in ['shiv', 'Sush', 4243, 4227]:
    print(j)

for i in ['shivarj', 'Sushmita', 4243, 4227]:
    print(i)



for i in ['shivarj', 'Sushmita', 4243, 4227,'shivarj', 'Sushmita', 4243, 4227]:
    print(i)



print()
print()
print()
print()

# while loop

y = 1
while (True):
    try:
        y = float(input("enter a number:"))
        y = y ** 2
        print('square of the numver is = ', end='')
        print(y)
    except ValueError:
        print("number entered is invalid")
    continue
