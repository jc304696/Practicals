LOWER = 32
UPPER = 127


"""print("Enter a number ({0} - {1}):".format(LOWER,UPPER))

for i in range(32, 127, 1):
    character = chr(i)
    print("Number {0:>3} is '{1:>2}' in ASCII".format(i, character))"""


def main():
    finished = False
    print("Enter a number ({}-{})".format(LOWER,UPPER))
    while not finished:
        try:
            number = int(input(">>> "))
            finished = get_number(number)
        except ValueError:
            print("please enter a valid number!")
            number = int(input(">>> "))
            finished = get_number(number)
    character = chr(number)
    print('The ASCII character for {} is {}'.format(number, character))

def get_number(number):
    if LOWER <= number <= UPPER:
        return True
    else:
        print("please enter a valid number!")
        return False

main()