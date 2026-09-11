while True:
    num = int(input("Guess the number:"))
    if num == 10:
        print("Yaay You got it")
        break
    else:
        print("Try again")


for row in range(5):
    for column in range(3):
        print("rw")
    print("\n")