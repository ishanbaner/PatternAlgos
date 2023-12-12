import random
import time
import matplotlib.pyplot as plt
def preprocess(l):
    value={}
    for i in range(len(l)):
        value[l[i]]=max(1,len(l)-i-1)
    value[-1]=len(l)
    return(value)

def search(txt,pat,num):
    values=preprocess(pat)
    n=len(txt)
    m=len(pat)
    t=m-1
    c=0
    ch=0
    stop=0
    while(t<n) and stop==0:
        for j in range(m):
            num+=1
            if t==n-1:
                stop=1
            if txt[t]!=pat[m-j-1]:
                if txt[t] in pat:
                    t+=values[txt[t]]+j
                else:
                    t+=values[-1]+j
                break
            t-=1
            c+=1
        if c==m:
            #print("Occ at ",t)
            t+=1+m
            ch=1
        c=0
    #if ch==0:
    #   print("No occurence")
        
    return(num)

X=[]
for u in range(4,200):
    X+=[u]
Y=[]
Y1=[]
for k in range(4,200):
    text=[]
    pattern=[]
    for i in range(k):
        #text+=[random.randint(0,9)]
        text+=[1]
    for j in range(4):
        #pattern+=[random.randint(0,9)]
        pattern+=[1]
    #print("text=",text," pattern=",pattern)
    se=search(text,pattern,0)
    Y+=[se]

for k1 in range(4,200):
    text1=[]
    pattern1=[]
    for i1 in range(k1):
        #text1+=[random.randint(0,9)]
        text1+=[1]
    for j1 in range(8):
        #pattern1+=[random.randint(0,9)]
        pattern1+=[1]
    #print("text=",text," pattern=",pattern)
    se1=search(text1,pattern1,0)
    Y1+=[se1]

plt.plot(X,Y)
plt.plot(X,Y1,color='red')
plt.show()
'''
text=[]
pattern=[]
for i in range(10):
    text+=[random.randint(0,9)]
for j in range(2):
    pattern+=[random.randint(0,9)]
text+=pattern
#print("text=",text," pattern=",pattern)
se=search([2, 6, 2, 2, 7, 3, 8, 2, 5, 1, 1, 2],[1,2],0)
'''
