#Write a decorator that prints "Function called" before executing a function.

def decfunction(func):
    def inner(*args,**kwargs):
        print("Function Called")
        return func(*args,**kwargs)
    return inner
    
@decfunction
def anyfunc():
    print("Inside Function")
    return "done"

#anyfunc()

print(anyfunc())