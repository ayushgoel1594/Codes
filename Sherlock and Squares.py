#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):

    c=a**(0.5)
    d=b**(0.5)
    num=int(math.floor(d) - math.ceil(c)+1)
    return(num)
    # for i in range(a,b+1):
    #     temp=((i**(0.5))*10)%10
    #     if(temp==0):
    #         cnt+=1
    #     #print(temp)
    # return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
