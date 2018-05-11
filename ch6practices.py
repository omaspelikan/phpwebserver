# ch6 practices
alien_0 = {'color':'green','points':5}
print('alien color is '+alien_0['color']+' and points is '+str(alien_0['points']))
alien_0['x_position']=2
alien_0['y_position']=20
print(alien_0)

alien_0['speed']='fast'
if alien_0['speed'] == 'slow':
    x_inc = 1
elif alien_0['speed'] == 'normal':
    x_inc = 2
elif alien_0['speed'] == 'fast':
    x_inc = 3
alien_0['x_position'] = alien_0['x_position'] + x_inc
print('Alien_0 X Posistion is ' + str(alien_0['x_position']) +'. Y Position is ' + str(alien_0['y_position']))

del alien_0['points']
print(alien_0)

favorite_language = {
    'mason':'python',
    'louis':'C',
    'alex':'ruby',
}
print(favorite_language)

# 6-1
p_info = {
    'First Name' : 'Mason',
    'Last Name' : 'Chen',
    'Age' : 40,
    'City' : 'Taipei',
    }
print(p_info)

# 6-2
luck_number = {
    'Mason' : 33,
    'Andy' : 55,
    'Michael' : 23,
    'kobe' : 24,
    'lebron' : 23,
    }   
print('Mason luck number is :',luck_number['Mason'])
print('Andy luck nunber is :',luck_number['Andy'])

# 6-3
keyword = {
    'for' : '\n \tDo a repeat action in the folowing lines.',
    'list' : '\n \tA list can store any information and have index to access it\'s data.',
    'tuple' : '\n \timmoveable list.',
    'if' : '\n \tCondition Action , if the condition is True ,then exec the following lines.',
    'print' : '\n \tPrint the information in parathese.',
    }
print('"For" keyword is :' + keyword['for'])
print('"list" keyword is :' + keyword['list'])
print('"tuple" keyword is :' + keyword['tuple'])
print('"if" keyword is :' + keyword['if'])
print('"print" keyword is :' + keyword['print'])
#print(keyword.items())
#print(keyword)
# 6-4
for key, discription in keyword.items():
    print('\nKeyWord :\t' + key)
    print('Note :' + discription)
keyword['set'] = 'Unorder unique lists'
keyword['sorted'] = 'Sort a container list'
keyword['ident'] = 'One of rules that help code easy to read.'
for key, discription in keyword.items():
    print('\nKeyWord :\t' + key)
    print('Note :' + discription)
for key in keyword.keys():
    print('Python keyword : ' + key.title())

for nu in set(luck_number.values()):
    print('luck number list: ' + str(nu))
# 6-5
river_nation = {'nile':'egypt','Long River':'china','Amazon':'South America'}
for riv, city in river_nation.items():
    print( riv.title() + ' is in ' + city.title())

for city in river_nation.values():
    print(city.title())
for riv in river_nation:
    print(riv.title())

# 6-6 Poll
luck_number_people = ['Mason','Andy','Michael','Wade','Anthony']
for people in luck_number_people:
    if people in luck_number.keys():
        print('Thanks you for Polling! ' + people)
    elif people not in luck_number.keys():
        print('Please join our polling! ' + people)

# 6-7
player0 = {'name':'Michael','number':23,'team':'bull'}
player1 = {'name':'Bryant','number':24,'team':'laker'}
player2 = {'name':'James','number':23,'team':'cav'}
great = [player0,player1,player2]
for g in great:
    for k,v in g.items():
        print(k,v)
    print('\n')

# 6-8
pet0 = {'name':'rory','animal':'dog','age':2,'owner':'joe'}
pet1 = {'name':'roovv','animal':'panda','age':1,'owner':'bahroo'}
pet2 = {'name':'mewdydo','animal':'cat','age':3,'owner':'hunger'}
pets = [pet0,pet1,pet2]
for pet in pets:
    for k,v in pet.items():
        print(k,v,)
    print('\n')
test1 = 5    
di = {test1:'three','four':4}
print(di[test1])
print(test1)

# 6-10

luck_number2 = { 'andy':{1,3,5},'bob':{2,4,6},'carl':{0,7,9} }
for name, number in luck_number2.items() :
    print(name.title() + '\'s luck number are', number)
