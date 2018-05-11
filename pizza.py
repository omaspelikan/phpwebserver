# pizza.py make pizza module
""" make pizza need size and topping """
def make_pizza(size,*topping):
    print('\nOrder pizza size is ' + str(size))
    for top in topping:
        print('have topping: ' + top)