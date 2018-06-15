#q 1   tuples
a=(1,2,3,"apple")
print(len(a))

#q 2
b=(1,2,3,4,5,6)
print(min(b))
print(max(b))

#q 3
l=(1,2,3,4)
n=1
for i in l:
    n=n*i
print(n)

#q 4  sets

a=set([1,2,3,4])
b=set([2,3,4])
print(a-b)
print(b-a)
print(a<=b)
print(b<=a)
print(a>=b)
print(b>=a)
print(a&b)

#q 5    Dictionary

d={}
c=0
while c<10:
   name=input("Enter name of 10 students ")
   mark=input("Enter your mark out of 100 ")
   if name not in d:
       d[name] = mark
       c=c+1
   else:
       print("name already exists in dictionary")
print(d)
#q 6
from operator import itemgetter
sorted_d=sorted(d.items(),key=itemgetter(1))
print(sorted(d.items()))

#q 7

m="qwertyqwerty"
d={}
for w in m:
    d[w]=m.count(w)
for x in sorted(d):
    print(x+'-'+str(d[x]))
