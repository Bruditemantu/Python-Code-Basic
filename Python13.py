##second max-elemnt in the lis
def secondmax(nums):
    maxi1=-1
    maxi2=-1
    for i in nums:
        if i>maxi1:
            maxi1=i
    for i in nums:
        if i>maxi2 and i<maxi1:
            maxi2=i
    if maxi1==maxi2:
        return maxi1
    else:
        return maxi2

#input
list1=[1,2,3,4,5,6,5,7]
print(secondmax(list1))                