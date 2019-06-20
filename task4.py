N = int(input())
max_value = max_count = 0
for i in range(1, N + 1):
    V, S = map(int, input().split())
    if S == 1:
        if V > max_value:
            max_count = i
            max_value = V
if S != 1:
    print(-1)
else:
    print(max_count)
