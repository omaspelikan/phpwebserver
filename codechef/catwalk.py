# python catwalk
number = input("How many time will you test? ")
number=int(number)

while number > 0:
    member = 20
    sum = 0
    while member > 0:
        time = input("please enter 10 member time ")
        indiv_len = len(time.split())
        member = member - indiv_len
        for x in time.split():
            if int(x) >= 5:
                sum = sum+1
    if sum >=10:
        print("it's not catwalk question.")
    else:
        print("it's catwalk question")
    number = number - 1

