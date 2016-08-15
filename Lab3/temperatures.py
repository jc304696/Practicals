__author__ = 'Lyle Martin'

def main():
    finished = False
    while not finished:
        option = user_input()
        finished = temp_conversion(option)
    print('Thank you.')

def user_input():
    global MENU, choice
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = str(input(">>> ")).upper()
    return choice

def temp_conversion(option):
        if option == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9.0 / 5 + 32
            print("Result: {:.2f} F".format(fahrenheit))
            finished = False
        elif option == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = 5 / 9 * (fahrenheit - 32)
            print("Result: {:.2f} C".format(celsius))
            finished = False
        elif option == "Q":
            finished = True

        return finished

main()


