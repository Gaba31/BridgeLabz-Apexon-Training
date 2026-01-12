# """
# 🧩 Problem Statement
# Extract currency amounts from the following text.
# Rules
# A valid currency amount:
# Starts with $
# Can have commas as thousand separators
# Can have optional decimals (2 digits)
# """
#
# text = ""The product costs $1,200.50 and the discounted price is $999.""
#


# HOF
import functools
L = [1,2,3,4,5,6,7,8,9]

print(functools.reduce(lambda x,y : x + y , L))