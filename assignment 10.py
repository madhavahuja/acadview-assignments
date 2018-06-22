#q 3
class circle():
    def __init__(self,radius):
        self.r=radius
    def getarea(self):
        print("area of circle : "+ str(3.14*self.r*self.r))
    def getcircumfrence(self):
        print("circumfrence of circle : " + str(2*3.14*self.r))
a=circle(3)
a.getarea()
a.getcircumfrence()

#q 2

class student():
    def __init__(self,name,rollno):
        self.n=name
        self.r=rollno
    def display(self):
        print("Name of the student is : " + str(self.n) + " rollno of the student is : " + str(self.r))
a=student("Madhav",16)
a.display()

#q 3

class temprature():
    def __init__(self,celsius,farheniet):
        self.c=celsius
        self.f=farheniet
    def celsius(self):
        print("temprature in celsius to farheniet is : " + str((self.c*1.8)+32))
    def farheniet(self):
        print("temprature in farheniet to celsius is : " + str((self.f-32)*0.556))
a=temprature(12,78)
a.celsius()
a.farheniet()

#q 4

class moviedetails:
    def __init__(self):
        moviename=input("enter movie name")
        an=input("enter artist name")
        year=int(input("enter year of movie release"))
        r=int(input("enter the rating of the movie"))
        self.name=moviename
        self.an=an
        self.year=year
        self.r=r
    def display(self):
        print("name : " + str(self.name) + " artist" + str(self.an) + " year of release" + str(self.year) + " rating out of 10" + str(self.r))
    def update(self,m,a,y,r):
        self.moviename2=m
        self.an2=a
        self.year2=y
        self.r2=r
        print("name " + str(self.moviename2) + " artist name" + str(self.an2) + " year of release" + str(self.year2) + "ratings out of 10" + str(self.r2))
c=moviedetails()
c.display()
moviename1=input("enter the updated movie")
an1=input("enter updated artist")
year1=int(input("enter the year of release"))
r1=int(input("enter the ratings out of 10"))
c.update(moviename1,an1,year1,r1)

#q 5

class expanditure:
    def __init__(self):
        b=int(input("enter savings"))
        a=int(input("enter money you spent"))
        self.a=a
        self.b=b
    def display(self):
        print("money saved is " + str(self.b) + " and money spent is " + str(self.a))
    def salary(self):
        self.c=self.a + self.b
    def displaysalary(self):
        print("total salary : ",self.c)
c=expanditure()
c.display()
c.salary()
c.displaysalary()