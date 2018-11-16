'''
Created on May 31, 2017

@author: ayush
'''
def game_of_thrones(msg):
    from collections import Counter
    cnt=Counter(msg)
    counter=0
    counter1=0
    for i in cnt.values():
        if i%2==0:
            counter+=1
        else:
            counter1+=1
    if(counter1==1 and len(msg)%2!=0):
        print('YES')
    elif(counter1==0 and len(msg)%2==0):
        print('YES')
    else:
        print('NO')


game_of_thrones('cdcdcdcdeeeef')