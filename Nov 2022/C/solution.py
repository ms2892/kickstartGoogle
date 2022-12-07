def findParent(dsu,indx):
    if not dsu[indx]:
        return [indx]
    else:
        res=[]
        for i in dsu[indx]:
            res+=findParent(dsu,i)
        return res

from collections import defaultdict

for _ in range(int(input())):
    N= int(input())
    A = [int(i) for i in input().split()]
    dsu = defaultdict(list)
    vis = [-1]*N
    for i in range(N-1):
        L,R = [int(i) for i in input().split()]
        if A[L-1]>A[R-1]:
            dsu[R-1].append(L-1)
        elif A[L-1]<A[R-1]:
            dsu[L-1].append(R-1)
    cnt=0
    max_n=[0]*N
    # print(dsu)
    
    for i in range(N):
#        if vis[i]==-1:
        max_n[i]=findParent(dsu,i)
    # print(max_n)
    dct={}
    for i in max_n:
        for j in i:
            if j in dct.keys():
                dct[j]+=1
            else:
                dct[j]=1
    mxm=0
    for i in dct.keys():
        mxm=max(dct[i],mxm)
    print("Case #{}: {}".format(_+1,mxm))