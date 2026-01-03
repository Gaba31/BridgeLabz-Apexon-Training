#Write a decorator that accepts a number n and repeats the function n times.

from functools import wraps

def num(n):
    def decfunction(func):
        @wraps(func)
        def inner(*args,**kwargs):
            return func(*args,**kwargs) * n
        return inner
    return decfunction
    
@num(3)
def myfunc(name):
    return name
    

print(myfunc("Brijesh"))
        
        