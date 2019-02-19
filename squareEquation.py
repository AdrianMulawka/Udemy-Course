import math
def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

print("Please give me 3 numbers to count the solution of the quadratic equation")

downloadedValue1 = input("Value of first variable:")
downloadedValue2 = input("Value of second variable:")
downloadedValue3 = input("Value of second variable:")

if not check_int(downloadedValue1) and check_int(downloadedValue2) and check_int(downloadedValue3):
    print("I will calculate the equation only if you give me integers")
else:
    a = int(downloadedValue1)
    b = int(downloadedValue2)
    c = int(downloadedValue3)

    if a == 0:
        print("This is not a square equation, a cannot equals 0!")
    else:
        delta = b*b - 4*(a*c)
        if delta < 0:
            print("No solutions")
        elif delta == 0:
            x1 = (-b - math.sqrt(delta)) / 2 * a
            print("The result is -", x1)
        else:
            x1 = (-b - math.sqrt(delta)) / 2 * a
            x2 = (-b + math.sqrt(delta)) / 2 * a
            print("The results equals -", x1, " and ", x2, ".")