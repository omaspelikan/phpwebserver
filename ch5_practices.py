# ch5 practices
cars = ['bmw','toyota','benz','lotus']
for car in cars:
    if car == 'bmw':
        print(car.title())
    else:
        print(car.upper())
a = 30
b = 40
if a > 29 and b < 41:
    print('in between 30 ~ 40')

# 5-1
number = 30
print('number is bigger than 25',number >25 )
print('number is below 20,',number <20)
# 5-2
food = (3,5,7,9)
a = 4
b = 5
print(a in food)
print(b in food)
ages = 18
if ages < 4:
    price = 0
elif ages < 18:
    price =5
elif ages < 65:
    price = 10   
else:
    price = 5
print('Your fee is $'+str(price))

# 5-3
alien_color = 'red'
if alien_color == 'green':
    print('you got 5 points')
elif alien_color == 'yellow':
    print('you got 10 points')
elif alien_color == 'red':
    print('you got 15 points')

# 5-6
age = 30
if age <2:
    print('you are a baby')
elif age <4:
    print('you are a toddler')
elif age <13:
    print('you are a kid')
elif age <20:
    print('you are a teenager')
elif age <65:
    print('you are a adult')
else:
    print('you are a elder')

# 5-7
fav_fruit = ['melon','banana','orange','berry']
if 'banana' in fav_fruit:
    print('you relly like banana')
if 'orange' in fav_fruit:
    print('you relly like orange')

# 5-8
logs = ['admin','1','2','3']
emy_logs=[]
if len(logs) == 0:
    print('We need to find some users!')
else:
    for log in logs:
        if log == 'admin':
            print('Hello '+log+' would you like to see a status report?')
        else:
            print('Hello '+log+' thank you for logging in again.')

# 5-10
current_user = ['John','Mason','Irene','Hana']
new_user = ['john','MASON','1','3','amy']
for nu in new_user:
    if nu.title() in current_user:
        print('there is current user name '+nu.title()+' please select another name.')
    else:
        print('this user name '+nu.title()+' is available.')

# 5-11
orderList = [1,2,3,4,5,6,7,8,9]
for o in orderList:
    if o == 1:
        print(str(o) + 'st')
    elif o == 2:
        print(str(o) + 'nd')
    elif o == 3:
        print(str(o) + 'rd')
    else:
        print(str(o) + 'th')
