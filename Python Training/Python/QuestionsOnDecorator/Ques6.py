# 🎯 Requirements
# The decorator should:

# Accept a number n

# Log the function name using __name__

# Print when the function starts and ends

# Repeat the function call n times

# Preserve function metadata (__name__, __doc__)

# Work with any arguments (*args, **kwargs)

# 🧪 Expected behavior
# Code usage:
# @repeat_and_log(3)
# def greet(name):
#     """Greets a user"""
#     print(f"Hello {name}")

# Calling:
# greet("Brijesh")

# Expected output:
# Starting function: greet
# Hello Brijesh
# Hello Brijesh
# Hello Brijesh
# Ending function: greet


# And:

# print(greet.__name__)  # greet
# print(greet.__doc__)   # Greets a user


from functools import wraps

def repeat_and_log(n):
    def decorator_function(func):
        
        @wraps(func)
        def inner(*args,**kwargs):
            print(f"Function Started :{func.__name__}")
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            print(f"Function Ended :{func.__name__}")
            return result
            
        return inner
    return decorator_function
            


@repeat_and_log(3)
def greet(name):
    """Greets a user"""
    print(f"Hello {name}")


print(greet("Brijesh"))    
    