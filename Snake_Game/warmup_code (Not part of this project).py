# Inheritance

#Example 1
# Parent class

# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, exhale.")
#
# # Inheriting from Animal class

# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#
#     # Modifying or extending the functionality of a parent class method
#     def breathe(self):
#         super().breathe()
#         print("Doing this underwater.")
#     def swim(self):
#         print("Moving in water.")
#
# nemo = Fish()
# nemo.swim()
# nemo.breathe()

# Example 2

# class Dog:
#     def __init__(self):
#         self.temperament = "loyal"
#
#     def bark(self):
#         print("Woof, woof!")
#
#
# class Labrador(Dog):
#     def __init__(self):
#         # As shown here, it's not mandatory to use the super() word to initialize the parent constructor
#         self.temperament = "Friendly"
#
#
# tom = Labrador()
# print(tom.temperament)
# tom.bark()

# List and tuples slicing

# # Define a list
# my_list = [1, 2, 3, 4, 5]
#
# # Get the first three elements of the list
# first_three = my_list[:3]
# print(first_three)  # Output: [1, 2, 3]
#
# # Get the last two elements of the list
# last_two = my_list[-2:]
# print(last_two)  # Output: [4, 5]
#
# # Get the middle two elements of the list
# middle_two = my_list[1:3]
# print(middle_two)  # Output: [2, 3]
#
# # Get every other element of the list
# every_other = my_list[::2]
# print(every_other)  # Output: [1, 3, 5]
#
# # Reverse the list
# reverse_list = my_list[::-1]
# print(reverse_list)  # Output: [5, 4, 3, 2, 1]
