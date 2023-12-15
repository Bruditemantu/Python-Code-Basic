## Write a Python program to find the common elements between two lists.
def commonelement(nums1,nums2):
    ans=[]
    for i in nums1:
        for j in nums2:
            if i==j:
                ans.append(i)
    return ans


#input
s1=[1,2,3,4,5,6,7]
s2=[8,9,10,11,4,5]
print(commonelement(s1,s2))