import numpy as np 
import random
j=k=0
kin=0
def findInverse(j):
    global k
    global kin
    k=random.randint(2,26)
    for i in range(1,26):
        if((k*i)%26==1):
            kin=i
            j=0
        else:
            j=j+1

s=input("enter the messege=")
findInverse(j)
if(j==0):
    findInverse(j)
print(k)
print(kin)
if(kin==0 or k==0):
    findInverse(j)
else:
    ap=[]
    mg=[]
    ck=[]
    ct=""
    pt=""
    a="abcdefghijklmnopqrstuvwxyz "
    print(a[26])
    for i in a:
        ap.append(i)
    for i in range(len(s)):
        for j in range(27):
            if(s[i]==ap[j]):
                mg.append(j)
    for i in range(len(mg)):
        if(mg[i]==26):
            mg[i]=26
        else:
            mg[i]=(mg[i]*k)%26
    for i in range(len(mg)):
        for j in range(27):
            if(mg[i]==j):
                ct+=ap[j]
    print("cipher text is=",end="  ")
    print(ct)
    for i in range(len(ct)):
        for j in range(27):
            if(ct[i]==ap[j]):
                ck.append(j)

    for i in range(len(ck)):
        if(ck[i]==26):
            ck[i]=26
        else:
            ck[i]=(ck[i]*kin)%26
    for i in range(len(ck)):
        for j in range(27):
            if(ck[i]==j):
                pt+=ap[j]
    print("plain text is=",end="  ")
    print(pt)