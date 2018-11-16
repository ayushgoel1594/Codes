'''
Created on May 27, 2017

@author: ayush
'''
#currently not solved
def separate_the_numbers(msg):
    p=''
    for i in range(0,len(msg)):
        j=i+1
        while(j<len(msg)):
            p+=msg[j]
            if(int(p)-int(msg[i])!=1):
                j=j+1
            else:
                break;
    
    pass

separate_the_numbers('91011')
    