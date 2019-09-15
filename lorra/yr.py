import sys
import math
#[[0,1,0],[0,0,1],[1,0,0]]
m = sys.stdin.readline()
l = len(m)
mx=[]
for i in m:
    if i.isdigit():
        mx.append(int(i))
v=int(math.sqrt(len(mx)))
mt=[]
for i in range(v):
    mt.append(mx[i*v:(i+1)*v])

    # temp = []
    # for j in range(v):
    #     temp.append(mx[i*v+j])
    # mt.append(temp)
print(mx,l,mt)