current_users = ['andrew', 'admin', 'shanti', 'srinivas', 'harika']

new_users = ['Andrew', 'Meghana', 'Shivani', 'Srinivas', 'sita']

for user in new_users:
    if user.lower() in current_users:
        print('Username taken. Please enter a new username.')
    else:
        print('Username is available.')
