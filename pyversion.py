import sys
print(sys.version)
sum = 0
alist = [1,3,5,7,9]
for a in alist:
    print(a)
for b in alist :
    sum = b + sum
# convert number to string
print('the total is '+str(sum))
title = "hello world Alex"
quota = ' Albert Einstein once said,\t “A person who never made a mistake never tried anything new.”'
#print string
print(title.title() + '\n')
print(title.upper())
print(title.lower())
print(quota)
print(quota.strip())
# doing float mathmatic
print(0.1 + 0.2)