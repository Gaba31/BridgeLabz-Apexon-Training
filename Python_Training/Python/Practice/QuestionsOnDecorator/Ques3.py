# Write a decorator that:
#takes a function returning a number
# multiplies the result by 10


from functools import wraps

def decfunction(func):
    @wraps(func)
    def inner(*args,**kwargs):
        return func(*args,**kwargs) * 10
    return inner
    
@decfunction
def myfunc(num):
    return num
   
print(myfunc(10))     
    