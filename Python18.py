##HIGHER ORDER FUNCTION IN PYTHON
from functools import reduce

##MAP()
nums=[1,2,3,4,5]
square=map(lambda x:x**2,nums)
print(list(square))


##Filter()
nums=[2,1,3,4,7,9,9,6]
even=filter(lambda x:x%2==0,nums)
print(list(even))


## Reduce
prime=[1,3,5,7,11,13]
total1=reduce(lambda x , y: x+y,prime,1)
print(total1)
total2=reduce(lambda x , y: x+y,prime,5)
print(total2)
