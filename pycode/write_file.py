#python write a file
nameHandle = open('play.txt','w')
for x in range(2):
    x = input("Please input a line")
    nameHandle.write(x+'\n')
nameHandle.close()