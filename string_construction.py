'''
Created on May 31, 2017

@author: ayush
'''

def string_construction(st):
    p=''
    counter=0
    for i in st:
        if i not in p:
            p+=i
            counter+=1
    print(counter)
    pass

string_construction('abcd')
string_construction('abab')
