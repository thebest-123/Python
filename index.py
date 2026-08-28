age = int(input("Enter age: "))

if age >= 18:
    print("You can vote")

else:
    print("You cant vote")




print("*********************************")

#0-5 infant
#6-12 child
#13-19 teenager
#20+ adult

if age >= 0 and age <= 5:
    print("infant")

elif age >= 6 and age <= 12:

    print("Child")  
elif age >= 13 and age <= 19:
    print("teenager")

elif age >= 20 and age <= 120:
    print("aldut")
else:
    print("invalid age")
