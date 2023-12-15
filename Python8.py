##Print in the list all even number in the same sequence
def even(nums):
    list=[]
    for i in nums:
        if i%2==0:
            list.append(i)

    print(list)

#Input
input=[2,4,5,6,9,10,15,17,19,20]
even(input)    
