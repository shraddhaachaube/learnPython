# #comment out to run a particular block of code
# #dictionary --> key:value pairs, unordered, mutable
# dict1 = {"name": "Sid", "age": 19, "city": "NYC"}
# print(dict1)

# dict2 = dict(name= "Anne", age= 18, city= "Boston")
# print(dict2["name"]) #vlaues are accessed using the key

# #inserting at the end of the dictionary
# dict2["grade"] = 'A'
# print(dict2)
# #we can overwrite the value of any key
# dict2["grade"] = 'B'
# print(dict2)

# #to delete from a dictionary using del

# dict3 = {"name": "Shri", "age": 20, "city": "ddn"}
# del dict3["city"]
# print(dict3)
# #using pop method
# dict3.pop("age")
# print(dict3)
# #using popitem  method which pops the last inserted item
# dict3.popitem()
# print(dict3)

# #to check whether a key is in the dictionary or not

# #by if else statement
# dict4 = {"name": "Kia", "age": 19, "city": "NYC"}
# if "name" in dict4:
#     print("Yes")
# else:
#     print("No")
# #by try except statement
# try:
#     print(dict4["age1"])
# except:
#     print("Error!")

# #printing keys using loop

# dict5 = {"name": "Ria", "age": 19, "city": "NYC"}
# for i in dict5.keys():
#     print(i)
# #prinitng values using loop
# for i in dict5.values():
#     print(i)
# #printing both key and values at once
# for i, j in dict5.items():
#     print(i, j)

# #copying a dictionary

# dict6 = {"name": "Maira", "age": 26, "city": "manchester"}
# dict6_cpy = dict6 #but in this if we will alter the copied dictionary, the original dictionary will also be altered
# print (dict6)
# dict6_cpy["Grade"] = 'A'
# print(dict6_cpy)
# print(dict6)

# #to avoid this

# dict7 = {"name": "kaira", "age": 16, "city": "Boston"}
# dict7_cpy = dict7.copy()
# #or dict7_cpy = dict(dict7)
# dict7_cpy["Grade"] = 'A'
# print(dict7_cpy)
# print(dict7)

# #update two dictionaries

# dict7.update(dict6)
# print(dict7)

# #we can use a tuple as a key 'cause it is immutable but not a list 'cause lists are mutable 
# #value can be anythings
