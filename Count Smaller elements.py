__author__ = 'Ashraf'

# arr = [12, 1, 2, 3, 0, 11, 4]
# n=len(arr)
#
# for i in range(len(arr)):
#     list1=[]
#     if arr[0] > arr[i+1]:
#         print(i)
#         list1=list1.append(i)
#     # print(list1)
def constructLowerArray(arr, n):
    L=[]
    # n=7
    for i in range(n-1):
        count=0
        for k in range(i+1,n):
            if arr[k]<arr[i]:
                count+=1
        L.append(count)
        # print(L)
    L.append(0)
    return L

print(constructLowerArray([12, 1, 2, 3, 0, 11, 4],7))
