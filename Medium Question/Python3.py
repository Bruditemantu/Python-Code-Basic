##3. Given an array of N integers, and an integer K, find the number of pairs of elements
#in the array whose sum is equal to K

##First Solution
def pairsum(nums,target):
    count=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                count+=1
    return count


#input
arr=[1,2,3,4,5,3]
target=6
print(pairsum(arr,target))


##SECOND SOLUTION
def pairsum2(nums,target):
    dict1={}
    count=0
    for i in nums:
        complement=target-i
        if complement in dict1:
            count+=dict1[complement]
        if i in dict1:
           dict1[i]+=1
        else:
           dict1[i]=1
    return count

## input
arr=[1,2,3,4,5]
target=6
print(pairsum2(arr,target))                
