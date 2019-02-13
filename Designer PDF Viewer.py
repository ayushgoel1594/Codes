#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    dic={}
    j=97
    for i in h:
        dic[chr(j)]=i
        j+=1
    l=len(word)
    c=0
    for i in word:
        if(dic[i]>c):
            c=dic[i]

    return l*c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
