# ch10-2 practices
import json
filename = 'txt/numbers.json'
number = [1,2,3,4,5,6,7,8,9,10]
with open(filename,'w') as file_obj:
    json.dump(number,file_obj)

with open(filename) as file_obj:
    numbers = json.load(file_obj)
print(numbers)

# 10-11
def input_fav_num(filename):
    """ input and save number to file.  / need import json module. """
    while True:
        try:
            with open(filename) as file_obj:
                read_fav_num(filename)
                break
        except FileNotFoundError:
            number = input('Please Enter your favor number.')
            try:
                int(number)
            except ValueError:
                print('You Have Enter not a number , try again.')
            else:
                with open(filename,'w') as file_obj:
                    json.dump(number,file_obj)
                    break

def read_fav_num(filename):
    """ Read number from file and print to console. """
    try:
        with open(filename) as file_obj:
            content = json.load(file_obj)
    except FileNotFoundError:
        print('Can find the file you want.')
    else:
        print('I know your fav number is ' + content)

input_fav_num('txt/number4.json')
#read_fav_num('txt/number.json')

