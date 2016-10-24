__author__ = "Lyle Martin"


def main():
    monthlyIncomes = []
    months = int(input('How many months? '))
    for income in range(1, months + 1):
        earnings = float(input("Enter income for month " + str(income) + ": "))
        monthlyIncomes.append(earnings)
        income += 1
    printReport(monthlyIncomes)

def printReport(monthlyIncomes):
    print('Income Report\n--------------')
    total = 0
    for line in range(0,len(monthlyIncomes)):
        total += monthlyIncomes[line]
        print("Month {0:4} - Income: $ {1:10.2f} Total: $ {2:10.2f}".format((line + 1), float(monthlyIncomes[line]), float(total)))
        line += 1

main()