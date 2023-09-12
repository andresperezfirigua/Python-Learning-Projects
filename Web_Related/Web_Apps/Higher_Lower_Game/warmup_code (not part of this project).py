# from flask import Flask
#
# app = Flask(__name__)
#
#
# def make_bold(function):
#     def wrapper():
#         return f'<b>{function()}</b>'
#     return wrapper
#
#
# def make_emphasis(function):
#     def wrapper():
#         return f'<em>{function()}</em>'
#     return wrapper
#
#
# def make_underlined(function):
#     def wrapper():
#         return f'<u>{function()}</u>'
#     return wrapper
#
# @app.route("/")
# def hello_world():
#     return "<h1>Hello, World!</h1>"
#
#
# @app.route('/bye')
# @make_bold
# @make_emphasis
# @make_underlined
# def bye():
#     return "<h2>See you soon!</h2>"
#
#
# @app.route('/username/<name>/<int:number>')
# def greet(name, number):
#     return f'<h2>Hello {name}, you are {number} years old</h2>'
#
#
# @app.route('/user/<username>')
# def welcome(username):
#     return f'<h2 style="text-align: center">Welcome {username}'
#
#
# if __name__ == '__main__':
#     # Running the app in debug mode to auto-reload
#     app.run(debug=True)



############## Example

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
#
# def is_autheticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in:
#             function(args[0])
#     return wrapper
#
# @is_autheticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")
#
#
# new_user = User('Andres')
# new_user.is_logged_in = True
# create_blog_post(new_user)

#
# #Decorators to add a tag around text on web page.
# def make_bold(function):
#     def wrapper():
#         return "<b>" + function() + "</b>"
#     return wrapper
#
# def make_emphasis(function):
#     def wrapper():
#         return "<em>" + function() + "</em>"
#     return wrapper
#
# def make_underlined(function):
#     def wrapper():
#         return "<u>" + function() + "</u>"
#     return wrapper
#
# @app.route('/')
# def hello_world():
#     #Rendering HTML Elements
#     return '<h1 style="text-align: center">Hello, World!</h1>' \
#            '<p>This is a paragraph.</p>' \
#            '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=200>'
#
#
# #Different routes using the app.route decorator
# @app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underlined
# def bye():
#     return "Bye!"
#
#
# #Creating variable paths and converting the path to a specified data type
# @app.route("/username/<name>/<int:number>")
# def greet(name, number):
#     return f"Hello there {name}, you are {number} years old!"
#
#
# if _name_ == "_main_":
#     #Run the app in debug mode to auto-reload
#     app.run(debug=True)


######### Exercise ######

# Create the logging_decorator() function 👇

# def logging_decorator(function):
#     def wrapper(*args, **kwargs):
#         print(f'You called {function.__name__}{args}')
#         print(f'It returned {function(args[0], args[1], args[2])}')
#     return wrapper
#
#
# # Use the decorator 👇
# @logging_decorator
# def a_function(a, b, c):
#     return a + b + c
#
# a_function(1, 2, 3)
