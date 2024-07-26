#Decorator - a function which takes another function as arg and returns a new function
def my_decorator(func):
    def wrapper():
        print("Starting.........")
        print("****************")
        func()
        print("Ending...........")
        print("****************")
    return wrapper()

@my_decorator
def say_hello():
    print("Say Hello")
