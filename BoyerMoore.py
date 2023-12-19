import random
import time
import matplotlib.pyplot as plt
def preprocess(l):#preprocessing as per the bad character rule
    value={}
    for i in range(len(l)):
        value[l[i]]=max(1,len(l)-i-1)         #The values[k] stores the position of k in the pattern from the right
    value[-1]=len(l)
    return(value)

def search(txt,pat):
    values=preprocess(pat)
    n=len(txt)
    m=len(pat)
    t=m-1
    c=0
    ch=0
    stop=0
    while(t<n) and stop==0:
        for j in range(m):
            if t==n-1:                         #The search stops once we have scanned the last suffix of the text
                stop=1
            if txt[t]!=pat[m-j-1]:             #In case of a mismatch 
                if txt[t] in pat:              #If the mismatched string is present in the pattern
                    t+=values[txt[t]]+j        #Shift the pattern in such way, that the unmatched string in the pattern matches the text's
                else:
                    t+=values[-1]+j            #If the unmatched string is not present, it will shift by the entire length
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
        

X=[]
for u in range(2,8000):
    X+=[u]
Y=[]
Y1=[]
for k in range(2,8000):
    text=[]
    pattern=[]
    for i in range(k):
        text+=[random.randint(0,9)]        #Generating random string of length k which varries from 2 to 8000
        #text+=[1]
    for j in range(4):
        pattern+=[random.randint(0,9)]     #Generating random pattern of length 4 
        #pattern+=[1]
    st=time.time()
    se=search(text,pattern)
    et=time.time()
    Y+=[(et-st)]

#Taking the average time taken for string lengths in mutliple of 100s
X2=[]
Y2=[]
co=0
check=0
for y in range(80):
    X2+=[y]
    Y2+=[0]
for t in range(len(Y)):
    if t<100*(co+1) and t>=100*co:
        Y2[co]+=Y[t]/100
        check+=1
    if check==100:
        co+=1
        check=0

plt.plot(X2,Y2)
#plt.plot(X,Y1,color='red')
plt.xlabel("Length of string in order of 100")
plt.ylabel("Time taken")
plt.show()
