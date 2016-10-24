finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a number: "))
        finished = True
    except ValueError:
        print("The entry was not a number")
print("Valid result is: {}".format(result))
