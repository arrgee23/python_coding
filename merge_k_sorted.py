"""
Given K sorted arrays arranged in form of a matrix. The task is to merge them. 
You need to complete mergeKArrays() function which takes 2 arguments, 
an arr[k][k] 2D Matrix containing k sorted arrays and an integer k denoting
 the number of sorted arrays. The function should return a pointer to the merged sorted arrays.

Input:
The first line of input contains the number of test cases, 
then T test cases follows. Each test case will contain an integer N 
denoting the number of sorted arrays. Then in the next line contains all
 the elements of the array separated by space.

Output:
The output will be the sorted merged array.

User Task:
The task is to complete the function mergeKArrays() which takes two arguments, 
and returns pointer to the modified array.

Constraints:
1 <= T <= 50
1 <= N <= 103
1 <= K <= 10

Example:
Input:
1
3
1 2 3 4 5 6 7 8 9 

Output:
1 2 3 4 5 6 7 8 9

Explanation:
Testcase 1:
Above test case has 3 sorted arrays of size 3, 3, 3
arr[][] = [[1, 2, 3],

             [4, 5, 6],

             [7, 8, 9]]
The merged list will be [1, 2, 3, 4, 5, 6, 7, 8, 9].
"""


# Your code goes here
import atexit
import io
import sys
import heapq
from collections import  defaultdict
# Contributed by : Nagendra Jha
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a= list(map(int,input().strip().split()))
        arr = []
        ind =0
        temp = []
        while ind<len(a):
            temp.append(a[ind])
            if (ind+1)%n == 0:
                arr.append(temp)
                temp = []
            ind+=1
        print(*mergeKArrays(arr,n))


''' This is a function problem.You only need to complete the function given below '''

def mergeKArrays(a,n):
    '''
    :param a: given array
    :param n: size of row and column
    :return: merged sorted list
    '''
    print(a)