__author__ = 'Lyle'

from Lab8.taxi import SilverServiceTaxi

total_cost = 0

car_1 = SilverServiceTaxi('Limo', 100, 2)
car_2 = SilverServiceTaxi('Hummer', 200, 4)
print(car_1)
print(car_2)
print('toatl cost: {}\n'.format(total_cost))

car_1.drive(10)
total_cost += car_1.get_fare()
car_2.drive(10)
total_cost += car_2.get_fare()
print(car_1)
print(car_2)
print('toatl cost: {}\n'.format(total_cost))

car_1.start_fare()
car_2.start_fare()
car_1.drive(30)
total_cost += car_1.get_fare()
car_2.drive(100)
total_cost += car_2.get_fare()
print(car_1)
print(car_2)
print('toatl cost: {}\n'.format(total_cost))