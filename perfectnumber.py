__author__ = 'Ashraf'
def PerfectNumber(n):
    List=[]
    sum=0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            List.append(i)

    for r in range(0,len(List)):
        sum = sum + List[r]
    return (True if sum ==n and n!=1 else False)
n=2
for n in range(10000):
    if PerfectNumber(n):
        print(n,'the number is perfect')
PerfectNumber(6)
