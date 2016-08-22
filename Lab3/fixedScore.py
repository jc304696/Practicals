__author__ = 'Lyle Martin'

def main():
    print('Press any letter to exit')
    while True:
        try:
            score = float(input("Enter score: "))
            score_check(score)
        except ValueError:
            print('Thank you')
            break


def score_check(score):
    if score < 0 or score > 100:
        print("Invalid Score")
    elif score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    else:
        print("Bad")

main()