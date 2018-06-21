import time,datetime,math,os
from time import gmtime,strftime
#q 1
print("time tuple is used to represent time in a way it is used to understand")
print("eg:index:0 year..index:1 month..index:2 day..index:3 hour..index:4 minute..index:5 sec..index:6 day")

#q 2

print("time: " + time.asctime(time.localtime()))

#q 3

print(time.strftime("%b"))

#q 4

print(time.strftime("%A"))

#q 5

date1=int(input("Enter date"))
year1=int(input("Enter year"))
mon1=int(input("Enter month"))
dateentered=datetime.date(year1,mon1,date1)
print(dateentered.strftime("%b"))

#q 6

print(strftime("%H %M %S",gmtime()))

#q 7

x=int(input("Enter any number: "))
print("the factorial is: "+ " " + str(math.factorial(x)))

#q 8

a=int(input("Enter 1 number"))
b=int(input("Enter 2 number"))
print("gcd is" + str(math.gcd(a,b)))

#q 9

print("current working directory"+str(os.getcwd()))
print("user environment"+str(os.environ))