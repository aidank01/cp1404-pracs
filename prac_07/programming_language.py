

class ProgrammingLanguage:
    def __init__(self, name = "", typing ="", reflection = False, year = 0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """ defines output string for each language"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self, typing):
        if typing == "dynamic".upper():
            typing = True
        else:
            typing = False

        if typing == True:
            return "Dynamic Typing"
        else:
            return "Static Typing"