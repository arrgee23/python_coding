"""
Given a pattern containing only I's and D's. I for increasing and D for decreasing.
Devise an algorithm to print the minimum number following that pattern.
Digits from 1-9 and digits can't repeat.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is a string, which contains only I's and D's in capital letter.

Output:
Print the minimum number following that pattern.

Constraints:
1 ≤ T ≤ 100
1 ≤ Length of String ≤ 8

Example:
Input
5
D
I
DD
IIDDD
DDIDDIID

Output
21
12
321
126543
321654798
"""

from sys import stdin,stdout

def calculate(symbols):
    arr = [1]
    
    #print(len(symbols))
    for i in range(len(symbols)):
        num = i+2
        arr.append(num)

        for j in range(i,-1,-1):
            sym = symbols[j]
            prev = arr[j]
            next = arr[j+1]

            if(prev > next and sym == 'I'):
                arr[j] = next
                arr[j+1] = prev
            elif(prev < next and sym == 'D'):
                arr[j] = next
                arr[j+1] = prev
            else:
                break

    s = ""
    for i in arr:
        s+=str(i)
    print(s)

t= int(stdin.readline())

for i in range(t):
    symbols = stdin.readline().strip()
    calculate(symbols)