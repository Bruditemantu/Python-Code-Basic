## common b/w two list
def common(list1,list2):
    ans=[]
    for i in list1:
        for j in list2:
            if i==j:
                ans.append(i)
    return ans

#input
l1 = [1, 2, 3, 4, 5] 
l2 = [4, 5, 6, 7, 8]
print(common(l1,l2))            