x = int(input())
a = 1
while x > 0:
    a *= x % 7
    x = x // 7
print(a)