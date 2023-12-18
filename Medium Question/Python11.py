##. Write a Python program to create a list of given strings individually of the list using
##Python map function

def maplist(string1):
    newstring=string1
    return list(map(list,newstring))


#input
string2=['Red', 'Blue', 'Black', 'White', 'Pink']
print(maplist(string2))
