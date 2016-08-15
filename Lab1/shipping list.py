menu = "C - Create shipping list\nQ - Quit"
WelcomeLine = "Welcome to the QuickyMart (select an option from the menu by entering the letter at the begining)"
print(WelcomeLine)
print(menu)


choice = input(">>> ").upper()
while choice != "Q":
    TotalCost = 0
    TotalNumberOfItems = 0
    if choice == "C":
        NumberOfItems = int(input("How many types of items are you wanting to ship? "))
        for number in range(0, NumberOfItems):
            cost = float(input("What is the price of item {:d}? $ ".format(number +1)))
            Qty = float(input("Quantity of item {:d}? ".format(number + 1)))
            print("\n")
            TotalCost += (cost * Qty)
            TotalNumberOfItems += Qty
        if TotalCost > 100:
            DiscountCost = TotalCost - (TotalCost * 0.1)
            print("Total Cost: $ {:.2f}".format(TotalCost))
            print("Total Cost with Discount: $ {:.2f}".format(DiscountCost))
            print("Total Number of Items: {:.1f} \n".format(TotalNumberOfItems))
        else:
            print("Total Cost: $ {:.2f}".format(TotalCost))
            print("Total Number of Items: {:.1f} \n".format(TotalNumberOfItems))
    else:
        print("Invalid Entry")
    print(WelcomeLine)
    print(menu)
    choice = input(">>> ").upper()
print("Thank you, come again.")

