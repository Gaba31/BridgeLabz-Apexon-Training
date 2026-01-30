"""
Power of 2
a. Desc -> Prints powers of 2 less than or equal to 2^N
b. I/P  -> Integer N such that 0 <= N < 31
c. Logic -> Compute 2^i for i from 0 to N
d. O/P  -> Prints powers of 2
"""

def power_of_2(n):
    if not 0 <= n < 31:
        raise ValueError("Value of n should be between 0 and 31 (31 exclusive)")
    return [2 ** i for i in range(n + 1)]
    
def main():
    try:
        n = int(input("Please enter value of n: "))
        powers = power_of_2(n)
        for value in powers:
            print(value)
    except ValueError as e:
        print("Error ->", e)

if __name__ == "__main__":
    main()
