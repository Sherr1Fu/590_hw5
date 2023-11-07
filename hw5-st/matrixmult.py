# This function takes 2 matricies (as lists of lists)
# and performs matrix multiplication on them.
# Note: you may not use any matrix multiplication libraries.
# You need to do the multiplication yourself.
# For example, if you have
#     a=[[1,2,3],
#        [4,5,6],
#        [7,8,9],
#        [4,0,7]]
#     b=[[1,2],
#        [3,4],
#        [5,6]]
#  Then a has 4 rows and 3 columns.
#  b has 3 rows and 2 columns.
#  Multiplying a * b results in a 4 row, 2 column matrix:
#  [[22, 28],
#   [49, 64],
#   [76, 100],
#   [39, 50]]
import time
import random
from collections import deque

def matrix_mul(a,b):
    # Write me
    result=[[0 for i in range(len(b[0]))]\
             for j in range (len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

if __name__ == "__main__":
    sizes = [2**i for i in range(2,10)]
    for size in sizes:
        result=[]
        result.append(size)
        square_morerows=[[random.random() for i in range (0,size)] for j in range (0,size*4)]
        square_morecols=[[random.random() for i in range (0,size*4)] for j in range (0,size)]
        square_N1=[[random.random() for i in range (0,size)] for j in range (0,size)]
        square_N2=[[random.random() for i in range (0,size)] for j in range (0,size)]
        #print(data)
        start=time.time()
        matrix_mul(square_morerows,square_morecols)
        end=time.time()
        runtime=end-start
        result.append(runtime)
        #
        start=time.time()
        matrix_mul(square_N1,square_N2)
        end=time.time()
        runtime=end-start
        result.append(runtime)
        #
        start=time.time()
        matrix_mul(square_morecols,square_morerows)
        end=time.time()
        runtime=end-start
        result.append(runtime)
        print(result[0],result[1],result[2],result[3],sep=",")