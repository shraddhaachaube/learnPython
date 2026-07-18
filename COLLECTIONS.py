# #comment out to run a particular block of code
# #collections --> Counter, namedtuple, orderedDict, defaultdict, deque

# from collections import Counter
# #
# a = "aaaabbbcc"
# my_counter = Counter(a)
# print(my_counter)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())

# print(my_counter.most_common(1))
# print(my_counter.most_common(1)[0])
# print(my_counter.most_common(1)[0][0])

# print(my_counter.elements())
# print(list(my_counter.elements()))

# from collections import namedtuple
# #
# Point = namedtuple('Point','x,y')
# pt = Point(3,9)
# print(pt)
# print(pt.x,pt.y)

# from collections import OrderedDict
# #used to create a dictionary that remembers the order in which the elements were inserted, but in this version of python a normal dictionary is also ordered
# ordered_dict = OrderedDict()
# ordered_dict['b'] = 2
# ordered_dict['c'] = 3
# ordered_dict['d'] = 4
# ordered_dict['a'] = 1
# print(ordered_dict)

# from collections import defaultdict
# #this creates a dictionary that returns a default value if the key is not present/defined, but in normal dictionary it will generate a key error
# d = defaultdict(float)
# d['A'] = 1
# d['B'] = 2
# print(d)
# print(d['A'])
# print(d['B'])
# print(d['C'])

# from collections import deque
# #a doble ended queue
# dq = deque()
# dq.append(1)
# dq.append(2)
# print(dq)

# dq.appendleft(3)
# print(dq)

# dq.extend([4,5,6])
# print(dq)

# dq.extendleft([7,8,9])
# print(dq)

# dq.pop()
# print(dq)

# dq.popleft()
# print(dq)

# dq.rotate(1)
# print(dq)

# dq.rotate(2)
# print(dq)

# dq.rotate(-1)
# print(dq)

# dq.clear()
# print (dq)

