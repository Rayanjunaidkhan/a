# write a recursive function that takes input a variable n and ouputs the nth term of the fibonacchi sequence
n = int(input("enter term number: "))

def fibonacchi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacchi(n - 1) + fibonacchi(n - 2)

print(fibonacchi(n))
