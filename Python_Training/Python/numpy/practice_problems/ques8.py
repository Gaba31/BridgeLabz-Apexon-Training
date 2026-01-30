# 1. Given an array, extract all **even numbers**.
# 2. Replace all values greater than 50 with `0`.
# 3. Count how many elements are > 25.
# 4. Find indices where values are divisible by 3.

import numpy as np

def main():
    arr = np.array([1,4,32,4,4,564,2,21,34,345,22,50,50,50])
    # print("Extract all even numbers")
    # print(np.unique(arr[arr%2==0]))
    print("Replacing all the values with 50 with 0")
    print(np.where(arr==50,0,arr))
    print("Count how many elements are > 25.")
    print(len(arr[arr>25]))
    print("indices where values are divisible by 3.")
    print(np.where(arr%3==0))


if __name__ == "__main__":
    main()