# removes duplicates from data.
# This function keeps the last occurence of each element
# and preserves order.
# So rmdup([1,2,3,2,1,4,2]) should return [3,1,4,2]
import time
import random
from collections import deque

def rmdup(data):
    # Write me
    seen={}
    result=deque()
    #data.reverse()
    for i in data[::-1]:
        if i not in seen:
            seen[i]=1
            result.appendleft(i)
    return result

if __name__ == "__main__":
    sizes = [2**i for i in range(12,23)]
    for size in sizes:
        result=[]
        result.append(size)
        data=[random.randrange(0,size//2048) for i in range (0,size)]
        #print(data)
        start=time.time()
        rmdup(data)
        end=time.time()
        runtime=end-start
        result.append(runtime)
        data=[random.randrange(0,size//16) for i in range (0,size)]
        start=time.time()
        rmdup(data)
        end=time.time()
        runtime=end-start
        result.append(runtime)
        data=[random.randrange(0,size*4) for i in range (0,size)]
        start=time.time()
        rmdup(data)
        end=time.time()
        runtime=end-start
        result.append(runtime)
        print(result[0],result[1],result[2],result[3],sep=",")


        
