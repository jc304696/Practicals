"""
Do-from-scratch Execise - Inheritance
Lyle Martin
"""

from Lab08.taxi import Taxi, SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

def main():
    total_cost = 0
    menu = 'q)uit, c)hoose taxi, d)rive'
    print("Let's drive!")
    print(menu)
    choice = input('>>> ')

    while choice != 'q':
        if choice == 'c':
            print('Taxis available:')
            print_taxis(taxis)
            users_choice = int(input('Choose taxi: '))
            taxi = taxis[users_choice]
            print('Bill to date: ${:.2f}'.format(total_cost))

        if choice == 'd':
            taxi.start_fare()
            distance_wished_to_travel = int(input('Drive how far: '))
            taxi.drive(distance_wished_to_travel)
            total_cost += float(taxi.get_fare())
            print('Your {} trip cost you ${:.2f}'.format(taxi.name, float(taxi.get_fare())))
            print('Bill to date: ${:.2f}'.format(total_cost))

        print(menu)
        choice = input('>>> ')

    print('Total trip cost: ${:.2f}'.format(total_cost))
    print('Taxis are now: ')
    print_taxis(taxis)

def print_taxis(taxis):
    for taxi in range(0, len(taxis)):
        print("{} - {}".format(taxi, taxis[taxi]))

main()