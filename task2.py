a = int(input())
b = int(input())
reverse_a = reverse_b = 0
if a > 0:
    a = a
    scale_a = 1
else:
    a = -a
    scale_a = -1

if b > 0:
    b = b
    scale_b = 1
else:
    b = -b
    scale_b = -1

a = str(a)
b = str(b)
a = list(map(int, a))
b = list(map(int, b))
if scale_a > 0:
    a.sort(reverse=True)
else:
    a.sort()

s = ''.join(map(str, a))
a = int(s)

if scale_b > 0:
    b.sort()
else:
    b.sort(reverse=True)

zeros = b.count(0)
for i in range(zeros):
    if b[i] == 0:
        b.insert(zeros + 1, 0)
s = ''.join(map(str, b))
b = int(s)
print(a * scale_a - b * scale_b)
