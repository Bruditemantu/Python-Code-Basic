##Question 6
def question7(string1,string2):
    res1=''.join(sorted(string1))
    res2=''.join(sorted(string2))
    if res1==res2:
        return True
    else:
        return False


#input
string1 = "listen"
string2 = "silent"
print(question7(string1,string2))