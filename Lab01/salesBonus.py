"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

MENU = "C - To calculate bonus\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        sales = float(input('Sales Amount: '))
        if sales >= 1000:
            bonus = sales * 0.15
        else:
            bonus = sales * 0.1
        print("Your bonus is ${:.2f}".format(bonus))
    else:
        print("invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print('Thank you.')


