import math
import os
import random
import re
import sys
from __builtin__ import str

# Complete the countingValleys function below.
def countingValleys(n, s):
    count = 0
    i = 0
    s.lower().split()
    while i < n:
        if s[i]==u:
            count = count+1
        elif s[i]==d:
            count = count-1
    pass
if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'OUTPUT.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()