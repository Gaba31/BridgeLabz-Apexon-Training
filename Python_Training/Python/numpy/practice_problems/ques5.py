# 5. Write a Python program to create a 2d array with 1 on the border and 0 inside.
# Expected Output:
# Original array:
# [[ 1. 1. 1. 1. 1.]
# [ 1. 1. 1. 1. 1.]
# [ 1. 1. 1. 1. 1.]
# [ 1. 1. 1. 1. 1.]
# [ 1. 1. 1. 1. 1.]]
import numpy as np

def convert_matrix(np_matrix):
    if np_matrix.ndim != 2:
        raise ValueError("Only 2-D arrays are supported")

    if np_matrix.shape[0] > 2 and np_matrix.shape[1] > 2:
        np_matrix[1:-1, 1:-1] = 0

    return np_matrix



def main():
    rows = int(input("Enter the number of rows"))
    col = int(input("Enter the number of col"))
    np_matrix = np.ones((rows,col))
    print(np_matrix)
    convert_matrix(np_matrix,rows,col)



if __name__ == "__main__":
    main()