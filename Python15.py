## Write a Python program to remove duplicates from a list.
def removeDuplicate(nums):
    list=[]
    for i in nums:
        if i not in list:
            list.append(i)
    return list

#input
s=[1,2,4,5,5,6,7]
print(removeDuplicate(s))        