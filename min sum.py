__author__ = 'Ashraf'
def MinSum(arr,n):
    arr = sorted(arr)
    num1=0
    num2=0
    for i in range(n):
        if i%2==0:
            num1=num1*10+arr[i]
        else:
            num2=num2 *10 +arr[i]
    return num1+num2
print(MinSum([6, 8, 4, 5, 2, 3],6))
