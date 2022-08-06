__author__ = 'Ashraf'

def prime(x,y):
    primelist=[]
    for i in range(x,y):
        if  i ==0 or i ==1:
            continue
        else:
            for j in range (2,int(i/2) +1):
                if i%j==0:
                    break
            else:
                primelist.append(i)
    print (primelist)
prime(0,100)