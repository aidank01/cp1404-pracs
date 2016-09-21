
from prac_07.programming_language import ProgrammingLanguage

def main():

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    print(ruby)


    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    print(python)


    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(vb)

    language_list = [ruby, python, vb]

    print("\nThe dynamically typed languages are:")
    for lang in language_list:
        if lang.typing == "Dynamic":
            print(lang.name)

main()
