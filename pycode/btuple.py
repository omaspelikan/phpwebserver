def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    btup=()
    for x in aTup:
        if len(x)%2:
            btup = btup + (x,)
 
            
    return btup
aTup=('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(aTup))