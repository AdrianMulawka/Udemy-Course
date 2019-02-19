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

#This program will help you find long words in the text, that is, words that consist of at least six characters

text = """United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier."""

listOfWords = text.split(" ")
print(listOfWords)

shortWords = []
longWords = []

for i in range(len(listOfWords)):
    if len(listOfWords[i]) <= 6:
        shortWords.append(listOfWords[i])
    if len(listOfWords[i]) > 6:
        listOfWords.append(listOfWords[i])
print("In text is %s words longer then six sighns." % len(shortWords))

