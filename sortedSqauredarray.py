"""
input: -7,-3,-1,4,8,12
output: 1,9,16,49,64,144"""


def mod2(x):
	if x<0:
		return -x;
	return x
	
x=list(map(int,input().split(',')))
reverse_ans=[]
i=0
j=len(x)-1

while i!=j:
	if mod2(x[i])<mod2(x[j]):
		reverse_ans.append(x[j]**2)
		j-=1
	else:
		reverse_ans.append(x[i]**2)
		i+=1
reverse_ans.append(x[i]**2)
reverse_ans.reverse()
print(reverse_ans)


