for _ in range(int(input())):
    n=[int(i) for i in input()]
    s = sum(n)
    num_add = 9-s%9
    if num_add==9:
        # num_add=0
        s=''
        s+=str(n[0])+'0'
        for i in range(1,len(n)):
            s+=str(n[i])
        # s+='0'
        print("Case #{}: {}".format(_+1,s))
        continue
    res=''
    i=0
    flg_added=0
    while(i<len(n)):
        if num_add<n[i]:
            res+=str(num_add)
            flg_added=1
            while(i<len(n)):
                res+=str(n[i])
                i+=1
            break
        else:
            res+=str(n[i])
        i+=1
    if flg_added==0:
        res+=str(num_add)
    print("Case #{}: {}".format(_+1,res))
    
    