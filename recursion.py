# purpose is to eliminate loops
# imagine there are many rooms in side each other
# go inside each room and find a number 
# once you out of rooms tell sum of all numbers
# recursion uses the same function by calling it in itself

# write a program that calculaltes the factotial of a number
n = int(input("num: "))
def factorial(n):
    if n == 0 :
        return 1
    
    return n * factorial(n - 1)
n = factorial(n)
print(n)
