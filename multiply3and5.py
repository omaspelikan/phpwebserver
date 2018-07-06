# multiply of 3 and 5  below 1000
# declare two list for 3 and 5
# My solution is to use two lists for storing values multiply by 3 and mulitply by 5 below 1000.
# then create one set to filter duplicate numbers which is a set feature that store only unique value.
# last step is printing the sum of the item of the set.

multithree = list()
multifive = list()
for i in range(1,1000):
    if (i % 3) == 0:
        multithree.append(i)
for j in range(1,1000):
    if (j % 5) == 0:
        multifive.append(j)   

#print(multithree)
#print(multifive)
group = set()   # a set to store unique value.
for i in multithree:
    group.add(i)
for j in multifive:
    group.add(j)
#print((group))
sum = 0
for k in group:
    sum +=k
print("Multiply 3 and 5 below 1000 , total sum is %d" %(sum))