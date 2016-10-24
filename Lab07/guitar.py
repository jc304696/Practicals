
from Lab07.guitarData import GuitarApp

fender = GuitarApp('Fender Stratocaster', 2014, 765.4)
gibson = GuitarApp('Gibson L-5 CES', 1922, 16035.40)
line = GuitarApp('Line 6 JTV-59', 2010, 1512.9)

my_guitars = [fender, gibson, line]

print("My guitars!")
for guitar in my_guitars:
    print("Name: {}".format(guitar.name))
    print("Year: {}".format(guitar.year))
    print("Cost: {:.2f}".format(float(guitar.cost)))
    print(guitar)
