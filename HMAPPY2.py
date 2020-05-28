"""https://www.codechef.com/LRNDSA05/problems/HMAPPY2"""
import math
T=int(input())
for i in range(T):
    N,A,B,K=list(map(int,input().split()))
    lcm=(A*B)//math.gcd(A,B)
    ans=N//A + N//B - 2*(N//lcm)
    if ans>= K:
        print("Win")
    else:
        print("Lose")
