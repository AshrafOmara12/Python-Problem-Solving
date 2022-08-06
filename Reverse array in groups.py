__author__ = 'Ashraf'


# arr=[1,2,3,4]
# if len(arr)%2==0:
#     middleindex=int((len(arr)-1)/2)
#     def Reverse():
#         newarry1=arr[middleindex::-1]
#         newarry2=arr[len(arr):middleindex:-1]
#         for i in newarry2:
#
#             newarry1.append(i)
#
#         return newarry1
# else:
#
#
# print(Reverse())
import math




def reverseInGroups(arr, N, K):

            arr1=arr[K-1::-1]
            new_arr_1=arr[N:K-1:-1]

            for i in  new_arr_1:
                arr1.append(i)

            return arr1

print(reverseInGroups([5,6,8,9],4,3))
# def main():
#     T=int(input())
#     while(T>0):
#         nk=[int(x) for x in input().strip().split()]
#         N=nk[0]
#         K=nk[1]
#         arr=[int(x) for x in input().strip().split()]
#         print(arr)
#
#         ob=Solution()
#         ob.reverseInGroups(arr,N,K)
#         for i in arr:
#             print(i, end="")
#         print()
#         T=-1
#
# if __name__ == '__main__':
#     main()
