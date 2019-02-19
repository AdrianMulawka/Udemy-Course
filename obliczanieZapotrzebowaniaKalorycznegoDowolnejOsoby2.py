# Jest to prosty kalkulator który ma za zadanie obliczyć dzienne zapotrzebpwanie
# kaloryczne uwzględniajac interakcję z użytkownikiem w konsoli

print("Cześć, pomogę Ci obliczyć Twoje zapotrzebowanie kaloryczne")
print("Ale by tego dokonać potrzebuję kilku informacji o Tobie")

płeć = input(str("Na początku muszę wiedzieć czy jesteś kobietą czy mężczyzną, wybież K/M"))

S = 0
if płeć == "M":
    S = 5
else:
    S = -161

imię = input(str("Teraz zdradź mi proszę jak masz na imię :)"))

print("Witaj ", imię, " w takim razie zabieramy się do pracy!")

wzrost = int(input("Teraz podaj nam swój wzrost w centymetrach"))

waga = int(input("Teraz poproszę zdradź mi ile wążysz "))

wiek = int(input("No i oczywiście muszę jeszcze wiedzieć ile masz lat"))

aktywnosc = {"A": 1.2, "B": 1.4, "C": 1.6, "D": 1.8, "E": 2.0}
print("Bardzo ważne jest również określenie poziomu Twojej aktywności, ")
print("W celu dokonania właściwego wyboru wzkaż proszę odpowiedni dla siebie wariant")

print("A - Praca siedząca, brak dodatkowej aktywności fizycznej")
print("B - Praca niefizyczna, mało aktywny tryb życia")
print("C - Lekka praca fizyczna ćwiczenia 3-4 razy w tygodniu")
print("D - Praca fizyczna ćwiczenia 5 razy w tugodnniu")
print("E - Ciężka praca fizyczna ćwiczenia 7 razy w tygodniu ")

p=input("Wybierz odpowiadającą dla siebie opcję A , B , C , D lub E")
ap=aktywnosc[p]



PPM = (10 * waga) + (6.25 * wzrost) + (5 * wiek) + S

print(imię, " Twoje dzienne zapotrzebowanie kaloryczne uwzględniająć przemianę materi wynosi ", PPM, " kcal")
print("Wynik z uwzględnieniem trybu aktywności fizycznej wynosi ",PPM*ap)
