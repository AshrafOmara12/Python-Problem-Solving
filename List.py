# List = [12, 35, 9, 56, 24]
# size=len(List)
# print(size)
# NewList=[List[len(List)-1],List[1],List[2],List[3],List[0]]
# print(NewList)



def swapping(List):
    # size= len(List)
    # temp = List[0]
    # List[0] = List[size - 1]
    # List[size - 1] = temp
    # List[0], List[-1] = List[-1], List[0]t
    # start,*middle,end = List
    # List = [end,*middle,start]
    first = List.pop(0)
    last = List.pop(-1)
    List.insert(0,last)
    List.append(first)
    return List
List=[12, 35, 9, 56, 24]
print(swapping(List))

