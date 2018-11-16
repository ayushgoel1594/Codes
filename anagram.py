'''
Created on May 31, 2017

@author: ayush
'''
from collections import Counter
def anagram(st):
   
    if(len(st)%2!=0):
        return -1
    
    s1=Counter(st[0:len(st)//2])
   
    s2 = Counter(st[len(st)//2:])
    diff =s1-s2
    #print(sum(diff.values()))
   
    return sum(diff.values())
    pass

ct=anagram('xaxbcxxx')
print(ct)