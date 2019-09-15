m=input('')
#"A={1,3,5,10},B={2,4,6,11},R=1"
A_=m.split('B')[0].split('=')[1].split("{")[1].split("}")[0]
B_=m.split('B')[1].split('R')[0].split('=')[1].split("{")[1].split("}")[0]
R_=m.split('R')[1].split('=')[1]
a,b,r=[],[],0
# print(len(A_),A_,B_,R_)
for i in A_.split(","):    a.append(int(i))
for i in B_.split(","):    b.append(int(i))
# print(a, b, r)
r=int(R_)
out,und =[], []
def parse(a,b,r):
    s=''
    for i in range(len(a)):
        for j in range(len(b)-1,-1,-1):
            if a[i]<=b[j]:
                if b[j]-a[i]<=r:
                    out.extend([a[i],b[j]])
                    break
            else:     und.append(a[i])
    for i in und:
        for j in b:
            if i <= j:
                out.extend([i,j])
                break
    for i in range(0,len(out),2):        s= s+'('+str(out[i])+','+str(out[i+1])+")"
    return s
out = parse(a,b,r)
print(out)



