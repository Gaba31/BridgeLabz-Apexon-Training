# Write a decorator that adds "Welcome " before the function’s return value

from functools import wraps

def decfunction(func):
    @wraps(func)
    #or
    #@functools.wraps(func)
    def inner(*args,**kwargs):
        return "Welcome " + func(*args,**kwargs)
    return inner
   
@decfunction 
def myfunc(name):
    return name

#Internally 
# myfunc = decfunction(func)

print(myfunc("Brijesh"))