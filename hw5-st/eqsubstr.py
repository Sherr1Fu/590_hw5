# Write a function, which when iven one string (s) and two characters
# (c1 and c2), computes all pairings of contiguous ranges of c1s
# and c2s that have the same length.  Your function should return
# a set of three-tuples.  Each element of the set should be
# (c1 start index, c2 start index, length)
#
# Note that s may contain other characters besides c1 and c2.
# Example:
#  s = abcabbaacabaabbbb
#      01234567890111111  <- indices for ease of looking
#                1123456
#  c1 = a
#  c2 = b
#  Observe that there are the following contiguous ranges of 'a's (c1)
#  Length 1: starting at 0, 3, 9
#  Length 2: starting at 6, 11
#  And the following contiguous ranges of 'b's (c2)
#  Length 1: starting at 1, 10
#  Length 2: starting at 4
#  Length 4: starting at 13
#  So the answer would be
#  { (0, 1, 1), (0, 10, 1), (3, 1, 1), (3, 10, 1), (9, 1, 1), (9, 10, 1),
#    (6, 4, 2), (11, 4, 2)}
#  Note that the length 4 range of 'b's does not appear as there are no
#  Length 4 runs of 'a's.
import time
import random
from collections import deque

def matching_length_sub_strs(s, c1, c2):
    # WRITE ME
    result=set()
    a_length={}
    b_length={}
    a_len=0
    b_len=0
    index=-1
    for i, sub in enumerate(s):
        if sub==c1:
            if a_len==0:
                index=i
            a_len+=1
            if (i+1)==len(s) or s[i]!=s[i+1]:
                if a_len not in a_length:
                    a_length[a_len]=[]
                a_length[a_len].append(index)
                a_len=0
        if sub==c2:
            if b_len==0:
                index=i
            b_len+=1
            if (i+1)==len(s) or s[i]!=s[i+1]:
                if b_len not in b_length:
                    b_length[b_len]=[]
                b_length[b_len].append(index)
                b_len=0
    for key in a_length:
        if key in b_length:
            for i in a_length[key]:
                for j in b_length[key]:
                    result.add((i,j,key))                         
    return result


# Makes a random string of length n
# The string is mostly comprised of 'a' and 'b'
# So you should use c1='a' and c2='b' when
# you use this with matching_length_sub_strs
def rndstr(n):
    def rndchr():
        x=random.randrange(7)
        if x==0:
            return chr(random.randrange(26)+ord('A'))
        if x<=3:
            return 'a'
        return 'b'
    ans=[rndchr() for i in range(n)]
    return "".join(ans)

def best(n):
    return 'a'*(n//2)+'b'*(n//2)

def worst(n):
    return 'ab'*(n//2)

if __name__ == "__main__":
    strgens=[best,worst,rndstr]
    #strgens=[best]
    sizes = [2**i for i in range(9, 15)]
    #sizes = [2**i for i in range(9, 13)]
    #sizes = [2**i for i in range(5,6)]
    for size in sizes:
        result=[]
        result.append(size)
        for sg in strgens:
            s=sg(size)
            start=time.time()
            matching_length_sub_strs(s, 'a', 'b')
            end=time.time()
            runtime=end-start
            result.append(runtime)
        print(result[0],result[1],result[2],result[3],sep=",")

    
