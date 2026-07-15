# class Student:
#     def __init__(self):
#         self._name = "Yash"

#     def show(self):
#         print(self._name)

# obj = Student()
# obj.show()
# print(obj._name) # can be used but it's not recommended 


# Private 

# class Student:
#     def __init__(self):
#         self.__name = "Yash"  #Private variable - Double underscore

#     def show(self):
#         print(self.__name)

# obj = Student()
# obj.show()
# print(obj.__name)


# Getter 

# class Student:
#     def __init__(self):
#         self.__name = "Vineet"

#     def get_mark(self): #getter
#         return self.__name
    
# obj = Student()
# print(obj.get_mark())

# class Student:
#     def __init__(self):
#         self.__marks = 0
