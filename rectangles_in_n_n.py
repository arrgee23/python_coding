"""
Find total number of Rectangles (excluding squares) in a N*N cheesboard.

Input:

The first line contains an integer T, depicting total number of test cases. 
Then following T lines contains an integer N that is the side of the chessboard.


Output:

Each seperate line showing the maximum number of rectangles possible.


Constraints:

1 ≤ T ≤ 1000
1 ≤ N ≤ 10000
 

Example:

Input :

2
1
2

Output :

0
4

 

Explanation :

For n=1 there is only one square possible and no rectangles so answer will be 0. 

For n=2 there will be 2 rectangles of dimension 1*2 and 2 rectangles of dimension 2*1. So answer if 4. 
"""
n2_sum_dict = {}
rect_count_dict = {}
def sum_n_2(n):
    global n2_sum_dict
    if n in n2_sum_dict:
        return n2_sum_dict[n]
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    n2_sum_dict[n] = sum
    return sum

def all_rect_count(n):
    global rect_count_dict
    if n in rect_count_dict:
        return rect_count_dict[n]
    sum = 0
    for height in range(1,n+1):
        for width in range(1,n+1):
            sum += n**2/(height*width)
    rect_count_dict[n] = sum
    return sum

from sys import stdin,stdout
t = int(stdin.readline().strip())

for i in range(t):
    n = int(stdin.readline().strip())

    stdout.write(str(int((all_rect_count(n)-sum_n_2(n))))+"\n")