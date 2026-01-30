# All Exceptions list (Official Documentation) -> https://docs.python.org/3/library/exceptions.html

# Exception Handling -> try,except,else,finally
#Types of Errors:
# 1. Logical Error
# 2.Syntax Error
# 3. Run Time Error


# #### Program without exception handling ####
# numerator = int(input("Please enter the numerator for division: "))
# denominator = int(input("Please enter the denominator for division: "))
# division = numerator/denominator
# print("The result is", division)
# print("Division is successful...")
#
# print("The line of code is doing some sensitive calculation. So must execute...")



# Eg Making any exception handling for divisible by 0

try:  # Whatever the code can give issue put that code in try block
    num = int(input("Enter num"))
    den = int(input("Enter den"))
    output = num//den
    print(f"Result -> {output}")
except ZeroDivisionError as e:      #There can be multiple exceptions
    print("Denominator can't be zero",e)
except ValueError as e:
    print("Value must be integer",e)
except Exception as e:      # We should always have generic exception other than specific exception
    print("Some Error Occured",e)
else:           # Else block will run only when there would be no exception
    print("Division Successfully")
finally: # This will run no matter what
    print("Close the resourse")


# But why there is a need of finally ?
# Let say we are opening a file and it crashes and get into exception block so the file is open
# it should be closed so that code of closing a file will be written in finally block.
# You can take the eg of database connection same as upper example

print("The line is doing some sensitive task so must execute")

