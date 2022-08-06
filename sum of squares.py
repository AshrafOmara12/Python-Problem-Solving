__author__ = 'Ashraf'
def Squares(n):
    sum=0
    for i in range(1,n+1):
        sum = sum+i*i*i
    return sum

print(Squares(5))