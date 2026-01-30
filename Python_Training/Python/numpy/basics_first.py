import numpy as np  #Importing numpy

# Creating 1-D Array

arr = np.array([1,2,3])    #For creating array in numpy we have to pass list in .array() function
print(arr)         #[1 2 3]   # We call this as vector
print(type(arr))   #<class 'numpy.ndarray'>


# Creating 2-D Array or matrix

arr = np.array([[1,2,3],[4,5,6],[7,8,9]]) #This creates a 2-D array or matrix
# print(arr)
# print(type(arr))


# Creating 3-D Array or Tensor

# arr = np.array([[[1,2,3],[4,5,6]]])
# print(arr)

# We can create n-D type of arrays in python

# How to make an array of specific type
# For that we use dtype parameter

arr = np.array([1,2,3,4,5],dtype=float)
print(arr)
arr = np.array([1,2,3,4,0],dtype=bool)
print(arr)

# For creating an array with just range we use arange() function
# For Eg: np.arange()
# Same as range() function

# arr = np.arange(1,11,2)
# print(arr)

# .reshape() function is used to shape the array
# It is majorly used with .arange() fucntion

# arr = np.arange(1,11).reshape(2,5) #rows = 2 , col = 5
# print(arr)  #with reshape it will create a 2D array
# arr = np.arange(1,13).reshape(5,5)
# print(arr)
# This is not possible because how 12 items can exist
# in 5*5 matrix

#############################################################

#np.ones() and np.zeros() -> They both are used to initialize array with 1 or 0
# They take tuple as an argument

arr = np.ones((3,3))  # rows = 3 , col = 3
# print(arr)
arr = np.zeros((5,5))
# print(arr)


# np.random.random() -> This will initilize array with random numbers . This will take tuple as an argument
# random numbers between 0 and 1
brr = np.random.random((3,4))
# print(brr)
# Why we are writting two randoms? Because random itself is a class and in that class we have random function

################################################################

#np.linspace(lower_range,upper_range,no.of items to generate)
# This will generate numbers at equal distance that why the name is linear space

crr = np.linspace(-10,10,10)
# print(crr)
# The distance bw -10 and -5.55555556 is same as the distance  bw 7.77 and 10.

################################################################

# np.identity() -> We can generate identity matrix using identity function
# What is a identity matrix -> Jiske diagonal items 1 hoo and rest of the items are zero

drr = np.identity(3) # This will create 3*3 matrix
print(drr)

#################################################################

# Default value of every array is float but we can change it using dtype

#################################################################





