#python GravityGuy
def check(lane):
    if lane == '.':
        return True
    else:
        return False

time = int(input("How many time do you test? "))

while time > 0:
    l1 = input("Please input Line 1 ")
    l2 = input("Please input Line 2 ")
    goal = False
    index = 0
    change = 0
    pos = 1
    while index < (len(l1)) and (len(l1) == len(l2)):
        if index == 0 :
            if check(l1[index]):
                pos = 1
                goal = True
            elif check(l2[index]):
                pos = 2
                goal = True
            else:
                goal = False
                break
        elif pos == 1:
            if check(l1[index]):
                pos = 1
            elif check(l2[index]):
                change = change + 1
                pos = 2
            else:
                goal = False
                break
        elif pos == 2:
            if check(l2[index]):
                pos = 2
            elif check(l1[index]):
                change = change + 1
                pos = 1
            else:
                goal = False
                break
        index = index +1
    if goal == True:
        print("Yes")
        print(change)
    else:
        print("No")
    time = time - 1