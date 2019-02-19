#This script contain few examples of using maths calculations with using loop while
firstRow = 1
lastRow = 31
currentRow = firstRow

while currentRow <= lastRow:
    print('Row number '+ str(currentRow))
    currentRow += 1

###################################################

i = 1
imax = 13

while i <= imax:
    a = i * i
    b = i * i * i
    print("Kwadrat dla liczby ",i, " wynosi ",a," sześcian dla liczby ",i," wynosi ",b,)
    i+=1
else:
    print("Skończyłem wyliczanie kwadratów i sześcianów liczb z zakresu od 1 do 13")

####################################################

I = 1
IMax = 16

while I <= IMax:
    c = 2**I
    print("Dwa do potęgi ",I, " równa się ",c,)
    I+=1
else:
    print("Oto lista potęg liczby 2 w zakresie od 1 do 16")

####################################################

j = 1
jMax = 10

while j <= jMax:
    print("x"*j)
    j+=1