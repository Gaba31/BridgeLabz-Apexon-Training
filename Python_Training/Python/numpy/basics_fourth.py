import numpy as np
a = np.random.randint(1,100,15)
# print(a)


#np.sort() -> Return a sorted copy of an array.

# print(np.sort(a))    #Return the sorted numpy array
# print(np.sort(a)[::-1]) # Will give array in reverse sorted order

# Why we are using .sort() in numpy instead of sorted() ?
# Because .sort() will return a numpy array whereas sorted() returns us a list.

# Sorting on 2-D array

a = np.arange(25).reshape(5,5)

# print(np.sort(a))     # By default row wise sorting

# Col wise sorting

# print(np.sort(a,axis = 0)[::-1])     # Col wise sorting in reverse order

###################################################################

a = np.random.randint(1,100,15)

# np.append() -> The numpy.append() appends values along the mentioned axis at the end of the array
# Same as append() in list
# take two parameters -> array and what to add

a = np.append(a,500)
# print(a)

#On 2-D array
a = np.arange(25).reshape(5,5)

# Add a new col at the end of the matrix containing one only

a = np.append(a,np.ones((a.shape[0],1)),axis = 1)     #a.shape[0]-> will give no of rows    a.shape[1]-> will give no of col
# print(a)

#######################################################

# np.concatenate -> numpy.concatenate() function concatenate a sequence of arrays along an existing axis.

c = np.arange(6).reshape(2,3)
# print(c)
d = np.arange(6,12).reshape(2,3)
# print(d)

new_arr = np.concatenate((c,d),axis = 1) # axis = 1 = hstack axis = 0 for vstack
# print(new_arr)

#########################################################

#np.unique() -> With the help of np.unique() method, we can get the unique values from an array given as parameter in np.unique() method.

e = np.array([1,1,2,2,3,3,4,4,5,5,6,6])
# print(np.unique(e))

############################################################

# np.expand_dims() -> This is used for expanding array means can covert n-d array to n+1 d array
# 2-d to 3-d ....................n-d to n+1 d

a = np.arange(15)
# print(a.shape) #(15,)
a = np.expand_dims(a,axis = 1)  #axis = 1 toh col wise expand kr dega
# print(a.shape)  #(15, 1)

############################################################

# np.where()-> The numpy.where() function returns the indices of elements in an input array where the given condition is satisfied.

a = np.random.randint(1,100,15)
# print(a)

# find all indices with value greater than 50
# print(np.where(a>50))

# replace all values > 50 with 0
# np.where(condition , what will happen if the cond is true , what will happen if the cond is false)

# print(np.where(a>50,0,a))

# replace even values with 0 and non even with 1
# print(a)
# print(np.where(a%2==0,0,1))

#############################################################

#np.argmax() -> The numpy.argmax() function returns indices of the max element of the array in a particular axis.

a = np.arange(1,25,2)

# print(np.argmax(a))
# print(np.argmin(a))

a = np.arange(25).reshape(5,5)
# print(a)
# print(np.argmax(a,axis = 0))      #Gives the indices of the column where max is present


####################################################

# np.cumsum() -> numpy.cumsum() function is used when we want to compute the cumulative sum of array elements over a given axis.

a = np.arange(1,20)
print(np.cumsum(a))

# If i directly do it on 2-D array without axis so it will convert it in 1-D then do cumsum
# If axis is provided then it will do acc to the asis

# np.cumprod() -> Add krne k badle multiply krta hh

######################################################

