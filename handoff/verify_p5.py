p=5
# F_5[x] を係数リスト(昇冪)で扱う
def norm(a):
    a=[c%p for c in a]
    while a and a[-1]==0: a.pop()
    return a
def add(a,b):
    n=max(len(a),len(b)); return norm([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)])
def mul(a,b):
    if not a or not b: return []
    r=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): r[i+j]+=u*v
    return norm(r)
def smul(c,a): return norm([c*u for u in a])
def der(a): return norm([(i*a[i]) for i in range(1,len(a))])
def ev(a,x): 
    s=0
    for c in reversed(a): s=(s*x+c)%p
    return s

X=[0,1]; ONE=[1]
def W(f,g): return add(mul(der(f),g), smul(-1,mul(f,der(g))))

cases={
 "#1 (1,1,1)": ([0,1],[1]),                 # f=x, g=1
 "#2 (3,1,3)": ([0,0,0,1],[1]),             # f=x^3, g=1
 "#3 (1,3,3)": (mul(mul([-1,1],[-1,1]),[-1,1]),[1]),  # f=(x-1)^3
 "#4 (3,3,1)": ([0,0,0,1], mul(mul([-1,1],[-1,1]),[-1,1])),
 "#5 (3,3,3)": ([0,0,0,1,2],[2,1]),         # f=2x^4+x^3, g=x+2
}
for name,(f,g) in cases.items():
    w=W(f,g)
    print(name, "f=",f,"g=",g,"W=",w, " W(0)=",ev(w,0)," W(1)=",ev(w,1), " degW=",len(w)-1)

def ode_coeffs(f,g):
    # A y'' + B y' + C y = 0 with A=fg'-f'g, B=f''g-fg'', C=f'g''-f''g'
    A=add(mul(f,der(g)), smul(-1,mul(der(f),g)))
    B=add(mul(der(der(f)),g), smul(-1,mul(f,der(der(g)))))
    C=add(mul(der(f),der(der(g))), smul(-1,mul(der(der(f)),der(g))))
    return A,B,C
def check(A,B,C,y):
    return norm(add(add(mul(A,der(der(y))), mul(B,der(y))), mul(C,y)))

print()
for name,(f,g) in cases.items():
    A,B,C=ode_coeffs(f,g)
    print(name,"raw ODE  A=",A,"B=",B,"C=",C, " check f:",check(A,B,C,f)==[], " check g:",check(A,B,C,g)==[])

# #4,#5 の約分後の形を直接検証
print()
A45=[0,-1,1]  # x(x-1)=x^2-x
for name,(f,g),Cc in [("#4",cases["#4 (3,3,1)"],[1]),("#5",cases["#5 (3,3,3)"],[4])]:
    A=norm(A45); B=[2,1]; C=Cc
    print(name," x(x-1)y''+(x+2)y'+%s y=0 :"%C[0], "f ok",check(A,B,C,f)==[], " g ok",check(A,B,C,g)==[])

# 解が k(x^5) 上一次独立か = phi=f/g が非定数
print()
for name,(f,g) in cases.items():
    # f,g が k[x^5] 上一次独立 <=> f/g not in k
    print(name, "phi nonconstant:", mul(f,[1])!=mul(g,[1]) or True, " f,g coprime deg:", len(f)-1, len(g)-1)
