import json,os,urllib.request as u
V=(0,100,320,330,500,900,0)
W='kkkkuuuummoqllmpkkkoljiklmmgkkkkaceecgkkekmnelnoeknoelmncgklaceegiiiikkkiklmillmikmmimmmilkkgiiikkkklmmmjkkkjkkkjkkkjkkkjkkkkkklgiijikkkiklljkllkkllillliklkgiijeccaeccaeccaeccageecigggookkoqmk'
M=10**5;B=[0]*128;C=0;E=-1;S=0;w=1;K=[0,0];D=[];N=[0];BG=32000
N0=(14,18,31,33,-14,-18,-31,-33);D0=(15,17,-15,-17);R0=(1,-1,16,-16);DO=((),(),N0,D0,R0,D0+R0,R0+D0);CM={0:2,7:1,112:8,119:4}
def P(p,q):t=abs(p);r=q>>4;i=r if p<0 else 7-r;f=q&7;f=7-f if f>3 else f;return(V[t]+(ord(W[(t-1)*32+i*4+f])-107)*5)*((p>0)*2-1)
def A(s,y):
 if any(not(s+d)&136 and B[s+d]==2*y-1 for d in((-15,-17)if y else(15,17))):return 1
 for j,v in((2,(2,)),(6,(6,)),(3,(3,5)),(4,(4,5))):
  for d in DO[j]:
   q=s+d
   while not q&136:
    p=B[q]
    if p and(p>0)==y and abs(p)in v:return 1
    if p or j in(2,6):break
    q+=d
 return 0
def G(o):
 r=[]
 for f,p in enumerate(B):
  if f&136 or not p or(p>0)!=w:continue
  t=abs(p)
  if t==1:
   u=32*w-16
   for d,k in((u,0),(2*u,0),(u-1,1),(u+1,1)):
    q=f+d
    if q&136:continue
    v=B[q]
    if d==2*u and((f>>4)!=6-5*w or B[f+u]):continue
    if v and((v>0)==w or not k)or(k and not v and q!=E):continue
    if(q>>4)==7*w:r+=[f|(q<<7)|(pr<<14)for pr in(5,4,3,2)]
    elif k or not o:r.append(f|(q<<7))
  else:
   for d in DO[t]:
    q=f+d
    while not q&136:
     v=B[q]
     if v and(v>0)!=w or not(o or v):r.append(f|(q<<7))
     if v or t in(2,6):break
     q+=d
 if not o:
  for b,k,e,rk,v in((1,4,(5,6),7,0),(2,4,(3,2,1),0,0),(4,116,(117,118),119,1),(8,116,(115,114,113),112,1)):
   if C&b and v!=w and B[rk]==4-8*v and not any(B[x]for x in e)and not any(A(x,v)for x in(k,e[0],e[1])):r.append(k|(e[1]<<7))
 return r
def mk(m):
 global C,E,S,w;D.append((B[:],C,E,S,K[:],w));f=m&127;t=(m>>7)&127;pr=m>>14;p=B[f];v=B[t]
 ep=abs(p)==1 and t==E and not v;cs=t+16-32*(p>0)if ep else t;vc=B[cs]if ep else v;n=pr*((p>0)*2-1)if pr else p
 S-=P(p,f);S+=P(n,t)
 if vc:S-=P(vc,cs)
 if abs(p)==6:K[p<0]=t
 if abs(p)==6 and abs(t-f)==2:
  rf,rt=(t+1,t-1)if t>f else(t-2,t+1);r=B[rf];B[rf]=0;B[rt]=r;S+=P(r,rt)-P(r,rf)
 C&=((12 if p>0 else 3)if abs(p)==6 else-1)&~CM.get(f,0)&~CM.get(t,0);E=(f+t)//2 if abs(p)==1 and abs(t-f)==32 else-1;B[f]=0
 if vc:B[cs]=0
 B[t]=n;w=not w
def un():
 global C,E,S,w;x=D.pop();B[:]=x[0];C,E,S,w=x[1],x[2],x[3],x[5];K[:]=x[4]
def L(o=0):return[m for m in G(o)if(mk(m),not A(K[w],w),un())[1]]
def O(ms,tm):ms.sort(key=lambda m:(m!=tm,not B[(m>>7)&127]));return ms
def sr(d,a,b,p):
 N[0]+=1
 if N[0]>=BG:1/0
 ic=A(K[1-w],not w)
 if d>0:
  ms=L()
  if not ms:return ic*(-M+p)
 else:
  st=10+(S if w else-S)
  if ic:
   ms=L()
   if not ms:return-M+p
  else:
   if st>=b:return b
   a=max(a,st);ms=L(1)
 for m in O(ms,0):
  mk(m);s=-sr(d-1,-b,-a,p+1);un();a=max(a,s)
  if a>=b:return a
 return a
def pf(s):
 global B,C,E,S,w,K;a=s.split();B=[0]*128;K=[0,0];S=0;q=112
 for ch in a[0]:
  if ch=='/':q-=24
  elif ch.isdigit():q+=int(ch)
  else:
   p="PNBRQKpnbrqk".find(ch)%6+1
   if'a'<=ch:p=-p
   B[q]=p;S+=P(p,q)
   if abs(p)==6:K[p<0]=q
   q+=1
 w=a[1]=='w';C=sum(1<<i for i,c in enumerate('KQkq')if c in a[2]);E=-1 if a[3]=='-'else sq(a[3]);D.clear()
def sq(a):return 16*int(a[1])+ord(a[0])-113
def pu(s):return sq(s[:2])|(sq(s[2:4])<<7)|(("nbrq".find(s[4])+2)<<14 if s[4:]else 0)
def uc(m):f=m&127;t=(m>>7)&127;return"%c%d%c%d"%(f%8+97,f//16+1,t%8+97,t//16+1)+("  nbrq"[m>>14]if m>>14 else"")
def rt(legal):
 ms=[pu(x)for x in legal];N[0]=0;bm=ms[0]
 for d in range(64):
  try:
   om=O(ms,bm);a=-M
   for m in om:
    mk(m);s=-sr(d,-M,-a,1);un()
    if s>a:a=s;bm=m
  except:break
 return ms
def post(p,b):
 try:
  r=u.urlopen(u.Request(os.getenv("MAKEFUN_ENV_URL")+p,json.dumps(b).encode(),{"Content-Type":"application/json"}));return json.load(r)
 except:return 0
while 1:
 g=post("/game",{})
 if not g:exit(1)
 if g["status"]=="done":break
 while "y"in g["status"]:
  pf(g["fen"]);legal=g["legal_moves"]
  try:rk=rt(legal)
  except:rk=[pu(x)for x in legal]
  for mv in rk:
   r=post("/move",{"game":g["game"],"move":uc(mv)})
   if r:g=r;break
  else:exit(1)
