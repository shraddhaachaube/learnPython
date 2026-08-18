# #comment out to run a particular block of code
# #ERRORS AND EXCEPTIONS

# #Raising an exception
# x = -5
# if x<0:
#     raise Exception ('x should be positive')

# #AssertionError
# y = -3
# assert(y>=0), 'y is not positive'

# #EXCEPTION HANDLING
# try:
#     a = 3/0
# except Exception as e:
#     print(e)

# #catching multiple errors
# try:
#     b = 5/1
#     c = b + '7' #type error
# except Exception as e:
#     print(e)
# else:
#     print("Everything is fine")
# finally:
#     print("Cleaning up..")

# #DEFINING EXCEPTION
# class ValueTooHighError(Exception):
#     pass

# class ValueTooSmallError(Exception):
#     def __init__(self, message, value):
#         self.message = message
#         self.value = value

# def test_value(x):
#     if x>100:
#         raise ValueTooHighError("Value is too high")
#     if x<5:
#         raise ValueTooSmallError("Value is too small -->", x)


# try:
#     test_value(200)
# except ValueTooHighError as e:
#     print(e)
# except ValueTooSmallError as e:
#     print(e.message, e.value)
