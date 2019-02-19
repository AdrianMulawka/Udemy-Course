# This is simple proposition of draw teams in championship
import random
countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
]

random.shuffle(countries)
groupNumner = 0
iMax = len(countries)

for i in range(len(countries)):
    if i % 4 == 0:
        groupNumner+=1
    print("Group %d" % (groupNumner))
    print(countries[i])