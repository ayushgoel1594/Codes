'''
Created on May 28, 2017

@author: ayush
'''
def palindrome_index(st):
    if(st==st[::-1]):
        print(-1)
        return
    loc=0
    st1=st
    for i in range(0,len(st)):
        st=st1
        st=st[0:i]+st[i+1:]
        if(st==st[::-1]):
            loc=i
            break
    print(loc)   
    
palindrome_index('wcwwc')