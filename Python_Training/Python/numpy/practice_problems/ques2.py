# 2. Create a 3x3 matrix with values ranging from 2 to 10.
# Expected Output:
# [[ 2 3 4]
# [ 5 6 7]
# [ 8 9 10]]

import numpy as np

def create_matrix():
    np_arr = np.arange(2, 11).reshape(3, 3)
    print(np_arr)


def main():
    print("Here is the 3 X 3 matrix which has values ranging from 2 to 10")
    create_matrix()


if __name__  == "__main__":
    main()