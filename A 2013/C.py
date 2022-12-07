def get_p_q(n):
    ptr=1
    p=1
    q=1
    while(ptr<len(n)):
        if n[ptr]=='0':
            p = p
            q = p+q
        else:
            p = p+q
            q = q
        ptr+=1
    return p,q

import fractions


def Normalize(p, q):
  r = fractions.Fraction(p, q)
  return r.numerator, r.denominator

def get_n(p,q):
    # n='1'
    n=''
    p, q = Normalize(p, q)
    while(p>1 or q>1):
        if p>q:
            n='1'+n
            p = p-q
        else:
            n='0'+n
            q = q-p
    n='1'+n
    # print(int(n,2),p,q)
    # x=input()
    return int(n,2)

for _ in range(int(input())):
    t = [int(s) for s in input().split()]
    if t[0]==1:
        n=t[1]
        bin_n = str(bin(n))
        bin_n = bin_n[2:]
        # print(n)
        if n==1:
            p=1
            q=1
        else:
            p,q = get_p_q(bin_n)
        print("Case #{}: {} {}".format(_+1,p,q))
    else:
        p=t[1]
        q=t[2]
        print("Case #{}: {}".format(_+1,get_n(p,q)))