## Write a Python function that finds the median of a list of numbers.
def findmedian(nums):
    length=len(nums)
    if length%2==0:
        median_right=length//2
        median_left=median_right-1
        median= (nums[median_right]+nums[median_left])/2
    else:
        mid=length//2
        median=nums[mid]
    return median


##input
list1=[7,2,5,1,9,3]
print(findmedian(list1))
        
