"""  https://www.codechef.com/LRNDSA05/problems/ZACKHAN """
import math
T=int(input())
for i in range(T):
    a,b=list(map(int,input().split()))
    print(math.gcd(a,b))
