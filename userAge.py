#this programm take age from user by conoler and give them
# information in which year he will have houndres years
import datetime

name=input(str("Hi what's Your name"))
print("Hello ", name)
wiek=int(input("Please give me information about your age and I told you in \n"
      "witch year you will be a haundred years old. So how old are you  "))
oldMan = 100-wiek

now=datetime.datetime.now()
x =(int(now.strftime("%Y"))) + oldMan

print("You Will be terrible old in ",x, " year")
