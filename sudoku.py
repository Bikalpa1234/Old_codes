from random import randrange
import random
import numpy
A=numpy.zeros((11,11))



A[4][2]=1
A[5][6]=2


def check(A,r,t):
    i=r
    j=t
    if A[i][j]==A[i-2][j-1] or A[i][j]==A[i-2][j+1] or A[i][j]==A[i-1][j-2] or A[i][j]==A[i-1][j+2] or A[i][j]==A[i+1][j-2] or A[i][j]==A[i+1][j+2] or A[i][j]==A[i+2][j-1] or A[i][j]==A[i+2][j+1] or A[i][j]==A[i-1][j] or A[i][j]==A[i+1][j] or A[i][j]==A[i][j-1] or A[i][j]==A[i][j+1] or (A[i][j]==A[i-1][j]+1) or (A[i][j]==A[i-1][j]-1) or (A[i][j]==A[i][j-1]-1) or (A[i][j]==A[i][j-1]+1) or (A[i][j]==A[i][j+1]-1) or (A[i][j]==A[i][j+1]+1) or (A[i][j]==A[i+1][j]-1) or (A[i][j]==A[i+1][j]+1) or check2(A,i,j)==1:
        return 1   
    else:
        return 0



def swap(A,i,j,o,n):
    o=o
    n=n
    A[i][j]=A[o][n]
    A[o][n]=A[i][j] 

def check2(A,i,j):
    q=0
    m=0
    for q in range(9):
        for m in range(9):
            if q!=j:
                if A[i][j]==A[i][q]:
                    return 1
             A[i][j]==A[m][i]:
                    return 1
                else:
                    return 0        
  
              

def value(A,i,j):
  #  if i<=5 and j<=5:
   #     m=0
    #    while True:
     #       A[i][j]=random.randint(1,10)
      #      print('..')
       #     if A[i][j]==A[i-2][j-1] or A[i][j]==A[i-2][j+1] or A[i][j]==A[i-1][j-2] or A[i][j]==A[i-1][j+2] or A[i][j]==A[i+1][j-2] or A[i][j]==A[i+1][j+2] or A[i][j]==A[i+2][j-1] or A[i][j]==A[i+2][j+1] or A[i][j]==A[i-1][j] or A[i][j]==A[i+1][j] or A[i][j]==A[i][j-1] or A[i][j]==A[i][j+1] or (A[i][j]==A[i-1][j]+1) or (A[i][j]==A[i-1][j]-1) or (A[i][j]==A[i][j-1]-1) or (A[i][j]==A[i][j-1]+1) or (A[i][j]==A[i][j+1]-1) or (A[i][j]==A[i][j+1]+1) or (A[i][j]==A[i+1][j]-1) or (A[i][j]==A[i+1][j]+1) or check2(A,i,j)==1:
        #        continue
         #   else:
          #      return A[i][j]
    #else:
    for k in range(1,10):
        A[i][j]=k
        if A[i][j]==A[i-2][j-1] or A[i][j]==A[i-2][j+1] or A[i][j]==A[i-1][j-2] or A[i][j]==A[i-1][j+2] or A[i][j]==A[i+1][j-2] or A[i][j]==A[i+1][j+2] or A[i][j]==A[i+2][j-1] or A[i][j]==A[i+2][j+1] or A[i][j]==A[i-1][j] or A[i][j]==A[i+1][j] or A[i][j]==A[i][j-1] or A[i][j]==A[i][j+1] or (A[i][j]==A[i-1][j]+1) or (A[i][j]==A[i-1][j]-1) or (A[i][j]==A[i][j-1]-1) or (A[i][j]==A[i][j-1]+1) or (A[i][j]==A[i][j+1]-1) or (A[i][j]==A[i][j+1]+1) or (A[i][j]==A[i+1][j]-1) or (A[i][j]==A[i+1][j]+1) or check2(A,i,j)==1:
            continue
        else:
            return A[i][j]



