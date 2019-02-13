#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jmp=0
    start = c.index(0)
    cnt=start
    print(start)
    while cnt<len(c):
        print("cnt",cnt)
        if cnt+2<len(c):
            if(c[cnt+2]==0):
                cnt=cnt+2
                jmp+=1
                print("jump1",jmp)
            else:
                cnt=cnt+1
                jmp+=1
                print("jump2",jmp)
        else:
            if(cnt+1==len(c)-1):
                cnt+=1
                jmp+=1
            else:
                cnt+=1
        #print("jump3",jmp)
    return(jmp)
    #    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
