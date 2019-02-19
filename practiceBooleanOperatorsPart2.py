# In this script implement examples of using boolean operators in practice

musclePain = False
fever = True
weakness = True

if musclePain and fever and weakness:
    print("Suspiction of influeneza")
else:
    print("The fli is unlikely")

###############################################

if musclePain and fever and weakness:
    print("Suspiction of influeneza")
elif not (fever and musclePain) and weakness :
    print("Just take a rest")
else:
    print("You may be cold")

################################################

isMan = True

if musclePain and fever and weakness or isMan and (musclePain and fever and weakness):
    print("Suspiction of influeneza")
elif not (fever and musclePain) and weakness :
    print("Just take a rest")
else:
    print("You may be cold")

###############################################

isCheckComplited = True

if isCheckComplited:
    print("Check is complited")
else:
    print("Check not done Yet!")

###############################################

print("Check is complited" if isCheckComplited else "Check not done Yet!")
