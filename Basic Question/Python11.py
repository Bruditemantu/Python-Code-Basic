##Question 11 answer
def singledigit(n):
    if n==0:
        return 0
    if n%9==0:
        return 9
    return (n%9)

##input
num= 9876
print(singledigit(num))