__author__ = 'Ashraf'
import itertools as it

# a=[1, 4, 20, 3, 10, 5]
# s=33
# for i in range(len(a)):
#     curr_sum=a[i]
#     for j in range(i+1,len(a)):
#         curr_sum=curr_sum+a[j]
#         if curr_sum==s:
#             print(i,j)

# def subArraySum(A, N, S):
#     for i in range(len(A)):
#         S0=A[i]
#         for j in range(i+1,len(A)):
#             if S0 > S or j == N:
#                 break
#             S0=S0+A[j]
#             if S==S0:
#                 return i+1, j+1
#
#
# print(subArraySum([1,2,3,7,5], 5, 12))
# Returns true if the
# there is a subarray
# of arr[] with sum
# equal to 'sum'
# otherwise returns
# false. Also, prints
# the result
# def subArraySum(arr, n, sum_):
#
# 	# Pick a starting
# 	# point
# 	for i in range(n):
# 		curr_sum = arr[i]
# 		j = i + 1
# 		while j <= n:
#
# 			if curr_sum == sum_:
# 				print ("Sum found between")
# 				print("indexes % d and % d"%( i, j-1))
#
# 				return 1
#
# 			if curr_sum > sum_ or j == n:
# 				break
#
# 			curr_sum = curr_sum + arr[j]
# 			j += 1
#
# 	print ("No subarray found")
# 	return 0
#
# # Driver program
# arr = [15, 2, 4, 8, 9, 5, 10, 23]
# n = len(arr)
# sum_ = 23
#
# subArraySum(arr, n, sum_)
#

# An efficient program
# to print subarray
# with sum as given sum

# Returns true if the
# there is a subarray
# of arr[] with sum
# equal to 'sum'
# otherwise returns
# false. Also, prints
# # the result.
# def subArraySum(arr, n, S):
#
# 	# Initialize curr_sum as
# 	# value of first element
# 	# and starting point as 0
# 	S0 = arr[0]
# 	start = 0
#
# 	# Add elements one by
# 	# one to curr_sum and
# 	# if the curr_sum exceeds
# 	# the sum, then remove
# 	# starting element
# 	i = 1
# 	while i <= n:
#
# 		# If curr_sum exceeds
# 		# the sum, then remove
# 		# the starting elements
# 		while S0 > S and start < i-1:
#
# 			S0 = S0 - arr[start]
# 			start += 1
#
# 		# If curr_sum becomes
# 		# equal to sum, then
# 		# return true
# 		if S0 == S:
# 			print ("Sum found between indexes")
# 			print ("% d and % d"%(start, i-1))
# 			return 1
#
# 		# Add this element
# 		# to curr_sum
# 		if i < n:
# 			S0 = S0 + arr[i]
# 		i += 1
#
# 	# If we reach here,
# 	# then no subarray
# 	print ("No subarray found")
# 	return 0


# arr = [15, 2, 4, 8, 9, 5, 10, 23]
# n = len(arr)
# # print(n)
# S = 23
#
# S_0=arr[0]
# # print(S_0)
# Start=0
# i = 1
# while i<=n:
# 	while S_0>S and Start<i-1:
# 		S_0=S_0-arr[Start]
# 		Start += 1
# 	if S_0==S:
# 		print(Start,i-1)
# 	if i<n:
# 		S_0=S_0+arr[i]
# 		# print(S_0)
# 	i+=1

# Python program to print Subarray with given sum using Linear complexity method
# The program will print the indexes if the currentsum is equal to the sum; else, it will print sum will not be found

def subarray(arr,n,sum):
  currentsum = arr[0]
  begin = 0

    # Add elements one by
    # one to currentsum and
    # if the currentsum exceeds
    # the sum, then remove
    # starting element
  i = 1
  while i <= n:

        # If currentsum exceeds
        # the sum, then remove
        # the starting elements
      while currentsum > sum and begin < i-1:

          currentsum = currentsum - arr[begin]
          begin = begin + 1

        # If currentsum becomes
        # equal to sum, then
        # return true
      if currentsum == sum:
          print("Sum found between indexes")
          print("% d and % d"%(begin, i-1))
          return 1

        # Add this element
        # to currentsum
      if i < n:
          currentsum = currentsum + arr[i]
      i = i + 1

    # If we reach here,
    # then no subarray
  print("No subarray found")
  return 0
print("Enter size of an array: ")
n=int(input())
print("Enter array elements: ")
i=0
A=[]
while(i<n):
  ele=int(input())
  A.append(ele)
  i=i+1
print("Enter value of sum: ")
sum=int(input())
subarray( A , n , sum )