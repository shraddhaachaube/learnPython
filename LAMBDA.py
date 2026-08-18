# #comment out to run a particular block of code
# #LAMBDA FUNCTION --> syntax-- lambda arguments: expression

# add10 = lambda x: x+10 #will work same as def add10(x): return x+10
# print(add10(7))

# mult = lambda x,y: x*y #with two arguments
# print(mult(3,7))

# #sorted using lambda as key argument 
# points = [(1,2),(10,4),(5,-1),(15,1)]
# sort_by_x = sorted(points)
# print(sort_by_x)
# sort_by_y = sorted(points, key= lambda x: x[1])
# print(sort_by_y)
# sort_by_sum = sorted(points, key= lambda x: x[0] + x[1])
# print(sort_by_sum)

# #map function using lambda
# #syntax--> map(func, seq)
# a = [1,2,3,4,5]
# b = map(lambda x: x*2, a) #multiplies each element by 2
# print(b)
# print(list(b))
# #achieving same by list comprehension
# c = [x*2 for x in a]
# print(c)

# #filter function using lambda
# #syntax--> filter(boolean_func, seq)
# d = [1,2,3,4,5,6,7]
# e = filter(lambda x: x%2==0, d)
# print(e)
# print(list(e))
# #achieving same by list comprehension
# f = [x for x in d if x%2==0]
# print(f)

# #reduce function using lambda
# #syntax--> reduce(func, seq)
# from functools import reduce
# g = [1,2,3,4]
# prod_g = reduce(lambda x,y: x*y, g)
# print(prod_g)
