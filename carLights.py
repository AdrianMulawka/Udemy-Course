"""This program help with automate light devices implementend in cars"""
###################################################
isAutomaticMode = True
is80PercentLight = True
isDirectLight = False
isRainy = True

turnLightsOn = isAutomaticMode and ( not isDirectLight or isRainy or is80PercentLight )
print(turnLightsOn)

print("Automatic mode:   ", isAutomaticMode)
print("Is the light good:", is80PercentLight)
print("Is sun low:       ", isDirectLight)
print("Is it rainy:      ", isRainy)
print("TURN LIGHTS ON:   ", turnLightsOn)