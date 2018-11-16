'''
Created on May 26, 2017

@author: ayush

Steve has a string, , consisting of lowercase English alphabetic letters. In one operation, he can delete any pair of adjacent letters with same value. For example, string "aabcc" would become either "aab" or "bcc" after operation.

Steve wants to reduce as much as possible. To do this, he will repeat the above operation as many times as it can be performed. Help Steve out by finding and printing 's non-reducible form!

Note: If the final string is empty, print Empty String .

Input Format

A single string, .

Constraints

Output Format

If the final string is empty, print Empty String; otherwise, print the final non-reducible string.

Sample Input 0

aaabccddd

Sample Output 0

abd

Sample Case 0

Steve can perform the following sequence of operations to get the final string:

    aaabccddd → abccddd
    abccddd → abddd
    abddd → abd

Thus, we print abd.

Sample Input 1

baab

Sample Output 1

Empty String

Explanation 1

Steve can perform the following sequence of operations to get the final string:

    baab → bb
    bb → Empty String

Thus, we print Empty String.

Sample Input 2

aa

Sample Output 2

Empty String

Explanation 2

Steve can perform the following sequence of operations to get the final string:

    aa → Empty String

Thus, we print Empty String.
'''
def super_reduced_string(st):
    i=0
    while(i<len(st)-1):
        f=0
        if(st[i]==st[i+1]):
            #st=st.replace(st[i],'',2)
            st=st[0:i]+st[i+2:]
            f=1
            
        if(f==1):
            i=0
        else:
            i=i+1
            
    if(st==''):
        print('Empty String')
    else:        
        print(st)
super_reduced_string('abccddd')
super_reduced_string('baab')
super_reduced_string('aaabccddd')
