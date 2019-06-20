from collections import Counter
S = sorted(input())
counter = Counter(S).most_common()
for i in range(3):
    print(counter[i][0], counter[i][1])
