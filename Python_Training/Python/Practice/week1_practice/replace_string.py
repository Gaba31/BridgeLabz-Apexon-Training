"""
        User Input and Replace String Template “Hello <<UserName>>, How are you?”
        a. I/P -> Take User Name as Input. Ensure UserName has min 3 char
        b. Logic -> Replace <<UserName>> with the proper name
        c. O/P -> Print the String with User Name
"""


def main():
    name = input("Enter User Name : ")
    if len(name)>=3:
        print(f"\"Hello <<{name}>> , How are you?\"")
    else:
        raise Exception("Please Enter atleast three characters")


if __name__ == "__main__":
    main()