#Q1.
print("Exception is - ZeroDivisionError")
a=3
try:
    if(a<4):
        a=a/(a-3)
except ZeroDivisionError:
    print("Zero division error")
else:
    print(a)

#Q2.
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("Element at 3rd index is not present")

#Q3.
print("An exception")

#Q4.
print("-5.0")
print("a/b result in 0")

#Q5.
try:
    import qwerty
    a=int(input("Enter any number="))
except ImportError:
    print("No such file exists")
except ValueError:
    print("Please enter integer")