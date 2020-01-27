sandwich_orders = ['bacon sandwich',
                   'pastrami',
                   'cheese sandwich',
                   'tuna sandwich',
                   'pastrami',
                   'ham sandwich',
                   'pastrami',
                   'chicken sandwich'
                   ]

print('We ran out of pastrami. Removing all pastrami orders')
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    finished_sandwiches.append(sandwich_orders.pop())

for sandwich in finished_sandwiches:
    print("Done making " + sandwich.title())
