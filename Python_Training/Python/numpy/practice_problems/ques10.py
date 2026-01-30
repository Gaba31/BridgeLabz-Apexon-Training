# 1. Stack two arrays vertically.
# 2. Stack two arrays horizontally.
# 3. Split an array into 3 equal parts.
# 4. Split a 2D array row-wise into 2 parts.

import numpy as np

def main():
    arr1 = np.arange(25).reshape(5,5)
    arr2 = np.arange(25,50).reshape(5,5)
    # 1. Stack two arrays vertically.
    # arr3 = np.hstack((arr1,arr2))
    # print(arr3)
    # 2. Stack two arrays horizontally.
    arr3 = np.vstack((arr1,arr2))
    # print(arr3)
    # 3. Split an array into 3 equal parts.
    arr4 = np.vsplit(arr3,2)
    print(arr4)


if __name__ == "__main__":
    main()