# Create an array from 1 to 12 and reshape it into 3×4.
import numpy as np

def main():
    n = int(input("Enter the number of values u want to store in list"))
    user_input = []
    for i in range(n):
        user_input.append(i)

    np_arr = np.array(user_input).reshape(3,4)
    print(np_arr)



if __name__ == "__main__":
    main()