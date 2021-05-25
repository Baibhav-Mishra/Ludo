# Festival = ['Lumbini', 'Mopin', 'Bihu', 'Chhath', 'Onam', 'Lohri', 'Pongal', 'Garba']
# x = input()
# t = 0
# while t < len(Festival):
#     if Festival[t] != x:
#         t += 1
#     else:
#         print('It is there')
#         break
# else:
#     print('It is not there')
#
# L=[5,3,4,5,6,3,1,2,1]
# freq = {}
# for i in L:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
#
# for key, value in freq.items():
#     print("% d:% d" % (key, value))

# l = [4, 8, 7, 5, 6, 2, 10]
# l.
# l.reverse()
# for i in range(len(l)):
#     l[i] = l[i] * 2
# print(l)

# A=(3,6,7,8,10,12,23,33,16,6,2,1)
# print(A[::3])
# print(A[3::])
# print(len(A[::-3]))

# A=(2,3,4,5,6)
# B=-2,-1,0,1,2
# for i in range(len(A)):
#     print(A[i]+B[i])
# B=B[:2]+(3,)+B[2:]
# for i in B:
#     if i in A:
#         print(i); print(A, B); x=A[1]
# y=B[-1]
# print(x, y)
# print(A,B)
#
# nums=(1,2,7,9,5,7,2,4,5,1,1,2)
# for i in range(1,10):
#     if i in nums:
#         index=nums.index(i)
#         c=nums.count(i)
#         print(i,'appears in nums',c,'times.',end=' ')
#         print('Its first occurance is at index',index)

weight={'A1':8,'A2':7,'B1':6,'B2':5,'C1':4,'C2':3,'D1':2,'D2':1,'E':0}
# for k in weight:
#     print(k,"-",weight[k])
# for k in weight.keys():
#     print(k,"-",weight[k])
# for k in weight.values():
#     print(k, end=' ')
for k,v in weight.items():
    print(k,"-",v)