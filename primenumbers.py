__author__ = 'Ashraf'

def IsPrime(n):

    if(n==1 or n==0):
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=100
for i in range(1,n+1):
    if IsPrime(i):
        print(i,end=" ")

IsPrime(50)