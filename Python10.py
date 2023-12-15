##Reverse Words in a String III

#Input and output
# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "Mr Ding"
# Output: "rM gniD
def reverseword(string):
    return " ".join(word[::-1] for word in string.split())

#input
s= "Let's take LeetCode contest"
print(reverseword(s))   
                

