#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    l=len(s)
    r=l**0.5
    c=math.ceil(r)
    r=math.floor(r)
    if(c*r<l):
        r=c
    print(c,r)
    a=[]
    k=0
    for i in range(r):
        a.append([])
        for j in range(c):
            if(k<l):
                a[i].append(s[k])
                k+=1
            else:
                a[i].append('')
    print(a)
    result=""
    k=0
    for i in range(c):
        for j in range(r):
            if(k<l):
                result+=a[j][i]
        result+=" "
    return(result.strip())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
