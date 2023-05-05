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