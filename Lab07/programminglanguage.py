"""name: Lyle Martin
   pratical: Lab 7 intermediate exercise

"""

class ProgrammingLangauge():
    def __init__(self, name="", typing="", reflection=False, year=1990):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            # print(True)
            return True
        else:
            # print(False)
            return False

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)


