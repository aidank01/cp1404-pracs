name  = "Gibson  L­5 CES"
year  = 1922
cost  = 16035.40
print("My  guitar:  " +  name  + ",  first  made  in  " +  str(year))

print("My  guitar:  {},  first  made  in  {}".format(name,  year))
print("My  guitar:  {0},  first  made  in  {1}".format(name,  year))
print("My  {0}  was  first  made  in  {1}  (that's  right,  {1}!)".format(name,  year))

#Formatting currency:
print("My  {}  would  cost  ${:,.2f}".format(name,  cost))
# Aligning columns:
numbers = [1, 19, 123, 456, -25]
for i in range(len(numbers)):
    print("Number  {0}  is  {1:>5}".format(i  + 1,  numbers[i]))


# dir(str)['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__',
# '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold',
# 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',
# 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
# 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
# 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
# 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title','translate', 'upper', 'zfill']