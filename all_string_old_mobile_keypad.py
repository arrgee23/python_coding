
d = {'2':"abc",'3':"def",'4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}



def helper(arr,i,size,buff):
    if(i==size):
        for char in buff:
            print(char,end='')
        
        print(end=' ')
        return
    
    curr_digit = arr[i]
    curr_string = d[curr_digit]

    for char in curr_string:
        buff.append(char)
        helper(arr,i+1,size,buff)

        buff.pop()

def calculate(arr,l):
    helper(arr,0,l,[])

t = int(input())

for i in range(t):
    l = int(input())
    arr = [i for i in input().strip().split()]

    calculate(arr,l)
    print()

    