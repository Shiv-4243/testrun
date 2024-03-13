# factorial using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("enter a number:"))
print("factorial of the number is ", factorial(n))


# fibonacci using recursion

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + fib(n - 1)


print(" fibonacci number is :",fib(n))

