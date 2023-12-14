##String based Question in the Python
## first and last letter of the string is Upercase change

#input str=this is a new day at brudite
#output : ThiS IS A NeW DaY AT BruditE.
def lettercapital(str):
    words=str.split()
    capatlisized_words=[]
    for word in words:
        if len(word)>1:
            capatlisized_word=word[0].upper()+word[1:-1]+word[-1].upper()
        else:
           capatlisized_word= word.upper()
        capatlisized_words.append(capatlisized_word)
    return ' '.join(capatlisized_words)


#input:
input1='this is a new day at brudite'
ans=lettercapital(input1)
print(ans)

