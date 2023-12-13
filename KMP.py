import random
import time
import matplotlib.pyplot as plt

def preprocess(patt):
    lps=[0]*(len(patt))
    leng=0
    lps[0]=0
    i=1
    while i<len(patt):
        if patt[i]==patt[leng]:
            leng+=1
            lps[i]=leng
            i+=1
        else:
            if leng>0:
                leng=lps[leng-1]
            else:
                lps[i]=0
                i+=1
    return(lps)

def KMP(pat,txt):
    nums=0
    m=len(pat)
    n=len(txt)
    arr=preprocess(pat)
    j=0
    i=0
    ch=0
    while n-i>=m-j:
        nums+=1
        if pat[j]==txt[i]:
            i+=1
            j+=1
        if j==m:
            ch=1
            #print("Found at ",i-j)
            j=arr[j-1]
        elif i<n and pat[j]!=txt[i]:
            if j!=0:
                j=arr[j-1]
            else:
                i+=1
    #if ch==0:
    #   print("Nope")
    return(nums)


X=[]
X2=[]
X3=[]
Y=[]
Y1=[]
Y2=[]
for g in range(4,200):
    X+=[g]
for t in range(4,200):
    text=[]
    pattern=[]
    for i in range(t):
        text+=[random.randint(0,9)]
    for j in range(4):
        pattern+=[j]
    text+=pattern
    res=KMP(pattern,text)
    Y+=[res]

for g in range(8,200):
    X2+=[g]
for t in range(8,200):
    text=[]
    pattern=[]
    for i in range(t):
        text+=[random.randint(0,9)]
    for j in range(8):
        pattern+=[j]
    text+=pattern
    res=KMP(pattern,text)
    Y1+=[res]

plt.plot(X,Y)
plt.plot(X2,Y1,color='RED')
plt.show()



#print(func([7,7,1],[1, 8, 4, 6, 5, 0, 3, 0, 9, 3, 2, 5, 6, 5, 5, 9, 7, 3, 7, 3, 7, 7, 1]))

