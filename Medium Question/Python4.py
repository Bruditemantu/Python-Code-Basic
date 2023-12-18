##Question 4
## Rotated the array right-wise in d rotated
def Rotatedarray(nums,k):
    n=len(nums)
    k=k%n
    nums[:]=nums[-k:]+nums[:-k]
    return nums

##input
list1=[1,2,3,4,5]
k=2
print(Rotatedarray(list1,k))        