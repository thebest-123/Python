def multiply(num1, num2):
    mul = num1 * num2
    print("Product:", mul)

multiply(20, 10)
multiply(5, 10)


def total_calc(bill_amount, tip_perc):
    # define function to calculate the tip on bill
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")

# specify only bill_amount
# default value of tip percentage is used

total_calc(150, 20)


def age(currentyear, birthyear ):
    sub = currentyear - birthyear
    print("age:", sub)
age(2026, 2014)
    