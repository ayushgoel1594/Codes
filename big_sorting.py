'''
Created on May 30, 2017

@author: ayush
'''
from builtins import sorted
def big_sort(unsorted):

    
#     for i in range(0,len(unsorted)):
#         max=i
#         flag=0
#         for j in range(i+1,len(unsorted)):
#             if(len(unsorted[j])>len(unsorted[max])):
#                 max=j
#                 flag=1
#             elif(len(unsorted[j])==len(unsorted[max])):
#                 for k in range(0,len(unsorted[j])):
#                     if(int(unsorted[j][k])>int(unsorted[max][k])):
#                         max=j
#                         flag=1
#                     elif(unsorted[j][k]<unsorted[max][k]):
#                         break
#                     else:
#                         continue
#             else:
#                 continue
#         if(flag==1):
#             unsorted[i],unsorted[max]=unsorted[max],unsorted[i]
#     print(unsorted.reverse())            
    #using the bucket sort method
    bucket={}
    for i in unsorted:
        length=len(i)
        if not length in bucket:
            bucket[length]=[]
    
        bucket[length].append(i)
    for key in sorted(bucket):
        for value in sorted(bucket[key]):
            print(value)
            pass    
    #using the zip list
    us=[]
    lengths=[]
    for j in unsorted:
        us.append(j)
        lengths.append(len(j))
    biglist=zip(lengths,us)
    print(sorted(biglist))
    for k in sorted(biglist):
        print(k[1]) 
    
big_sort(['31415926535897932384626433832795','1','3','10','3','5'])