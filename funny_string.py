'''
Created on May 27, 2017

@author: ayush

Suppose you have a String, , of length that is indexed from to . You also have some String, , that is the reverse of String . is funny if the condition is true for every character from to .

Note: For some String , denotes the ASCII value of the -indexed character in . The absolute value of an integer, , is written as .

Input Format

The first line contains an integer, (the number of test cases).
Each line of the subsequent lines contain a string, .

Constraints

Output Format

For each String (where ), print whether it is or on a new line.

Sample Input

2
acxz
bcxz

Sample Output

Funny
Not Funny

Explanation

Test Case 0:



As each comparison is equal, we print .

Test Case 1:
, but
At this point, we stop evaluating (as ) and print . 
'''
def funny_string(st):
    st_reverse=st[::-1]
    for i in range(0,len(st)-1):
        if(abs(ord(st[i])-ord(st[i+1]))==abs(ord(st_reverse[i])-ord(st_reverse[i+1]))):
            flag=1
        else:
            flag=0
            break;
    if(flag==1):
        print('Funny')
    else:
        print('Not Funny')

    pass

funny_string('acxz')
funny_string('bcxz')