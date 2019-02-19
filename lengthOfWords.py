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

