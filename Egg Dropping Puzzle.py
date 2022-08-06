# __author__ = 'Ashraf'
# A Dynamic Programming based Python
# Program for the Egg Dropping Puzzle
INT_MAX = 32767

# Function to get minimum number of trials needed in worst
# case with n eggs and k floors
def eggDrop(n, k):
	# A 2D table where entry eggFloor[i][j] will represent minimum
	# number of trials needed for i eggs and j floors.
	eggFloor = [[0 for x in range(k + 1)] for x in range(n + 1)]

	# We need one trial for one floor and0 trials for 0 floors
	for i in range(1, n + 1):
		eggFloor[i][1] = 1
		eggFloor[i][0] = 0

	# We always need j trials for one egg and j floors.
	for j in range(1, k + 1):
		eggFloor[1][j] = j

	# Fill rest of the entries in table using optimal substructure
	# property
	for i in range(2, n + 1):
		for j in range(2, k + 1):
			eggFloor[i][j] = INT_MAX
			for x in range(1, j + 1):
				res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x])
				if res < eggFloor[i][j]:
					eggFloor[i][j] = res

	# eggFloor[n][k] holds the result
	return eggFloor[n][k]

# Driver program to test to printDups
n = 1
k = 3
print("Minimum number of trials in worst case with" + str(n) + "eggs and "
	+ str(k) + " floors is " + str(eggDrop(n, k)))

# This code is contributed by Bhavya Jain

# #User function Template for python3
# import cmath
#
#
# def eggDrop(n, k):
#         a = 1
#         b = 1
#         c = -2*k
#         d = (b**2) - (4*a*c)
#         sol1 = (-b-cmath.sqrt(d))/(2*a)
#         sol1=abs(round(sol1.real))
#         sol2 =(-b+cmath.sqrt(d))/(2*a)
#         sol2=abs(round(sol2.real))
#         # print(sol1)
#         # print(sol2)
#         if sol1<sol2:
#             return sol1
#         else:
#             return sol2
#
#
# print(eggDrop(1,2))