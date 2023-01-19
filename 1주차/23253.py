import sys
input = sys.stdin.readline

n,m = map(int,input().split())
p=True
for i in range(m):
    a= int(input())
    k = list(map(int, input().split()))
    for j in range(a-1):
        if k[j]<k[j+1]:
            p=False
            break
    if not p:
        break
if p:#true일경우
    print("Yes")
else:#false일경우
    print("No")