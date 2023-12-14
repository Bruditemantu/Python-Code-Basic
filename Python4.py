##Question Four
#Single Number II
##Example 1:
# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:

# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
def singleelement(num):
    unique_set=set(num)
    sum1=sum(unique_set)*3-sum(num)
    ans=sum1//2
    return ans

#input 
num1=[0,1,0,1,0,1,99]
print(singleelement(num1))
