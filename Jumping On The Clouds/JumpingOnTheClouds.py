#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'OUTPUT.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
