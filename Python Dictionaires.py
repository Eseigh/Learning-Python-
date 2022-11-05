cities = {'Wales': 'Cardiff',
          'England': 'London',
          'Scotland': 'Edinburgh',
          'Northern Ireland': 'Belfast',
          'Ireland': 'Dublin'}
print(cities)

cities = {'Wales': 'Cardiff',
          'England': 'London',
          'Scotland': 'Edinburgh',
          'Northern Ireland': 'Belfast',
          'Ireland': 'Dublin'}
print(cities)
print('cities[Wales]:', cities['Wales'])  # Accessing Items via Keys
cities['France'] = 'Paris'  # Adding a New Entry
print(cities)
cities['Wales'] = 'Swansea'  # Changing a Keys Value
print(cities)
cities.pop('Northern Ireland')  # Removing an Entry
print(cities)
cities.clear()  # clearing the dictionary
print(cities)

cities = {'Wales': 'Cardiff',
          'England': 'London',
          'Scotland': 'Edinburgh',
          'Northern Ireland': 'Belfast',
          'Ireland': 'Dublin'}
for country in cities:
    print(country, ',', cities[country])

cities = {'Wales': 'Cardiff',
          'England': 'London',
          'Scotland': 'Edinburgh',
          'Northern Ireland': 'Belfast',
          'Ireland': 'Dublin'}
print(cities.values())
print(cities.keys())
print(cities.items())

cities = {'Wales': 'Cardiff',
          'England': 'London',
          'Scotland': 'Edinburgh',
          'Northern Ireland': 'Belfast',
          'Ireland': 'Dublin'}
print('Wales' in cities)
print('France' not in cities)

print(len(cities))  # Obtaining the Length of a Dictionary
seasons = {'Spring': ('Mar', 'Apr', 'May'),
           'Summer': ('June', 'July', 'August'),
           'Autumn': ('September', 'October', 'November'),
           'Winter': ('December', 'January', 'February')}
print(seasons['Spring'])
print(seasons['Spring'][1])
