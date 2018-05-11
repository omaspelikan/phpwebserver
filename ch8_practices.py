# ch8 practice
def sayHI(name):
    """ function input a name """
    print('Hello , ' + name.title())

sayHI('michael')

# 8-1 
def display_message():
    """ Display this chapter study stuff """
    print("This is chapter 8 Function , which define a section of code can be called in the program.")

display_message()

# 8-2 parameter
def fav_book(title):
    print('My favorite book is ' + title)

fav_book('12 rules of life')

# 8-3 make shirt
def make_shirt(size='L',text='I Love Python!'):
    print('your shirt size is ' + size + ' and text print on is "' + text +'"')

make_shirt('M','Time\'s UP')
make_shirt(size='L',text='Help yourself!')
make_shirt('M')
make_shirt()

# 8-6 city name
def city_country(city,country):
    pair = {city:country}
    return pair

print(city_country('taipei','taiwan'))
print(city_country('texas','usa'))
print(city_country('san paul','brazil'))


# 8-7 make album
def album(artist,title,number_tracks=""):
    if number_tracks == "":
        ma = {'Artist':artist,'Album Title':title}
    else:
        ma = {'Artist':artist,'Album Title':title,'Number of Tracks':number_tracks}
    return ma

print(album('aser','basketball'))
print(album('jackson','thriller',10))
print(album('bach','season'))

# 8-8 user album
def user_album(artist,title):
    ua = {'Artist':artist,'Title':title}
    return ua

flag = 'yes'

while flag != 'no':
    artist = input('Pleae enter Artist name: ')
    title = input('Please enter title: ')
    flag = input('Add another one? (yes / no )')
    print(user_album(artist,title))
#    print(user_album)

# 8-9 / 8-10 / 8-11

def show_magicians(mag_list):
    for a in mag_list:
        print('Here come , ' + a.title())

def make_great(mag_list):
    for a in range(len(mag_list)):
        mag_list[a] = 'Great ' + mag_list[a]

def make_great_unchanged(Umag_list):
    for a in range(len(Umag_list)):
        Umag_list[a] = 'Great ' + Umag_list[a]
    return Umag_list


magicians = ['david','brake','Liu']
list_unchanged = []
show_magicians(magicians)
# make_great(magicians)
list_unchanged = make_great_unchanged(magicians[:])
show_magicians(list_unchanged)
show_magicians(magicians)
