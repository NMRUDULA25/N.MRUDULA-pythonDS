import numpy as np
# arr=np.arange(10) array range->arange
# arr1=np.arange(10,50,5)
# arr2=np.arange(50,10,-5)
# print(arr)
# print(arr1)
# print(arr2)
#n=3
# for i in range(n):
#     odd=(2*i)+1
#     print(odd*(odd+1),odd+1,odd)
#using Numpy method - arange convert list to dot array 
# col3=np.arange(1,2*n,2)
# col2=np.arange(1,2*n+1,2)
# col1=col2*col3
# res=np.column_stack((col1,col2,col3))
# print(res)
list1=[10,80,60,40,20,90]
arr=np.array(list1)
print(arr)
#without using numpy
op=[1]*len(list1)
print(op)
#Method in Numpy - ones_like
op1=np.ones_like(arr)
print(op1)
matrix=np.ones((3,3))
print(matrix)
mat1=np.random.randint(10,50,size=(3,4))
print(mat1)
otp=np.random.randint(100000,999999)
print(otp)
list=[10,30,20,40,50,60,70,80,90]
arr=np.array(list)
print(np.max(arr))
print(np.mean(arr))
print(np.sum(arr))

arr=np.arange(10)
arr[arr%2==0]*=2
print(arr)
arr1=np.array([1,2,3,4,5,6,-6,-7,9])
arr1[arr1<0]=0
print(arr1)

