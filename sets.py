# #comment out to run a particular block of code
# #sets --> unordered, mutable, no duplicates

# set1 = {1,2,3}
# print(set1)

# #if there are duplicate elements they will be considered as one single element

# set2 = set("Hello")
# print(set2)

# #to create an empty set

# set3 = set()
# print(type(set3))

# set3.add(9)
# set3.add(7)
# set3.add(5)
# set3.add(3)
# set3.add(1)
# set3.add(11)
# print(set3)

# set3.remove(1)
# print(set3)
# set3.discard(5)
# print(set3)
# set3.pop() #removes 1st element
# print(set3)
# set3.clear()
# print(set3)

# #accessing elements using for loop

# set4 = {3,5,8,10,78}
# for i in set4:
#     print(i)

# #to check whether the element is present in the set or not

# set5 = {2,4,5,6,7,8}
# if 3 in set5:
#     print("Yes")
# else:
#     print("No")

# #intersection and union

# odds = {1,3,5,7,9}
# evens = {0,2,4,6,8}
# primes = {2,3,5,7}

# u = odds.union(evens)
# print(u)

# i = odds.intersection(primes)
# print(i)
# j = evens.intersection(primes)
# print(j)

# #difference 

# setA = {1,2,3,4,5,6,7,8,9}
# setB = {1,2,3,11,12,16}
# print(setA.difference(setB))
# print(setB.difference(setA))

# #symmetric difference

# print(setA.symmetric_difference(setB))

# #updating sets

# setA.update(setB)
# print(setA)

# #intersection update

# setB.intersection_update(setA)
# print(setB)

# #difference update

# setA.difference_update(setB)
# print(setA)

# #symmetric differnce update

# setA.symmetric_difference_update(setB)
# print(setA)

# #issubset
# seta = {1,2,3,4,5,6}
# setb = {1,2,3}
# print(seta.issubset(setb))
# print(setb.issubset(seta))

# #issuperset
# seta1 = {1,2,3,4,5,6}
# setb1 = {1,2,3}
# print(seta1.issuperset(setb1))
# print(setb1.issuperset(seta1))

# #isdisjoint
# seta2 = {1,2,3,4,5,6}
# setb2 = {7,8,9}
# print(seta2.isdisjoint(setb2))

# #copying set
# seta3 = {1,2,3,4,5,6}
# setb3 = seta3.copy() #or setb3 = set(seta3) --- setb3 = seta3 --> by this assignment if we alter setb3, then seta3 will be automatically altered
# setb3.add(7)  
# print(seta3)
# print(setb3)

# #frozenset --> a frozenset cannot be altered, but union, intersection and difference method works
# a = frozenset([1,3,5,6,8])
# print(a)