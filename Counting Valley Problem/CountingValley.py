import math
import os
import random
import re
import sys
from __builtin__ import str

# Complete the countingValleys function below.
def countingValleys(n, s):

    pass
if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'OUTPUT.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()