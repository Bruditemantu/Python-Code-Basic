##Question No:9 answer
def charchtercount(string):
    result=' '
    count=1
    for i in range(len(string)):
        if i!=len(string)-1 and string[i]==string[i+1]:
            count+=1
        else:
            result+=string[i]+str(count)
            count=1    
    return result

##input
list1="wwwwaaadebbbbbw"
print(charchtercount(list1))