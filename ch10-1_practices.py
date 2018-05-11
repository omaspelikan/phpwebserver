# 10-1

while True:
    first_n = input('Pleae First number. ')
    
    if first_n == 'q':
        break
    second_n = input('Please Second number. ')
    
    try:
        answer = int(first_n)/int(second_n)
    except ZeroDivisionError:
        print('You can\'nt divide by 0!')
    else:
        print(answer)

filename = ['txt/program_pool.txt','txt/guestbook.txt', 'abc.txt']

def word_count(filename):
    """ count the words in the file """
    try:
        with open(filename) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        print('This file ' + filename + ' is not exist.')
    else:
        word = content.split()
        print('word counts: ' + str(len(word)))
for file in filename:
    word_count(file)



def addition(num1,num2):
    try:
        sum = int(num1) + int(num2)
    except ValueError:
        print('The number you enter in not a number. ')
    else:
        sum = int(num1) + int(num2)
        print(sum)


while True:
    n = input('Please input number 1 value: ')
    m = input('Please input number 2 value: ')
    if n =='quit':
        break
    elif m =='quit':
        break
    else:
        addition(n,m)
# 10-8 
dog = 'txt/dog.txt'
cat = 'txt/cats.txt'
def pet_list(filename):
    try:
        with open(filename) as file_obj:
            content = file_obj.read()
    except FileNotFoundError:
        print('The file: ' + filename + ' is not found.')
    else:
        print('\n' + content)

pet_list(dog)
pet_list(cat)