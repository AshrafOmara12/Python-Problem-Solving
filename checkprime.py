__author__ = 'Ashraf'
def checkprime(n):
    for i in range (2,int(n/2)+1):
        if n%i==0:
            print("The number is not prime")
            break
    else:
        print("number is prime")

# checkprime(20)

print(ord('9'))