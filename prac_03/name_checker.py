"""Name checking program. Will feature try methods for errors checking and loop logic"""

user_name = ''
while len(user_name.strip()) == 0 :
    user_name = input('What is your name?: ')
    if len(user_name.strip()) == 0:
        print('Input can not be blank')
print(user_name[1::2])