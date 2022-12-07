for _ in range(int(input())):
    I = input()
    P = input()
    
    ptr_i=0
    ptr_p=0
    flg_check=0
    for i in range(len(P)):
        if ptr_i==len(I):
            flg_check=1
            break
        if I[ptr_i]==P[i]:
            ptr_i+=1
        # print(ptr_i,i)
    # print(ptr_i,len(I))
    if ptr_i==len(I):
        flg_check=1
    if flg_check==1:
        print("Case #{}: {}".format(_+1,len(P)-len(I)))
    else:
        print("Case #{}: {}".format(_+1,"IMPOSSIBLE"))
