#python Johnny and the Beanstalk
test_time = int(input("How many bean will you plant? "))
while test_time > 0 and test_time <=20:
    rule = True
    level_beanstalk = int(input("How many level will your beanstalk grow? "))
    leaf = input("How many leaf will each level have? ")
    leaf = leaf.split()
    sum = 1
    level_index = 1
#    y = 0
    if level_beanstalk > 0 and level_beanstalk <= 10**6:
        for x in leaf:
            if sum == 1 and int(x) == 0:
                rule == True
            elif sum == 2 and int(x) == 1:
                rule = True    
            elif int(x) > 2**(sum-2):
                rule = False
                print('it false')
            sum = sum +1


        if rule == True:
            print("Yes")
        else:
            print("No")
    else:
        print("exceed limit level")
    test_time = test_time -1
