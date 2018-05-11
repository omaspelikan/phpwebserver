# exercise 3-4, 3-5, 3-6
guestList = ['Superman','Batman','Wonderwoman','Flash']
print('guest list : ', guestList, 'were invited to dinner.')
for a in guestList:
    print(a.title()+' was invited to dinner.')
# change one guest
re_guest = guestList.pop(1)
print(re_guest + ' will not come to dinner party.')
guestList.append('Aquaman')
for a in guestList:
    print(a.title()+' was invited to dinner.')
print('\n\nguest list : ', guestList, 'were invited to dinner.')

#3-6
print('I have preorder a bigger table for dinner party')
guestList.insert(0,'Superwoman')
#print(int(len(guestList)/2))
guestList.insert((int(len(guestList)/2)),'Joker')
guestList.append('Harley')
#print(guestList)
for a in guestList:
    print(a.title()+' was invited to dinner.')

# 3-7
print('I cannot get a bigger table for dinner, so plan has changed ,only two quests I can invite.')
while (len(guestList) >2):
    print('sorry '+guestList.pop()+' only first 2 peple can join dinner party.')
for b in guestList:
    print('congra! '+ b +' you have be invited to dinner party.')
del guestList[0]
del guestList[0]
#print(guestList)
print('There are ', guestList, ' people in dinner party')
