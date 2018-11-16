'''
Created on May 31, 2017

@author: ayush
Sherlock considers a string, , to be valid if either of the following conditions are satisfied:

    All characters in have the same exact frequency (i.e., occur the same number of times). For example, is valid, but is not valid.
    Deleting exactly character from will result in all its characters having the same frequency. For example, and are valid because all their letters will have the same frequency if we remove occurrence of c, but is not valid because we'd need to remove characters.

Given , can you determine if it's valid or not? If it's valid, print YES on a new line; otherwise, print NO instead.

Input Format

A single string denoting .

Constraints

    String consists of lowercase letters only (i.e., [a-z]).

Output Format

Print YES if string is valid; otherwise, print NO instead.

Sample Input 0

aabbcd

Sample Output 0

NO

Explanation 0

We would need to remove two characters from to make it valid, because a and b both have a frequency of and c and d both have a frequency of . This means is invalid because we'd need to remove more than character to make all its letters have the same frequency, so we print NO as our answer.
'''
def sherlock_valid_string(st):
    from collections import Counter

    cnt=Counter(st)
    counter=0 
  
    mx=max(Counter(st).values())
    mn=min(Counter(st).values())
    x=Counter(cnt.values())
    
    p=''
    q=''
    counter1=0
    if(mx==mn):
        print('YES')
        return
    for key,i in cnt.items():
        if i==1:
            counter+=1
            p=key
        if i==mx:
            counter1+=1
            q=key
    if(counter==1):
            st=st.replace(p,'')
            mx=max(Counter(st).values())
            mn=min(Counter(st).values())
            if(mx==mn):
                print('YES')
                return
            else:
                print('NO')
    elif(counter1==1):
            st=st.replace(q,'')
            mx=max(Counter(st).values())
            mn=min(Counter(st).values())
            if(mx==mn):
                print('YES')
                return
            else:
                print('NO')
    else:
        print('NO')
    pass

sherlock_valid_string('hfchdkkbfifgbgebfaahijchgeeeiagkadjfcbekbdaifchkjfejckbiiihegacfbchdihkgbkbddgaefhkdgccjejjaajgijdkd')