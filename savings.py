#This program will help you calculate how much money you will save depending on the amount of funds deposited, the interest rate of the deposit and time.

initialCapital = 20000
interest = 0.03
maxTimeYear = 10
capital = initialCapital

i = 0

for i in range(i, maxTimeYear):
    capital = round((1 + interest) * capital, 2)
    print("In % s year you saved %s money" % (i, capital))
    i+=1

yourSavedMoney = capital-initialCapital

print("By 10 years economize you saved %s money " % (yourSavedMoney))

