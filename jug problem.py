#jug problem
#euclid's theorem
x=int(input("enter the size of first jug "))
y=int(input("enter the size of second jug "))
a=0
b=0
needed=int(input("enter the remaining size needed"))
if needed==x:
    print("the solution is 1 gallon  of jug 1  and 0 gallons of jug 2" )
elif needed==y:
    print("the solution is 0 gallon  of jug 1  and 1 gallons of jug 2" )
else :
    while not(a!=needed and b==needed) and not(a==needed and b!=needed):
        if a==0:
            a=x
        elif (b+a)<=y:
            b=b+a
            a=0
        elif b==y:
            b=0
        else:
            a=a-y+b
            b=y
        print("a: ",a, "b: ",b)



