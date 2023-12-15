##Write a Python program to find the factorial of a number.
def factorial(n):
    if n==0:
        return 0
    if n==1:
        return 1
    
    return n*factorial(n-1)

##input
print(factorial(5))
