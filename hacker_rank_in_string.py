'''
Created on May 27, 2017

@author: ayush
'''
def hacker_rank_in_string(st):
    fixed_string='hackerrank'
    flag=0
    
    j = 0;
    for i in range(0,len(st)) :
        if (j < len(fixed_string) and st[i] == fixed_string[j]):
            j+=1;
            
    if(j==len(fixed_string)):
        print('YES')
    else:
        print('NO')        
hacker_rank_in_string('knarrekcah')
hacker_rank_in_string('hackerrank')
hacker_rank_in_string('hackerone')
hacker_rank_in_string('abcdefghijklmnopqrstuvwxyz')
hacker_rank_in_string('rhackerank')
hacker_rank_in_string('ahankerck')
hacker_rank_in_string('hacakaeararanaka')
hacker_rank_in_string('hhhhaaaaackkkkerrrrrrrrank')
hacker_rank_in_string('crackerhackerknar')
hacker_rank_in_string('hhhackkerbanker')
