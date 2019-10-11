"""# reading writing
from sys import stdin,stdout

t = int(stdin.readline())

i=0
for i in range(t):
    l = int(stdin.readline())
    arr = [int(i) for i in (stdin.readline().split())]

stdout.write("foobar")

"""

# printing as printf
a = 300.98803
print("integer %d float %2.2f "%(a,a))

#init 2d array
n = 3
mat = [[0 for i in range(n)] for j in range(n)]
print(mat)



print("--------------------------------------------------------------")
#using stack and queue

stack = []
stack.append(0)
stack.append(2)
print("Before popping")
print(stack)
print("popped: ")
print(stack.pop())
print("After Popping: ")
print(stack)

#queue
queue = []
queue.append(1)
queue.append(2)
#dequeueing
queue.remove(queue[0])
#or
queue.pop(0)




#more efficient queue or stack
print("--------------------------------------------------------------")
from collections import deque
stack = deque(maxlen=100)
queue = deque(maxlen=100)

stack.append(1)
stack.append(2)

queue.append(3)
queue.append(4)
print(stack)
print(queue)

n1 = stack.pop()
print(n1)
n2 = queue.popleft()
print(n2)
print(stack)
print(queue)




#Using heap in python
print("--------------------------------------------------------------")
import heapq

l = [12,5,22,221,82,10,9]
heapq.heapify(l)
print(l)
heapq.heappush(l,-3)
print(l)
a = heapq.heappop(l)
print(a)
print(heapq.nlargest(3,l))
print(heapq.nsmallest(3,l))

#using sets in pyhton
print("--------------------------------------------------------------")
a = {1,2,3}
#checking value contain
print(5 in a)
b = {3,4,5}
#various operation
c = a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)
print(c)
print(a)

#using hashtable or dict 
print("--------------------------------------------------------------")
dic = {"name":"rahul","age":22}

for key in dic:
    print(key," ",dic[key])

#deletes an element
del(dic["name"])

#removes entire dictionary
#dict.clear()
