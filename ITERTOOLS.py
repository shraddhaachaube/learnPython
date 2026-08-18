# #comment out to run a particular block of code
# #itertools --> used to handle iterators --> product, permutations, combinations, accumulate, groupby, and infinite iterators


# #PRODUCT
# from itertools import product
# a = [1,2]
# b = [3,4]
# prod = product(a,b) #returns the cartesian product
# print(list(prod))
# c = [3]
# print(list(product(a,c, repeat=2)))


# #PERMUTATIONS
# from itertools import permutations
# #returns all the possible orderings 
# d = [1,2,3]
# perm = permutations(d)
# print(list(perm))
# print(list(permutations(d,2)))


# #COMBINATIONS
# from itertools import combinations, combinations_with_replacement
# e = [1,2,3,4]
# comb = combinations(e,2) #returns all possible combinations with specified length
# print(list(comb))
# comb_wr = combinations_with_replacement(e,2) #returns all possible combinations with specified length with repetition allowed
# print(list(comb_wr))


# #ACCUMULATE
# from itertools import accumulate
# import operator
# g = [1,2,5,3,4]
# acc1 = accumulate(g) #computes the sum by default
# print(g)
# print(list(acc1))
# acc2 = accumulate(g, func=operator.mul) #multiplies each element
# print(list(acc2))
# acc3 = accumulate(g, func=max)# returns the maximum
# print(list(acc3))

# #taking input from the user and calculating sum of two numbers without using +, - operators
# f = list()
# f.append(float(input("Enter the 1st number : ")))
# f.append(float(input("Enter the 2nd number : ")))
# acc = accumulate(f)
# sum = list(acc)
# print("The sum of the given two numbers is : ", sum[-1])


# #GROUPBY
# from itertools import groupby
# #groups by key
# def smaller_than_3(x):
#     return x<3

# g = [1,2,3,4]
# group_obj = groupby(g, key= smaller_than_3)
# for key, value in group_obj:
#     print(key, list(value))
# #by lambda function
# group_obj1 = groupby(g, key= lambda x: x>3)
# for key, value in group_obj1:
#     print(key, list(value))

# persons = [{'name': 'Sam', 'age': 18},{'name': 'Ram', 'age': 19},{'name': 'Sid', 'age': 19},{'name': 'Dia', 'age': 20} ]
# group_obj2 = groupby(persons, key= lambda x: x['age'])
# for key, value in group_obj2:
#     print(key, list(value))


# #INFINITE ITERATORS
# from itertools import count, cycle, repeat
# #loops infinitely until any break condition is given
# for i in count(10):
#     print(i)
#     if i == 15:
#         break

# h = [1,2,3]
# # for i in cycle(h):
# #     print(i) #this will print the h in a cycle infinitely

# for i in repeat(h,7):
#     print(i)

