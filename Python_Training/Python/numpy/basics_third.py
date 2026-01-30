#Numpy vs Python list

# Comparision on speed

# Taking two list containing crore items each and adding those into 3rd list

a = [x for x in range(10000000)]
b = [x for x in range(10000000,20000000)]
c = []
import time

curr_time = time.time() #Give current time in sec
# for i in a:
#     c.append(a[i]+b[i])
#
time_taken = time.time()-curr_time
# print(time_taken)
# This operation has taken almost 2.5 sec

# Now let see using numpy array

import numpy as np
n1 = np.arange(10000000)
n2 = np.arange(10000000,20000000)

curr_time = time.time()
# n3 = n1 + n2
time_taken = time.time()-curr_time
# print(time_taken)
# It has taken 0.03 sec

# How much fast it is?
# print(2.50/0.03350400924682617) #74

# numpy array is 74 times faster than list


# Why it has a lot of difference ?
# Because numpy internally uses c language type array which is static and has fixed size and it is
# not a referencial array means data ko directly memory mee store karte ho naki uska address

# Python list are dynamic in nature every time inc its size by 2 (copy hota rhta h toh usmee time lgta h).
# And second thing that it is a referncial array means we store its address . and for accessing element
# it will go to the address and find the value so it takes a lot of time

# That's why numpy array are much better and faster than Python lists.

# Now will see the difference in terms of memory.

a = [i for i in range(10000000)]
import sys

print(sys.getsizeof(a)) #It will give size in bytes  #89095160 bytes taken by a

# Same case in numpy

b  = np.arange(10000000)
print(sys.getsizeof(b))

# By default numpy is also 64 bit system  and equivalent to list memory size.
# But we can change the size anytime with dtype we have flexibility in terms of that.
# Numpy is better in  terms of convenience  as well .

# Three Point in which numpy is better than list.
# 1.convenience
# 2. Memory
# 3. speed

########################################################################

# Advance indexing
# For Eg
a = np.arange(12).reshape(4,3)

# Fancy Indexing

# Now i want 1st row , 3row and 4th row
# So there is no pattern matching so we can use fancy indexing
# In fancy indexing we pass index in lists

# print(a[[0,2,3]])
# [[ 0  1  2]
#  [ 6  7  8]
#  [ 9 10 11]]

# Now i want 1st , third and fourth column

# print(a[:,[0,1,2]])

# Boolean Indexing
# It is used when we want data , based on logic not on pattern.
# like find all numbers that are divisible by 5 or we can say greater than 3.

#For Eg

a = np.random.randint(1,100,24).reshape(6,4)
print(a)

#Find all numbers greater than 50
# print(a>50) # This will give boolean array
# But we want number greater than 50
# So here comes the concept of boolean masking , so now we will mask this boolean array on orignal array
# print(a[a>50])   #[61 75 77 96 79 79 74 88 99 63 80 57]

# Find all numbers are even
# print(a[a%2==0]) #[74 20 38 10 96 86 50 48 28 28]

# Find all numbers are even and greater than 50
# print(a[(a>50) & (a%2==0)])  #[94 76 92 88 90 56 72 90 86]
# We are using logical and here

# Find all numbers that are not divisible by 7
# print(a[!(a%7==0)])

#####################################################################

#Broadcasting

# The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.
# The smaller array is “broadcast” across the larger array so that they have compatible shapes. It means
# we will grow smaller array to the bigger array .

# same shape
# a = np.arange(6).reshape(2,3)
# b = np.arange(6,12).reshape(2,3)
#
# print(a)
# print(b)
#
# print(a+b)


# This will add because of same shape .

# diff shape
# a = np.arange(6).reshape(2,3)
# b = np.arange(3).reshape(1,3)
#
# print(a)
# print(b)
#
# print(a+b)

# This will add because of broadcasting first matrix size is (2,3) and second matrix
# size is (1,3) so we will grow this to (2,3) and do addition bw these two arrays.


# Broadcasting Rules
# 1. Make the two arrays have the same number of dimensions.
#
# If the numbers of dimensions of the two arrays are different, add new dimensions with size 1 to the head of the array with the smaller dimension.
# 2. Make each dimension of the two arrays the same size.
#
# If the sizes of each dimension of the two arrays do not match, dimensions with size 1 are stretched to the size of the other array.
# If there is a dimension whose size is not 1 in either of the two arrays, it cannot be broadcasted, and an error is raised.


# More examples

# a = np.arange(12).reshape(4,3)
# b = np.arange(3)
#
# print(a)
# print(b)
#
# print(a+b)

# First we add 1 in front of (3) and make it a 2-D array (1,3)
# then we will stretch 1 to 4 and make it (4,3)
# Then addition is possible

#Eg
# a = np.arange(12).reshape(3,4)
# b = np.arange(3)
#
# print(a)
# print(b)
#
# print(a+b)

# THis will not work because after adding 1 to (3) it will become (1,3)
# then we will stretch it tilll 3 so it become (3,3) but now
# (3,3) and (3,4) are not of same size so they can't add with each other.


# Eg:
# a = np.arange(3).reshape(1,3)
# b = np.arange(3).reshape(3,1)
#
# print(a)
# print(b)
#
# print(a+b)

# This is possible because we will grow both 1 to 3 and after
# that they will become equivalent then we can add it in it .

#Eg
# a = np.arange(3).reshape(1,3)
# b = np.arange(4).reshape(4,1)
#
# print(a)
# print(b)
#
# print(a + b)

# Same as above example

#Eg
# a = np.array([1])
# # shape -> (1,1)
# b = np.arange(4).reshape(2,2)
# # shape -> (2,2)
#
# print(a)
# print(b)
#
# print(a+b)

# Eg
# a = np.arange(12).reshape(3,4)
# b = np.arange(12).reshape(4,3)
#
# print(a)
# print(b)
#
# print(a+b)

# This won't work because they both are of same size and
# does not contain 1 so it can;'t grow so they can;t add .

#Eg

# a = np.arange(16).reshape(4,4)
# b = np.arange(4).reshape(2,2)
#
# print(a)
# print(b)
#
# print(a+b)

# Same as above.



