# Working with a collection Challenge

# Nearest stars to Earth

stars = [
    'Sol',
    'Alpha Centauri',
    'Barnard',
    'Wolf 359',
]

print(stars[3])

# Highest peak on each tectonic plate

peaks = {
    'African': 'Kilimanjaro',
    'Antarctic': 'Vinson',
    'Australian': 'Puncak Jaya',
    'Eurasian': 'Everest',
    'North_American': 'Denali',
    'Pacific': 'Mauna Kea',
    'South_American': 'Aconcagua',
}

print(peaks['Pacific'])

# CreatinChallengeg for loop Challenge

fruits = [
    'apples',
    'bananas',
    'dragon fruit',
    'mangos',
    'nectarines',
    'pears',
]

print('Our fruit selection:')
for fruit in fruits:
    print(fruit)

# Strings Challenge

miles = input('Enter a distance in miles: ')
miles_value = float(miles)
kilometers_value = miles_value * 1.609344
print(kilometers_value)

# Debugging Challenge


def plant_recommendation(care):
    if care == 'low':
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'high':
        print('orchid')


plant_recommendation('low')
plant_recommendation('medium')
plant_recommendation('high')
