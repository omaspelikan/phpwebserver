#python Grader
from math import *

def polysum(n, s):
    ''' n is number sides of regular polygon
        s is length of each side
    '''
    area = (0.25 * n * (s**2))/(tan(pi/n))
    sq_of_perimeter = s**2
    return '{:.{prec}f}'.format(area + sq_of_perimeter, prec=4)
