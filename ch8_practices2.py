# 8-12
def sandwich(*food):
    print(food)
order1 = {'oil','sugar','peanut'}
sandwich('oil','sugar','peanut')
sandwich('salt','carrot','cabbage','tomato')
sandwich(order1)

# 8-13
def user_profile(first,last,**other):
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key,value in other.items():
        profile[key] = value

    return profile

my_profile = user_profile('mason','chen',gender = 'male', bloodtype = 'B')
print(my_profile)


# 8-14
def car_profile(manufacturer , model , **description):
    profile = {}
    profile['Manufacturer'] = manufacturer
    profile['Model'] = model
    for key , value in description.items():
        profile[key] = value
    return profile
    
car = car_profile('Honda','CV', color = 'yellow' , door = 5)
print(car)