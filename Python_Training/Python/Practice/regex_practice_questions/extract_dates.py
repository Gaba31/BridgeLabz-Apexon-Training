"""
✅ Task
Extract all valid dates from text in two formats:
dd-mm-yyyy
dd/mm/yyyy
Where:
dd → 01 to 31
mm → 01 to 12
yyyy → 4 digits


"""



text = """
My birthday is 12-08-1995 and my sister's is 23/11/2000.
Some invalid dates: 32-01-2020, 15/13/2019, or 00-00-0000 should not match.
"""

"""
    Output
        12-08-1995
        23/11/2000
"""

import re

text = "Important dates are 01-12-2023, 31/01/2020 and 15 08 1999."

pattern = r"\b(?:0[1-9]|[12][0-9]|3[01])[- /](?:0[1-9]|1[0-2])[- /][1-9]\d{3}\b"

dates = re.findall(pattern, text)
print(dates)


