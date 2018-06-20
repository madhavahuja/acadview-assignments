#q 1
def area(r):
    a=3.14*r*r
    print(a)
r=float(input("Enter the radius of the circle"))
area(r)

#q 2

def perfect(n):
    sum = 0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
        return True
    else:
        return False
for i in range(1,1001):
    if(perfect(i)==True):
        print("perfect number is" + str(i))
    else:
        pass

#q 3

def mul_table(n,i=1):
    if i==11:
        return
    print(str(n) + " x " + str(i) + " = " + str(n*i))
    mul_table(n,i+1)
mul_table(int(input("enter the number")))

#q 4
def pow(a,b):
    if(b==0):
        return 1
    else:
        return(a*pow(a,b-1))
a=int(input("enter number"))
b=int(input("enter power"))
p=pow(a,b)
print(p)

#q 5

a={}
def fact(i):
    if(i==1):
        return 1
    else:
        f=i*fact(i-1)
        return f
a1=int(input("enter number"))
f1=fact(a1)
a[a1]=f1
print("dictionary",a)