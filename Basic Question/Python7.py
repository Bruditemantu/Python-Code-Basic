##Question7
##LCM of the Two number
import math
def lcm(a,b):
    gcd=math.gcd(a,b)
    lcm=(a*b)//gcd
    return lcm


##input
number1=12
number2=18
print(lcm(number1,number2))