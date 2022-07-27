import SM3
import random
    
def Coprime(a, b):
    while a != 0:
        a, b = b % a, a
    if b != 1 and b != -1:
        return 1
    return 0

def gcd(a, m):
    if Coprime(a, m):
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    if u1 > 0:
        return u1 % m
    else:
        return (u1 + m) % m

def T_add(P,Q):
    if (P == 0):
        return Q
    if (Q == 0):
        return P
    if P == Q:
        aaa=(3*pow(P[0],2) + a)
        bbb=gcd(2*P[1],p)
        k=(aaa*bbb)%p 
    else:
        aaa=(P[1]-Q[1])
        bbb=(P[0]-Q[0])
        k=(aaa*gcd(bbb,p))%p 

    Rx=(pow(k,2)-P[0] - Q[0]) %p
    Ry=(k*(P[0]-Rx) - P[1])%p
    R=[Rx,Ry]
    return R



def T_mul(n, l):
    if n == 0:
        return 0
    if n == 1:
        return l
    t = l
    while (n >= 2):
        t = T_add(t, l)
        n = n - 1
    return t

a = 2
b = 2       
p = 17 #椭圆曲线参数，y^2=x^3+2x+2
G = [5, 1]
n = 19
message='Satoshi'
e=hash(message)
d = 7
Pubk = T_mul(d, G)
ID='1234567812345678'
ZZ=str(len(ID))+ID+str(a)+str(b)+str(G[0])+str(G[1])+str(Pubk[0])+str(Pubk[1])
Za=SM3.SM3_test(ZZ)

def Sign(M,k):
    global n,G,d,Za
    M_=Za+M
    e = SM3.SM3_test(M_)
    R=T_mul(k,G)
    r=(R[0]+int(e,16)) % n
    e=hash(message)
    s=(gcd(1+d, n) * (k - d * r)) % n
    return r,s

def Verify(r,s):
    global Pubk,n,G,message,Za
    M_=Za+message
    e = SM3.SM3_test(M_)
    t=(r+s)%n
    S=T_add(T_mul(s,G),T_mul(t,Pubk))
    R=(int(e,16)+S[0])%n
    if(R==r):
        return True
    else: return False

k=int(SM3.SM3_test(str(d)+SM3.SM3_test(Za+message)+'SM2'),16)
k=k%n
r,s=Sign(message,k)
print("原始签名为:",r,s)
print("验证：")
if(Verify(r,s)):
    print('True')
else: print('False')



