#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = len(c)
    i = 0
    count=0
    while i < n+1:
        if i+2 < n and c[i+2]!=1:
            # print ("2 Langkah")
            i=i+2
            count = count +1
        elif i+1<n and c[i+1]!=1:
            # print ("1 Langkah")
            i=i+1
            count = count+1
        else:
            break

        # print count

    return count

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'OUTPUT.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
