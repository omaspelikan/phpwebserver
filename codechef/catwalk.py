# python catwalk
case = input("How many cases will you test? ")
case=int(case)

while case > 0:
    member = 100
    count = 0
    data_correct = True
    while member > 0:
        data = input("Please enter completed time of 10 people ")
        indiv_len = len(data.split())
        if indiv_len != 10:
            print("Your input need to be count as 10 integer")
        else:
            for x in data.split():
                if int(x) > 60:
                    print("time out")
                    data_correct = False
                elif int(x) < 1:
                    print("Wrong time")
                    data_correct = False
                elif int(x) <= 30:
                    count = count + 1
        if data_correct == False:
            data_correct = True
        else:
            member = member - indiv_len
                    
    if count <= 60:
        print("No")
    else:
        print("Yes")
    case = case - 1


