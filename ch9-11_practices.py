# 9-11
from restaurant import Restaurant, Icecream_stand
restaurant = Restaurant('Mr Chuang','Rice')
restaurant.describe_restaurant()
restaurant.open_restaurant()


restaurant1 = Restaurant('Lucky','Hong Kong Tea')
restaurant2 = Restaurant('Fresh','sushi')
restaurant3 = Restaurant('Orion','Steak')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


restaurant1.set_number_served(10)
restaurant2.increment_number_served(5)

icestand1 = Icecream_stand('CreamDaddy')
icestand1.flavor('berry','orange','lemon','milk')
icestand1.describe_restaurant()
icestand1.open_restaurant()
icestand1.display_flavor()