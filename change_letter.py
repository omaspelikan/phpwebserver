# Using the Python language, have the function LetterChanges(str) take the str parameter being 
# passed and modify it using the following algorithm. Replace every letter in the string with 
# the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every 
# vowel in this new string (a, e, i, o, u) and finally return this modified string.
def LetterChanges(str): 
    str0 =[]
    for i in str:
        if 'z' > i >='a':
            check = chr(ord(i)+1)
            if check == 'e':
                str0.append('E')
            elif check == 'i':
                str0.append('I')
            elif check == 'o':
                str0.append('O')
            elif check == 'u':
                str0.append('U')
            else:
                str0.append(check)
        elif i =='z':
            str0.append('a')
        else:
            str0.append(i)
    str=''.join(str0)
    # code goes here 
    return str
# keep this function call here  
print (LetterChanges(input()))
