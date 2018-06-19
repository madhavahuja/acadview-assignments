#q 1

'''l=[]
for a in range(10):
    a=int(input("Enter 10 inegers"))
    l.append(a)
print(l)'''

#q 2

'''while(true):
    print("infinte")'''

#q 3
'''l=[]
j=[]
for a in range(10):
    a=int(input("Enter 10 integers"))
    l.append(a)
    j.append(a*a)
print(l)
print(j)'''

#q 4
l=[]
j=[]
k=[]
for i in range(10):
    a=input("Enter integer strings and float")
    if(isinstance(a,int)):
        l.append(a)
    elif(isinstance(a,str)):
        j.append(a)
    else:
        k.append(a)
print("integer",l)
print("string",j)
print("fload",k)
#q 5
even=[]
odd=[]
for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even" + str(even) +"odd" + str(odd))

#q 6
for i in range(0,4):
    print("")
    for j in range(0,i+1):
        print("*",end="")

#q 7

d={"name": "madhav", "age":20}
for i in d:
    d.get(i)
    print(i)

#q 8

l=[]
for i in range(0,5):
    n=int(input("enter the number"))
    l.append(n)
print(l)
i=[]
a=int(input("Enter the value"))
x=l.index(2)
x=l.remove(2)
print(l)