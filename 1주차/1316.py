import sys
from collections import Counter
input = sys.stdin.readline

a = int(input())
data1 = [(input().strip()) for _ in range(a)]


group_words = 0
for i in range(len(data1)):
    error = 0
    for j in range(len(data1[i])-1):
        if(data1[i][j]!=data1[i][j+1]):
            new=data1[i][j+1:]
            #print(new)
            if new.count(data1[i][j]) > 0:#data1[i][j]값과 new가 같으면 다 돌면서+1해주기
                #print()
                error += 1
    if error == 0:
        group_words += 1
print(group_words)