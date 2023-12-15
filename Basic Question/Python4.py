##Ouestion 4
def question4(start,end):
    sum=0
    while(start<=end):
        if start%2!=0:
            sum+=start
            start=start+1
        else:
            start=start+1    
    return sum

print(question4(1,10))