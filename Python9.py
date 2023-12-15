##Check the string is palindrome or not
def checkPalindrome(string):
 
    # for i in range(len(string)):
    string1=string[::-1]

    
    print(string1)
    if string==string1:
        print("YES")
    else:
        print("No")

checkPalindrome('naman')