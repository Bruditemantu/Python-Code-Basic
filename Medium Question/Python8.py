##Ouestion 8
##Write a Python function that counts the number of vowels in a given string.
def countvowel(string):
    count=0
    p=string.lower()
    for i in p:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count+=1
    return count        

##input
hr= "Hello, World!"
print(countvowel(hr))        