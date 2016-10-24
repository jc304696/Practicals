__author__ = 'Lyle'

from Lab08.taxi import Taxi
total_cost = 0

car_1 = Taxi('Prius 1', 100)
print(car_1)
print(total_cost)

car_1.drive(40)
total_cost = car_1.get_fare()
print(car_1)
print(total_cost)

car_1.start_fare()
car_1.drive(100)
total_cost = car_1.get_fare()
print(car_1)
print(total_cost)
