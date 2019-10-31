import math
import os
import random
import re
import sys


#Complete the SockMerchant Function below.
from __builtin__ import str


def sockMerchant(n, ar):
    ar.sort()
    print ar
    return count

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'OUTPUT.txt'
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    n = int(raw_input())
    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n,ar)
    # print(result)
    fptr.write(str(result)+'\n')

    fptr.close()