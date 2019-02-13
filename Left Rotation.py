#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    if(d>n):
        d=d%n
    #print(d)
    i=0
    while(i<d):
        temp=a[0]
        del a[0]
        a.append(temp)
        i+=1
    print(*a)