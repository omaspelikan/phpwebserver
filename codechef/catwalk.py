# python catwalk
case = input("How many cases will you test? ")
case=int(case)

while case > 0:
    member = 100
    count = 0
    while member > 0:
        data = input("Please enter completed time of 10 people ")
        indiv_len = len(data.split())
        if indiv_len != 10:
            print("Your input need to be count as 10 integer")
        else:
            member = member - indiv_len
#            time=''.join(data)
            for x in data.split():
                if int(x) >= 30:
                    count = count + 1
    if count <=60:
        print("No")
    else:
        print("Yes")
    case = case - 1


