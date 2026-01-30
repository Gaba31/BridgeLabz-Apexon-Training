# Count frequency of each element in an array.

import numpy as np

def main():
    arr = np.array([3,3,5,5,5,4,4,4])
    unique_elements , counts = np.unique(arr,return_counts=True)
    print(unique_elements)
    print(counts)


if __name__ == "__main__":
    main()