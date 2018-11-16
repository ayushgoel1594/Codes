'''
Created on May 27, 2017

@author: ayush
'''
def sos_message(msg):
    o=[]
    counter=0
    while msg:
        o.append(msg[:3])
        msg=msg[3:]
    for i in o:
    
        if i[0]!='S'   :
            counter+=1
        if i[1]!='O':
            counter+=1
        if i[2]!='S':
            counter+=1
    print(counter)

sos_message('SOSPPSSQSSOR')
sos_message('SOSSOT')