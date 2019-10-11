from sys import stdin,stdout

t = int(stdin.readline())

i=0
for i in range(t):
    l = stdin.readline()
    arr = [int(i) for i in (stdin.readline().split())]

    expected_sum = int((l(l+1))/2)

    for i in range(l):
        expected_sum -= arr[i]

    stdout.write(str(expected_sum))