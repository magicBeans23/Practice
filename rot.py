import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    l = list()
    for i in range(0, len(a)):
        k = i-d
        print(i, k, d)
        if k < 0:
            k = k+len(a)
        l.insert(k, a[i])
    return l

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
