#!/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    i = 0
    x = 0
    count = 0
    s = s.lower()
    inlen = len(s)

    #check the amount of a in the parent string
    while i < len(s):
        if s[i]=='a':
            count = count+1
            i=i+1
        else:
            i=i+1

    #calculate repetition
    rep = n/inlen
    count = count*rep

    #calculate the excess
    res = n%inlen
    while x < res:
        if s[x]=='a':
            count = count+1
            x=x+1
        else:
            x=x+1


    return count

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'OUTPUT.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
