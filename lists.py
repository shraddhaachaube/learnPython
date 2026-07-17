# #comment out to run a particular block of code
# # lists --> ordered, mutable, allows duplicate elements

# l1 = ["A", "B", "C"]
# print(l1)

# l2 = [1, 35,11,14,98,30,22,77,30]
# print(l2)


# l4 = list() # or l2 = [] ----> empty list 
# print(l4)

# #accessing element using index
# print(l1[0])
# print(l1[1])
# print(l1[2])
# print(l1[-1])
# #print(l1[3]) error -- index out of range

# #printing list by iteration
# for i in l2:
#     print(i)

# #checking if the item is in the list
# if 10.11 in l2:
#     print("yes")
# else :
#     print("no")

# #to check the length of the list
# print(len(l2))

# #to add element at the end of the list
# l1.append("Hello")
# print(l1)

# #to add element at a specific index
# l1.insert(1, 1000)
# print(l1)

# #to delete the last element of the list
# l1.pop()
# print(l1)

# #to delete a particular item
# l1.remove("C")
# print(l1)

# #to delete whole list
# l1.clear()
# print(l1)

# #to reverse the list
# l2.reverse()
# print(l2)

# #to sort the list in ascending order
# l2.sort()
# print(l2)

# #if we don't wamt to change the list we can use sorted for sorting

# l3 = ['A', 'P', 'F','Y','B','Z']
# new_l3 = sorted(l3)
# print(new_l3)
# print(l3)
# #for same elements
# l5 = [1] * 5
# print(l5)
# #concatination
# con_list = l5 + l3
# print(con_list)

# #slicing

# l6 = [3,5,7,56,90,88,4,11]
# print(l6[1:5])
# print(l6[:5])
# print(l6[5:])
# print(l6[::2])
# print(l6[::-1])
 
# #to copy a list

# l7 = [1,2,3,4,5,6,7,8]
# l7_cpy = l7
# #l7_cpy = l7.copy()
# #l7_cpy = l7[:]
# #l7_cpy = list(l7)
# print(l7_cpy)
# l7_cpy.append("Hie")
# print(l7)
# #but in this, if we update l7_cpy, l7 will also be updated automatically-- to avoid this we use the commented methods above 

# #squaring a list

# mylist = [1,2,3,4,5]
# sqlist = [i*i for i in mylist]
# print(mylist)
# print(sqlist)
