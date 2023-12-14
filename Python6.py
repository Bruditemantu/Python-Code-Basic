##Ouestion 6
## Find the vowel word that present in the string

s = set("aeiou")
l = [ "aeiou" , "getatier", "getaeiou"]
# newl  = [ele for ele in l if s.issubset(ele) ]
newl=[]
for ele in l:
    if s.issubset(ele):
        newl.append(ele)

print(newl)  