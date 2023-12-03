import math
n = input()
m = list(map(int, input().split()))
lead, member = map(int, input().split())
answer = 0 
for i in m :
    if lead >= i :
        answer += 1
        continue
    else : answer += math.ceil((( i - lead ) / member ) + 1)
print(int(answer))