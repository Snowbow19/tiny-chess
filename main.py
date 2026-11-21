import json,os,urllib.request as u
V=(0,100,320,330,500,900,0)
W=']]»»iv]j]_]R^f]]"9/]<j<u<u<j/]"9FQR]R^R^RiSiR]FQ]]^i]]]]]]]]]]]]FRR]R]]]]]R]R]FR8,8,8,8,D8PEu]vh'
M=10**5;B=[0]*128;C=0;E=-1;S=0;w=1;K=[0,0];D=[];N=[0];BG=48000;J=[0]*128
N0=(14,18,31,33,-14,-18,-31,-33);D0=(15,17,-15,-17);R0=(1,-1,16,-16);DO=((),(),N0,D0,R0,D0+R0,R0+D0);CM={0:2,7:1,112:8,119:4,4:3,116:12}
def P(p,q):t=abs(p);r=q>>4;i=r if p<0 else 7-r;f=q&7;f=min(f,7-f);j=32*t+i*4+f-32;v=ord(W[j//2])-33;v-=34*(v>93);return(V[t]+(divmod(v,11)[j&1]-5)*10)*(p//abs(p))
def A(s,y):
 if any(not(s+d)&136 and B[s+d]==2*y-1 for d in((-15,-17)if y else(15,17))):return 1
 for j in(2,6,3,4):
  v=(j,5)if 2<j<5 else(j,)
  for d in DO[j]:
   q=s+d
   while not q&136:
    p=B[q]
    if p and(p>0)==y and abs(p)in v:return 1
    if p or j%4==2:break
    q+=d
 return 0
def G(o):
 r=[]
 for f,p in enumerate(B):
  if f&136 or not p or(p>0)^w:continue
  t=abs(p)
  if t==1:
   u=32*w-16
   for d,k in((u,0),(2*u,0),(u-1,1),(u+1,1)):
    q=f+d
    if q&136:continue
    v=B[q]
    if d==2*u and((f>>4)!=6-5*w or B[f+u]):continue
    if v and((v>0)==w or not k)or not v and k and q!=E:continue
    if(q>>4)==7*w:r+=[f|(q<<7)|(pr<<14)for pr in(5,4,3,2)]
    elif k or not o:r.append(f|(q<<7))
  else:
   for d in DO[t]:
    q=f+d
    while not q&136:
     v=B[q]
     if v and(v>0)^w or not(o or v):r.append(f|(q<<7))
     if v or t in(2,6):break
     q+=d
 if not o:
  for b in(1,2,4,8):
   v=b>2;k=4+112*v;s=b%3==1;e=(k+1,k+2)if s else(k-1,k-2,k-3);rk=k+3 if s else k-4
   if C&b and v!=w and B[rk]==4-8*v and not any(B[x]for x in e)and not any(A(x,v)for x in(k,e[0],e[1])):r.append(k|(e[1]<<7))
 return r
def mk(m):
 global C,E,S,w;D.append((B[:],C,E,S,K[:]));f=m&127;t=m>>7&127;pr=m>>14;p=B[f];v=B[t]
 ep=p*p==1 and t==E and not v;cs=t+16-32*(p>0)if ep else t;vc=B[cs];n=pr*(p//abs(p))if pr else p
 S+=P(n,t)-P(p,f)
 if vc:S-=P(vc,cs)
 if p*p==36:K[p<0]=t
 if p*p==36 and abs(t-f)==2:
  d=t<f;rf=t+1-3*d;rt=t-1+2*d;r=B[rf];B[rf]=0;B[rt]=r;S+=P(r,rt)-P(r,rf)
 C&=~CM.get(f,0)&~CM.get(t,0);E=(f+t)//2 if p*p==1 and abs(t-f)==32 else-1;B[f]=0
 if vc:B[cs]=0
 B[t]=n;w=not w
def un():
 global C,E,S,w;x=D.pop();B[:]=x[0];C,E,S=x[1:4];w=not w;K[:]=x[4]
def L(o=0):return[m for m in G(o)if(mk(m),A(K[w],w)^1,un())[1]]
def O(ms,tm,p):ms.sort(key=lambda m:(m!=tm,-V[abs(B[m>>7&127])]*10+abs(B[m&127])-V[m>>14],m!=J[p]));return ms
def sr(d,a,b,p):
 N[0]+=1
 if N[0]>=BG:1/0
 ic=A(K[~w],not w);d+=ic and 0<d<3
 if d>0:
  ms=L()
  if not ms:return ic*(-M+p)
 else:
  st=10+S*(w*2-1)
  if d<-16:return st
  if ic:
   ms=L()
   if not ms:return-M+p
  else:
   if st>=b:return st
   a=max(a,st);ms=[m for m in L(1)if st+V[abs(B[m>>7&127])]+V[m>>14]+200>=a]
 for m in O(ms,0,p):
  mk(m);s=-sr(d-1,-b,-a,p+1);un();a=max(a,s)
  if a>=b:J[p]=m if not B[m>>7&127]else J[p];return a
 return a
def pf(s):
 global B,C,E,S,w,K;a=s.split();B=[0]*128;K=[0,0];S=0;q=112
 for ch in a[0]:
  if ch=='/':q-=24
  elif ch.isdigit():q+=int(ch)
  else:
   p="PNBRQK".find(ch.upper())+1
   if'a'<=ch:p=-p
   B[q]=p;S+=P(p,q)
   if p*p==36:K[p<0]=q
   q+=1
 w=a[1]=='w';C=sum(1<<i for i,c in enumerate('KQkq')if c in a[2]);E=-1 if a[3]=='-'else sq(a[3]);D.clear()
def sq(a):return 16*int(a[1])+ord(a[0])-113
def pu(s):return sq(s[:2])|(sq(s[2:4])<<7)|(("nbrq".find(s[4])+2)<<14 if s[4:]else 0)
def uc(m):f=m&127;t=m>>7&127;return"%c%d%c%d"%(f%8+97,f//16+1,t%8+97,t//16+1)+"  nbrq"[m>>14].strip()
def rt(legal):
 ms=[pu(x)for x in legal];N[0]=0;bm=ms[0]
 for d in range(9):
  try:
   om=O(ms,bm,0);a=-M
   for m in om:
    mk(m);s=-sr(d,-M,-a,1);un()
    if s>a:a=s;bm=m
  except:break
 return[bm]+[x for x in ms if x-bm]
def post(p,b):
 try:
  r=u.urlopen(os.getenv("MAKEFUN_ENV_URL")+p,json.dumps(b).encode());return json.load(r)
 except:return 0
while 1:
 g=post("/game",{})
 g or exit(1)
 if"done"in g["status"]:break
 while "y"in g["status"]:
  pf(g["fen"]);legal=g["legal_moves"]
  try:rk=rt(legal)
  except:rk=list(map(pu,legal))
  for mv in rk:
   r=post("/move",dict(game=g["game"],move=uc(mv)))
   if r:g=r;break
  else:exit(1)
