def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    divisor=0
    if a>b:
        divisor = b
        while a%divisor!=0 or b%divisor!=0:
            divisor -=1
        return divisor
    else:
        divisor = a
        while a%divisor!=0 or b%divisor!=0:
            divisor-=1
        return divisor

print(gcdIter(2,12))
print(gcdIter(6,12))
print(gcdIter(9,12))
print(gcdIter(17,12))