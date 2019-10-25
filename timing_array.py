import timeit

setup1="""
import numpy as np
import random
limit = 2*10**4
a = [random.randint(0,limit)]*limit
"""

setup2="""
limit = 10**8
import random
a = [random.randint(0,limit)]*limit
"""
#arr = array.array('i',[0])*(limit+1)

exe = "mat = np.zeros((limit,limit))"

exe2 = "mat = [[0 for i in range(limit)] for j in range(limit)]"
#print(timeit.timeit(setup=setup2,
 #                   stmt = exe2, 
  #                  number = 11) )

exe3="""
for i in range(limit):
    arr[a[i]]=3
"""

print(timeit.timeit(setup=setup1,
                    stmt = exe, 
                    number = 5) )

print(timeit.timeit(setup=setup1,
                    stmt = exe2, 
                    number = 5) )
