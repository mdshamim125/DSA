def reverseOfString(s):
    if(len(s)==0 or len(s)== 1):
        return s
    return reverseOfString(s[1:])+s[0]

word=input("Enter a string: ")
print(reverseOfString(word))