# In this script is three examples of using boolean operators in practice

minLike = 500
minShare = 100
numLike = 50
numShare = 50

if minShare <= numShare and minLike <= numLike :
    print('Thank for your likes and shares, we have for you 10% discount for our all assortment')
elif minLike > numLike:
    print('If we get ' +str(minLike-numLike)+' more likes we will start our discount for our assortment')
elif minShare > numShare:
    print('If we get ' +str(minShare-numShare)+ ' more shares we will start our discount for our assortment')

##########################################################################################################

isWeeksnd = False
isOrderPizza = False
isOrderBigDrink = False

if not isWeeksnd and (isOrderPizza or isOrderBigDrink):
    print ("Thanks for your order, we have for you voucher for extra free burger")
elif not (isOrderBigDrink or isOrderPizza):
    print("If you order pizza or Big Drink too we give you voucher for free burger")
elif isWeeksnd:
    print("For orders between monday and friday for pizza or Big Drink we give you burger voucher")
