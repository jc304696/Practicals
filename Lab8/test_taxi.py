__author__ = 'Lyle'

from Lab8.taxi import Taxi

car_1 = Taxi('Prius 1', 100, 1.20)
car_1.drive(40)
print(car_1)

car_1.start_fare()
car_1.drive(100)
print(car_1)
