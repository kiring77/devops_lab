import ipaddress


mask = [1, 2]
l1 = []
N = int(input('N = '))
for i in range(N):
    mask[i] = ipaddress.ip_address(input())


M = int(input('M ='))
for i in range(M):
    count = 0
    c1, c2 = input().split()
    ip1 = ipaddress.ip_address(c1)
    ip2 = ipaddress.ip_address(c2)
    for j in range(N):
        g = int(ip1)
        v = int(ip2)

        if (g & int(mask[j])) == (v & int(mask[j])):
            count += 1
    l1.append(count)
for i in l1:
    print(i)
