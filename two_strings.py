'''
Created on May 31, 2017

@author: ayush
'''

def two_strings(st1,st2):
    flag=0
    for i in st1:
        if i in st2:
            flag=1
            
    if(flag==1):
        print('YES')
    else:
        print('NO')
    pass

two_strings('hello', 'world')