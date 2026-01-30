# 1. Add a 1D array `[1,2,3]` to each row of a 2D matrix.
# 2. Normalize each row of a matrix (row sum = 1).
# 3. Standardize an array (mean=0, std=1) without loops.
# 4. Compute Euclidean distance between two vectors.




import numpy as np

def main():
    matrix = np.array(
        [[10,20,30],
        [11,22,33],
        [51,52,53]]
    )

    arr = np.array([1,2,3])

    matrix = matrix + arr
    print(matrix)

    #Normalize each row of a matrix (row sum = 1).

    row_sum = matrix.sum(axis=1)
    matrix = matrix/row_sum
    print(matrix)






if __name__ == "__main__":
    main()