def error1(A,i,j):
    if A[i][j]==A[i-2][j-1]:
        return i-2
    elif  A[i][j]==A[i-2][j+1]:
        return i-2
    elif A[i][j]==A[i-1][j-2]:
        return i-1
    elif A[i][j]==A[i-1][j+2]:
        return i-1
    elif A[i][j]==A[i+1][j-2]:
        return i+1
    elif A[i][j]==A[i+1][j+2]:
        return i+1
    elif A[i][j]==A[i+2][j-1]:
        return i+2
    elif A[i][j]==A[i+2][j+1]:
        return i+2
    elif A[i][j]==A[i-1][j]:
        return i-1
    elif A[i][j]==A[i+1][j]:
        return i+1
    elif A[i][j]==A[i][j-1]:
        return i
    elif A[i][j]==A[i][j-1]:
        return i
    elif A[i][j]==A[i][j+1]:
        return i
    elif A[i][j]==A[i-1][j]+1:
        return i-1
    elif A[i][j]==A[i-1][j]-1:
        return i-1
    elif A[i][j]==A[i][j-1]-1:
        return i
    elif A[i][j]==A[i][j-1]+1:
        return i
    elif A[i][j]==A[i][j+1]-1:
        return i
    elif A[i][j]==A[i][j+1]+1:
        return i
    elif (A[i][j]==A[i+1][j]-1):
        return i+1
    elif (A[i][j]==A[i+1][j]+1):
        return i+1
    elif A[i][j]==A[0][j]:
        return 0
    else:
        u=0
        for u in range(9):
            if u!=i:
                if A[i][j]==A[u][j]:
                    return u
                else:
                    return i        
          





def error2(A,i,j):
    if A[i][j]==A[i-2][j-1]:
        return j-1
    elif  A[i][j]==A[i-2][j+1]:
        return j+1
    elif A[i][j]==A[i-1][j-2]:
        return j-2
    elif A[i][j]==A[i-1][j+2]:
        return j+2
    elif A[i][j]==A[i+1][j-2]:
        return j-2
    elif A[i][j]==A[i+1][j+2]:
        return j+2
    elif A[i][j]==A[i+2][j-1]:
        return j-1
    elif A[i][j]==A[i+2][j+1]:
        return j+1
    elif A[i][j]==A[i-1][j]:
        return j
    elif A[i][j]==A[i+1][j]:
        return j
    elif A[i][j]==A[i][j-1]:
        return j-1
    elif A[i][j]==A[i][j-1]:
        return j-1
    elif A[i][j]==A[i][j+1]:
        return j+1
    elif A[i][j]==A[i-1][j]+1:
        return j
    elif A[i][j]==A[i-1][j]-1:
        return j
    elif A[i][j]==A[i][j-1]-1:
        return j-1
    elif A[i][j]==A[i][j-1]+1:
        return j-1
    elif A[i][j]==A[i][j+1]-1:
        return j+1
    elif A[i][j]==A[i][j+1]+1:
        return j+1
    elif (A[i][j]==A[i+1][j]-1):
        return j
    elif (A[i][j]==A[i+1][j]+1):
        return j
    else:
        u=0
        for u in range(9):
            if u!=j:
                if A[i][j]==A[i][u]:
                    return u
                else:
                    return j    
                 
                   


for i in range(9):
    for j in range(9):
        if i==4 and j==2:
            continue
        if i==5 and j==6:
            continue
        else:    
            print(i,j)
            A[i][j]=value(A,i,j)
            print(A[i][j])
            if A[i][j]==None:
                A[i][j]=randrange(1,10)
            b=1
            while b==1:
                b=check(A,i,j)
                if b==1:
                    o=error1(A,i,j)
                    n=error2(A,i,j)
                    i=o
                    j=n
                    A[i][j]=random.randint(1,9)
                
                    


print(A)
