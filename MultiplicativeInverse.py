import numpy as np 
import random
j=k=kin=0
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
ap=[]
mg=[]
ck=[]
ct=""
pt=""
a="abcdefghijklmnopqrstuvwxyz"
for i in a:
    ap.append(i)
print(ap)
for i in range(len(s)):
    for j in range(26):
        if(s[i]==ap[j]):
            mg.append(j)
mg=[(x*k)%26 for x in mg]
print(mg)
for i in range(len(mg)):
    for j in range(26):
        if(mg[i]==j):
            ct+=ap[j]
print("cipher text is=",end="  ")
print(ct)
for i in range(len(ct)):
    for j in range(26):
        if(ct[i]==ap[j]):
            ck.append(j)

ck=[(x*kin)%26 for x in ck]
for i in range(len(ck)):
    for j in range(26):
        if(ck[i]==j):
            pt+=ap[j]
print("plain text is=",end="  ")
print(pt)