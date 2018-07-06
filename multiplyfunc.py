# multiply of x and y  below range
# declare two list.
# My solution is to use two lists for storing values multiply by x and mulitply by y below range1.
# then create one set to filter duplicate numbers which is a set feature that store only unique value.
# last step is printing the sum of the item of the set.
def multiply(x,y,range1):
    multi1 = list()
    multi2 = list()
    for i in range(1,range1):
        if (i % x) == 0:
            multi1.append(i)
    for j in range(1,range1):
        if (j % y) == 0:
            multi2.append(j)   
    group = set()   # a set which is to store unique value.
    for i in multi1:
        group.add(i)
    for j in multi2:
        group.add(j)
    sum = 0        
    for k in group:
        sum +=k
    print("Multiply %d and %d below %d , total sum is %d" %(x,y,range1,sum))

multiply(2,5,10)
