import math
import os
import random
import re
import sys
from __builtin__ import str

# Complete the countingValleys function below.
def countingValleys(n, s):
    gunung = False
    valley = False
    i = 0
    count = 0
    gunungcount=0
    valleycount=0
    # print n
    # print s
    while i < n:
        # print (s[i])
        if s[i]=='U':
            count = count+1
        elif s[i]=='D':
            count = count-1

        if count != 0 and gunung==False and valley==False:
            if s[i] == 'U':
                gunung = True
            elif s[i]=='D':
                valley = True
        elif count == 0:
            if gunung:
                gunungcount = gunungcount+1
                gunung = False
            elif valley:
                valleycount = valleycount+1
                valley = False
        i = i+1
    return valleycount

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'OUTPUT.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()