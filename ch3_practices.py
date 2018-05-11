#ch3 practics file
cars = ["ford","civic","Dodge",30]
print(cars)
print(type(cars))
print(cars[0])
print(cars[1])
print(cars[3])
print(type(cars[3]))
i = 0
for i in cars:
    print(i)
print(cars[0].title())

message = 'this is a ' + cars[2]
print(message.title())


# 3.1
fnames = ['zoe','cherry','linda','helen','amy']
for i in fnames:
    message = 'Hello, long time no see, ' + i.title()
    print(message)
fnames.append('cathy')
print(fnames)
fnames.insert(1,'Rose')
print(fnames)
del fnames[1]
print(fnames)

#pop list
popped_fnames = fnames.pop()
print('poped fname is '+ popped_fnames)
print('now fname list is ' , fnames)
print('now try to pop second name and print it.')
print('pop name is '+ fnames.pop(1))

#del and .remove
carList = ['Honda','Toyota','Lotus','Subaru']
del carList[0]           # del method remove item using index
print(carList)
carList.remove("Lotus")  # remove method remove item using value
print(carList)
# append and insert item to list
carList.append('Benz')
print(carList)
carList.insert(1,'Dodge')
print(carList)

# Nest
alien_0 = {'color':'green','points':5,'speed':'slow'}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
alien_List = [alien_0,alien_1,alien_2]
print(alien_List)

# create multi dictionary in List
for alien in range(30):
    alien_List.append(alien_0)
for a in alien_List[:5]:
    print(a)
print('How many Alien in List: '+ str(len(alien_List)))

# dict in dict
os = {
    'xp':{'year':1998,'servicepack':'sp3'},
    'me':{'year':2000,'servicepack':''},
    '7':{'year':2003, 'servicepack':'sp1'},
    }


