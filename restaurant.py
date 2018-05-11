# Module restaurant
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


class Icecream_stand(Restaurant):
    """ icecream inherenct Restaurant Class """
    def __init__(self,restaurant_name,cuisine_type='Ice Cream'):
        super().__init__(restaurant_name,cuisine_type)
    
    def flavor(self,*taste):
        self.flavor_list = taste
        
    def display_flavor(self):
        print('we have serve flavor :',self.flavor_list)

        