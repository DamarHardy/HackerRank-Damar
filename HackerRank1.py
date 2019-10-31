import math
import os
import random
import re
import sys


#Complete the SockMerchant Function below.
from __builtin__ import str


def sockMerchant(n, ar):
    count = 0
    cond = True
    prevlen = n
    new = 0
    while cond:
        if prevlen == new:
            cond = False

        for i in range(0,len(ar),1):
            for x in range(i+1,len(ar),1):
                prevlen = len(ar)
                print (ar[i],ar[x])
                print prevlen
                if ar[i]==ar[x]:
                    print ("true")
                    count = count + 1
                    del ar[x]
                    del ar[i]
                    new = len(ar)
                    print ar
                    print new
                    break
                else:
                    continue
            break

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