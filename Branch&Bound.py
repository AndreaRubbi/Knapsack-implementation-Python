import random
import time

def Sort(Ls,Lu):
    def ratio(e):
        return e[1]/e[0]
    v=range(len(Lu))
    X=[[Ls[x],Lu[x]] for x in v]
    Y=sorted(X,key=ratio)
    S=[Y[x][0] for x in v]
    U=[Y[x][1] for x in v]
    return S,U

def optimistic(Lu,Ls,p):
    Sum=Ls[2]
    j=Ls[0]
    while j>Ls[1][p-1] and p>0:
        a=Lu[p-1]
        Sum+=a
        j-=Ls[1][p-1]
        p-=1
    if p!=0:
        a=Lu[p-1]
        b=Ls[1][p-1]
        Sum+=int(a*(j/b))
    return Sum

def fourth(e):
    return e[0][3]
def third(e):
    return e[2]

def resolve(n,Lu,Ls,p,r=[],Q=[]):
    if p==0:
        return Ls,r
    z=Ls.copy()
    z[0]-=Ls[1][p-1]
    z[2]+=Lu[p-1]
    z[3]=optimistic(Lu,Ls,p)
    Ls[3]=optimistic(Lu,Ls,p-1)
    if z[0]>=0:
        Q+=[[Ls,p-1,r],[z,p-1,r+[p]]]
    else:
        Q+=[[Ls,p-1,r]]
    Q=sorted(Q,key=fourth,reverse=True)
    best=Q.pop(0)
    return resolve(n,Lu,best[0],best[1],best[2],Q)
    
def control(n,Ls,Lu):
    X=Sort(Ls,Lu)
    Ls=X[0]
    Lu=X[1]
    #print(' Ls:',Ls,'\n','Lu:',Lu)
    T=[n,Ls,0,0]            
    return resolve(n,Lu,T,len(Ls))

def test_it():
    for z in [5,10,15,20,25]:
        Ls=[random.randint(1,10)for x in range(z)]
        Lu=[random.randint(1,10) for x in range(z)]
        n=z*7
        print_it(n,Ls,Lu)

def print_it(n,Ls,Lu):
    x=time.time()
    res=control(n,Ls,Lu)
    w=time.time()
    print('remaining space= '+str(res[0][0])+'/'+str(n)+'Gb',
          'total value in space= '+str(res[0][2])+'/'+str(sum(Lu))
          +'♥','elements in space= '+str(res[1]),sep='\n')
    print('time needed: ',w-x)
    return n,Sort(Ls,Lu)
x=test_it()




