import math
import os
import random
import re
import sys

class Sols:
# Complete the sockMerchant function below.
    def sockMerchant(self,n, ar):
        ls = [0]*100
        npairs=0
        for i in ar:
            ls[i-1] += 1

        for l in ls:
            if l >= 2:
                npairs += l//2
        return npairs

def countingValleys(n, s):
    lvl = 0
    lvlLast = 0
    nValley = 0
    for c in s:
        if c == 'D':
            lvl -= 1
        else:
            lvl += 1

        if lvlLast < 0 and lvl == 0:
            nValley += 1

        lvlLast = lvl

    return nValley

def jumpingOnClouds(c):
    n = len(c)
    count = 0
    i = 0
    while i < n-2:
        if c[i+2] == 0:
            i += 2
            count += 1
        else:
            i += 1
            count += 1
    if i < n-1:
        count +=1




if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())
    #
    # c = list(map(int, input().rstrip().split()))
    #
    # result = jumpingOnClouds(c)
    #fptr.write(str(result) + '\n')
    for i in range(1,8,2):
        print(i)

    #fptr.close()
#9
#10 20 20 10 10 30 50 10 20