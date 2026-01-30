#### Debugging During Development With assert ####
# Python offers a specific exception type that you should only use when debugging your program during
# development. This exception is the AssertionError. The AssertionError is special because you
# shouldn’t ever raise it yourself using raise. Instead, you use the assert keyword to check whether
# a condition is met and let Python raise the AssertionError if the condition isn’t met.
# In Production
number = 15
if number > 10:
    raise Exception(f"The number should not exceed 10. ({number=})")
print(number)
# In development for debuging
number = 15
assert (number < 10), f"The number should not exceed 10. ({number=})"
print(number)

"""
    Best Practices:
        1. Catch specific exceptions instead of generic Exception class to differentiate errors
        2. Print custom error messages from except blocks upon failures
        3. Use finally clause to execute sections of cleanup code reliably
        4. Define custom exception classes to match application scenarios
        5. Use try-except blocks only where needed.
            Don’t wrap your entire code in a massive try-except block; limit it to potential 
            error-prone sections.
            Don’t overuse try-except blocks in business logic to avoid hiding real issues
        6. Avoid using except: without specifying the exception type, as it can catch unintended errors.
        7. Use logging to record exceptions for later analysis.
"""

"""
    Advantage: Improved program reliability, Cleaner Code, Simplified error handling, easier debugging
    Disadvantage: Performance Overhead, Increased Code Complexity, Possible Security risks
Overall, the benefits of exception handling in Python outweigh the drawbacks, but it’s important to 
use it judiciously and carefully in order to maintain code quality and program reliability.
"""