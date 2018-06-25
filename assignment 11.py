#q 1
'''class animal:
    def annimal_attribute(self):
        print("animal attribute calling")
class tiger(animal):
    def show(self):
        self.annimal_attribute()
x=tiger()
x.show()

#q 2

#AB
#AB

#q 3

class cop:
    def __init__(self):
        self.n=input("enter name")
        self.age=int(input("enter age")
        self.work=input("enter work experience")
        self.d=input("enter designation")
    def display(self):
        print("name = %s \t age = %d \t experience = %s \t designation = %s"%(self.n,self.age,self.work,self.d))
    def update(self):
        self.n=input("enter name")
        self.age=int(input("enter age"))
        self.work = input("enter work experience")
        self.d = input("enter designation")
class mission(cop):
    def add_mission_details(self):
        self.m=input("mission details : ",self.n)
    def mission_display(self):
        print("name = %s \t age = %d \t experience = %s \t designation = %s"%(self.n,self.age,self.work,self.d))
m=mission()
m.display()
m.update()
m.add_mission_details()
m.mission_display()'''

#q 4

class shape:
    def show2(self):
        self.l=int(input("enter length"))
        self.b=int(input("enter breadth"))
class rectangle(shape):
    def area(self):
        self.show2()
        self.a=self.l*self.b
    def show1(self):
        print("area of rectangle : ",self.a)
class square(shape):
    c=0
    def area(self):
        self.show2()
        if(self.l==self.b):
            self.a=self.l*self.l
            self.c=1
        else:
            print("enter same length and breadth")
    def show1(self):
        if(self.c==1):
            print("area of square is : ",self.a)
        else:
            pass
r=rectangle()
s=square()
r.area()
r.show1()
s.area()
s.show1()
