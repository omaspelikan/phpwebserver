#ch10 file io
filename = 'restaurant.py'
filename2 = 'pizza.py'
with open(filename) as file_object:
    for content in file_object:
        print(content.rstrip())
with open(filename2) as file_object:
    line = file_object.readlines()

filestring = ''
for i in line:
    filestring+=i.strip()

print(filestring)
print(len(filestring))

# 10-1
content2 = ''
filename3 = 'python_learning.txt'
with open(filename3) as file_object:
    #content = file_object.read()
    content2 = file_object.readlines()
    #print(content.rstrip())

#print(content)
for c in content2:
    print(c.rstrip().replace('*','&'))

# write to a file
filename4 = 'test.txt'
content4 =''
with open(filename4,'a') as file_object:
    file_object.write('This is a continuted line to the original content.\n')
    content4 = file_object.write('and it will show how to append to file.\n')
print('character counts: ',content4)

# 10-3 Guest Book
file = 'txt/guestbook.txt'
flag = True
while flag:
    guest_name = input('Welcome , Please enter your name: or Enter \'no\' to quit. /> ')
    if guest_name !='no':
        with open(file,'a') as file_object:
            file_object.write(guest_name + '\n')
    else:
        flag = False
# 10-5 program poll
flag = True
file = 'txt/program_pool.txt'
while flag:
    response = input('Please Enter your comment about programming or Enter \'quit\' to quit. /> ')
    if response != 'quit':
        with open(file,'a') as file_object:
            file_object.write(response + '\n')
    else:
        flag = False