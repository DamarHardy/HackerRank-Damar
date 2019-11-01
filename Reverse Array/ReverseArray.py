#!/bin/python

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(arr):
    arr.reverse()
    for value in arr:
        print value,
    return arr
if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'OUTPUT.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = reverseArray(arr)

    fptr.write(str(res) + '\n')
    fptr.close()
