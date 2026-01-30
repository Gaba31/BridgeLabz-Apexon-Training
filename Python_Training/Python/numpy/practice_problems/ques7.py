# 2. From a 2D array, extract:
#     - first row
#     - last column
#     - a 2×2 submatrix
#     - Now flaten this 2-D array to 1-D array
#      - Now make this vector into column vector


import numpy as np

def main():

    np_arr = np.arange(25).reshape(5,5)
    print("This is a 2D array")
    print(np_arr)
    print("Extacting first row")
    print(np_arr[0])
    print("Extracting last column")
    print(np_arr[:,4:])
    print("Extracting sub martrix")
    print(np_arr[0:2,0:2])
    print("Flatening this 2D array")
    np_arr = np_arr.ravel()
    print(np_arr.ravel())
    print("Converting into a column vector")
    np_arr = np_arr.reshape(-1,1)
    print(np_arr)
    # reshape(-1,1)-> for col vector
    # reshape(1,-1) -> for row vector




if __name__ == "__main__":
    main()