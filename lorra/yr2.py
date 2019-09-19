#'ababa;ststs'

# import sys
# m = sys.stdin.readline()
m=input()
x = m.split(";")[0]
y = m.split(";")[1]
# print x,y
if len(x)!= len(y):
    print False
else:
    print [x.index(i) for i in x] == [y.index(i) for i in y]
    # print [*map(x.index, x)] == [*map(y.index, y)]

# else:
#     s2t = {}
#     mapped_t = set()
#     f = 0
#     for i in range(len(x)):
#         if x[i] in s2t:
#             if s2t[x[i]] != y[i]:
#                 print False
#                 f = 1
#                 break
#         else:
#             if y[i] in mapped_t:
#                 print False
#                 f = 1
#                 break
#             mapped_t.add(y[i])
#             s2t[x[i]] = y[i]
#     if not f:
#         print True
