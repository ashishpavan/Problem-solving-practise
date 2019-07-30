"""
    **
    **
   ****
   ****
  ******
  ******
 ********
 ********
**********
**********

"""
x=int(input("enter the number of lines"))
if x%2==0:
    space=x
else :
    space=x+1
space=space//2
for i in range(1,x+1):
    # space logic
    if i % 2 != 0:
        space -= 1
    for ik in range(space):
        print(" ",end="")

    #"*" logic
    if i%2==0:
        n=i
    else:
        n=i+1
    for j in range(n):
        print("*",end="")
    print(" ")