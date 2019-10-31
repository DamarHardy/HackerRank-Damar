import math
import os
import random
import re
import sys


#Complete the SockMerchant Function below.
from __builtin__ import str


def sockMerchant(n, ar):
    ar.sort()
    i = 0
    count = 0
    while i < n:
        if i+1 < n:
            if ar[i]==ar[i+1] and (i+1)<n:
                count = count +1
                i=i+2
            else:
                i=i+1
        else:
            break
    return count

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'OUTPUT.txt'
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    n = int(raw_input())
    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n,ar)
    print(result)
    fptr.write(str(result)+'\n')

    fptr.close()