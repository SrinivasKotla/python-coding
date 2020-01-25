alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
print('\nAlien before modifying: '+str(alien_0))

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print('\nAlien after modifying: '+str(alien_0))
