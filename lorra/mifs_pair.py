import os
dp = 'MIFS'
at = open('at_pairs_428.txt', 'w+')
bt = open('bt_pairs_428.txt', 'w+')
ab = open('ab_pairs_428.txt', 'w+')
abt = open('abt_pairs_321.txt', 'w+')
all = open('all_pairs_856_749.txt', 'w')
pl=os.listdir(dp)
pl.sort()
a,b,t=[],[],[]
m,n,x,y = 0, 0, 0, 0
for i in range(0,len(pl),6):
    l = pl[i:i+6]
    a = list(filter(lambda x: 'A' in x, l))
    b = list(filter(lambda x: 'B' in x, l))
    t = list(filter(lambda x: 'T' in x, l))
    for j in range(len(a)):
        for k in range(len(t)):
            if m: at.writelines(['\n',a[j],'   ', t[k] ,'   ','0'])
            else:
                at.writelines([a[j], '   ', t[k], '   ', '0'])
                m+=1
    for j in range(len(a)):
        for k in range(len(b)):
            if n : ab.writelines(['\n', a[j], '   ', b[k], '   ', '1'])
            else :
                ab.writelines([a[j], '   ', b[k], '   ', '1'])
                n+=1
    for j in range(len(t)):
        for k in range(len(b)):
            if x: bt.writelines(['\n', t[j], '   ', b[k], '   ', '0'])
            else:
                bt.writelines([t[j], '   ', b[k], '   ', '0'])
                x+=1
    for n in [a,b,t]:
        if y:
            abt.writelines(['\n', n[0], '   ', n[1], '   ', '1'])
        else:
            abt.writelines([n[0], '   ', n[1], '   ', '1'])
            y+=1
at.close()
bt.close()
ab.close()
abt.close()
at = open('at_pairs_428.txt', 'r')
bt = open('bt_pairs_428.txt', 'r')
ab = open('ab_pairs_428.txt', 'r')
abt = open('abt_pairs_321.txt', 'r')
for tx in [at,bt,ab,abt]:
    for line in tx:
        all.write(line)
    all.write('\n')

at.close()
bt.close()
ab.close()
abt.close()
all.close()

