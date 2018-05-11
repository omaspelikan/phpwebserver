# ch7 practices
#message = input('What Game do you recently play? ')
#print(message+' is a greate game in PS4.')


# 7-1 rental car
#car = input('Which Car do you rent? ')
#print('here you are a ' + car.title())

# 7-2 restaurant table
people = input('How many people will join the Dinner? ')
people = int(people)
if people > 8:
    print('Sorry Sir you must wait 10 minutes to have the table.')
else:
    print('Come in the table is ready.')

# exercise flag
#print('Hello please type any sentences and i will repeat it until u type quit ')
#active = True
#while active:
#    message = input('Please keyin the sentence ')
#    if message == 'quit':
#        active = False
#    else:
#        print(message)

# print odd number less than 10
#current = 0
#while current < 10:
#    current += 1
#    if (current % 2) == 0:
#        continue
#    else:
#       print(current)

# 7-4 pizza topping
while True:
    topping = input('What topping you want on the pizza? ')
    if topping == 'quit':
        break
    else:
        print(topping + ' adding on the pizza.')

# 7-5 movie ticket
while True:
    age = input('What is your age? ')
    if age =='quit':
        break
    elif int(age) < 3:
        print('Movie fee is $0')
    elif int(age) < 12:
        print('Movie fee is $10')
    elif int(age) >= 12:
        print('Movie fee is $15')

# remove duplicate pet
pets = ['dog','cat','panda','cat','pig','pony']
while 'cat' in pets:
    pets.remove('cat')

print(pets)

# poller
poll = {}
active = True
while active:
    name = input('What is your name? ')
    lucky_number = input('What is your lucky number? ')
    poll[name] = lucky_number
    repeat = input('Would you like another one to poll? (yes/no) ')
    if repeat== 'no':
        active = False

for name, number in poll.items():
    print(name.title() + ' lucky number is ' + number)