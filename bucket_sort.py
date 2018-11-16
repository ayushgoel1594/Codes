'''
Created on May 31, 2017

@author: ayush
'''
def bucket_sort(lst):
    
    bucket={}
    for i in lst:
        length=i*10%10
        if length not in bucket:
            bucket[length]=[]
        bucket[length].append(i)
        
    for key in sorted(bucket):
        for value in sorted(bucket[key]):
            print(value)
    pass

bucket_sort([0.12,0.72,0.21,0.78,0.94,0.26,0.39])