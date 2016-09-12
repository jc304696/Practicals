"""name: Lyle Martin
   practical: Lab 7 do from scratch excercise

   """
CURRENT_YEAR = 2016

class GuitarApp():
    def __init__(self, name="", year=1900, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:.2f} {}".format(self.name, self.year, float(self.cost), "(Vinttage)" if self.is_vintage() else "")

    def get_age(self):
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
