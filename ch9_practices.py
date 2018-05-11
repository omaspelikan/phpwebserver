# ch9 practices 
""" Class """
class Dog(object):
    """ Dog class have name and age and can sit and roll. """
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(self.name + ' is sitting.')

    def roll(self):
        print(self.name + ' is rolling.')


my_dog=Dog('willy',6)
your_dog=Dog('Snoopy',3)
print('my dog name is ' + my_dog.name + ' and ' + str(my_dog.age) + ' years old.')
my_dog.sit()
my_dog.roll()
print('your dog name is ' + your_dog.name + ' and ' +str(your_dog.age) + ' years old')
your_dog.sit()

# 9-1 
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.cuisine=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print('\nRestaurant Name is ' + self.name)
        print('Cuisine is ' + self.cuisine)
        print('there is ' + str(self.number_served) + ' people served.')

    def open_restaurant(self):
        print(self.name + ' is open.')

    def set_number_served(self,set_number):
        self.number_served=set_number
        print(self.name , 'have' ,self.number_served, 'People served.')

    def increment_number_served(self,increment):
        self.number_served+=increment
        print(self.name , 'have' ,self.number_served, 'People served.')
    
restaurant = Restaurant('Mr Chuang','Rice')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2
restaurant1 = Restaurant('Lucky','Hong Kong Tea')
restaurant2 = Restaurant('Fresh','sushi')
restaurant3 = Restaurant('Orion','Steak')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 9-4
restaurant1.set_number_served(10)
restaurant2.increment_number_served(5)

# 9-5 user info
class User_info():
    def __init__(self,name,group):
        self.name=name
        self.group=group
        self.number_of_login=0

    def print_info(self):
        print('\nUser ' + self.name)
        print('Group ' + self.group)
        print('Number of Login ' + str(self.number_of_login))
    
    def login_attemp(self):
        print('\nUser ' + self.name + ' have ' + str(self.number_of_login) + ' Login attemps.')

    def increment_login_attemps(self,number):
        self.number_of_login=number

    def reset_login_attemps(self):
        self.number_of_login=0


user1=User_info('mason','wheel')
user2=User_info('mp3','media')
user1.print_info()
user2.print_info()
user1.increment_login_attemps(5)
user1.login_attemp()
user1.reset_login_attemps()
user1.login_attemp()

# 9-6 icecream stand
""" icecream inherenct Restaurant Class """
class Icecream_stand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type='Ice Cream'):
        super().__init__(restaurant_name,cuisine_type)
    
    def flavor(self,*taste):
        self.flavor_list = taste
        
    def display_flavor(self):
        print('we have serve flavor :',self.flavor_list)

icestand1 = Icecream_stand('CreamDaddy')
icestand1.flavor('berry','orange','lemon','milk')
icestand1.describe_restaurant()
icestand1.open_restaurant()
icestand1.display_flavor()

# 9-7 / 9-8
class Admin(User_info):
    def __init__(self,name,group):
        super().__init__(name,group)
        self.privileges=Privileges()

 

class Privileges():
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):
        print(self.privileges)

user3=Admin('root','admin')
user3.privileges.show_privileges()


from collections import OrderedDict
fav_language = OrderedDict()
fav_language['john'] = 'python'
fav_language['Mary'] = 'C'
fav_language['Ken'] = 'Perl'
for key,value in fav_language.items():
    print(key + ' fav language is ' + value)

print(fav_language)
print(fav_language)

# 9-14 Dice
from random import randint
class Dice():
    """ Create a Dice of specific sides and have roll method """
    def __init__(self,side=6):
        self.sides = side

    def roll_dice(self):
        return (randint(1,self.sides))
dice6 = Dice()
dice10 = Dice(10)
dice20 = Dice(20)
count = 1
while count <= 10:
    print(dice6.roll_dice())
    count=count+1
print('\n')
count = 1
while count <= 10:
    print(dice10.roll_dice())
    count=count+1
print('\n')
count = 1
while count <= 10:
    print(dice20.roll_dice())
    count=count+1
        


