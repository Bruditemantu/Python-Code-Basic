##Range b/w the prime number
def checkprime(n):
    flag=0
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
   
    return True

def prime(start,end):
    while start<end:
        if checkprime(start):
            print(start)
            start+=1
        else:
            start+=1
#input
prime(6,15)                           