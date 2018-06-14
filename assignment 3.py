#q 1
x,y,z=input("enter any number").split(",")
l=[]
l.append(x)
l.append(y)
l.append(z)
print(l)

#q 2
list=["google","apple","facebook","microsoft","tesla"]
l.append(list)
print(l)

#q 3
print(sum(c.count("google") for c in list))

#q 4
a=[5,6,9,8,3,5,7,9,0]
a.sort()
print(a)

#q 5
a=[1,2,3,5,6,7]
b=[2,4,5,6,8]
c=a+b
c.sort()
print(c)

#q 6    stack
a=[1,2,3,4,5,6,7,8]
a.pop()
print(a)
a.append(9)
print(a)

#queue
import queue
a = queue.Queue(maxsize=20)
a.put(1)
a.put(2)
a.put(3)
a.put(4)
print(a.get())
print(a.get())
print(a.get())
print(a.get())

#q 7 optional question

l=[1,2,3,4,5,6,7,8,9]

odd=[]
even=[]
count=0
for x in l:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print("Even list",even,len(even))
print("Odd list",odd,len(odd))
