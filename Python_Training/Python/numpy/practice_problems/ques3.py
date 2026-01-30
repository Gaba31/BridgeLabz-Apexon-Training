# 3. Write a Python program to create a null vector of size 10 and update sixth value to 11.
# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# Update sixth value to 11
# [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
import numpy as np

def create_null_vector():
    np_arr = np.zeros(10)
    print(np_arr)
    np_arr[5] = 11
    print(np_arr)

def main():
    print("Creating null vector of size 10")
    create_null_vector()



if __name__ == "__main__":
    main()