words = ['','double ','triple ','quadruple ','quintuple ','sextuple ','septuple ','octuple ','nonuple ','decuple ']
num_words = ['zero','one','two','three','four','five','six','seven','eight','nine']

for _ in range(int(input())):
    nums, splits=[s for s in input().split()]
    splits = [int(s) for s in splits.split('-')]
    ptr_nums=0
    ptr_splits=0
    res=''
    prev_lim=0
    while(ptr_nums<len(nums)):
        k=ptr_nums
        lim=splits[ptr_splits]
        # print(prev_lim,lim)
        while(k+1<len(nums) and k+1<prev_lim+lim):
            # print(k)
            if k-ptr_nums+1==10:
                break
            if nums[k]==nums[k+1]:
                k+=1
            else:
                break
        if k==prev_lim+lim:
            # print("----")
            prev_lim+=lim
            ptr_splits+=1
            continue
        
        cnt = k-ptr_nums+1
        # print(words[cnt-1] + num_words[int(nums[ptr_nums])]+' ')
        res+=words[cnt-1] + num_words[int(nums[ptr_nums])]+' '
        # print(k)
        ptr_nums=k+1
        
        
    print("Case #{}: {}".format(_+1,res))