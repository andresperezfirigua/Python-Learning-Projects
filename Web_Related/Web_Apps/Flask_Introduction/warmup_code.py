import time


def decorator_funct(function):
    def wrapper(name):
        time.sleep(3)
        function(name)
    return wrapper

time.ctime()

@decorator_funct
def hello(name):
    print(f'Hi {name}')


hello('andres')
