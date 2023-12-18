##Write a Python program to check if a number is a power of two using recursion.
def checkpowtwo(n):
    if n<=0:
        return False
    if n==1:
        return True
    if n%2!=0:
        return False
    return checkpowtwo(n//2)


##input
n=16
print(checkpowtwo(n))
       