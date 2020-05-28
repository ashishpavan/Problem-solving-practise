""" Brute Force
https://www.codechef.com/LRNDSA05/problems/CHEFSQRS
"""
_max_size=1e+8
SPF=[1]*int(_max_size)
i=2
while (i*i)<_max_size:
    if SPF[i]==1:
        SPF[i]=i
        j=i*i
        count=1
        while j<_max_size:
            if SPF[j]==1:
                SPF[j]=i
            j=j+i
    i+=1
T=int(input("Now Enter"))
for i in range(T):
    N=int(input())
    A=SPF[N]
    B=N//SPF[N]
    while SPF[B]!=B:
        x=(A+B)/2
        if x==(A+B)//2:
            A,B=min(A,B),max(A,B)
            print(min((A+B)//2,(B-A)//2)**2)
            continue
        A=A*SPF[B]
        B=B//SPF[B]
    if (A+B)/2==(A+B)//2:
        A,B=min(A,B),max(A,B)
        print(min((A+B)//2,(B-A)//2)**2)
        continue
    print(-1)
    
