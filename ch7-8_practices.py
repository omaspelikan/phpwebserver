# 7-8 Deli / 7-9
sandwich_orders = ['plain','double','beef','pork','pastrami','corn','pastrami']
sandwich_finished = []

print('we have run out of pastrami.')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    order = sandwich_orders.pop()
    print('I made you a ' + order + ' sandwich')
    sandwich_finished.append(order)
    
print('I have finished ', sandwich_finished, ' sandwich.')
    