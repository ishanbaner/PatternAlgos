import random
import time
import matplotlib.pyplot as plt

def preprocess(patt):            
    lps=[0]*(len(patt))         #lps[i] stores the length of the longest prefix of patt[0..i] which is also a suffix of patt[0..i] 
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
    m=len(pat)
    n=len(txt)
    arr=preprocess(pat)
    j=0
    i=0
    ch=0
    while n-i>=m-j:
        if pat[j]==txt[i]:
            i+=1
            j+=1
        if j==m:            #We report occurence if match occurs for the entire pattern length
            ch=1
            #print("Found at ",i-j)
            j=arr[j-1]      #Start the scanning from the position till which we have already scanned
        elif i<n and pat[j]!=txt[i]:
            if j!=0:
                j=arr[j-1]
            else:
                i+=1
    #if ch==0:
    #   print("Nope")


X=[]
Y=[]
for g in range(4,8000):
    X+=[g]                                  
for t in range(4,8000):
    text=[]
    pattern=[]
    for i in range(t):
        text+=[random.randint(0,9)]                       #generating random string of length k which varries from 4 to 8000
    for j in range(4):
        pattern+=[random.randint(0,9)]                    #generating random pattern of length of length 4
    text+=pattern
    st=time.time()
    res=KMP(pattern,text)
    et=time.time()
    Y+=[et-st]

X2=[]
Y2=[]
co=0
check=0

#We will be plotting the average time taken for lengths in multiples of 100
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

plt.xlabel("Length of string in order of 100")
plt.ylabel("Time")
plt.show()
