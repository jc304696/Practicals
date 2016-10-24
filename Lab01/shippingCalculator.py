MENU = "A - Add item\nT - To return total cost\nQ - To quit"
print(MENU)
choice = input(">>> ").upper()


while choice != "Q":

    if choice == "A":
        number_of_items = int(input("How many items?"))
        total_items += number_of_items
        cost_of_item = float(input("What is the cost of the item: "))
        total_cost = total_cost + (cost_of_item * number_of_items)
        print("There are currently {:.2f}".format(number_of_items))
    elif choice == "T":
        if total_cost > 100:
            total_cost = total_cost * 0.1
        print("Total items:  {:.2f}".format(total_items))
        print("Total cost: ${:.2f}".format(total_cost))
    else:
        print("Invalid entry")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you")
