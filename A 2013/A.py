for _ in range(int(input())):
    n=int(input())
    a=[int(s) for s in input().split()]
    odd=[]
    eve=[]
    for i in a:
        if i%2==0:
            eve.append(i)
        else:
            odd.append(i)
    res=[]
    odd.sort()
    eve.sort()
    eve_ptr=len(eve)-1
    odd_ptr=0
    for i in range(n):
        if a[i]%2==1:
            res.append(str(odd[odd_ptr]))
            odd_ptr+=1
        else:
            res.append(str(eve[eve_ptr]))
            eve_ptr-=1
    print("Case #{}: {}".format(_+1,' '.join(res)))
