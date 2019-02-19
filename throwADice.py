# This is script to simulate throwing of dice
import random

"""min = 1
max = 6

dice = random.randint(min,max)

if dice == 1:
    print("o")
elif dice == 2:
    print("o \no")
elif dice == 3:
    print("o \no \no")
elif dice == 4:
    print("o o\no o")
elif dice == 5:
    print("o o\n o\no o")
elif dice == 6:
    print("o o\no o\no o")
else:
    print("Sorry our cube have only six sides :)")"""

min = 1
max = 6
dice = []
i = 1
j = len(dice)
while i <= 5:
    dice.append(random.randint(min,max))
    i += 1
    print(dice)

dice.sort()
print(dice)

for dice[j] in dice:
    if dice[j] == 1:
        print(dice[j], "\no")
    elif dice[j] == 2:
        print(dice[j], "\no \no")
    elif dice[j] == 3:
        print(dice[j], "\no \no \no")
    elif dice[j] == 4:
        print(dice[j], "\no o\no o")
    elif dice[j] == 5:
        print(dice[j], "\no o\n o\no o")
    elif dice[j] == 6:
        print(dice[j], "\no o\no o\no o")