s=input("enter the numbers")
x=[int(i) for i in s.split(',')]
print(x,len(x))
for i in range(len(x)):
    for j in range(len(x)-1-i):
        if x[j] > x[j+1]:
            x[j] , x[j+1]= x[j+1], x[j]
print(x)