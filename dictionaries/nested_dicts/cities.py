cities = {
    'mumbai': {
        'country': 'india',
        'population': 12478447,
        'fact': 'Mumbai is the financial and entertainment capital of India'
        },
    'new york': {
        'country': 'USA',
        'population': 8398748,
        'fact': 'New York is home to the highest number of billionaires of any city in the world.'
        },
    'paris':{
        'country': 'France',
        'population': 2148271,
        'fact': 'Paris has the second busiest metro system in Europe after the Moscow Metro.'
        }
    }

for city, info in cities.items():
    print('\nCity: '+city.title())
    print(city.title() + " city is located in the country " +
          info['country'].title() + ".\nIt has an estimated population of " +
          str(info['population']) + ".")
    print(info['fact'])
