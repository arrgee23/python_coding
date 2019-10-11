from sys import stdin,stdout
"""
Given a sequence A of size N, find the length of the longest 
increasing subsequence from a given sequence .
The longest increasing subsequence means to find a subsequence 
of a given sequence in which the subsequence's elements are in sorted order, 
lowest to highest, and in which the subsequence is as long as possible. 
This subsequence is not necessarily contiguous, or unique.

Note: Duplicate numbers are not counted as increasing subsequence.
"""
def find_lis(arr,l):
    x = [1]

    for i in range(1,l):
        found = False
        
        maximum = 1
        for j in range(i-1,-1,-1):
            #print(j)
            
            if(arr[j]<arr[i]):
               maximum = max([maximum,x[j]+1]) 
        x.append(maximum)

    return max(x)

t = int(stdin.readline())

for i in range(t):
    l = int(stdin.readline())
    arr = [int(a) for a in stdin.readline().split()]
    
    ans = find_lis(arr,l)
    print(ans)