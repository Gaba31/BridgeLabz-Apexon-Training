# 1. Write a Python program to convert a list of numeric value into a one-dimensional
# NumPy array.
# Expected Output:
# Original List: [12.23, 13.32, 100, 36.32]
# One-dimensional numpy array: [ 12.23 13.32 100. 36.32]
import numpy as np

def main():
    n = int(input("Enter the value of n : "))
    user_input = []
    for i in range(n):
        user_input.append(input(f"Enter the {i}th value : "))

    numpy_array = np.array(user_input,dtype=float)
    print(numpy_array)
    print(type(numpy_array))




if __name__ == "__main__":
    main()