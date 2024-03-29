"""
Given a positive integer N, count all possible distinct binary strings of length N such that there are no consecutive 1’s. Output your answer mod 10^9 + 7.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.
Each test case contain an integer N representing length of the binary string.

Output:
Print the count number of binary strings without consecutive 1’s of length N.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100

Example:
Input:
2
3
2

Output:
5
3

Explanation:
Testcase 1: case 5 strings are (000, 001, 010, 100, 101)
Testcse 2:  case 3 strings are (00,01,10)
"""
import array

limit = 10**9+7
arr = array.array('i',[0])*(100+1)
arr[1] = 2
arr[2] = 3

def fib_like(n):
    #print(n)
    #nice dp step
    if(arr[n]==0):
        arr[n] = (fib_like(n-1)+fib_like(n-2))%limit
    
    return arr[n]

t = int(input())
#print(t)
for i in range(t):
    n = int(input())
    print(fib_like(n))

