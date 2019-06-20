x = int(input())
y = int(input())

c = x ^ y
print(c)
print(list(bin(c)).count('1'))
