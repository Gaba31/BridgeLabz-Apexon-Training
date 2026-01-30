# Every numpy array is a object of numpy class
# So every numpy object can access some numpy class atributes

# Demo Arrays
import numpy as np

a1 = np.arange(1,10,dtype=np.int32)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

#############################################################

# Array Attributes
# ndim -> Tells the dimension of an array

# print(a1.ndim) #1
# print(a2.ndim) #2
# print(a3.ndim) #3

# shape -> Will tell us how many items exists in each dimension

# print(a1.shape)  #(9,)
# print(a2.shape)  #(3, 4)
# print(a3.shape)  #(2, 2, 2)

# What this (2,2,2) tells us first 2 -> How many 2-D arrays are there in this
# second 2 tells no. of rows of each array and third 2 tells the no. of col of each array

# size -> Will tells us how many items are there in array
# For Eg

# print(a3.size) #8


# itemsize -> Will tell us the size of each item in an array
# bydefault int in 64bits and float is of 64bits in python
# but we can use 32 bit int in python as well

# print(a1.itemsize)  # 4,8byte depending on which int type we are using


# dtype -> Tells us the data type of item present in an array

# print(a1.dtype)
# print(a2.dtype)


# Changing datatype

# astype is used for changing data type of an array
# astype return a new array itself it does not change inplace

# print(a3.dtype)
a3 = a3.astype(np.int32)
# print(a3.dtype)


########################################################################

# Array Operations

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)


# We can do scaler operations
# scaler operation means ek single numpy array ke upper ekk single number(scaler) se operate krte hoo

# arithmetic -> +,-,**,*,/,// etc We can use any of these operators

# print(a1*2)  # each number will multiply with 2

# relational -> >,<,>=,<=,==,!= etc

# print(a2>15) # Compares each value with 15 and return's result in boolean format

# Vector operations -> When we basically do operations on two numpy array

# print(a1+a2)  # Addition is possible because they both are of same size .

##########################################################################

# Array Functions

#For Eg:
a1 = np.random.random((3,3))
a1 = np.round(a1*100)
# print(a1)


# max , min , sum , prod

# print(np.max(a1))
# print(np.min(a1))
# print(np.sum(a1))

# How to find out maximum in each row
# Set axis = 1 for row and 0 for column
# print(np.max(a1,axis=1)) #This will return a list of max numbers in each row

#mean,median,std,var (Statics methods)
# We can use axis with also same as above


#Trignometric function  (We will never use these functions)
# sin,cos,tan

# dot product (Very Useful)
# When there are two matrix
# First maxtix col should be equal to second matrix row then only dot product can happen
# And the result will be first matrix row X second matrix column

m1 = np.arange(6).reshape(2,3)
m2 = np.arange(6).reshape(3,2)

m3 = np.dot(m1,m2)
# print(m3)

# log and exponent function
# For Eg: np.log() , np.exp()

# round(),ceil(),floor()
# round() will round off the value
# ceil() will go to the upper limit of the value
# floor() will go to the lower limit of the value

#####################################################################

# Indexing and Slicing
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

# print(a1) #[0 1 2 3 4 5 6 7 8 9]

# How to find out last element in upper array
# Same pythonic way

# print(a1[-1]) #9

# print(a2)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

#How to find out certain position in 2-D array

# print(a2[1,3])  #7


# How to print centain value in 3-D array
# print(a3)
# [[[0 1]
#   [2 3]]
#
#  [[4 5]
#   [6 7]]]


# print(a3[1,0,1]) # a3[which 2-D array 1st or 2nd, row_of_that_selected_matrix, col_of_that_selected_matrix]

# Same things apply on 4D and so on

# Slicing (Same as python)
# print(a1[2:5:2])

# Slicing become instresting for 2-D and above matrix

# print(a2)

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Print the first row of the matrix

# print(a2[0,:])  #[0 1 2 3]

# Print 3rd column only

# print(a2[:,2])  #[ 2  6 10]

# Jb bhi aapko particular row chaiye tbh aapko saree col chaiye
# Jb bhi aapko particualar col chaiye tbh aapko saare row chaiye

# Now i want [[5,6],[9,10]]

# print(a2[1:,1:3])
# Output ->
#[[ 5  6]
 # [ 9 10]]


# Now i want 0 , 3, 8, 11 from the matrix

# print(a2[::2,::3])
# we need all rows that why : :  and 2 will used for jump same for col


# Now i want 1,3,9,11 from the matrix .
# print(a2[::2,1::2])
# Output ->
# [[ 1  3]
#  [ 9 11]]

# Now i need only 4 and 7 .
# print(a2[1:2,0::3])  #[[4 7]]

# Now i need 1,2,3,5,6,7

# print(a2[0:2,1::])
# [[1 2 3]
#  [5 6 7]]

## Now we will work on 3D array

a3 = np.arange(27).reshape(3,3,3)
# print(a3)
# [[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]]
#
#  [[ 9 10 11]
#   [12 13 14]
#   [15 16 17]]
#
#  [[18 19 20]
#   [21 22 23]
#   [24 25 26]]]

# Now have to print the 2nd row of first array

# print(a3[0,1,])  #[[3 4 5]]

# Now have to print the middle column of the second matrix

# print(a3[1,:,1:2])
# Output ->
# [[10]
#  [13]
#  [16]]


# Now have to print 22,23,25,26

# print(a3[2,1:,1:])
# Output ->
# [[22 23]
#  [25 26]]

#Now have to print 0,2,18,20

# print(a3[::2,0,0::2])
# Output ->
# [[ 0  2]
#  [18 20]]

################################################################

#Iteration

# Iterate over 1-D array

# for i in a1:
#     print(i)
#
# # Iterate over 2-D array
#
# for i in a2:
#     print(i) #It will print each row of the matrix
#
# # Iterate over 3-D array
# for i in a3:
#     print(i) #It will print each array in the matrix


# How to convert any Dimension Array to 1-D array and print it
# Use nditer() function it will convert any Dimensional array to 1 D array

for i in np.nditer(a3):
    print(i)


########################################################

# Reshaping
# reshape -> We already covered

# Transpose -> Row ko col aur col ko row me convert krr deta hh

a4 = np.transpose(a2)
#or
a4 = a2.T
# print(a4)


# ravel -> convert n-D array to 1-d array

print(a2.ravel())

################################################################

# Agar result dikh jae python mee toh samjah lena vo ek temporary operation h
# Aur agar result na dikhe toh samjh lena vo ek peramenent operation hh

#####################################################################

# Stacking  -> Arrays ko jodna
#For Eg
a4 = np.arange(12).reshape(3,4)
a5 = np.arange(12,24).reshape(3,4)

#hstack
a6 = np.hstack((a4,a5)) #Can give any number of matrix in tuple format
# It will join it vertically

print(a6)


#vstack -> This will join array horizonataly


###########################################################

# Spliting -> It is just the opposite of stacking

#hsplit -> vertically kattega
#vsplit -> horizontally katte ga

print(np.hsplit(a6,2)) #2 is for kitnee hisse mee kaatna hh

######################################################

class Demo:
    pass

d = Demo()

a7 = np.array([1,2,3,6.00,d])
print(type(a7[-1]))
print(a7)





