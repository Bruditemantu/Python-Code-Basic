##find the unique element in the list
def unique(list1):
    unique_set=set(list1)
    return list(unique_set)

##input
l1=[1,2,3,4,5,5]
print(unique(l1))