from sys import stdin,stdout
t = int(stdin.readline())

def calculate(arr,k):
    dic = {}
    for num in arr:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num]+=1

    count = 0
    for num in arr:
        if(k-num in dic):
            if(k-num == num):
                count += dic[k-num] - 1
            else:
                count += dic[k-num]

            # num has already been paired, so decrease its count
            dic[num] -= 1

    return count

for i in range(t):
    a = [int(n) for n in stdin.readline().strip().split()]
    k = a[1]
    arr = [int(n) for n in stdin.readline().strip().split()]
    count = calculate(arr,k)
    print(count)