from itertools import product

def rem(a,Np,p): return a % (p**Np)

def in_C(s, N, p):
    # condition 1
    if sum(s) > p**N - 2: return False
    s1,s2,s3 = s
    if not (abs(s2-s3) <= s1 <= s2+s3): return False
    # condition 2
    for Nq in range(1, N):
        ok = False
        for choice in product([0,1], repeat=3):
            t = []
            for i in range(3):
                r = s[i] % (p**Nq)
                t.append(r if choice[i]==0 else p**Nq - 1 - r)
            if sum(t) <= p**Nq - 2 and abs(t[1]-t[2]) <= t[0] <= t[1]+t[2]:
                ok = True; break
        if not ok: return False
    return True

def countC(N,p):
    M = p**N
    return sum(1 for s in product(range(M), repeat=3) if in_C(s,N,p))

# my old lambda-formulation
def count_lambda(N,p):
    M=p**N
    lams=[l for l in range(1,M) if l%2==1 and l%p!=0]
    c=0
    for a,b,d in product(lams,repeat=3):
        if a+b+d < 2*M and a<b+d and b<a+d and d<a+b: c+=1
    return c

for p in [3,5,7,11,13]:
    print("p=%d  N=1: #C=%d  #lambda=%d  p(p^2-1)/24=%d"%(p,countC(1,p),count_lambda(1,p),p*(p*p-1)//24))
for p in [3,5,7]:
    print("p=%d  N=2: #C=%d  #lambda=%d"%(p,countC(2,p),count_lambda(2,p)))
# check nesting C_N subset C_{N+1}
for p in [3,5]:
    bad=[s for s in product(range(p),repeat=3) if in_C(s,1,p) and not in_C(s,2,p)]
    print("p=%d  C_1 not in C_2:"%p, bad)
for p in [3,5]:
    bad=[s for s in product(range(p**2),repeat=3) if in_C(s,2,p) and not in_C(s,3,p)]
    print("p=%d  C_2 not in C_3:"%p, len(bad))

print("\n--- table of #C_N ---")
for p in [3,5,7,11,13]:
    row=[]
    for N in [1,2]:
        row.append(countC(N,p))
    print("p=%2d : %s"%(p,row))
print("p=3, N=3 :", countC(3,3))
