__author__ = 'Ashraf'
list1=[1,4,3,6,5,7]
# list.sort()
# # print(len(list))
# size=len(list)
# # list.append('a')
# print(list)

def MissingNumber(list1,n):
    list2=[]

    for i in range(1,int(len(list1))+2):
        list2.append(i)
    new_list = list(set(list2).difference(list1))
    for s in new_list:
        return s
    #return new_list[0]
print(MissingNumber([1,2,3,5],5))





# print(list1)
# print(list[0])
# if list[1]-list[0]==list[2]-list[1]:
#     print(True)
# else:
#     print(list[1]-list[0],list[2]-list[1])
# print(size)
