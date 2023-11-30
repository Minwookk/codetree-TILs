import sys 
m = int(input())
n = list(map(int, input().split()))
num_list = [0] * 10
for i in range(m):
    if len(str(n[i])) == 3 :
        N = str(n[i])[0]
        num_list[int(N)] += 1
    else : 
        num_list[0] += 1
for j in range(len(num_list)):
    if num_list[j] == 0 :
        continue
    else : 
        print(j, "-", num_list[j])