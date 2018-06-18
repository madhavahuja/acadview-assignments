#q 1
a=int(input("Enter year"))
if(a%4==0):
    print("Its a leap year")
else:
    print("Its not a leap year")

#q 2
a=int(input("enter the length"))
b=int(input("enter the breadth"))
if(a==b):
    print("its a square")
else:
    print("its a rectangele")

#q 3

a=int(input("enter age of 1st person"))
b=int(input("Enter the age of 2nd person"))
c=int(input("Enter the age of 3rd person"))
if(a>b):
    if(a>c):
        print("1st person is oldest")
    else:
        print("3rd person is oldest")
elif(c>b and a>b):
    print("2nd person is youngest")
elif(b>c and a>c):
    print("3rd person is youngest")
elif(b>d and b>c):
    print("2nd person is oldest")
else:
    if(c>a):
        print("2nd person is youngest")
#q 4

a=int(input("enter the points out of 200"))
if(a>=1 and a<=50):
    print("Sorry! No prize this time")
elif(a>50 and a<=150):
    print("Congratulations! you won wodden dog")
elif(a>150 and a<=180):
    print("Congratulations! you won a book")
elif(a>180 and a<=200):
    print("Congratulations! you won chocolates")
else:
    print("you have entered incorrect points")

#q 5

a=int(input("Enter the total number of units where each unit costs ₹100"))
sum=a*100
if(sum>=1000):
    b=sum-(sum/10)
    print("total prize:- ",b)
else:
    print("total prize:- ",sum)
