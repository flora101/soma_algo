import sys
from collections import Counter
input = sys.stdin.readline

a= int(input())
data = [int(input()) for _ in range(a)]#int일때는 input만 해주면 됨

#print(sum(data)//a)#몫은 //
print(round(sum(data)/a))
data.sort()
#print(data)
print(data[a//2])

#최빈값 구하기
s = Counter(data).most_common()
#print(s)
if len(s) > 1:
    if s[0][1] == s[1][1]:
        print(s[1][0])
    else:
        print(s[0][0])
else:
    print(s[0][0])

print(max(data)-min(data))