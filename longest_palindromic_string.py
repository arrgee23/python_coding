from sys import stdin,stdout

t = int(stdin.readline().strip())

def calculate(string,l):
    dp = [ [ 0 for j in range(l)] for i in range(l)]
    #print(string,l)
    # 1 length string always palindrome
    maxlen = 1
    maxinterval = (0,0)

    for i in range(l):
        dp[i][i] = 1

    # handle case for 2 length strings
    for i in range(l-1):
        if(string[i] == string[i+1]):
            if(maxlen<2):
                maxlen = 2
                maxinterval = (i,i+1)
            
            dp[i][i+1] = 1
    #print(dp)
    
    # handle case for rest
    for interval in range(2,l):
        start = 0
        end = interval

        while(start< l and end < l):
            if(string[start] == string[end] and dp[start+1][end-1] == 1):
                if(maxlen<interval+1):
                    maxlen = interval+1
                    maxinterval = (start,end)
                dp[start][end] = 1
            start += 1
            end += 1
    
    return maxinterval

for i in range(t):
    string = stdin.readline().strip()
    l = len(string)
    interval = calculate(string,l)
    stdout.write(string[interval[0]:interval[1]+1]+"\n")
    