import random
import time

def resolve(Lu,Ls,p,r=[]):
    if p==0:
        r+[p]
        return Ls,r
    elif Ls[1][p-1]>Ls[0]: 
        return resolve(Lu,Ls,p-1,r)
    else:
        z=Ls.copy()
        z[0]-=Ls[1][p-1]
        z[2]+=Lu[p-1] 
        return max(resolve(Lu,z,p-1,r+[p]),
                   resolve(Lu,Ls,p-1,r),key=third)

def third(e):
        return e[0][2]

def control(n,Ls,Lu):
    T=[n,Ls,0]
    le=len(Ls)
    return resolve(Lu,T,le)

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

x=test_it()
            

            
        
    
