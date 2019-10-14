"""
Given a string, find the rank of the string amongst its permutations sorted lexicographically. 
Return 0 if the characters are repeated in the string.

For example:

Input : 'acb'
Output : 2

The order permutations with letters 'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba

The answer might not fit in an integer, so return your answer % 1000003

Input:

The first line of input contains an integer T denoting the number of test cases. Each test case consist of a string in 'lowercase' only in a separate line.


Output:

Print the rank of the string amongst its permutations.

Constraints:

1 ≤ T ≤ 50

1 ≤ |s| ≤ 15

Example:

Input:
2
abc
acb
Output:
1
2
"""
import math
def rank(s):
    #arr = [c for c in s]
    sorted_arr = sorted(s)
    hash = [-1]*26

    for idx,c in enumerate(sorted_arr):
        key = ord(c)-ord('a')
        
        # we have a duplicate
        if(hash[key] > 0):
            return 0

        hash[key] = idx+1
    
    ans = 1
    l = len(s)
    for idx,char in enumerate(s):
        key = ord(char)-ord('a')
        after = hash[key]-1

        ans = (ans+after*math.factorial(l-1-idx))%1000003

        #adjust rank
        for i in range(key+1,26):
            hash[i] = hash[i]-1

    return ans


t = int(input())

for i in range(t):
    s = input()
    print(rank(s))