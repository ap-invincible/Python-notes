import numpy as np 
# a = np.array([1,2,3])
# print(a)

# b = np.array([[1,2,3,4], [5,6,7,8],[11,22,33,44]], dtype='int32')
# print(b)

#Dimension of a matrix
# print(b.shape)

#Size
# print(b.nbytes)

#Getting a specific element from the matrix
# element_x = b[2,2]
# print(element_x)

#Get a specific row or column
# rowx = b[1, :]
# columnx = b[:, 2]
# print(rowx)
# print(columnx)

#Indexing in numpy  ::: list-name[wheretostart  ,  indexing and step]
# index_x = b[0 , 1:6:2]
# print(index_x)

#Modifying data
#Changing a specific element
# print('previous entry was:', b[1,3])
# b[1,3] = 14
# print('new entry is:', b[1,3])

#Changing a whole row
# print('The previous row was:', b[2, :])
# b[2, :] = [9,2,3,7]
# print('The new entry is:', b[2, :])

#Null matrix
# zeromatrix = np.zeros((3,8))
# print(zeromatrix)

#Matrix creation of our choice
# thirtytwo = np.full((3,4), 32)
# print(thirtytwo)

#How to copy an existing matrix's dimension to create a new matrix/array
# four = np.full(b.shape, 4)
# print(four)
# four2 = np.full_like(b, 4)
# print(four2)

#Identity matrix
# identitym = np.identity(5)
# print(identitym)


#Making a matrix like the one below
# [ 1 1 1 1 1 ]
# [ 1 0 0 0 1 ]
# [ 1 0 9 0 1 ]
# [ 1 0 0 0 1 ]
# [ 1 1 1 1 1 ] 

#My method - Absolute shit
# matrixbase = np.zeros((5, 5))
# matrixbase[:, 0] = 1
# matrixbase[0, :] = 1
# matrixbase[4, :] = 1
# matrixbase[:, 4] = 1
# matrixbase[2, 2] = 9
# print(matrixbase)

#The logical method
# matrix = np.ones((5,5))
# # print(matrix)
# mzero = np.zeros((3,3))
# mzero[1,1] = 9
# # print(mzero)
# matrix[1:4, 1:4] = mzero
# print(matrix)

#Copying arrays in numpy directly can result in changing the source array into the new one if the copied array gets modified
#Below is an example for the same
# a = np.array([1,2,3])
# # b = a
# # b[0] = 100
# # print(a)    #a got changed along with b.
# b = a.copy()    #copying an array in numpy
# b[0] = 100
# print(a)
# print(b)

#Mathematics
# a = np.array([[1,2,3,4], [5,6,7,8]])
# print(a * 2)
# b = np.array([[5,2,4,7], [1,8,4,9]])
# print(a + b)
# print(a * b)    #Multiplication and division are done for the elements at the exact same index in both matrices
#This abov funtion cannot multiply matrices directly, it just multiplies the entries
# print(np.sin(a))    #Finding out the sin of the array


#Linear Algebra
# a = np.full((2,3), 5)
# # print(a)
# b = np.full((3,2), 2)
# mul = np.matmul(a,b)  #Matrix multiplication function in numpy
# print(mul)

#Finding determinant
# c = np.identity(3)
# print(np.linalg.det(c))     #This function finds the determinant of the given matrix
# print(np.linalg.inv(c))     #This funtion finds the inverse of the given matrix
# print (inv(np.matrix(c)))

#Statistics
# stats = np.array([[1,2,3],[4,5,6]])
# print(np.min(stats), np.max(stats), np.sum(stats))
############Maths ended


#Resizing arrays
# a = np.array([[1,2,3,4],[5,6,7,8]])
# print(a)
# b = a.reshape((4,2))
# print(b)

#Stacking --> Adding stacks into the same matrix
# arr = np.array([1,2,3,4])
# at = np.array([5,6,7,8])
# #Vertical Stacking
# # z = np.vstack([arr,at,arr,arr,at])
# # print(z)
# #Horizontal Stacking
# z = np.hstack([arr,at])
# print(z)

#Using numpy to read filedata
# filedata = np.genfromtxt('fil-name', delimiter='  ')
# print(filedata)

