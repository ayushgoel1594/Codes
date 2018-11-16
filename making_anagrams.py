'''
Created on May 31, 2017

@author: ayush
'''
def making_anagrams(st1,st2):
    from collections import Counter
    c1=Counter(st1)
    c2=Counter(st2)
    
    diff=c1-c2
    diff1=c2-c1
    
    final_diff=sum(diff.values())+sum(diff1.values())
    return final_diff

c=making_anagrams('cde', 'abc')
print(c)