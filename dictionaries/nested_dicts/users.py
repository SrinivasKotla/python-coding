user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

user_1 = {
    'username': 'ravis',
    'first': 'ravi',
    'last': 'sharma',
    }

user_2 = {
    'username': 'rambo',
    'first': 'ram',
    'last': 'babu',
    }

users = [user_0, user_1, user_2]

for user in users:
    for key, val in user.items():
        print(key.title()+": "+val)
    print('\n')
