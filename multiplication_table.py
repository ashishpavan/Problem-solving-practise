#hitesh_choudary first solution
x=int(input("enter the number whose multiplication table u want"))
n=0
for i in range(12):
    n=n+x
    print(x,"*",(i+1),"=",n)