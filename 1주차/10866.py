import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
d = deque()
for i in range(N):
    command = input().split()
    if command[0] == "push_front":
        d.appendleft(command[1])#why command[1]
    elif command[0]=="push_back":
        d.append(command[1])#append right하면 안됨?
    elif command[0]=="pop_front":
        if d:
            print(d[0])
            d.popleft()
        else:
            print("-1")
    elif command[0]=="pop_back":
        if d:
            print(d[len(d)-1])
            d.pop()#pop right해주면 안돼?
        else:
            print("-1")
    elif command[0]=="size":
        print(len(d))
    elif command[0]=="empty":
        if len(d)==0:
            print("1")
        else:
            print("0")
    elif command[0]=="front":
        if len(d)==0:
            print("-1")
        else:
            print(d[0])
    elif command[0]=="back":
        if len(d)==0:
            print("-1")
        else:
            print(d[len(d)-1])