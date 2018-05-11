# ch4 practices

# 4-1
pizza_taste = ['cheese','hawai','charol beagon']
for p in pizza_taste:
    print("my favor pizza taste " +p.title())
print('There are all my fave pizza taste, especially ' + pizza_taste[2]+ \
' is definie good')

# 4-2
animals = ['dog','cat','pig']
for a in animals:
    print(a.title() +' is a cute animal')

print('they are so cute and so adorable')

# range function
for i in range(1,6):
    print(i)
# print even number
even_number = list(range(2,11,2))
print(even_number)

# print exponent
squares = []
for a in range(2,11):
    square = a ** 2
    squares.append(square)
print(squares)

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# line comprehension
square = [value ** 2 for value in range(1,11,2)]
print(square)

# 4-3 ,4-4
#for i in range(1,10000):
#    print(i)
# 4-5
millionList = [value for value in range(1,1000000)]
print(min(millionList))
print(max(millionList))
print(sum(millionList))
# 4-6
for i in range(1,21,2):
    print(i)
# 4-7
for i in range(3,31,3):
    print(i)
# 4-8 Cube / 4-9 cube 1~10
for i in range(1,11):
    print(i**3)
cubes = [i**3 for i in range(1,11)]
print(cubes)

print(cubes[1:3])
print(cubes[-7:])
for cu in cubes[-7:]:
    print(cu)

# copy list
newcubes = cubes[:]
print('Here is new cubes list: ',newcubes)

# not copy List
myFood = ['pizza','cookie','meat']
hisFood = myFood
myFood.append('ice cream')
print('My Food List: ',myFood)
hisFood.append('water melon')
print('His Food List: ',hisFood)

# 4-10 Slices
drinks = ['beer','tea','coffee','milk','water','juice']
print('Drink List:',drinks)
print('First three Drinks are : ',drinks[0:3])
print('Middle of List :',drinks[int(5/2):(int(5/2)+3)])
print('Last of Drinks List: ',drinks[-3:])

# 4-11 
newDrinks = drinks[:]
drinks.append('Milk Tea')
newDrinks.append('Soda')
print('My New Drinks List: ',drinks)
print('His New Drinks List: ',newDrinks)

# 4-12 Loop
for i in drinks:
    print('My New drinks List: '+i)
for i in newDrinks:
    print('His new Drinks List: '+i)

# tuple
rectangle = (10,5)
print('length of rectangle: ',rectangle[0])
print('height of rectangle: ',rectangle[1])
# cannot assign tuple -> rectangle[0] = 20

# 4-11
food = ('soup','steak','pork','carrot')
for f in food:
    print('We offer '+f)
food =('coffee','steak','carrot','salad')
for f in food:
    print('We offer '+f)
