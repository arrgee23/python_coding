
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer

# reading writing
from sys import stdin,stdout

t = int(stdin.readline())

i=0
for i in range(t):
    l1 = int(stdin.readline())
    arr = [int(i) for i in (stdin.readline().split())]
    l2 = int(stdin.readline())
    arr2 = [int(i) for i in (stdin.readline().split())]
    print(canCompleteCircuit(arr,arr2))
    
def canCompleteCircuit(A, B):
    cum = []
    for a,b in zip(A,B):
        cum.append(a-b)
    #print(cum)
    i = hole_filling(A,B)
    return i
       
def hole_filling(A,B):
     
        l = len(A)
        i=0
        cum = 0
        s=0
        reset = False
        total = 0
        while(i<l):
            total += A[i%l]-B[i%l]
            if(A[i%l]-B[i%l]>=0):
                if(reset):
                    s = i%l
                    reset = False
                cum += A[i%l]-B[i%l]
            
            else:
                if(A[i%l]-B[i%l]+cum<0):
                    reset = True
                    cum = 0
                else:
                    cum = cum + A[i%l]-B[i%l]
                    
            i+=1
        if(total<0):
            return -1
        else:
            return s