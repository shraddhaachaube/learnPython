# #comment out to run a particular block of the code
# #STRINGS --> ordered, immutable, text representation
# my_string = "Hello World"
# print(my_string)

# #acessing by index
# print(my_string[0])
# print(my_string[-1])

# #slicing 
# print(my_string[1:5])
# print(my_string[::2])
# print(my_string[::-1])

# #accessing all characters through loop
# for i in my_string:
#     print(i)

# #checking if the character is in the string or not
# if 'w' in my_string:
#     print("yes")
# else:
#     print("no")

# #concatenation
# firstName = "Tom"
# lastName = "Holland"
# print(firstName + lastName)
# print(firstName + ' ' + lastName)

# #trimming the unwanted spaces
# space = "   Hie, Sid here   "
# print(space)
# space = space.lstrip() #removes left side spaces
# print(space)
# space = space.rstrip() #removes right side spaces
# print(space)
# #to remove both side spaces at once use strip()

# #to upper case
# case_change = "HellO EveryOne"
# print(case_change)
# print(case_change.upper())

# #to lower case
# print(case_change.lower())

# #startswith
# print(case_change.startswith('H'))
# print(case_change.startswith('HellO'))
# #endswith
# print(case_change.endswith('o'))
# print(case_change.endswith('One'))

# #finding index
# string1 = "Hellloo Dear"
# print(string1.find('D'))
# print(string1.find('el'))
# print(string1.find('p'))

# #counting no. of character or substrings
# print(string1.count('l'))
# print(string1.count('lo'))

# #replacing string or character
# string2 = "I'm okay, don't worry"
# print(string2.replace('okay', 'fine'))
# print(string2)
# print(string2.replace('o', ' This is crazy '))

# #string to list
# myString = "How are you doing"
# myList = myString.split()
# print(myList)
# myString1 = "How,are,you,doing"
# print(myString1.split(","))

# #list to string
# new_string = ' '.join(myList)
# print(new_string)

# #string formatting --> %, .format(), f-Strings --- " % " --> %s for string, %d for integer, %f for floting point, %.3f to the specific point, in this it will give only 3 digits after the decimal point
# var = "Tom"
# myString2 = "The variable is %s" % var
# print(myString2)

# myString3 = "Hi this is {}".format(var)
# print(myString3)
# var1 = 3.1467649
# myString4 = "The variables are {} and {:.3f}".format(var,var1)
# print(myString4)

# myString5 = f"They are {var} and {var1 :.3f}"
# print(myString5)
