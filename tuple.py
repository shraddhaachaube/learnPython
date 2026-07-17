# #comment out to run a particular block of code
# #tuples --> ordered, immutable, allows duplicate element
# import sys
# import timeit

# mytuple = ("hello", 33, "bye") #or can be written as mytuple = "hello", 33, "bye"
# print(mytuple)

# #if we pass a single element inside parenthesis it will be considered as a string -- to make it tuple we need to add a comma at the end of the element
 
# isTuple = ("okay")
# print(type(isTuple))
# singleTuple = ("okay",)
# print(type(singleTuple))

# #tuple from a list using tuple function

# lTuple = tuple(["hnn", 46, "okayyzz"])
# print(lTuple)
# #accessing element using index
# lTuple1 = (1,"hie", 99)
# print(lTuple1[0])
# print(lTuple1[-1])
# #print(lTuple1[3]) error --index out of range

# #lTuple[0] = "hello" --> error 'cause tuples are immutable

# #printing element through iteration

# mytuple1 = (11,"this", 77)
# for i in mytuple1:
#     print(i)

# #checking if the element is present in the tuple or not

# mytuple2 = ("max", 88, "rio")
# if "max" in mytuple2:
#     print("yes")
# else:
#     print("no")

# #checking the length of the tuple

# mytuple3 = ('a','b','b','d','e')
# print(len(mytuple3))
# #for counting the number of something in the tuple
# print(mytuple3.count('b'))

# #checking the index of an element

# ituple = ('a', 'l', 'i', 'a', 'b')
# print(ituple.index('l'))
# #tuple to list conversion
# mylist = list(ituple)
# print(mylist)

# #slicing

# stuple = (9,7,6,3,4,0,3,7,5)
# print(stuple[2:6])
# print(stuple[:5])
# print(stuple[4:])
# print(stuple[::2])
# print(stuple[::-1]) #for reversing

# #unpacking items

# untuple = (1,2,3,4,5)
# a1, *a2, a3 = untuple
# print(a1)
# print(a3)
# print(a2) # *a2 add all the elements in between and create a list and assign it to the variable

# #comparing list and tuple on the basis of size by importing sys and using sys.getsizeof

# cmp_list = [1, "hello", 44, 'A']
# cmp_tuple = (1, "hello", 44, 'A')
# print(sys.getsizeof(cmp_list), "bytes")
# print(sys.getsizeof(cmp_tuple), "bytes")

# #comparing list and tuple on the basis of time it takes to create both 1 million times by importing timeit and using timeit.timeit

# print(timeit.timeit(stmt="[1,2,3,4,5]", number = 1000000))
# print(timeit.timeit(stmt="(1,2,3,4,5)", number = 1000000))

