

class ProgrammingLanguage:
    def __init__(self, name="", is_dynamic= (), is_reflection = (), year = ()):
        self.name = name
        self.is_dynamic()
        self.is_reflection()
        self.year = input(int)