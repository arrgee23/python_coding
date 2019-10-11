# Given a string S. The task is to print all permutations of a given string.

from sys import stdin,stdout

def swap(s,i,j):
    t = s[i]
    s[i] = s[j]
    s[j] = t



def perm_helper(s,k,vector):

    if(k==len(s)-1):
        ss = ''
        for char in s:
            ss+=char    
        vector.append(ss)

    else:
        for i in range(k,len(s)):
            swap(s,k,i)
            perm_helper(s,k+1,vector)
            swap(s,k,i)

def permute(s):
    vector = []
    perm_helper(s,0,vector)
    vector = sorted(vector)
    for v in vector:
        print(v,end=' ')


t = int(stdin.readline().strip())

for i in range(t):
    s = list(stdin.readline().strip())
    permute(s)
    
    print()