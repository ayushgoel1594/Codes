n, inputs = [int(n) for n in input().split(" ")]
lst = [0]*(n+1)
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]
    lst[x-1] += incr
    if((y)<=len(lst)):
        lst[y] -= incr;
    #print(list)
m = x = 0
for i in lst:
   x=x+i;
   if(m<x):
        m=x;
print(m)