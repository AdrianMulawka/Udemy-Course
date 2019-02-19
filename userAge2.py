# this program take age from user and give them information in which year he will be a hundred years man
import datetime

name=input(str("Hi what's Your name"))
print("Hello ", name)
wiek=int(input("Please give me information about your age and I told you in \n"
      "witch year you will be a hundred years old  man. So how old are you  "))
oldMan = 100-wiek

now=datetime.datetime.now()
x =(int(now.strftime("%Y"))) + oldMan

print("You Will be terrible old in ",x, " year")
