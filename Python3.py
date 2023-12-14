##Third Question
#Reverse the Target value of the string
#input: abcdefgijklm target=4
#output:dcbaigfemlkj
def reversestring(string):
    result=' '
    target=4
    for i in range(0,len(string),target):
        segement=string[i:i+target]
        result+=segement[::-1]
    return result

##input part
input1='abcdefghijklmnopht'
print(reversestring(input1))    