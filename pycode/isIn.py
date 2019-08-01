def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr)==0:
        return print("not found.")
    elif char == aStr[int(len(aStr)/2)]:
        return char
    elif char > aStr[int(len(aStr)/2)] and int(len(aStr))>1:
        aStr=aStr[int(len(aStr)/2):]
        print(aStr)
        return isIn(char,aStr)
    elif char < aStr[int(len(aStr)/2)] and int(len(aStr))>1:
        aStr=aStr[:int(len(aStr)/2)]
        print(aStr)
        return isIn(char, aStr)


test_str='abcdefghirz'
x = 'y'
print(isIn(x,test_str))