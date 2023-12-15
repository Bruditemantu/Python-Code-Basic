##question 9
def question8(nums):
    dict={}
    for i in nums:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict

##input
list= [1, 2, 3, 2, 4, 1, 2, 4, 5]
print(question8(list))