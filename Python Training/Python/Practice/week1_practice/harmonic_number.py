"""
Harmonic Number
a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
(http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).
b. I/P -> The Harmonic Value N. Ensure N != 0
c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
d. O/P -> Print the Nth Harmonic Value.
"""


def nth_harmonic_number(n):
    if n==1:
        return 1.0
    elif n<=0:
        raise ValueError("Enter a number greater than 0")


    nth_value =  1/n + nth_harmonic_number(n-1)
    return nth_value


def main():
   try:
        n = int(input("Enter the value of n : "))
        print(nth_harmonic_number(n))
   except ValueError as e:
       print("Error -> ",e)


if __name__ == "__main__":
    main()