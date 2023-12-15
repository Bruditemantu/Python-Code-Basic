##Write a Python program to count the frequency of each element in a list.

def countoccurence(string):
    # string1="manturaj"
    dict={}
    for i in string:
        if i in dict:
          dict[i]+=1
        else:
           dict[i]=1
# print(str(dict))
    return dict 

#input
ans1="manturaj"
frequency=countoccurence(ans1)
print(str(frequency))      




