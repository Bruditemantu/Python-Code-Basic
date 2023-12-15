##Write a Python program to check if a number is prime.
def checkprime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


#Input
print(checkprime(7))