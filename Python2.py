##Second Python Question
# Count the occurence of the charcter in the string
## Input:aaabbccaabb
## output:a3b3c2a2b2

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


##Input
input1='aaabbccaabb'
print(charchtercount(input1))