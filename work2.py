def greet(name):#parameter:
    print("Good morning",name)
    print("How was your night?")


greet("David")#argument
print("\n")
greet("Evan")
print("\n")
greet("Danstan")

def add(a,b,c):
    addition = a+b+c
    print(addition)

add(10,20,30)

def sub(a,b):
    sub = a-b
    return sub
print(sub(30,20))


def details():
    name =input("Enter name:")
    age = int(input("Enter age:"))
    print(name)
    print(age)


details()