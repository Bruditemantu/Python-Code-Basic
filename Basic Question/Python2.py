##Question2
def question2(string):
    alpha=0
    number=0
    for i in string:
        if(i.isnumeric()):
            number+=1
        elif(i.isalpha()):
            alpha+=1    
             
    
    print(alpha,number)


#input
question2('mantu123')