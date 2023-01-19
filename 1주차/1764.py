import sys
from collections import Counter
input = sys.stdin.readline

a,b = map(int,input().split())
data1 = [(input().strip()) for _ in range(a)]#문자열 입력
data2 = [(input()).strip() for _ in range(b)]
data1= Counter(data1)
data2= Counter(data2)
# print(data1)
# print(data2)
result=data1 & data2#교집합은 &쓰기
#print(result)
ans= len(result)
print(ans)
result= sorted(result)
for i in result:
    print(i)